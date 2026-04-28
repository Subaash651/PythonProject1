from ftplib import print_line

#String reverse
name = "Subaash"
rev = name[::-1]
print(rev)


#Integer reverse
s =987654321
a = list(str(s))
a = a[::-1]
for i in a:
    print(i,end="")