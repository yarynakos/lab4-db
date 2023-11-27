class ZoneDTO:
    def __init__(self, zone_id, zone_name, access_level_name, object_id):
        self.zone_id = zone_id
        self.zone_name = zone_name
        self.access_level_name = access_level_name
        self.object_id = object_id

    @classmethod
    def from_dict(cls, data):
        return cls(zone_id=data.get('zone_id'), zone_name=data.get('zone_name'),
                   access_level_name=data.get('access_level_name'), object_id=data.get('object_id'))

    def to_dict(self):
        return {
            'zone_id': self.zone_id,
            'zone_name': self.zone_name,
            'access_level_name': self.access_level_name,
            'object_id': self.object_id
        }
