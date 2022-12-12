import random

print( "\
   ___   ___   ___   ___    ___     _       ___     _     ___   ___   _         ___      _____   ___      _   ___   ___     _  \n \
 | _ \ |_ _| | __| |   \  | _ \   /_\     | _ \   /_\   | _ \ | __| | |       / _ \    |_   _| |_ _|  _ | | | __| | _ \   /_\  \n \
 |  _/  | |  | _|  | |) | |   /  / _ \    |  _/  / _ \  |  _/ | _|  | |__    | (_) |     | |    | |  | || | | _|  |   /  / _ \ \n \
 |_|   |___| |___| |___/  |_|_\ /_/ \_\   |_|   /_/ \_\ |_|   |___| |____|    \___/      |_|   |___|  \__/  |___| |_|_\ /_/ \_\ \n ")
print("Este juego es al mejor de 3 partidas!")
#funcion para elegir 
def choose_options():
  options = ('piedra', 'papel', 'tijera')
  user_option = input('piedra, papel o tijera => ')
  user_option = user_option.lower()

  if not user_option in options:
    print('esa opcion no es valida')
    # continue
    return None, None

  computer_option = random.choice(options)

  print('User option =>', user_option)
  print('Computer option =>', computer_option)
  return user_option, computer_option

#funcion para revisar reglas
def check_rules(user_option, computer_option, user_wins, computer_wins):
  if user_option == computer_option:
    print('Empate!')
  elif user_option == 'piedra':
    if computer_option == 'tijera':
      print('piedra gana a tijera')
      print('user gano!')
      user_wins += 1
    else:
      print('Papel gana a piedra')
      print('computer gano!')
      computer_wins += 1
  elif user_option == 'papel':
    if computer_option == 'piedra':
      print('papel gana a piedra')
      print('user gano')
      user_wins += 1
    else:
      print('tijera gana a papel')
      print('computer gano!')
      computer_wins += 1
  elif user_option == 'tijera':
    if computer_option == 'papel':
      print('tijera gana a papel')
      print('user gano!')
      user_wins += 1
    else:
      print('piedra gana a tijera')
      print('computer gano!')
      computer_wins += 1
  return user_wins, computer_wins


#funcion para correr el juego
def run_game():
  computer_wins = 0
  user_wins = 0  
  rounds = 1
  while True:
    print('*' * 10)
    print('ROUND', rounds)
    print('*' * 10)

    print('computer_wins', computer_wins)
    print('user_wins', user_wins)
    rounds += 1

    user_option, computer_option = choose_options()
    user_wins, computer_wins = check_rules(user_option, computer_option, user_wins, computer_wins)

    if computer_wins == 2:
      print("\
    ########  ######## ########  ########  ####  ######  ######## ########  #### #### \n \
    ##     ## ##       ##     ## ##     ##  ##  ##    ##    ##    ##        #### ####  \n \
    ##     ## ##       ##     ## ##     ##  ##  ##          ##    ##        #### ####   \n \
    ########  ######   ########  ##     ##  ##   ######     ##    ######     ##   ##     \n \
    ##        ##       ##   ##   ##     ##  ##        ##    ##    ##                     \n \
    ##        ##       ##    ##  ##     ##  ##  ##    ##    ##    ##        #### ####     \n \
    ##        ######## ##     ## ########  ####  ######     ##    ########  #### ####      \n ")
      break

    if user_wins == 2:
      print('\
         ######      ###    ##    ##    ###     ######  ######## ########  #### ####  \n \
        ##    ##    ## ##   ###   ##   ## ##   ##    ##    ##    ##        #### ####  \n \
        ##         ##   ##  ####  ##  ##   ##  ##          ##    ##        #### ####   \n \
        ##   #### ##     ## ## ## ## ##     ##  ######     ##    ######     ##   ##     \n \
        ##    ##  ######### ##  #### #########       ##    ##    ##                     \n \
        ##    ##  ##     ## ##   ### ##     ## ##    ##    ##    ##        #### ####      \n \
         ######   ##     ## ##    ## ##     ##  ######     ##    ########  #### ####        \n')
      break

run_game()