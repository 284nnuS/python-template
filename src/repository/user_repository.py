from model import User
from .base_repository import BaseRepository
from sqlalchemy.orm import Session
from schemas import UserCreate


class UserRepository(BaseRepository):
    def __init__(self, session: Session):
        super().__init__(session)

    def get_by_name(self, _name: str) -> User | None:
        user = self.session.query(User).filter_by(name=_name).first()
        return user

    def create(self, _user: User) -> User:
        self.session.add(_user)
        self.session.commit()
        self.session.refresh(_user)
        return _user
