import clases as c

#Para crear un personaje y ponerlo y así

def create_new_character(cl,name,age,gender,power,raze):
    #Verify de raze
    if raze == "Arcont":
        character = c.Arcont(name,age,gender,power,raze)
        set_the_character_list(character,cl)
    elif raze == "Tanoki":
        character = c.Tanoki(name,age,gender,power,raze)
        set_the_character_list(character,cl)
    elif raze == "Human":
        character = c.Human(name,age,gender,power,raze,"Rich","uwu")
        set_the_character_list(character,cl)

def create_new_fusion(cl,name,age,gender,power,razes):
    character = c.Fusion(name,age,gender,power,razes)
    set_the_character_list(character,cl)
    
    
def set_the_character_list(c,cl):
    cl.append(c)
    print("Your character was Upload succesfly")
    return cl

def delete_character(c):
    from character_list import character_list as cl
    for i, char in enumerate(cl):
        if char is c:
            cl.remove(cl[i])
            del c
            break    

def fusion_characters_function_pass(cl):
        from verify_data import verify_fusion_characters as veri_fusi 
        valid = False
        c1 = None
        while not valid:
            c1 = input("Select a character: ")
            c1,valid = veri_fusi(c1,cl)

        valid = False
        c2 = None
        while not valid:
            c2 = input("Select another character: ")
            c2,valid = veri_fusi(c2,cl)
        char1 = cl[c1]
        print(f"Character 1 to fusion: {char1.name}")
        char2 = cl[c2]
        print(f"Character 2 to fusion: {char2.name}")
        while True:
            acc = input("Are you sure of fusion your characters?: Y/N: ")
            acc = acc.lower()
            if acc == "y": 
                new_character = char1 + char2
                create_new_fusion(cl, *new_character)
                break
            elif acc == "n": break
            else: print("Please, enter a valid instruccion.")
        