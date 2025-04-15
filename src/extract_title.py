def extract_title(markdown):
    """
    Extracts the first h1 header (line starting with a single #) from the markdown string.
    Returns the header text with # and whitespace stripped.
    Raises ValueError if no h1 header is found.
    """
    for line in markdown.splitlines():
        if line.strip().startswith("# "):
            return line.strip()[2:].strip()
        # Optionally support "#Title" (no space)
        if line.strip().startswith("#") and not line.strip().startswith("##"):
            return line.strip()[1:].strip()
    raise ValueError("No h1 header found in markdown")

import unittest

class TestExtractTitle(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(extract_title("# Hello"), "Hello")
        self.assertEqual(extract_title("#    Hello world   "), "Hello world")
        self.assertEqual(extract_title("#Hello"), "Hello")
        self.assertEqual(extract_title("   #   Hello again  "), "Hello again")

    def test_first_h1(self):
        md = """
# First Title
Some text
# Second Title
"""
        self.assertEqual(extract_title(md), "First Title")

    def test_no_h1(self):
        with self.assertRaises(ValueError):
            extract_title("No header here\n## Subheader\nText")
        with self.assertRaises(ValueError):
            extract_title("")

    def test_h2_h3_ignored(self):
        md = """
## Not h1
### Not h1 either
# Yes this one
"""
        self.assertEqual(extract_title(md), "Yes this one")

if __name__ == "__main__":
    unittest.main()
