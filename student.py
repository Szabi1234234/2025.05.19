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








#print(f"név :{tivadar.name} kor: {tivadar.age} score : {tivadar.score}")

