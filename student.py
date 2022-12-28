from stu import student
import unittest
class test_stu(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("\nsetupclass")
    @classmethod
    def tearDownClass(cls):
        print("\nteardownclass")

    def setUp(self):
        print("\nsetup")
    def tearDown(self):
        print("\nteardown")
    def testemail(self):
        s1=student('deepu','sai',94)
        self.assertEqual(s1.email,'deepu.sai@gmail.com')
        s1.first = 'deepika'
        self.assertEqual(s1.email,'deepika.sai@gmail.com')
        print("\nemail")
    def test_fullname(self):
        s=student('hari','priya',83)
        self.assertEqual(s.fullname,'haripriya')
        print("\nfullname")
    def test_apply_bonus(self):
        s1=student('hari','priya',6)
        s1.apply_bonus()
        self.assertEqual(s1.marks,9,9)
        print("\napply_bonus")