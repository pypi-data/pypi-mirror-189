# This file is placed in the Public Domain.


"path"


import unittest


from opq.utl import fntime


FN = "opq.evt.Event/2d390009cef944e68ce686e5709a54d7/2022-04-11/22:40:31.259218"


class TestPath(unittest.TestCase):

    def test_path(self):
        fnt = fntime(FN)
        self.assertEqual(fnt, 1649709631.259218)
