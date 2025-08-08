#create a list
My_List = []

#Append elements to the list
My_List.append(10)
My_List.append(20)
My_List.append(30)
My_List.append(40)

#print(My_List)

#Insert an element at a specific position
My_List.insert(2, 15)

#Extend the list with multiple elements
My_List.extend([50, 60, 70])

# Remove the last element
My_List.pop() 

# Sort the list
My_List.sort()

pos = My_List.index(30)
print("Position of 30 in the list:", pos)
