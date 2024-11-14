from typing import List

class Role:
    def __init__(self, role_id, name, description):
        self.__role_id = role_id
        self.name = name
        self.description = description
        self.__accesses = []
        self.__permissions = []

    def assign_accesses(self, accesses: List['Area']):
        self.__accesses.extend(accesses)

    def assign_permissions(self, permissions: List[str]):
        self.__permissions.extend(permissions)

    def update_description(self, description):
        self.description = description