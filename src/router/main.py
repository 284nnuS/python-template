from .v1 import login_router, user_router, project_router
from fastapi import APIRouter
api_router = APIRouter()


@api_router.on_event("startup")
async def startup() -> None:
    from sqlalchemy.orm import Session
    from core.db import engine
    from service import UserService, ProjectService
    with Session(engine) as session:
        user_service = UserService(session)
        user_service.create_default()
        project_service = ProjectService(session)
        project_service.create_default()
api_router.include_router(login_router.router, tags=["login"])
api_router.include_router(user_router.router, tags=["user"])
api_router.include_router(project_router.router, tags=["project"])
