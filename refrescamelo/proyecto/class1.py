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