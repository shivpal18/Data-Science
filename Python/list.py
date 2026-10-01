# a = [12,13,14,15,16,24.5]
# # print(a[-2])
# for i in range(len(a)):
#     print(a[i])



numbers = [5,2,9,1,5,6]

numbers.append(10)    #Adds 10 to the end
numbers.insert(2,15)    #inserts 15 at index 2
numbers.extend([20,25,30])    #Adds multiple elements at the end
numbers.remove(5)    #Remove the first occurence of 5
popped_item = numbers.pop(3)   #removes and store the element at index 3
index = numbers.index(6)    #Finds the index of 6
count_5 = numbers.count(5)    # counts occurence of 5
numbers.sort()    #sort the list in ascending order
numbers.reverse()    #reverse the list order
new_numbers = numbers.copy()    # creates a copy of list
numbers.clear()    #removes all elements from the list
