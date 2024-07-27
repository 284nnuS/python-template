from .user import User
from .project import Project
from core.db import Base, engine

Base.metadata.create_all(engine)