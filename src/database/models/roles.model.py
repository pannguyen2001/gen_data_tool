# create model for role
class Role:
    def __init__(self, role_id: int, role_name: str):
        self.role_id = role_id
        self.role_name = role_name

    def __repr__(self):
        return f"Role(role_id={self.role_id}, role_name={self.role_name})"
