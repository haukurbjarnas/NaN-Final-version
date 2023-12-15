class Aircraft:
    def __init__(self, name, type_id, license_class_number: int, capacity: int) -> None:
        self.name = name
        self.type_id = type_id
        self.license_class_number = license_class_number
        self.capacity = capacity