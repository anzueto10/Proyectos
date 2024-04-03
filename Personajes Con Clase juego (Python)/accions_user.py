from create_characters import create_new_character as create, delete_character as delete, fusion_characters_function_pass as fusi_char


#Estos son las acciones del usuario
def edit_character_data(character,pass_value,pass_value2):
    while not pass_value2:
        action = input("Do you wanna edit some feature of your character?, Y/N: ").lower()
        if action == "y": 
            while True:
                features = vars(character)
                print("\n")
                for key in features:
                    print(f"{key.capitalize()}")
                action = input("What feature do you wanna edit?, enter the feature name, example(Name): ").lower()
                if action in features:
                    valid = False
                    character.set_character_data(action,valid)
                    pass_value = True 
                    pass_value2 = True 
                    break
                else:
                    print("Please, enter a valid feature.")
        elif action == "n": 
            pass_value = True 
            pass_value2 = True
            break
        else: print("Please, enter a valid instruccion.")
    return pass_value,pass_value2

def show_actual_characters(cl):
    print("----CHARACTERS----")
    for i,character in enumerate(cl):
        print(f"{i+1}.{character.name}")
    print("----CHARACTERS----")
    return character

def see_characters_data(cl): 
    pass_value = False
    pass_value2 = False
    while not pass_value:
        character = show_actual_characters(cl)
        action = input("See the character: ")
        try:
            action = int(action) - 1
            if 0 <= action < len(cl):
                character = cl[action] 
                print(character.show_data())
                pass_value, pass_value2 = edit_character_data(character,pass_value,pass_value2)
            else:print("Enter a valid number of character.")
        except: print("Please, enter a valid instruccion.")

def create_characters(cl): 
    import get_data as get
    character_data = get.get_input_the_user_the_data()
    create(cl,*character_data)

def delete_characters(cl):
    pass_valid = False
    while not pass_valid:
        confirm = input("Are you sure from delete some character, Y/N: ")
        confirm = confirm.lower()

        if confirm == "y": 
            while True:
                show_actual_characters(cl)
                action = input("What character do you wanna delete?: ")
                try:
                    action = int(action) - 1
                    if 0 <= action < len(cl):
                        character = cl[action]
                        delete(character)
                        print("Your character was deleted succesfly uwu.")
                        pass_valid = True
                        break
                    else:print("Enter a valid number of character.")
                except: print("Please, enter a valid instruccion")
        elif confirm == "n": break
        else: print("Please, enter a valid instruccion.")

def fusion_characters(cl):
    confirm_y_n(cl,"Are you sure of fusion your characters?: Y/N: ", fusi_char)
    
def confirm_y_n(cl,msg,pass_function):
    result = None
    show_actual_characters(cl)
    pass_valid = False
    while not pass_valid:
        confirm = input(msg)
        confirm = confirm.lower()
        if confirm == "y":
            result, pass_valid = pass_function(cl)
            return result, pass_valid
        elif confirm == "n": break
        else: print("Please, enter a valid instruccion.")

def exit_save(): 
    import character_list as exit
    exit.exit_game = True