import random

user_wins = 0
computer_wins = 0
draws = 0 # aggiunta la variabile dei pareggi

options = ["carta", "sasso", "forbice"]

while True:
    user_input = input("Digita Carta/Sasso/Forbice o Q per Uscire: " ).lower()
    if user_input == "q":
        break
        
    if user_input not in options:
        print("Input non valido. Riprova.")
        continue
    random_number = random.randint(0,2)
    # carta: 0, sasso: 1, forbici: 2
    
    computer_pick = options[random_number]
    print("Cpu lancia", computer_pick + ".")
    
    if user_input == computer_pick:
        print("Pareggio")
        draws += 1 # incremento la variabile dei pareggi
    elif (user_input == "sasso" and computer_pick == "forbice") or (user_input == "carta" and computer_pick == "sasso") or (user_input == "forbice" and computer_pick == "carta"):
        print("Hai Vinto!")
        user_wins += 1
    else:
        print("Hai Perso !")
        computer_wins += 1
        
    
print("Hai Vinto", user_wins, "volte")  
print("Cpu ha vinto", computer_wins, "volte") 
print("Pareggi", draws, "volte") # stampo il numero di pareggi
print("Arrivederci")
