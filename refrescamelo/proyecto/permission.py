from proyecto.employee import Employee

class Permission:
    def __init__(self, permission_id, name, description, level):
        self.__permission_id = permission_id
        self.name = name
        self.description = description
        self.level = level

    def modify_level(self, level):
        self.level = level

    def assign_to_user(self, employee: Employee):
        print(f"Permisos {self.name} asignados al empleado: {employee.first_name} {employee.last_name}")