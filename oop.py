class Person:
    def __init__(self, name, age , gender):
        self.name = name 
        self.age= age 
        self.gender = gender
        
    def introduce(self):
        print(f"Hello my name is {self.name} and I am {self.age} years old , and i am a {self.gender}")        # 

# Creating the Instance of the Person class 
person = Person("frankline omari", 21 , "male") 

# calling the method to display the person's information 

person.introduce()