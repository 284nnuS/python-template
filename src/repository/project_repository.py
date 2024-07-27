from model import Project
from .base_repository import BaseRepository
from sqlalchemy.orm import Session


class ProjectRepository(BaseRepository):
    def __init__(self, session: Session):
        super().__init__(session)

    def get_by_id(self, _id: str) -> Project | None:
        project = self.session.query(Project).filter_by(id=_id).first()
        return project

    def get_by_name(self, _name: str) -> Project | None:
        project = self.session.query(Project).filter_by(name=_name).first()
        return project

    def create(self, _project: Project) -> Project:
        self.session.add(_project)
        self.session.commit()
        self.session.refresh(_project)
        return _project

    def delete(self, _id: str) -> None:
        project = self.session.query(Project).filter_by(id=_id)
        if project is not None:
            self.session.delete(project)
            self.session.commit()
        return

