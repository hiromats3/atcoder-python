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
        input = """101"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2"""
        output = """-1"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """999983"""
        output = """999982"""
        self.assertIO(input, output)

    def test_入力例_ex1(self):
        input = """7"""
        output = """1"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
