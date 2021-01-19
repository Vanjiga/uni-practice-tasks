import car_engine
import car

amount = int(input("How many cars would you like to add? "))
if amount > 0:
    car_type=[]
    for i in range(amount):
        manufacturer = str(input(""))
        model = str(input(""))
        year_of_production = int(input(""))
        number_of_doors = int(input(""))
        power = float(input(""))
        engine_volume = float(input(""))
        fuel_type = str(input(""))

        engine = car_engine.car_engine(power,engine_volume, fuel_type)

        car= car.car(manufacturer, model, year_of_production, number_of_doors)
        car_type.append(car)

    for j in range (amount -1):
        for i in range (amount -1):
            if car.price


else:
    print("inadequate number ")

    


