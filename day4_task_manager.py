tasks=["写作业","xvexiPython"]

def show_tasks(tasks):
    print("\n当前任务：")
    for i,task in enumerate(tasks):
        print(i+1,task)

#先展示任务
show_tasks(tasks)

#添加新任务
new_task=input ("\n请输入新任务:")
tasks.append(new_task)

#再展示一次
show_tasks(tasks)

while True:
    show_tasks(tasks)
    new_task=input("请输入新任务（输入q退出）：")

    if new_task=="q":
        break
    tasks.append(new_task)