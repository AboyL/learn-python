# inputResult = input('请输入内容:')
# print(inputResult)

x,y=1,2
print(x,y)


# 变量比较
print("ABC" > "ABD") # False
# print("ABC" >   123) # 报错
print(123.1 >   123) # True
print("123.0" > "123") # True
# print("123.0" > 123) # 报错
print("123.0" > '2') # False

# 成员运算符
x='x'
print(x in 'xzzzz') # True
print(x in 'zzz') # False

# 身份运算符
s = "abcdefg"
print(s[0]) # a
print(s[-1]) # g
print(s[1:5:2]) # bd
print(s[1:5]) # bcde

# 字符串的函数
"xyzxyzxyz".count('x') # 3
"xyzxyzxz".count('xy') # 2
"xyzxyzxz".count('a') # 0
"xyzxyzxz".isalnum() # True
",".join("abcdefg") # a,b,c,d,e,f,g
"a,b,c,d".split(",")    # ['a', 'b', 'c', 'd']
"xyz".startswith("y") # False


# 数字
print(1+2) # 3
print(1-2) # -1
print(1*2) # 2
print(5/15) # 0.3333333333333333
print(5//15) # 0
print(5%15) # 5
print(15%5) # 0
