from pydantic import BaseModel, Field


class ProjectCreate(BaseModel):
    name: str = Field(description="Project name")

