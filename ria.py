import requests


class Ria:
    def __init__(self, api_key, category_id):
        self.api_key = api_key
        self.url = "https://developers.ria.com/auto/"
        self.category_id = category_id

    def make_request(self, url_addon, **kwargs):
        if 'parameters' in kwargs:
            res = requests.get('{0}/{1}?api_key={2}'.format(self.url, url_addon, self.api_key), params=kwargs['parameters'])
        else:
            res = requests.get('{0}/{1}/?api_key={2}'.format(self.url, url_addon, self.api_key))

        if res.status_code != 200:
            raise RiaRequestException(res.status_code, res.json())
        return res.json()


    def get_categories(self):
        url_path = "categories"
        res = self.make_request(url_path)
        return res

    def get_bodystyles(self):
        pass


    def get_marks(self):
        url_path = "categories/{0}/marks".format(self.category_id)
        res = self.make_request(url_path)
        return res

    def get_mark_id(self, mark_name):
        res = self.get_marks()
        for mark in res:
            if mark['name'] == mark_name:
                return mark['value']
        raise MarkNotFoundException()


    def get_models(self, mark_name):
        # https://developers.ria.com/auto/categories/2/marks/9/models?api_key=YOUR_API_KEY
        mark_id = self.get_mark_id(mark_name)
        url_path = 'categories/{0}/marks/{1}/models'.format(self.category_id, mark_id)
        return self.make_request(url_path)

    def get_model_id(self, mark_name, model_name):
        models = self.get_models(mark_name)
        for model in models:
            if model['name'] == model_name:
                return model['value']
        raise ModelNotFoundException(mark_name, model_name)


    def set_fuel(self, name):
        fuels = {
            "Бензин":1,
            "Дизель":2,
            "Газ":3,
            "Газ / Бензин":4,
            "Гібрид":5,
            "Електро":6,
        }
        return fuels[name]

    def get_cars(self, mark, model, fuel,price_ot, price_do  ,**kwargs):
        parameters = {'abroad':2, 'custom': 1, 'currency': 1, 'state[2]': 10, 'city[2]': 2, 'gearbox[0]':0 }
        mark_id = self.get_mark_id(mark)
        model_id = self.get_model_id(mark, model)
        fuel_id = self.set_fuel(fuel)
        # "https://developers.ria.com/auto/search?api_key=YOUR_API_KEY&PARAMETERS"
        # Example
        # https://developers.ria.com/auto/search?api_key=YOUR_API_KEY
        # &category_id=1
        # (marka_id[1]=84)
        # (model_id[1]=123123)
        # (s_yers[1]=2012 & po_yers[1]=2016)
        # (price_ot=1000 price_do=60000)
        # (type[0]=1)
        # (gearbox[1]=2)
        # (engineVolumeFrom=1.4&engineVolumeTo=3.2)
        parameters = {
            'marka_id[1]':mark_id,
            'model_id[1]': model_id,
            'type[0]': fuel_id,
            "price_ot": price_ot,
            "price_do": price_do

            }

        return self.make_request("search", parameters=parameters)



    def get_car_details(self, id):
        # https://developers.ria.com/auto/info?api_key=YOUR_API_KEY&auto_id=
        self.make_request("info", {'auto_id': id})
        pass


class RiaRequestException(Exception):
    def __init__(self, code, text):
        self.code = code
        self.text = text

class MarkNotFoundException(Exception):
    def __init__(self, name):
        self.text = "Mark {0} not found".format(name)

class ModelNotFoundException(Exception):
    def __init__(self, model, mark):
        self.text = "Model {0} of mark {1} not found".format(model, mark)