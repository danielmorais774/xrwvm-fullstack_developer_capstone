from .models import CarMake, CarModel

def initiate():
    car_make_data = [
        {"name":"NISSAN", "description":"Great cars. Japanese technology", "country": "Japan"},
        {"name":"Mercedes", "description":"Great cars. German technology", "country": "Germany"},
        {"name":"Audi", "description":"Great cars. German technology", "country": "Germany"},
        {"name":"Kia", "description":"Great cars. Korean technology", "country": "Korea"},
        {"name":"Toyota", "description":"Great cars. Japanese technology", "country": "Japan"},
    ]

    car_make_instances = []
    for data in car_make_data:
            car_make_instances.append(CarMake.objects.create(name=data['name'], description=data['description']))


    # Create CarModel instances with the corresponding CarMake instances
    car_model_data = [
      {"name":"Pathfinder", "dealer": 1, "type":"SUV", "year": 2023, "car_make":car_make_instances[0]},
      {"name":"Qashqai", "dealer": 1, "type":"SUV", "year": 2023, "car_make":car_make_instances[0]},
      {"name":"XTRAIL", "dealer": 1, "type":"SUV", "year": 2023, "car_make":car_make_instances[0]},
      {"name":"A-Class", "dealer": 1, "type":"SUV", "year": 2023, "car_make":car_make_instances[1]},
      {"name":"C-Class", "dealer": 1, "type":"SUV", "year": 2023, "car_make":car_make_instances[1]},
      {"name":"E-Class", "dealer": 1, "type":"SUV", "year": 2023, "car_make":car_make_instances[1]},
      {"name":"A4", "dealer": 1, "type":"SUV", "year": 2023, "car_make":car_make_instances[2]},
      {"name":"A5", "dealer": 1, "type":"SUV", "year": 2023, "car_make":car_make_instances[2]},
      {"name":"A6", "dealer": 1, "type":"SUV", "year": 2023, "car_make":car_make_instances[2]},
      {"name":"Sorrento","dealer": 1, "type":"SUV", "year": 2023, "car_make":car_make_instances[3]},
      {"name":"Carnival","dealer": 1, "type":"SUV", "year": 2023, "car_make":car_make_instances[3]},
      {"name":"Cerato", "dealer": 1, "type":"Sedan", "year": 2023, "car_make":car_make_instances[3]},
      {"name":"Corolla", "dealer": 1, "type":"Sedan", "year": 2023, "car_make":car_make_instances[4]},
      {"name":"Camry", "dealer": 1, "type":"Sedan", "year": 2023, "car_make":car_make_instances[4]},
      {"name":"Kluger", "dealer": 1, "type":"SUV", "year": 2023, "car_make":car_make_instances[4]},
        # Add more CarModel instances as needed
    ]

    for data in car_model_data:
            CarModel.objects.create(name=data['name'], car_make=data['car_make'], dealer=data['dealer'], type=data['type'], year=data['year'])