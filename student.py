class Student:
    name = ""
    age = 0
    sex = ""
    score = 0

    def introduce(self):
        print(f"név :{self.name} kor: {self.age} score : {self.score}")
    def learn(self, points):
        self.score += points




tivadar = Student()

#print(tivadar)

tivadar.name = "El tivadar"
tivadar.age = 16
tivadar.sex = "male"
tivadar.score = 20

#print(f"név :{tivadar.name} kor: {tivadar.age} score : {tivadar.score}")

tivadar.introduce()
tivadar.learn(12)
tivadar.introduce()