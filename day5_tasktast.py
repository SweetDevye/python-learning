tasks=["吃饭","学习Python","健身","家教"]
def show_tasks(tasks):
    print("今天任务：")
    for i,task in enumerate(tasks):
        print(i+1,task)


#while循环一直添加任务
while True:
    show_tasks(tasks)
    choice=input("/n输入新任务(输入q退出,输入d删除任务）：")
    
    if choice=="q":
        break
   
    
    elif choice=="d":
        num=int(input("请输入要删除的任务编号："))
        tasks.pop(num-1)
        print("任务删除成功")

    else:
        tasks.append(choice)