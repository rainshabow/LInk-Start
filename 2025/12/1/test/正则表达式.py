# 正则表达式是一种用来匹配字符串的强有力的武器。
# 它的设计思想是用一种描述性的语言来给字符串定义一个规则，
# 凡是符合规则的字符串，我们就认为它“匹配”了，否则，该字符串就是不合法的。
# Python提供re模块，包含所有正则表达式的功能。
import re
# re.match()方法尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match()就返回None。
print(re.match('www', 'www.runoob.com').span())  # 在起始位置匹配
print(re.match('com', 'www.runoob.com'))         # 不在起始

# re.search()方法扫描整个字符串并返回第一个成功的匹配。
print(re.search('www', 'www.runoob.com').span()) # 在起始
print(re.search('com', 'www.runoob.com').span()) # 不在起始

# re.findall()方法找到正则表达式所匹配的所有子串，并返回一个列表，如果没有找到匹配的，则返回空列表。
print(re.findall('runoob', 'www.runoob.com'))    # 找到
print(re.findall('com', 'www.runoob.com'))       # 找到
print(re.findall('cn', 'www.runoob.com'))        # 没有找到

# re.split()方法按照能够匹配的子串将字符串分割后返回列表。
print(re.split(r'.', 'www.runoob.com'))          # 用.分割
print(re.split('o', 'www.runoob.com', 1))       # 用o分割，最多分割一次

# re.sub()方法用于替换字符串中的匹配项。
print(re.sub('runoob', 'google', 'www.runoob.com')) # 替换runoob为google
print(re.sub('o', 'a', 'www.runoob.com', 1))               # 替换第一个o为a

# re.compile()方法用于编译正则表达式，生成一个正则表达式（Pattern）对象，供其他函数使用。
# 编译后调用对应的方法时不用再给出正则字符串。
pattern = re.compile('runoob')            # 编译模式
m = pattern.search('www.runoob.com')     # 查找匹配项
print(m.span())                          # 返回匹配位置

# 在正则表达式中，如果直接给出字符，就是精确匹配。
# 除了可以直接匹配指定字符外，正则表达式还可以使用一些特殊字符来表示某一类字符。
# 可以使用以下字符进行精确匹配：
#   .可以匹配任意字符
#   \s可以匹配空格
#   \d可以匹配数字
#   \w可以匹配字母或数字
print(re.match('r...o', 'runoob').span())  # .匹配任意字符
print(re.match('r\sunoob', 'r unoob').span())  # \s匹配空格
print(re.match('r\dsunoob', 'r1sunoob').span())  # \d匹配数字
print(re.match('r\wsunoob', 'rAsunoob').span())  # \w匹配字母或数字

# 除了上面介绍的匹配单个字符的特殊字符外，正则表达式还提供了一些表示数量的特殊字符：
# 可以使用以下字符描述字符数量：
#   *表示前一个字符出现0次或多次
#   +表示前一个字符出现1次或多次
#   ?表示前一个字符出现0次或1次
#   {n}表示前一个字符出现n次
#   {n,m}表示前一个字符出现n到m次

print(re.match('r.*b', 'runoob').span())  # r开头，b结尾，中间任意字符
print(re.match('r.+b', 'runoob').span())  # r开头，b结尾，中间至少一个字符
print(re.match('r.?b', 'rb').span())      # r开头，b结尾，中间0个或1个字符
print(re.match('r\s+b', 'r   b').span())  # r开头，b结尾，中间至少一个空格
print(re.match('r\d+b', 'r123b').span())  # r开头，b结尾，中间至少一个数字
print(re.match('r\w{4}b', 'runoob').span())  # r开头，b结尾，中间3个字母或数字
print(re.match('r\w{2,4}b', 'runoob').span())  # r开头，b结尾，中间2到4个字母或数字

# 正则表达式的强大之处还在于它可以使用“或”操作符（|）来匹配多种可能性。
print(re.match('runoob|google', 'runoob').span())  #匹配runoob
print(re.match('runoob|google', 'google').span())  #匹配google

# 此外还有一些特殊的匹配方式：
#   ^表示字符串的开头
#   $表示字符串的结尾
#   []表示字符集
print(re.match('^runoob', 'runoob.com').span())  #开头匹配runoob
print(re.search('com$', 'runoob.com').span())    #结尾匹配com
print(re.match('[rR]unoob', 'runoob').span())    #匹配runoob或Runoob
print(re.match('[0-9][0-9][0-9]', '123abc').span())  #匹配3个数字
print(re.match('[a-zA-Z_][a-zA-Z0-9_]*', '_var123').span()) #匹配Python的合法变量名

# 用正则表达式切分字符串比用固定的字符更灵活
print('a b   c'.split(' '))                  # 普通的用空格分割，无法识别连续的空格
print(re.split(r'\s+', 'a b   c'))           # 用任意数量的空格分割
print(re.split(r'[\s\,\;]+', 'a,b;; c  d'))  # 用多种符号分割

# 除了简单地判断是否匹配之外，正则表达式还有提取子串的强大功能
m = re.match(r'(\w+) (\w+)(?P<sign>.*)', 'Hello World!!!') # 匹配句子
print(m.group(0))       # 匹配的整个字符串
print(m.group(1))       # 第1个括号匹配的子串
print(m.group(2))       # 第2个括号匹配的子串
m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345') # 匹配电话号码
print(m.group(1))       # 获取区号
print(m.group(2))       # 获取本地号码
# 使用(?P<name>...)命名的括号可以直接获取名字来获取匹配的子串
m = re.match(r'^(?P<area>\d{3})-(?P<number>\d{3,8})$', '010-12345')
print(m.group('area'))    # 获取区号
print(m.group('number'))  # 获取本地号码

# 正则匹配默认是贪婪匹配，也就是匹配尽可能多的字符。
print(re.match(r'^(\d+)(0*)$', '102300').groups())  # 贪婪匹配
# 加上?后变为非贪婪匹配
print(re.match(r'^(\d+?)(0*)$', '102300').groups())  # 非贪婪匹配


