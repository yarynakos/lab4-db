class SystemsDTO:
    def __init__(self, system_id, system_name):
        self.system_id = system_id
        self.system_name = system_name

    @classmethod
    def from_dict(cls, data):
        return cls(system_id=data.get('system_id'), system_name=data.get('system_name'))

    def to_dict(self):
        return {'system_id': self.system_id, 'system_name': self.system_name}
