# 把变量从内存中变成可存储或传输的过程称之为序列化，在Python中叫pickling，在其他语言中也被称之为serialization，marshalling，flattening等等
# 序列化之后，就可以把序列化后的内容写入磁盘，或者通过网络传输到别的机器上。
# 反过来，把变量内容从序列化的对象重新读到内存里称之为反序列化，即unpickling。
# Python提供了pickle模块来实现序列化和反序列化。

path = 'test_file/'

import pickle
d = dict(name='Bob', age=20, score=88)
# pickle.dumps()方法把任意对象序列化成一个bytes
data = pickle.dumps(d)
print(data)
# pickle.loads()方法反序列化出对象
print(pickle.loads(data))
# pickle.dump()方法把对象序列化后写入一个file-like Object
with open(path + 'dump.txt', 'wb') as f:
    pickle.dump(d, f)
# pickle.load()方法从一个file-like Object中读取内容并反序列化出对象
with open(path + 'dump.txt', 'rb') as f:
    d2 = pickle.load(f)
    print(d2)
# Pickle的问题和所有编程语言特有的序列化问题一样，就是不同版本的Python可能会不兼容。
# 另外，由于pickle序列化的是Python特有的对象，所以只能在Python程序之间传递，
# 如果要在不同语言之间传递对象，就必须使用JSON。

# JSON是一种非常流行的用于存储和交换数据的格式，全称JavaScript Object Notation，
# 它是一个字符串，可以被所有语言读取和写入，也是一种非常好的人类可读的格式。
# 在Python中，可以使用json模块来对JSON格式的数据进行编解码。
import json
# Python对象->JSON字符串：json.dumps()
d = dict(name='Bob', age=20, score=88)
json_str = json.dumps(d)
print(json_str)
# JSON字符串->Python对象：json.loads()
print(json.loads(json_str))
# json.dumps()方法返回一个str，内容就是标准的JSON。
# 如果我们要把JSON写入文件，可以直接调用json.dump()方法，
with open(path + 'dump.json', 'w') as f:
    json.dump(d, f)
# 要把JSON从文件中读取出来，可以调用json.load()方法，
with open(path + 'dump.json', 'r') as f:
    d2 = json.load(f)
    print(d2)
# 注意json.dumps()方法返回的内容是str，如果我们要在网络上传输，或者保存到文件，
# 就需要先编码为bytes，例如UTF-8编码：
json_bytes = json_str.encode('utf-8')
print(json_bytes)
# 要把bytes还原为str，就需要用decode()方法：
print(json_bytes.decode('utf-8'))
# JSON不仅可以转换dict，还可以转换list、tuple等，只要是符合JSON标准的数据类型。
# 但是，像set、bytes等Python特有的数据类型是无法直接转换为JSON的，
# 必须先转换为list或str等标准数据类型。
class student :
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score
def student_to_dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }
Bob = student('Bob', 20, 88)       
print(json.dumps(Bob, default=student_to_dict)) 
# 通常class的实例都有一个__dict__属性，它就是一个dict，用来存储实例变量。
# 也有少数例外，比如定义了__slots__的class
print(json.dumps(Bob, default=lambda obj: obj.__dict__))