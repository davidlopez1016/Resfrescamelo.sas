from proyecto.role import Role

class Area:
    def __init__(self, area_id, name, description, access_type="Físico"):
        self.__area_id = area_id
        self.name = name
        self.description = description
        self.__restrictions = []
        self.access_type = access_type

    def view_restrictions(self):
        return self.__restrictions

    def add_restriction(self, role: Role):
        if role not in self.__restrictions:
            self.__restrictions.append(role)

    def remove_restriction(self, role: Role):
        if role in self.__restrictions:
            self.__restrictions.remove(role)