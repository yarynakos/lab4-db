class UserDTO:
    def __init__(self, user_id, surname, name, phone, email, access_level_name):
        self.user_id = user_id
        self.surname = surname
        self.name = name
        self.phone = phone
        self.email = email
        self.access_level_name = access_level_name

    @classmethod
    def from_dict(cls, data):
        return cls(user_id=data.get('user_id'), surname=data.get('surname'),
                   name=data.get('name'), phone=data.get('phone'), email=data.get('email'),
                   access_level_name=data.get('access_level_name'))

    def to_dict(self):
        return {
            'user_id': self.user_id,
            'surname': self.surname,
            'name': self.name,
            'phone': self.phone,
            'email': self.email,
            'access_level_name': self.access_level_name
        }
