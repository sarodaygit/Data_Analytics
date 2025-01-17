# Python file: array_list_tuple_operations.py

### 2. Lists ###

# Creating a List
lst = [10, 20, 30, 40, 50]
print("List:", lst)

# Inserting into List
lst.insert(3, 35)  # Insert 35 at index 3
print("List after insertion:", lst)

# Appending to List
lst.append(60)  # Append 60 to the end
print("List after appending:", lst)

# Deleting from List
lst.remove(35)  # Remove the element 35
print("List after deletion:", lst)

# Indexing in List
print("Element at index 2:", lst[2])

# Slicing a List
print("List slice [2:5]:", lst[2:5])

# Length of List
print("Length of list:", len(lst))

# List Concatenation
lst2 = [70, 80, 90]
lst += lst2
print("List after concatenation:", lst)

# List Comprehension (Creating a list based on a condition)
even_numbers = [x for x in lst if x % 2 == 0]
print("Even numbers from the list:", even_numbers)

# Traversing the List
print("Traversing the list:")
for element in lst:
    print(element, end=' ')
print("\n")

