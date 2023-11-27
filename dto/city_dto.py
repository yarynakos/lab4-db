class CityDTO:
    def __init__(self, city_id, city_name, country_name):
        self.city_id = city_id
        self.city_name = city_name
        self.country_name = country_name

    @classmethod
    def from_dict(cls, data):
        return cls(city_id=data.get('city_id'), city_name=data.get('city_name'), country_name=data.get('country_name'))

    def to_dict(self):
        return {
            'city_id': self.city_id,
            'city_name': self.city_name,
            'country_name': self.country_name
        }
