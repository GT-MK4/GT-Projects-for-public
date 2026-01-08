## code work 100%
print("---welcome to GT task manager---")
tasks=[]
while True:
    i=0
    num=input("\n choose ur number (1-4):\n 1.add task\n 2.view tasks\n 3.delete task\n 4.exit \n enter ur choice: ")
    if num=="1":
        new_task = input("enter task name: ")
        tasks.append(new_task)
        print("task add ")
    if num=="2":
        print("---your tasks are:")
        for t in tasks:
            if t!="":
                i+=1
                print(f"{i}. {t}")
        print("\n this all tasks")
    if num=="3":
        i=0
        for t in tasks:
            if t!="":
                i+=1
                print(f"{i}. {t}")
        numdel=int(input("enter task number to delete: "))
        numdel-=1
        tasks.pop(numdel)
        print("complet delete !!")
    if num=="4":
        print("exiting task manager")
        break
    elif num!="1" and num!="2" and num!="3" and num!="4" :
        print("sorry you can just choose number (1-4)")
 