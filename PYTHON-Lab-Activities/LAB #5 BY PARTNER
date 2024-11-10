color = ["black", "white", "yellow"]

print("Menu: ")
print("1. Insert")
print("2. Search")
print("3. Update")
print("4. Remove")

choice = int(input("Enter choice: "))
if choice == 1:
    color1 = input("Enter item: ")
    index = int(input("Index: "))
    color.insert(index, color1)
    print(color)

if choice == 2:     
    find = input("Find: ")
    if find in color:
        x = color.index(find)
        print(find, "is at index", x)

if choice == 3:
    update = input("Update: ")
    newValue = input("New Value: ")
    y = color.index(update)
    color[y] = newValue
    print(color)

if choice == 4:
    remove = input("Remove: ")
    z = color.index(remove)
    color.pop(z)
    print(color)

#WITH LOOPING STATEMENT
color = ["black", "white", "yellow"]

i = 0
while i < 6:
    print("Menu: ")
    print("1. Insert")
    print("2. Search")
    print("3. Update")
    print("4. Remove")
    print("5. Exit")

    choice = int(input("Enter choice: "))
    if choice == 1:
        color1 = input("Enter item: ")
        index = int(input("Index: "))
        color.insert(index, color1)
        print(color)

    elif choice == 2:     
        find = input("Find: ")
        if find in color:
            x = color.index(find)
            print(find, "is at index", x)
        else:
            print(find, "is not included :((")

    elif choice == 3:
        update = input("Update: ")
        newValue = input("New Value: ")
        y = color.index(update)
        color[y] = newValue
        print(color)

    elif choice == 4:
        remove = input("Remove: ")
        z = color.index(remove)
        color.pop(z)
        print(color)

    elif choice == 5:
        break
    
    else:
        print("Invalid")
