from fastapi import APIRouter, Depends
from ..dependencies import get_current_user, SessionDependency
from service.project_service import ProjectService
from model import Project
from fastapi import HTTPException
from fastapi.responses import JSONResponse
from schemas import ProjectCreate

router = APIRouter()

@router.get("/project/get_by_name/{project_name}")
def get_me(
    project_name: str,
    session: SessionDependency,
    current_user: Depends = Depends(get_current_user),
):
    """
    OAuth2 compatible token login, get an access token for future requests
    """
    project_service = ProjectService(session)
    project = project_service.get_by_name(project_name)
    return project

@router.post("/project/create/")
def get_me(
    project_create: ProjectCreate,
    session: SessionDependency,
    current_user: Depends = Depends(get_current_user),
):
    """
    OAuth2 compatible token login, get an access token for future requests
    """
    project_service = ProjectService(session)
    project = project_service.get_by_name(project_create.name)
    if not project:
        project_service.create(project_create)
        return JSONResponse("Project created successfully.", status_code=201)
    else:
        raise HTTPException(400,"Project already exists")


