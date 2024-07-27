from repository.project_repository import ProjectRepository
from sqlalchemy.orm import Session
from core.security import verify_password, get_password_hash
from schemas import ProjectCreate
from model import Project


class ProjectService:
    def __init__(self, session: Session):
        self.session = session
        self.project_repository = ProjectRepository(session)

    def create(self, project_create: ProjectCreate) -> Project:
        new_project = Project(
            name=project_create.name
        )
        self.project_repository.create(new_project)
        return new_project

    def create_default(self):
        name_default = 'default'
        default_project = ProjectCreate(
            name=name_default
        )

        if not self.is_exists(name_default):
            self.create(default_project)

    def is_exists(self, _name: str) -> bool:
        project = self.project_repository.get_by_name(_name)
        return project is not None

    def get_by_name(self, _name: str) -> Project:
        project = self.project_repository.get_by_name(_name)
        return project

