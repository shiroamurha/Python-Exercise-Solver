```
def animal():
    animal = input("É mamífero? ").upper()
    if animal == "SIM":
        animal = input("É quadrúpede? ").upper()
        if animal == "SIM":
            animal = input("É carnívoro? ").upper()
            if animal == "SIM":
                print("O animal escolhido foi o leão.")
            else:
                animal = input("É herbívoro? ").upper()
                if animal == "SIM":
                    print("O animal escolhido foi o cavalo.")
                else:
                    animal = input("Tem asas? ").upper()
                    if animal == "SIM":
                        print("O animal escolhido foi o morcego.")
                    else:
                        animal = input("Tem baleia? ").upper()
                        if animal == "SIM":
                            print("O animal escolhido foi a baleia.")
                        else:
                            animal = input("Tem patas? ").upper()
                            if animal == "SIM":
                                print("O animal escolhido foi o homem.")
                            else:
                                animal = input("É réptil? ").upper()
                                if animal == "SIM":
                                    animal = input("Tem escamas? ").upper()
                                    if animal == "SIM":
                                        print("O animal escolhido foi a cobra.")
                                    else:
                                        print("O animal escolhido foi o crocodilo.")
                                else:
                                    animal = input("Tem asas? ").upper()
                                    if animal == "SIM":
                                        print("O animal escolhido foi a águia.")
                                    else:
                                        animal = input("Tem casco? ").upper()
                                        if animal == "SIM":
                                            print("O animal escolhido foi o tartaruga.")
                                        else:
                                            animal = input("Tem penas? ").upper()
                                            if animal == "SIM":
                                                print("O animal escolhido foi o pinguim.")
                                            else:
                                                print("O animal escolhido foi o avestruz.")
        else:
            animal = input("Tem asas? ").upper()
            if animal == "SIM":
                animal = input("Tem penas? ").upper()
                if animal == "SIM":
                    print("O animal escolhido foi o pinguim.")
                else:
                    print("O animal escolhido foi a águia.")
            else:
                animal = input("Tem casco? ").upper()
                if animal == "SIM":
                    print("O animal escolhido foi o tartaruga.")
                else:
                    animal = input("Tem escamas? ").upper()
                    if animal == "SIM":
                        print("O animal escolhido foi o crocodilo.")
                    else:
                        animal = input("É macaco? ").upper()
                        if animal == "SIM":
                            print("O animal escolhido foi o macaco.")
                        else:
                            print("O animal escolhido foi o homem.")
    else:
        animal = input("Tem asas? ").upper()
        if animal == "SIM":
            animal = input("Tem penas? ").upper()
            if animal == "SIM":
                print("O animal escolhido foi a águia.")
            else:
                print("O animal escolhido foi o morcego.")
        else:
            animal = input("Tem escamas? ").upper()
            if animal == "SIM":
                animal = input("Tem bico? ").upper()
                if animal == "SIM":
                    print("O animal escolhido foi o pato.")
                else:
                    print("O animal escolhido foi a cobra.")
            else:
                print("O animal escolhido foi o homem.")
animal()

