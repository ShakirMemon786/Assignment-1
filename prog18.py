str1="shakir is god"

max_string=max(str1.split(), key=len)
print("the maximum string is",max_string)

min_string=min(str1.split(), key=len)
print("the minimum string is",min_string)
print("the orignal string is",str1)

