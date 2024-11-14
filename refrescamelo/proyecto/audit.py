from proyecto.employee import Employee
from proyecto.area import Area

class Audit:
    def __init__(self, audit_id, employee_id, action, area, date=None, details=""):
        self.__audit_id = audit_id
        self.__employee_id = employee_id
        self.__action = action
        self.__area = area
        self.__date = date
        self.__details = details

    def register_action(self, employee: Employee, action: str, area: Area):
        print(f"Recordatorio del registro: {action} por {employee.first_name} {employee.last_name} en área {area.name}")

    def view_history(self):
        print(f"Historial de registros: acción {self.action} por empleado {self.employee_id} en {self.date} en área {self.area}")