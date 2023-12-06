class AccessLevelDTO:
    def __init__(self, access_level_name):
        self.access_level_name = access_level_name

    @classmethod
    def from_dict(cls, data):
        return cls(access_level_name=data.get('access_level_name'))

    def to_dict(self):
        return {'access_level_name': self.access_level_name}
