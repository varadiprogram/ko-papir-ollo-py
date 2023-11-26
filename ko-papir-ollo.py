import random
import time


# algoritmus1 = ["kő", "papír", "olló",]
# print(random.choice(algoritmus1))

while True:
    # kő - papír - olló választó
    valasztasod = input("kő , papír , olló: ")
    print("")
    # kő választási lehetőség
    if valasztasod == "kő":
        # random kiválaszt valamit a listából
        algoritmus1 = ["kő", "papír", "olló",]
        ellenseg_valasztas = random.choice(algoritmus1)
        time.sleep(0.8)
        print(f"ellenség választása: {ellenseg_valasztas}")
        print("")
    # papír választási lehetőség
    elif valasztasod == "papír":
        # random kiválaszt valamit a listából
        algoritmus1 = ["kő", "papír", "olló",]
        ellenseg_valasztas = random.choice(algoritmus1)
        time.sleep(0.8)
        print(f"ellenség választása: {ellenseg_valasztas}")
        print("")
    # olló választási lehetőség
    elif valasztasod == "olló":
        # random kiválaszt valamit a listából
        algoritmus1 = ["kő", "papír", "olló",]
        ellenseg_valasztas = random.choice(algoritmus1)
        time.sleep(0.8)
        print(f"ellenség választása: {ellenseg_valasztas}")
        print("")
    # ha valami nem elront a felhasználó
    else:
        print("Valamit elronott kérem inditsa úrja a programot")
