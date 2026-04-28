s = "aple"

if len(set(s)) < len(s):
    print(s, "is a dejavu")
else:
    print(s, "is not a dejavu")

#
# s = "aple"
# dejavu = False
#
# for i in range(len(s)):
#     for j in range(i+1, len(s)):
#         if s[i] == s[j]:
#             print(s, "is a dejavu")
#             dejavu = True
#             break
#     if dejavu:
#         break
#
# if not dejavu:
#     print(s, "is not a dejavu")