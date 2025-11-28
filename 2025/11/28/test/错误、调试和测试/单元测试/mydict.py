# 编写一个自定义字典类 MyDict，继承自内置的 dict 类，该类的行为与dict相同，
# 但是可以通过属性访问，形如：
# >>> d = Dict(a=1, b=2)
# >>> d['a']
# 1
# >>> d.a
# 1
class MyDict(dict):
    def __init__(self, **kw):
        super().__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value
    