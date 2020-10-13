#① len(str)：表示返回该字符串的长度；
print(len("cloveryml"))
#② str.count(sub,start=0,end=len(str)):表示返回sub在str里面出现的次数，如果start或者end指定则返回指定范围内sub出现的次数
name="cloveryml"
print(name.count("l"))
print(name.count("l",2))
print(name.count("l",2,5))
#③ str.startswith(prefix,start=0,end=len(str))表示检查字符串是否是以prefix开头，是则返回True,否则返回False。如果start和end 指定值，则在指定范围内检查。
name="cloveryml"
print(name.startswith("cl"))
print(name.startswith("m"))
print(name.startswith("m",2))
#④ Str.endswith(suffix,start=0,end=len(str))表示检查字符串是否是以suffix结束，是则返回True,否则返回False。如果start和end 指定值，则在指定范围内检查。
name="cloveryml"
print(name.endswith("yml"))
print(name.endswith("m"))
print(name.endswith("y",2,8))
#⑤ Str.find(sub,start=0,end=len(str))表示检查sub是否包含在字符串中str中，如果start和end指定范围，则检查是否包含在指定范围内，如果是则返回开始的索引值，否则返回-1
name="cloveryml"
print(name.find("yml"))
print(name.find("l",2))
print(name.find("m",2,8))
#⑦ Str.index(sub,start=0,end=len(str)):与find()方法一样，只不过如果sub不在str中会报一个异常
name="cloveryml"
print(name. index ("yml"))
print(name.index ("l",2))
print(name. index ("m",2,8))
#⑧ Str.rfind(sub,start=0,end=len(str)):与find()函数类似，不过是从右边开始查找
name="cloveryml"
print(name.rfind("yml"))
print(name.rfind("l",2))
print(name.rfind("l",2,8))
#⑨ Str.rindex(sub,start=0,end=len(str)):与index()函数类似，不过是从右边开始查找
name="cloveryml"
print(name. index ("yml"))
print(name.index ("l",2))
print(name. index ("w",2,8))
#⑩ Str.lstrip():默认删除字符串左边的空格
name="   cloveryml   "
print(name. lstrip())
#⑪Str.rstrip()默认删除字符串右边的空格
name="  cloveryml   "
print(name. rstrip())
#⑫ Str.strip()、:默认删除字符串左右两边的空格
print(name. strip())
#⑬ str.replace(old,new,max=str.count(old)):表示将字符串中的old替换成new,如果max指定，则替换不超过max次。
name="cloveryml"
print(name.replace("l","L",2))
#⑭ str.join(seq):以str作为分隔符，将seq中所有的元素合并为一个新的字符串
name="yim"
print("A".join(name))
#⑮ str.split(sub=””,num=str.count(obj)):表示以sub为分割符截取字符串，如果num有指定值，则截取num次
name="cloveryml"
print(name.split("l"))
#⑯ str.splitlines(keepends=False):表示安装行（”\r”,”\n”,”\r\n”）分割
name="clover\ny\rml"
print(name. splitlines())
#⑰str.isdigit():判断是否是纯数字字符串
a="1599855"
print(a.isdigit())
#⑱str.lower():将大写转换成小写
a="REWE4440rrr"
print(a.lower())
#⑲str.upper():将小写转换成大写
a="REWE4440rrr"
print(a.upper())
