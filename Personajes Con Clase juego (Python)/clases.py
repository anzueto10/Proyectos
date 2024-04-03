from abc import ABC, abstractmethod

#Clase para los personajes:
class Character(ABC):
    @abstractmethod
    def __init__(self,name,age,gender,power,raze):
        self.name = name
        self.age = age
        self.gender = gender
        self.power = power
        self.raze = raze
    
    def talk(self):
        print(f"Hello, my name is {self.name}, I'm {self.age} years old. I'm a {self.gender} and my level power is {self.power}")
    
    def attack(self,other):
        print(f"{self.name} is attacking to {other.name} with {self.power} of power")
    
    def show_data(self):
        data = self.get_character_data
        name,age,gender,power = data
        return f""" 
----STATS----
    
    Name: {name}
    Age: {age}
    Gender: {gender}
    Power: {power}

----STATS----
              """

    #Métodos
    def __add__(self,other):
        from create_characters import delete_character as dele
        new_name = self.name + other.name
        new_age = int(self.age) + int(other.age)
        if self.gender == other.gender:
            new_gender = "Woman"
        elif self.gender == other.gender:
            new_gender = "Man"
        else:
            new_gender = "No Binarie"
        new_power = int(self.power) + int(other.power)
        razes = f"{self.raze} {other.raze}"
        dele(self)
        dele(other)
        print("Your characters were fusion succesfly.")
        return new_name, new_age, new_gender, new_power, razes

    
    @property
    def get_character_data(self): return self.name,self.age,self.gender,self.power

    def set_character_data(self,attribute,v):
        import get_data as get
        if attribute == 'name':
            self.name = get.get_name_data(v)
        elif attribute == 'age':
            self.age = get.get_age_data(v)
        elif attribute == 'gender':
            self.gender = get.get_gender_data(v)
        elif attribute == 'power':
            self.power = get.get_power_data(v)
        else:
            print(f"Attribute '{attribute}' not recognized")
    
#Hay 3 clases, humanos, arcontes y tanokis

class Human(Character):
    def __init__(self,name,age,gender,power,raze,economy,work):
        super().__init__(name,age,gender,power,raze)
        self.econmy = economy
        self.work = work

    def working(self):
        print(f"{self.name} is working on {self.work}")
    
    def buy(self):
        print(f"{self.name} will buy a thing")

class Arcont(Character):
    def __init__(self,name,age,gender,power,raze,naccion,element):
        super().__init__(name,age,gender,power,raze)
        self.naccion = naccion
        self.element = element
    
    def get_character_data(self): return self.name,self.age,self.gender,self.power,self.naccion,self.element

    def show_data(self):
        data = self.get_character_data()
        name,age,gender,power,naccion,element = data
        print(f""" 
----STATS----
    
    Name: {name}
    Age: {age}
    Gender: {gender}
    Power: {power}
    Nacion: {naccion}
    Element: {element}

----STATS----
              """)
    

class Tanoki(Character):
    def __init__(self,name,age,gender,power,raze,velocity,fly_capacity):
        super().__init__(name,age,gender,power,raze)
        self.vel = velocity
        self.fly = fly_capacity
    
    def fly_character(self):
        print(f"{self.name} is flying at {self.fly} on the ground")

    def get_character_data(self): return self.name,self.age,self.gender,self.power,self.vel,self.fly

    def show_data(self):
        data = self.get_character_data()
        name,age,gender,power,velo,fly = data
        print(f""" 
----STATS----
    
    Name: {name}
    Age: {age}
    Gender: {gender}
    Power: {power}
    Velocity: {velo}
    Fly Capacity: {fly}

----STATS----
              """)
        
class Fusion(Character):
    def __init__(self,name,age,gender,power,razes):
        super().__init__(name,age,gender,power,razes)
        self.razes = razes
    
