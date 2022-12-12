from ria import Ria

API_KEY = "7m4IScx47sB2A9pIzy2FBemH5c5MuapYV2NunRA0"

if __name__ == "__main__":
    ria = Ria("7m4IScx47sB2A9pIzy2FBemH5c5MuapYV2NunRA0", 1)

    # print(ria.get_categories())

    # print(ria.get_marks())

    # print(ria.get_mark_id("Toyota"))

    # print(ria.get_models("Toyota"))

    # print(ria.set_fuel("Бензин"))

    #print(ria.get_model_id("Toyota", "RAV4"))

    #print(ria.get_cars("Toyota", "RAV4","Бензин"))

    print(ria.get_car_details(33511720))