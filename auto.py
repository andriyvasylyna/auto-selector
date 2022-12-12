class Mark:
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name

    @property
    def id(self):
        return self.id

    @property
    def name(self):
        return self.name

class Model:
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name

    @property
    def id(self):
        return self.id

    @property
    def name(self):
        return self.name

class Fuel:
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name

    @property
    def id(self):
        return self.id

    @property
    def name(self):
        return self.name


class Auto:

    def __init__(self, mark: Mark, model: Model, fuel: Fuel, year: int, bodystyle, price: int, milege: int):
        self.mark = mark
        self.model = model
        self.fuel = fuel
        self.year = year
        self.bodystyle = bodystyle
        self.price = price
        self.milege = milege

    @property
    def year(self):
        return self.year

    @property
    def price(self):
        return self.price

    @property
    def milege(self):
        return self.milege




