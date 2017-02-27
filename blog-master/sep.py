sep = [11,2,4,5,6,7,89,0,44,66,77,88,99]
print filter(lambda x:x % 2,sep)

print [x for x in sep if x % 2]

print [(x + 1,y + 1)for x in range(3) for y in range(5)]