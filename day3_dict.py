student={
    "name":"panmeiye",
    "age":19,
    "major":"Computer Science"
}
for key,value in student.items():
    print(key,":",value)

if student["age"] >=18:
    print("成年人")
else:
    print("未成年人")

exec(open("d:/Python-code/python-learning/day3_dict.py").read())
