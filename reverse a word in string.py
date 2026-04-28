s = "Hello World How Are You"
words = s.split()
result=""
for word in words:
    result=word+" "+result
print(result.strip())