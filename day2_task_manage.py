def show_tasks(task):
    print("今天的任务：")

    for i,task in enumerate(task):
        print("任务",i+1,":",task)

tasks=["写作业","学习Python","健身"]

show_tasks(tasks)