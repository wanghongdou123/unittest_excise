import unittest
from report.HTMLTestRunner_PY3 import HTMLTestRunner
import os


class demo(unittest.TestCase):
    def setUp(self):
        print("setup")

    def tearDown(self):
        print("teardown")

    def test_case01(self):
        print("test_case01")
        self.assertEqual(1, 1,"判断相等")
        self.assertIn('h','this')

    @unittest.skipIf(1+1==2,"skip")
    def testcase02(self):
        print("testcase02")

    # @classmethod
    # def setUpClass(cls):
    #     print("setupclass")
    #
    # @classmethod
    # def tearDownClass(cls):
    #     print("teardownclass")


class demo1(unittest.TestCase):

    def test_case1(self):
        print("test_demo01 case1")

    def test_case2(self):
        print("test_demo01 case2")


class demo2(unittest.TestCase):

    def test_case1(self):
        print("test_demo02 case1")

    def test_case2(self):
        print("test_demo02 case2")



if __name__ == '__main__':
    # unittest.main()

    report_title = "xxx用例测试报告"
    desc = '用于展示xxx'
    report_file = './report/report.html'
    print(os.getcwd())

    testsuite = unittest.TestSuite()
    # testsuite.addTest(demo("test_case01"))
    # testsuite.addTest(demo1("test_case1"))
    # testsuite.addTest(demo2("test_case1"))
    # unittest.TextTestRunner().run(suit)


    testsuite.addTest(unittest.TestLoader().loadTestsFromTestCase(demo1))
    testsuite.addTest(unittest.TestLoader().loadTestsFromTestCase(demo2))


    # 执行特定的类

    # suit1 = unittest.TestLoader().loadTestsFromTestCase(demo)
    # suit2 = unittest.TestLoader().loadTestsFromTestCase(demo2)
    # suit_final = unittest.TestSuite([suit1,suit2])
    # unittest.TextTestRunner().run(suit_final)


    # 匹配某个目录下以test开头的py文件，执行这些文件下的所有case
    # discover = unittest.defaultTestLoader.discover("./testlearning",'test*.py')
    # unittest.TextTestRunner().run(discover)



    with open(report_file,'wb') as report:
        runner = HTMLTestRunner(stream=report, title=report_file, description=desc)
        runner.run(testsuite)

