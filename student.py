class Student():

#konstruktor az osztaly peldanyositasahoz
    def __init__(self, name, sex, age = 0):
        self.name = name
        self.age = age
        self.sex = sex
        self.score = 10

    
    
    
    def introduce(self):
        print(f"név :{self.name} kor: {self.age} score : {self.score}")
    def learn(self, points):
        self.score += points




tivadar = Student("El tivadar", 16, "male")
leila = Student("leila ", "female")



#print(f"név :{tivadar.name} kor: {tivadar.age} score : {tivadar.score}")

tivadar.introduce()
tivadar.learn(12)
tivadar.introduce()


leila.introduce()
leila.learn(-2)
leila.introduce()