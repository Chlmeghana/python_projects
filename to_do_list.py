tasks=[]
while True:
    print("1.Display your Tasks\n2.Add a Task\n3.Mark a task as done\n4.exit\n")
    c=int(input("enter choice: \n"))
    if(c==1):
        if tasks:
            p=1
            for i in tasks:
                if(i["completed"]):
                    x="Done"
                else:
                    x="Not Done"
                print(p,i["title"],x)
                p+=1
        else:
            print("No tasks")
    elif(c==2):
        name=input("enter Name of the task: ")
        d={"title":name,"completed":False}
        tasks.append(d)
    elif(c==3):
        if tasks:
            for i in tasks:
                if(i["completed"]):
                    x="Done"
                else:
                    x="Not Done"
                print(i["title"],x)
        n=int(input("Enter no. of the task: "))
        n-=1
        tasks[n]["completed"]=True 
    elif(c==4):
        print("exiting...")
        break 
    else:
        print("wrong choice")