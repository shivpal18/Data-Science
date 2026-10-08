# s={1,2,3,4,5,4}
# print(s)



# b=hash("hello")
# print(b)

# c=hash((1,2,3,4))
# print(c)



# a={1,2,8,3,4,5}
# for i in a:
#     print(i)



# a={1,2,3,4,5}
# # a.remove(2)
# # a.pop()
# a.clear()
# print(a)



a={1,2,3,4,5}
b={4,5,6,7,8}

# s=a.union(b)
# s=a.intersection(b)
# s=a.difference(b)
# s=b.difference(a)
# s=b-a
s=b^a

print(s)