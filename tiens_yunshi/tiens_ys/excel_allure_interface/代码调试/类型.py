result = 3 * 4
print(result)
lis= [1 , 2] * 2
lis1= [1 + 2] * 2
print(lis,lis1)
str = "abc"*3
str1 = 'abc'+'3'
print(str,str1)
dict1 = {'a' : 1,'b' : 2}
dict2 = {'a' : 3,'c' : 4}
dii = {**dict1,**dict2}#**代表解包，直接拿到他的值
print(dii)
def func(a,b,c):
    print(a,b,c)

args = ('abc', 'b', '3')
func(*args)  # 等价于 func(1, 2, 3)
