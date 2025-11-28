import unittest
from mydict import MyDict

# 编写单元测试时， 我们需要编写一个测试类， 继承自 unittest.TestCase，
# 对每一类测试都需要编写一个test_xxx()方法。
# 由于unittest.TestCase提供了很多内置的条件判断，我们只需要调用这些方法就可以断言输出是否是我们所期望的。
class TestMyDict(unittest.TestCase):
    def test_init(self):
        # 最常用的断言就是assertEqual()， 它用来判断期待值和实际值是否相等。
        d = MyDict(a=1, b='test')
        self.assertEqual(d.a, 1) # 断言 d.a 的值为 1
        self.assertEqual(d.b, 'test') # 断言 d.b 的值为 'test'
        self.assertTrue(isinstance(d, dict)) # 断言 d 是 dict 的子类

    def test_key(self):
        d = MyDict()
        d['key'] = 'value' # 通过键访问
        self.assertEqual(d.key, 'value') # 断言 d.key 的值为 'value'

    def test_attr(self):
        d = MyDict()
        d.key = 'value'
        self.assertTrue('key' in d) # 断言 'key' 在字典中
        self.assertEqual(d['key'], 'value') # 断言 d['key'] 的值为 'value'

    def test_keyerror(self):
        # 另一类常用的断言就是assertRaises()， 它用来断言抛出指定类型的Error。
        d = MyDict()
        with self.assertRaises(KeyError): # 断言访问不存在的键会抛出 KeyError
            value = d['empty']

    def test_attrerror(self):
        d = MyDict()
        with self.assertRaises(AttributeError): # 断言访问不存在的属性会抛出 AttributeError
            value = d.empty

    # 可以在单元测试中编写两个特殊的setUp()和tearDown()方法。
    # 这两个方法会分别在每调用一个测试方法的前后分别被执行。
    def setUp(self):
        print('setUp...')

    def tearDown(self):
        print('tearDown...')    

# 最简单的运行单元测试的方法是调用 unittest 模块的 main() 函数
# 这样就可以将测试脚本当做正常的脚本运行，Python会自动运行该模块中的所有测试用例
if __name__ == '__main__':
    unittest.main()

# 另一种方法是在命令行通过参数-m unittest 来运行单元测试
# >>> python -m unittest mydict_test.py
# 这是一种比较常用的运行方式，适合批量运行多个测试模块
# 还可以在命令行通过参数-m unittest discover 来批量运行某个目录下的所有测试用例
# >>> python -m unittest discover -s test -p '*_test.py'
# 并且，有很多工具可以自动运行单元测试，比如常用的IDE PyCharm就集成了单元测试功能，
# 希望反复执行某一个测试方法，而不是每次都运行所有的测试方法，可以通过指定module.class.method来运行单个测试方法：
# >>> python -m unittest mydict_test.TestMyDict.test_init
# 其中，module是文件名mydict_test（不含.py），class是测试类TestMyDict，method是指定的测试方法名test_attr。
# 如果希望执行test_attr()和test_attrerror()两个测试方法，我们可以传入-k参数，用attr来匹配：
# >>> python -m unittest mydict_test -k attr -v
# >>> test_attr (mydict_test.TestDict.test_attr) ... ok
# >>> test_attrerror (mydict_test.TestDict.test_attrerror) ... ok