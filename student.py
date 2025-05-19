class Student:
    name = ""
    age = 0
    sex = ""
    score = 0

tivadar = Student()

print(tivadar)

tivadar.name = "El tivadar"
tivadar.age = 16
tivadar.sex = "male"
tivadar.score = 20

print(f"név :{tivadar.name} kor: {tivadar.age} score : {tivadar.score}")