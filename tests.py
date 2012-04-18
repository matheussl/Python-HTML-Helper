import unittest
from html import *

class HtmlTest(unittest.TestCase):
    
    def setUp(self):
        pass

    def test_tag(self):
        tag = TAG('content')
        self.assertEqual(tag.__str__(), '<tag>\n    content\n</tag>')