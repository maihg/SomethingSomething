import random
import time

def randnum():
    return random.randint(1,10)

def try_to_multiply():
    rand1 = randnum()
    rand2 = randnum()

    user_input = input("Hva er "+ str(rand1) + " ganget med " + str(rand2) + "? ")
    user_input = (int(user_input))

    product = rand1 * rand2
    print("Fasit: ", product)
    return (user_input == product)

# while-løkke for å se hvor lenge man klarer å svare riktig
# må klare 5, 10 eller 30 riktig
correct = True
count = 0
#rounds = 1

user_input2 = input("Lett, middels eller vanskelig? ")
if user_input2 == "lett":
    rounds = 5
elif user_input2 == "middels":
    rounds = 10
elif user_input2 == "vanskelig":
    rounds = 30
else:
    print("Ukjent valg. Programmet stoppes.")
    correct = False;

while correct:
    tic = time.perf_counter()
    correct = try_to_multiply()
    count += 1
    
    if correct:
        print("Du har klart: " + str(count) + "\n")
    else:
        print("Å nei, der ble det feil :/")  
    if count == rounds:
        print("Woho! Du klarte alle :)")
        toc = time.perf_counter()
        print(f"Tid brukt: {toc - tic:0.4f} sekunder") 
        break


