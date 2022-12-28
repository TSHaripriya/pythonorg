from stu import student
import unittest
class test_stu(unittest.TestCase):
    def test_email(self):
        s1=student('deepu','sai',94)
        self.assertEqual(s1.email,'deepu.sai@gmail.com')
        s1.first = 'deepika'
        self.assertEqual(s1.email,'deepika.sai@gmail.com')
