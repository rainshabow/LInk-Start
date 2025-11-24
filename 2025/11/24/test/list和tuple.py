#列表（list）是Python中一种常用的数据结构，用于存储有序的元素集合。
#列表中的元素可以是不同类型的数据，包括数字、字符串、甚至其他列表。
list1 = [1, 2, 3, 4, 5]
list2 = ['apple', 'banana', 'cherry']
list3 = [1, 'hello', 3.14, [5, 6, 7]]
print("list1 =", list1)
print("list2 =", list2)
print("list3 =", list3)

#访问列表元素可以使用索引，索引从0开始
print("list1的第一个元素:", list1[0])  # 输出1
print("list2的第二个元素:", list2[1])  # 输出banana
print("list3的第四个元素:", list3[3])  # 输出[5, 6, 7]
#可以使用负数索引从列表末尾访问元素，-1表示最后一个元素，-2表示倒数第二个元素，以此类推
print("list1的最后一个元素:", list1[-1])  # 输出5
print("list2的倒数第二个元素:", list2[-2])  # 输出banana

#list是可变的，可以修改、添加和删除元素
list1[0] = 10  # 修改第一个元素
print("修改后的list1:", list1)
list1.append(6)  # 在末尾添加新元素6
print("添加新元素后的list1:", list1)
list1.insert(2, 20)  # 在索引1位置插入新元素20
print("插入新元素后的list1:", list1)
list1.pop()  # 删除并返回最后一个元素
print("删除最后一个元素后的list1:", list1)
list1.pop(3)  # 删除并返回索引3位置的元素
print("删除索引3位置元素后的list1:", list1)
list1.remove(20)  # 删除第一个值为20的元素
print("删除第一个值为20的元素后的list1:", list1)

#tuple（元组）是另一种常用的数据结构，与list类似，也是用于存储有序的元素集合。
#但与list不同的是，tuple是不可变的，一旦创建就不能修改。
tuple1 = (1, 2, 3, 4, 5)
tuple2 = ('apple', 'banana', 'cherry')
tuple3 = (1, 'hello', 3.14, (5, 6, 7))
print("tuple1 =", tuple1)
print("tuple2 =", tuple2)
print("tuple3 =", tuple3)
#访问tuple元素也可以使用索引，索引从0开始
print("tuple1的第一个元素:", tuple1[0])  # 输出1
print("tuple2的第二个元素:", tuple2[1])  # 输出banana
print("tuple3的第四个元素:", tuple3[3])  # 输出(5, 6, 7)
#可以使用负数索引从tuple末尾访问元素，-1表示最后一个
print("tuple1的最后一个元素:", tuple1[-1])  # 输出5
print("tuple2的倒数第二个元素:", tuple2[-2])  # 输出
#tuple是不可变的，不能修改、添加或删除元素
#下面的代码会引发错误
#tuple1[0] = 10  # 尝试修改第一个元素，会引发TypeError
#tuple1.append(6)  # 尝试添加新元素，会引发AttributeError
#tuple1.pop()  # 尝试删除元素，会引发AttributeError
#但是如果tuple中包含可变对象（如list），可以修改该可变对象的内容
tuple4 = (1, 2, [3, 4, 5])
print("修改前的tuple4:", tuple4)
tuple4[2][0] = 30  # 修改tuple中list的第一个元素
print("修改后的tuple4:", tuple4) 