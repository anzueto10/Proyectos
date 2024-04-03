from accions_user import see_characters_data as see_char, create_characters as create_char, delete_characters as del_char, fusion_characters as fusion_char, exit_save as exit

#Para verificar que los datos estén correctos
def verify_name(name):
    if len(name) > 30: return "The name can't be 30 letters or more"
    else: return True

def verify_age(age):
    try:
        age = int(age)
        return True
    except:
        return "The age is not valid, enter a number only"
    
def verify_gender(gender):
    gender = gender.lower()
    if gender == "m" or gender == "w" or gender == "nb" or gender == "fg": 
        if gender == "m": return True, "Man"
        elif gender == "w": return True, "Woman"
        elif gender == "nb": return True, "No Binarie"
        elif gender == "fg": return True, "Fluid Gender"
    else: return "The gender is not valid, enter a valid input", ""

def verify_power(power):
    try:
        power = int(power)
        if power > 30000: return "The power level exceeds what is established, enter a valid power"
        elif power <= 0: return "The power can't be 0 or negative"
        else: return True
    except: return "Please, enter a valid power, only numbers"

def verify_raze(raze):
    raze = raze.lower()
    if raze == "a" or raze == "t" or raze == "h":
        if raze == "a": return True, "Arcont"
        elif raze == "t": return True, "Tanoki"
        elif raze == "h": return True, "Human"
    else:  return "The raze is invalid, enter a valid raze", ""

def verify_fusion_characters(c,cl):
    try: 
        c = int(c) - 1
        if 0 <= c < len(cl): return c,True
        else: print("Please, enter a valid character.")
    except: print("Please, enter a valid character.")
    

def verify_accion(ac,cl):
    try:   
        ac = int(ac)
        if ac == 1: see_char(cl)
        if ac == 2: create_char(cl)
        if ac == 3: del_char(cl)
        if ac == 4: fusion_char(cl)
        if ac == 5: exit()
    except: return "That is an invalid instruccion"