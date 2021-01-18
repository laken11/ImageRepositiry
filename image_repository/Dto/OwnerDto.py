class RegisterOwnerDto:
    first_name: str
    last_name: str
    email: str
    password: str
    confirm_password: str
    username: str
    owner_info: str


class EditOwnerDto:
    first_name: str
    last_name: str
    email: str
    username: str


class ListOwnerDto:
    first_name: str
    last_name: str
    email: str
    username: str


class OwnerDetailsDto:
    first_name: str
    last_name: str
    email: str
    username: str

