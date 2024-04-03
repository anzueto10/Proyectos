import verify_data as veri

#Obtener la data que ingrea el usuario
def get_name_data(valid):
    while valid == False:
        character_name = input("Enter the name from your character: ")
        valid = veri.verify_name(character_name)
        if valid != True:
            print(valid)
            valid = False
    return character_name

def get_age_data(valid):
    while valid == False:
        age_character = input("Enter the age from your character, only numbers: ")
        valid = veri.verify_age(age_character)
        if valid != True:
            print(valid)
            valid = False
    return age_character

def get_gender_data(valid):
    while valid == False:
        gender_character = input("Enter the gender from your character: W for women, M for men, NB for No Binarie, FG, por fluid gender: ")
        valid, gender_character = veri.verify_gender(gender_character)
        if valid != True:
            print(valid)
            valid = False
    return gender_character

def get_power_data(valid):
    while valid == False:
        power_character = input("Enter the power from your character, enter numbers, maximum 30,000 of power: ")
        valid = veri.verify_power(power_character)
        if valid != True:
            print(valid)
            valid = False
    return power_character

def get_raze_data(valid):
    while valid  == False:
        raze_character = input("What raze will be your character? A for Arcont, H for Human, T for Tanoki: ")
        valid,raze_character = veri.verify_raze(raze_character)
        if valid != True:
            print(valid)
            valid = False
    return raze_character


#Esto no lo terminé
def get_economy_data(valid): pass

def get_work_data(valid): pass

def get_naccion_data(valid): pass

def get_element_data(valid): pass

def get_velocity_data(valid): pass

def get_fly_data(valid): pass

def get_extra_raze_data(r,valid):
    if r == "Tanoki":
        get_velocity_data(valid)
        get_fly_data(valid)
    elif r == "Human":
        get_economy_data(valid)
        get_work_data(valid)
    elif r == "Arcont":
        get_naccion_data(valid)
        get_element_data(valid)

def get_the_data_from_character():
        valid = False
        #El usuario ingresa los nombres y son verificados para ver si son válidos    
        character_name = get_name_data(valid)
        valid = False

        age_character = get_age_data(valid)
        valid = False

        gender_character = get_gender_data(valid)
        valid = False

        power_character = get_power_data(valid)   
        valid = False
            
        raze_character = get_raze_data(valid)
        get_extra_raze_data(raze_character,valid)
                
        return character_name, age_character, gender_character, power_character, raze_character

def get_input_the_user_the_data():
    character_data = get_the_data_from_character()
    return character_data