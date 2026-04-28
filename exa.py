from operator import indexOf

l = [1,2,3,8,7,6,9,4,5]
le=int(len(l)/2)
spt_var = l[0:le]
end_var = l[le::]
final = end_var[::-1]

print(spt_var + final)

