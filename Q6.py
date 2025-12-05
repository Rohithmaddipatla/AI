list = [10, 20, 30]
print("Original List:", list)

list.append(40)
print("After append(40):", list)

list.extend([50, 60])
print("After extend([50, 60]):", list)

list.insert(1, 15)  
print("After insert(1, 15):", list)

list.remove(30)
print("After remove(30):", list)

list.pop(2)   
print("After pop(2):", list)

del list[0]
print("After del list[0]:", list)