class ObjectDTO:
    def __init__(self, object_id, type_of_object, number_of_flors, city_id):
        self.object_id = object_id
        self.type_of_object = type_of_object
        self.number_of_flors = number_of_flors
        self.city_id = city_id

    @classmethod
    def from_dict(cls, data):
        return cls(object_id=data.get('object_id'), type_of_object=data.get('type_of_object'),
                   number_of_flors=data.get('number_of_flors'), city_id=data.get('city_id'))

    def to_dict(self):
        return {
            'object_id': self.object_id,
            'number_of_flors': self.number_of_flors,
            'type_of_object': self.type_of_object,
            'city_id': self.city_id
        }
