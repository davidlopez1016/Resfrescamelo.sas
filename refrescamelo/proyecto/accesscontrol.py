from proyecto.employee import Employee
from proyecto.area import Area

class AccessControl:
    def __init__(self, employee_id, area_id, status, date=None):
        self.__employee_id = employee_id
        self.__area_id = area_id
        self.__status = status
        self.__date = date

    def verify_access(self, employee: Employee, area: Area):
        if employee.role and employee.role in area.view_restrictions():
            self.status = "otorgado"
        else:
            self.status = "denegado"
        return self.status

    def register_access(self, employee: Employee, area: Area):
        access_status = self.verify_access(employee, area)
        print(f"Acceso {access_status} por empleado {employee.first_name} {employee.last_name} al área {area.name}")

    def view_access_status(self):
        return self.status