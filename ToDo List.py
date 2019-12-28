# Todo App using List
# Options
# 1.Add items
# 2.Delete Items
# 3.Delete All items
# 4.Exit From App

todolist=[]
print("\n--------------------------\n        Main Menu\n--------------------------\n")
print("1.Add items\n2.Delete Items\n3.Delete All items\n4.Exit From App")
while True:
    userinput=input("Enter The Command which you want to Perform like 1,2,3,4 ")
    if  userinput=="1":
        print("\n--------------------------\n        Adding Item\n--------------------------\n")
        item=input("Enter the New Item ")
        todolist.append(item)
        print("Your item has Been Successfully Added ",todolist)
    elif userinput=="2":
        print("\n--------------------------\n        Deleting Item\n--------------------------\n")
        if len(todolist)>0:
            print(todolist)
            item=input("Which Item Do You want to Delete")
            if item in todolist:
                todolist.remove(item)
                print("Your Item has been Successfully removed ",todolist)
            else:
                print("Item Not Found")
        else:
            print("No Item Found")
    elif userinput=="3":
        if len(todolist)>0:
            todolist.clear()
            print("Your List is Now Clear you Can Check ",todolist)
        else:
            print("Your List is already Empty")
    elif userinput=="4":
        break
    else:
        print("Invalid Command try Again")
