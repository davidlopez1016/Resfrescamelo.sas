from proyecto.employee import Employee
from proyecto.role import Role
from proyecto.area import Area
from proyecto.permission import Permission
from proyecto.audit import Audit
from proyecto.accesscontrol import AccessControl

empleado = Employee(emp_id=1, first_name="Juan", last_name="Pérez", email="juan@example.com", phone="1234567890")
rol = Role(role_id=1, name="Gerente", description="Administra el área de ventas")
area = Area(area_id=1, name="Oficina", description="Área de acceso restringido")
permiso = Permission(permission_id=1, name="Acceso Completo", description="Permite acceso completo", level="Alto")
auditoria = Audit(audit_id=1, employee_id=1, action="Ingreso", area="Oficina")
control_acceso = AccessControl(employee_id=1, area_id=1, status="pendiente")

empleado.assign_role(rol)
rol.assign_accesses([area])
control_acceso.register_access(empleado, area)