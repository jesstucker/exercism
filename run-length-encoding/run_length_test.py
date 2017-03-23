# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest

from run_length import encodeR, decodeR


class WordCountTests(unittest.TestCase):

    def test_encodeR(self):
        self.assertMultiLineEqual('2A3B4C', encodeR('AABBBCCCC'))

    def test_decodeR(self):
        self.assertMultiLineEqual('AABBBCCCC', decodeR('2A3B4C'))

    def test_encodeR_with_single(self):
        self.assertMultiLineEqual(
            '12WB12W3B24WB',
            encodeR('WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB'))

    def test_decodeR_with_single(self):
        self.assertMultiLineEqual(
            'WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB',
            decodeR('12WB12W3B24WB'))

    def test_combination(self):
        self.assertMultiLineEqual('zzz ZZ  zZ', decodeR(encodeR('zzz ZZ  zZ')))

    def test_encodeR_unicode_s(self):
        self.assertMultiLineEqual('⏰3⚽2⭐⏰', encodeR('⏰⚽⚽⚽⭐⭐⏰'))

    def test_decodeR_unicode(self):
        self.assertMultiLineEqual('⏰⚽⚽⚽⭐⭐⏰', decodeR('⏰3⚽2⭐⏰'))


if __name__ == '__main__':
    unittest.main()
