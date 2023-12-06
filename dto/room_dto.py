class RoomDTO:
    def __init__(self, room_id, room_name, type_of_room, zone_id, object_id):
        self.room_id = room_id
        self.room_name = room_name
        self.type_of_room = type_of_room
        self.zone_id = zone_id
        self.object_id = object_id

    @classmethod
    def from_dict(cls, data):
        return cls(room_id=data.get('room_id'), room_name=data.get('room_name'),
                   type_of_room=data.get('type_of_room'), zone_id=data.get('zone_id'),
                   object_id=data.get('object_id'))

    def to_dict(self):
        return {
            'room_id': self.room_id,
            'room_name': self.room_name,
            'type_of_room': self.type_of_room,
            'zone_id': self.zone_id,
            'object_id': self.object_id
        }
