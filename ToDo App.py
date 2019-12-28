# ToDO app will perform following ations
#1.Add Tasks
# 2.View Tasks
# 3.Delete Tasks
# 4.Terminate App
def isInteger(inputCommand):
    try:
        int(inputCommand)
        return True
    except ValueError:
        return False
def addtask(taskdictionary):
    print("\n--------------------------\n        Adding Tasks\n--------------------------\n")
    itemindex=len(taskdictionary)+1
    itemname=input("Task #{} ".format(itemindex))
    taskdictionary.update({itemindex:itemname})
    print("Your Task #{} has Successfully Added".format(itemindex))
def viewtask(taskdictionary):
    print("\n--------------------------\n        Viewing Task\n--------------------------\n")
    if len(taskdictionary)>0:
        for itemindex,itemname in taskdictionary.items():
            print("Task #{} : {}".format(itemindex,itemname))
    else:
        print("Your Dictionary is Empty")
def deletetask(taskdictionary):
    print("\n--------------------------\n        Delete Tasks\n--------------------------\n")
    if len(taskdictionary)>0:
        for itemindex,itemname in taskdictionary.items():
            print("Task #{} : {}".format(itemindex,itemname))
        userindex=int(input("Enter the index which you want to Remove e.g 1,2,3"))
        if userindex in taskdictionary.keys():
            taskdictionary.pop(userindex)
            print("Task #{} has succesfully removed".format(userindex))
        else:
            print("Invalid Index Try Again")
    else:
        print("No Task Found")

makedictionary={
    1:"Add Tasks",
    2:"View Tasks",
    3:"Delete Tasks",
    4:"Terminate App"
}
taskdictionary={ }
while True:
    print("\n--------------------------\n        Main Menu\n--------------------------\n")
    print("Options")
    for key,value in makedictionary.items():
        print(key,value)
    command=input("Enter The Command Which want to Perform ")
    if isInteger(command)== True:
        taskcommand=int(command)
        if taskcommand>0 and taskcommand<=4:
            if taskcommand==1:
                addtask(taskdictionary)
            if taskcommand==2:
                viewtask(taskdictionary)
            if taskcommand==3:
                deletetask(taskdictionary)
            if taskcommand==4:
                break
        else:
            print("Invalid Command")
    else:
        print("Invalid Command")
