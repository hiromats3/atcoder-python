from main import resolve
# please paste testcode here
import sys
from io import StringIO
import unittest


class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)

    def test_入力例_1(self):
        input = """2 3 2
..#
###"""
        output = """5"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2 3 4
..#
###"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """2 2 3
##
##"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """6 6 8
..##..
.#..#.
#....#
######
#....#
#....#"""
        output = """208"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
