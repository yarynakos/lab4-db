class CountryDTO:
    def __init__(self, country_name):
        self.country_name = country_name

    @classmethod
    def from_dict(cls, data):
        return cls(country_name=data.get('country_name'))

    def to_dict(self):
        return {'country_name': self.country_name}
