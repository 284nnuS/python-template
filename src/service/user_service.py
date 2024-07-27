from repository.user_repository import UserRepository
from sqlalchemy.orm import Session
from core.security import verify_password, get_password_hash
from schemas import UserCreate
from model import User

class UserService:
    def __init__(self, session: Session):
        self.session = session
        self.user_repository = UserRepository(session)

    def authenticate(self, name: str, password: str) -> User | None:
        user = self.user_repository.get_by_name(name)
        if not user:
            return None
        is_authenticated = verify_password(password, user.password)
        if not is_authenticated:
            return None
        return user

    def create(self, user_create: UserCreate) -> User:
        new_user = User(
            name=user_create.name,
            password=get_password_hash(user_create.password),
            email=user_create.email,
        )
        self.user_repository.create(new_user)
        return new_user

    def create_default(self):
        name_default = "admin"
        password_default = "1234"
        email_default = "example@xyz.com"
        default_user = UserCreate(
            name=name_default,
            password=password_default,
            email=email_default
        )
        if not self.is_exists(name_default):
            self.create(default_user)

    def is_exists(self, name: str) -> bool:
        user = self.user_repository.get_by_name(name)
        return user is not None

    def get_by_name(self, name: str) -> User:
        user = self.user_repository.get_by_name(name)
        return user
