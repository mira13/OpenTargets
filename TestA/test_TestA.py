import TestA
import unittest
import sys
from io import StringIO
import subprocess

class TestHello(unittest.TestCase):

    def test_as_program(self):

        str_diseas = b'Run diseas analysis for EFO_0000616\r\nStandart deviation for disease EFO_0000616 = 0.0\r\nMean for disease EFO_0000616 = 1.0\r\nMax for disease EFO_0000616 = 1.0\r\nMin for disease EFO_0000616 = 1.0\r\n'
        self.assertEqual(
            subprocess.check_output(["python", "./TestA/TestA.py", "-d", "EFO_0000616"]),
            str_diseas
        )

        str_target = b'Run target analysis for ENSG00000157764\r\nStandart deviation for target ENSG00000157764 = 0.0\r\nMean for target ENSG00000157764 = 1.0\r\nMax for target ENSG00000157764 = 1.0\r\nMin for target ENSG00000157764 = 1.0\r\n'
        self.assertEqual(
            subprocess.check_output(["python", "./TestA/TestA.py", "-t", "ENSG00000157764"]),
            str_target
        )

if __name__ == '__main__':
    unittest.main()