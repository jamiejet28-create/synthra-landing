"""Automated validation tests for SYNTHRA landing and waitlist pages."""

import os
import re
import unittest
from html.parser import HTMLParser
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent


class SimpleHTMLAnalyzer(HTMLParser):
    def __init__(self):
        super().__init__()
        self.tags = []
        self.ids = set()
        self.links = []
        self.images = []
        self.meta_tags = []
        self.link_tags = []
        self.styles = []
        self.scripts = []
        self._current_tag = None
        self._current_data = []

    def handle_starttag(self, tag, attrs):
        attr_dict = dict(attrs)
        self.tags.append((tag, attr_dict))
        if "id" in attr_dict:
            self.ids.add(attr_dict["id"])
        if tag == "a" and "href" in attr_dict:
            self.links.append(attr_dict["href"])
        if tag == "img" and "src" in attr_dict:
            self.images.append(attr_dict["src"])
        if tag == "meta":
            self.meta_tags.append(attr_dict)
        if tag == "link":
            self.link_tags.append(attr_dict)
        if tag in ("style", "script"):
            self._current_tag = tag
            self._current_data = []

    def handle_endtag(self, tag):
        if tag == self._current_tag:
            content = "".join(self._current_data)
            if tag == "style":
                self.styles.append(content)
            elif tag == "script":
                self.scripts.append(content)
            self._current_tag = None
            self._current_data = []

    def handle_data(self, data):
        if self._current_tag:
            self._current_data.append(data)


class TestSynthraLanding(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.index_path = REPO_ROOT / "index.html"
        cls.waitlist_path = REPO_ROOT / "waitlist.html"
        cls.nojekyll_path = REPO_ROOT / ".nojekyll"

    def test_essential_files_exist(self):
        self.assertTrue(self.index_path.exists(), "index.html must exist")
        self.assertTrue(self.waitlist_path.exists(), "waitlist.html must exist")
        self.assertTrue(self.nojekyll_path.exists(), ".nojekyll must exist for GitHub Pages")

    def test_index_html_structure_and_links(self):
        content = self.index_path.read_text(encoding="utf-8")
        parser = SimpleHTMLAnalyzer()
        parser.feed(content)

        # Check essential IDs exist for anchor navigation
        for expected_id in ["forge", "how", "buy"]:
            self.assertIn(expected_id, parser.ids, f"Expected #{expected_id} anchor in index.html")

        # Check internal anchor links match existing IDs
        for href in parser.links:
            if href.startswith("#") and len(href) > 1:
                target_id = href[1:]
                self.assertIn(target_id, parser.ids, f"Link target #{target_id} does not exist in index.html")
            elif not href.startswith("http") and not href.startswith("mailto:") and not href.startswith("#"):
                clean_target = href.split("?")[0].split("#")[0]
                target_file = REPO_ROOT / clean_target
                self.assertTrue(target_file.exists(), f"Linked file {clean_target} does not exist")

        # Verify waitlist is linked from index.html
        waitlist_links = [l for l in parser.links if "waitlist.html" in l]
        self.assertGreater(len(waitlist_links), 0, "waitlist.html should be discoverable and linked from index.html")

    def test_no_broken_local_css_assets(self):
        for html_file in [self.index_path, self.waitlist_path]:
            content = html_file.read_text(encoding="utf-8")
            parser = SimpleHTMLAnalyzer()
            parser.feed(content)

            for style_block in parser.styles:
                # Find all url(...) references in CSS
                urls = re.findall(r'url\s*\(\s*["\']?([^"\'\)]+)["\']?\s*\)', style_block)
                for u in urls:
                    u_clean = u.strip()
                    if u_clean.startswith("data:") or u_clean.startswith("http://") or u_clean.startswith("https://"):
                        continue
                    # Any local relative url must exist
                    asset_path = REPO_ROOT / u_clean
                    self.assertTrue(asset_path.exists(), f"Asset url({u_clean}) in {html_file.name} does not exist")

    def test_meta_and_favicons(self):
        for html_file in [self.index_path, self.waitlist_path]:
            content = html_file.read_text(encoding="utf-8")
            parser = SimpleHTMLAnalyzer()
            parser.feed(content)

            # Check for favicon
            favicon_links = [l for l in parser.link_tags if "icon" in l.get("rel", "")]
            self.assertGreater(len(favicon_links), 0, f"Favicon link missing in {html_file.name}")

            # Check Open Graph tags
            og_props = {m.get("property") for m in parser.meta_tags if "property" in m}
            for expected_og in ["og:title", "og:description", "og:type"]:
                self.assertIn(expected_og, og_props, f"Missing {expected_og} in {html_file.name}")

            # Check Twitter card tags
            twitter_names = {m.get("name") for m in parser.meta_tags if "name" in m}
            self.assertIn("twitter:card", twitter_names, f"Missing twitter:card in {html_file.name}")

    def test_waitlist_functionality_and_cleanliness(self):
        content = self.waitlist_path.read_text(encoding="utf-8")
        parser = SimpleHTMLAnalyzer()
        parser.feed(content)

        # Confirm form exists with expected inputs
        has_email = any(
            t == "input" and attrs.get("type") == "email" and attrs.get("name") == "email"
            for t, attrs in parser.tags
        )
        self.assertTrue(has_email, "waitlist.html must include an email input with name='email'")

        # Confirm back link to index.html exists
        index_links = [l for l in parser.links if "index.html" in l or l == "./"]
        self.assertGreater(len(index_links), 0, "waitlist.html must include a back link to index.html")

        # Verify no leftover prompt or agent leak artifacts
        self.assertNotIn("Grok cannot open Settings", content, "Leaked debug text should not be present in waitlist.html")
        self.assertNotIn("User: Pages flip", content, "Leaked debug text should not be present in waitlist.html")


if __name__ == "__main__":
    unittest.main()
