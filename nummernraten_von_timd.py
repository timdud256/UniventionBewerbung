from random import randint

# Read user input until its its correct
wrong = True
value = randint(0,100)

while wrong: # Der while loop läuft bis es richtig geraden
    guess = int(input("Erraten sie die Zahl > "))
        
    if (guess == value): # If guess is equal print you won
        print("Richtig geraten!")
        wrong = False # Hier setzen wir 'wrong' auf False damit der while loop aufhört und das programm beendet
    elif (guess < value): # If guess is lower print lower
        print("Die gesuchte Zahl ist größer")
    elif (guess > value): # If guess is greater print greater
        print("Die gesuchte Zahl ist kleiner")

