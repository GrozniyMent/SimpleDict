#CustomDict v1.0.1
#By Ratushnyak A.E.

#----Init----#

print("///////////////////////////////////////")
print("//                                   //")
print("//            Simple Dict            //")
print("//         By Ratushnyak A.E         //")
print("//                                   //")
print("///////////////////////////////////////")
print("//                                   //")
print("//              Github               //")
print("//                                   //")
print("// github.com/GrozniyMent/SimpleDict //")
print("//                                   //")
print("///////////////////////////////////////")

#----Script----#
global ls
ls = list()

print("Enter \"append\" to add new element to your dictionary\nEnter \"display\" to display your dictionary\nEnter \"remove\" to remove any element of your dictionary")

def writeData():
    t1 = input("Word:")
    t2 = input("Translate:")

    ls.append(t1)
    ls.append(t2)

def displayData():
    print(ls)

def removeData():
    index = len(ls)
    int(index)
    i = 0
    for i in range(0, index):
        print(f"{i}. {ls[i]}")
    ch = input("Enter number of element which you want to remove:")
    ch = int(ch)
    if ch <= index:
        removedElement = ls.pop(ch)
        print(f"You successfully removed element \"{removedElement}\"")

def cmd():
    con = input("mydict@admin ~$ ")
    if con == "append":
        writeData()
    elif con == "display":
        displayData()
    elif con == "remove":
        removeData()
    else:
        cmd()

cmd()
