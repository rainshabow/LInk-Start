#通过列表生成式，我们可以直接创建一个列表。但是，受到内存限制，列表容量肯定是有限的。
#而生成器不需要将所有的元素都存储在内存中，而是每次需要的时候才生成一个元素，因此，生成器可以表示一个无限大的序列。

#要创建一个生成器，只需要将一个列表生成式的[]改为()即可
g = (x * x for x in range(10))
#通过next()函数获得生成器的下一个元素
print(next(g))  # 输出: 0
print(next(g))  # 输出: 1
print(next(g))  # 输出: 4
#也可以使用for循环来遍历生成器
for n in g:
    print(n)

# generator非常强大。如果推算的算法比较复杂，用类似列表生成式的for循环无法实现的时候，还可以用函数来实现。
# 例如，下面的代码创建了一个生成器，可以不断地计算下一个斐波那契数：
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'
# yield语句就是一个生成器，和return语句不一样，return是返回一个值并退出函数，而yield是返回一个值，并暂停函数的执行，下次再执行时从当前位置继续执行。
# 所以，含有yield的函数就是一个生成器函数，调用生成器函数，返回一个生成器对象。
# 例如，调用上面的fib函数，创建一个生成器：
fib_generator = fib(10)
for num in fib_generator:
    print(num)
# 注意，函数中return语句用于在生成器函数执行完毕时，向调用者传递一个终止信息。在for循环中，这个终止信息会被忽略。
# 如果想要捕获这个终止信息，可以捕获StopIteration错误，返回值包含在StopIteration的value中：
fib_generator = fib(10)
while True:
    try:
        x = next(fib_generator)
        print('fib_generator:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break
# 练习
# 请编写一个generator，依次返回杨辉三角的每一行
def triangles(max):
    L = [1]
    yield L

    i = 1
    while i < max:
        i += 1
        newL = []
        newL.append(L[0])
        for i in range(0,len(L) - 1):
            newL.append(L[i] + L[i + 1])
        newL.append(L[-1])
        L = newL
        yield L
    return 'done'

g = triangles(10)
for line in g:
    print(line)