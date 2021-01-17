class CreateImageDto:
    name: str
    tag: str
    tag2: str
    tag3: str
    description: str
    owner_id: int
    image: str


class EditImageDto:
    name: str
    tag: str
    tag2: str
    tag3: str
    description: str
    image: str
    owner_id: int


class ListImageDto:
    name: str
    id: int
    tag: str
    tag2: str
    tag3: str
    description: str
    user: object
    owner_info: str
    image: str


class ImageDetailsDto:
    name: str
    tag: str
    tag2: str
    tag3: str
    user: object
    owner_info: object
    description: str
    name: int
    image: str
    owner_id: int

