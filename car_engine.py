def car_engine( power, engne_volume, fuel_type ):
    if fuel_type not in ("dizel","benzin","gas","electric"):
        print("inadequate fuel type ")
        return -1
    return{"power" : power, "engine_volume" : engne_volume, "fuel_type" : fuel_type}