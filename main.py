import car_engine
import car

amount = int(input("How many cars would you like to add? "))
if amount > 0:
    car_type=[]
    for i in range(amount):
        manufacturer = str(input("manufacturer of the car? "))
        model = str(input("model of the car? "))
        year_of_production = int(input("year of production? "))
        number_of_doors = int(input("number of doors?"))
        power = float(input(""))
        engine_volume = float(input(""))
        fuel_type = str(input(""))

        engine = car_engine.car_engine(power,engine_volume, fuel_type)

        car= car.car(manufacturer, model, year_of_production, number_of_doors)
        car_type.append(car)

    for j in range (amount -1):
        for i in range (amount -1):
            if car.price_of_registracion(car_type[i]) > \
                car.price_of_registracion(car_type[i+1]):
                temp = car_type[i]
                car_type[i] = car_type[i+1]
                car_type[i+1] = temp

    print('\nCar with least amount of registration cost: \n')
    print(("{0:22s}" "{1:19s}" "{2:20s}" "{3:19s}").format("Proizvodjac:",\
                                                           car_type[0]["naziv"],\
                                                           "Vrsta goriva:",\
                                                            car_type[0]["motor"]["vrsta"]))

    print(("{0:22s}" "{1:19s}" "{2:20s}" "{3:12.2f} cm^3  ").format("Model:",\
                                                                    autici[0]["model"],\
                                                                    "Zapremina motora:",\
                                                                    autici[0]["motor"]["zapremina"]))

    print(("{0:22s}" "{1:18d} " "{2:20s}" "{3:12.2f} K.S.  ").format("Godina proizvodnje:",\
                                                                     autici[0]["godina"],\
                                                                     "Snaga motora:",\
                                                                     autici[0]["motor"]["snaga"]))

    print(("{0:22s}" "{1:18d} " "{2:20s}" "{3:12.2f} Dinara").format("Broj vrata:",\
                                                                     autici[0]["br_vrata"],\
                                                                     "Cena registracije:",\
                                                                     automobil.getCenaRegistracije(autici[0])))



else:
    print("inadequate number ")

    


