from typing import List

class Employee:
    def init(self, emp_id, first_name, last_name, email, phone, role=None, shift="", uniform_color=None, assigned_area=None):
        self.emp_id = emp_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.role = role
        self.shift = shift
        self.uniform_color = uniform_color
        self.assigned_area = assigned_area

    def assign_role(self, role):
        self.role = role

    def update_details(self, first_name, last_name, email, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone

    def view_accesses(self):
        if self.role:
            return self.role.accesses
        return []

    def audit_accesses(self):
        print(f"Registro de acceso del empleado {self.emp_id}")


class Role:
    def init(self, role_id, name, description):
        self.role_id = role_id
        self.name = name
        self.description = description
        self.accesses = []
        self.permissions = []

    def assign_accesses(self, accesses: List['Area']):
        self.accesses.extend(accesses)

    def assign_permissions(self, permissions: List[str]):
        self.permissions.extend(permissions)

    def update_description(self, description):
        self.description = description


class Area:
    def init(self, area_id, name, description, access_type="Físico"):
        self.area_id = area_id
        self.name = name
        self.description = description
        self.restrictions = []
        self.access_type = access_type

    def view_restrictions(self):
        return self.restrictions

    def add_restriction(self, role: Role):
        if role not in self.restrictions:
            self.restrictions.append(role)

    def remove_restriction(self, role: Role):
        if role in self.restrictions:
            self.restrictions.remove(role)


class Permission:
    def init(self, permission_id, name, description, level):
        self.permission_id = permission_id
        self.name = name
        self.description = description
        self.level = level

    def modify_level(self, level):
        self.level = level

    def assign_to_user(self, employee: Employee):
        print(f"Permisos {self.name} asignados al empleado: {employee.first_name} {employee.last_name}")


class Audit:
    def init(self, audit_id, employee_id, action, area, date=None, details=""):
        self.audit_id = audit_id
        self.employee_id = employee_id
        self.action = action
        self.area = area
        self.date = date
        self.details = details

    def register_action(self, employee: Employee, action: str, area: Area):
        print(f"Recordatorio del registro: {action} por {employee.first_name} {employee.last_name} en área {area.name}")

    def view_history(self):
        print(f"Historial de registros: acción {self.action} por empleado {self.employee_id} en {self.date} en área {self.area}")


class AccessControl:
    def init(self, employee_id, area_id, status, date=None):
        self.employee_id = employee_id
        self.area_id = area_id
        self.status = status
        self.date = date

    def verify_access(self, employee: Employee, area: Area):
        if employee.role and employee.role in area.restrictions:
            self.status = "otorgado"
        else:
            self.status = "denegado"
        return self.status

    def register_access(self, employee: Employee, area: Area):
        access_status = self.verify_access(employee, area)
        print(f"Acceso {access_status} por empleado {employee.first_name} {employee.last_name} al área {area.name}")

    def view_access_status(self):
        return self.status