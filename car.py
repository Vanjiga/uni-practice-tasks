import car_engine 
import math

def car (manufacturer, model, year_of_production, number_of_doors):
    if type(car_engine) != dict:
        return -1 
    for keys in car_engine.keys():
        if keys not in ["power", "engine_volume ", "fuel_type"]:
            return -1
        return{
            "manufacturer" : manufacturer,
            "model" : model,
            "year_of_production" : year_of_production,
            "number_of_doors" : number_of_doors
        }


def price_of_registracion(e):
    if type(e) != dict:
        return -1

    return 22414*(1-1/e["engine"]["power"])*((e["engine"]["engine_volume"]-500))/(1+250*math.sqrt(2020-e["year_of_production"]))