print("---welcome to GT task manager---")
task1=""
task2=""
task3=""
task4=""
task5=""
task=[task1,task2,task3,task4,task5]
print("---welcome to GT task manager---")
i= 0
while True:
    num=int(input("choose ur number (1-4):\n 1.add task\n 2.view tasks\n 3.delete task\n 4.exit \n enter ur choice: "))
    print("1.add task\n 2.view tasks \n 3.delete task \n 4.exit")
    if num==1:
        task_name = input("enter task name: ")
        if task1=="":
            task1=task_name
            print("task added\n")
        elif task2=="" and task1!="":
            task2=task_name
            print("task added\n")
        elif task3=="" and task2!="":
            task3=task_name
            print("task added\n")
        elif task4=="" and task3!="":
            task4=task_name
            print("task added\n")
    print("\n")
    if num==2:
        print("---your tasks are:")
        for t in task:
            if t!="":
                i+=1
                print(f"{i}. {t}")
                print("complet delete!!")
    if num==3:
        num=int(input("enter task number to delete: "))
        print("task")
        num+=1
        task.pop(num-1)
    if num==4:
        print("exiting task manager")
        break