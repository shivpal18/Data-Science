# a = [12,13,14,15,16,24.5]
# # print(a[-2])
# for i in range(len(a)):
#     print(a[i])



# numbers = [5,2,9,1,5,6]

# numbers.append(10)    #Adds 10 to the end
# numbers.insert(2,15)    #inserts 15 at index 2
# numbers.extend([20,25,30])    #Adds multiple elements at the end
# numbers.remove(5)    #Remove the first occurence of 5
# popped_item = numbers.pop(3)   #removes and store the element at index 3
# index = numbers.index(6)    #Finds the index of 6
# count_5 = numbers.count(5)    # counts occurence of 5
# numbers.sort()    #sort the list in ascending order
# numbers.reverse()    #reverse the list order
# new_numbers = numbers.copy()    # creates a copy of list
# numbers.clear()    #removes all elements from the list



# l=[1,2,3,4,5]
# l[0]=10
# print(l)



# l=[-45,67,12,-68,-69,34]
# print("Positive elements are ")
# for i in l:
#     if i>=0:
#         print(i)
# print("Negative elements are")
# for i in l:
#     if i<0:
#         print(i)



# l=[12,45,69,89,23,25,69]
# sum = 0
# for i in l:
#     sum = sum + i

# print(sum/len(l))



# l=[12,34,547,456,358,654]

# largest = l[0]
# index = 0

# for i in range(len(l)):
#     if l[i] > largest:
#         largest = l[i]
#         index = i

# print(f"your largest number is {largest} at index {index}")



# l=[12,16,13,19,17]
# largest=l[0]
# sec_largest=l[0]

# for i in l:
#     if i> largest:
#         sec_largest = largest
#         largest=i
#     elif i>sec_largest:
#         sec_largest=i

# print(sec_largest, largest)



a=[12,13,14,15,16]
for i in range(len(a)-1):
    if a[i]<a[i+1]:
        continue
    else:
        print("your list is not sorted")
        break
else:
    print("your list is sorted")