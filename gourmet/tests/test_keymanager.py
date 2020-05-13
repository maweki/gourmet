import os.path
import unittest

from hypothesis import given
from hypothesis.strategies import text


from gourmet.keymanager import KeyManager

class TestImports (unittest.TestCase):

    @given(text())
    def test_word_splitter(self, txt):
        ws = KeyManager.word_splitter

        self.assertListEqual(ws.split(txt), ws.split(txt.strip())) # Whitespaces at the ends don't matter
        for s in ws.split(txt):
            self.assertIsInstance(s, str)
            self.assertTrue(s)
            self.assertEqual(s, s.strip())

if __name__ == "__main__":
    unittest.main()
