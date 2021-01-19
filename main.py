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


else:
    print("inadequate number ")

    


