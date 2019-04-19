def odd_values_string(str):
  result = "" 
  for i in range(len(str)):
    if i % 2 == 0:
      result = result + str[i]
  return result

print("after removing answer is",odd_values_string('abcdef'))
print("after removing answer is",odd_values_string('python'))
