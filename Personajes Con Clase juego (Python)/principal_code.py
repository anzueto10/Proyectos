import get_data as get
from verify_data import verify_accion as veri
from create_characters import create_new_character as creates

#Juego que te permite registrar a tus personajes

#SISTEMA PARA INTERACTUAR CON EL USER


def start_game():
    import character_list as cl
    start_game_v = False
    accion = None
    do_something = False
    interact_with_the_user(cl.character_list, start_game_v, accion, do_something)
    

def interact_with_the_user(character_list,start_game_v,accion,do_something):
    character_data = get.get_input_the_user_the_data()
    creates(character_list, *character_data)
    start_game_v = True
    import character_list as exit
    while not exit.exit_game:
        if start_game_v == False: get.get_the_data_from_character(start_game_v)
        else:
            accion = input("""
---------------What you wanna do?
1. See my characters
2. Create a Character
3. Delete a Character
4. Fusion Characters
5. Exit & Save
                           :""")
            do_something = veri(accion,character_list)
            if do_something == False: print(do_something)

start_game()