import unittest

class SmileTaskTest(unittest.TestCase):
    def setUp(self):
        print('befor each test')

    def tearDown(self):
        print('after each test')

    def test_add(self):
        self.a=2
        self.b=3
        self.c=self.a+self.b
        
        print(self.c)
        print(self.c)
        return self.c
    

if __name__ == '__main__':

    # 定义组装测试套件"
    suite = unittest.TestSuite()
    #组装测试套件
    suite.addTest(SmileTaskTest("test_add"))

    #####执行测试套件####
    runner=unittest.TextTestRunner()
    runner.run(suite)
