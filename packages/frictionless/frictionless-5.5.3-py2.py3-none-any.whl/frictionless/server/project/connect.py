from __future__ import annotations
from typing import Optional
from pydantic import BaseModel
from fastapi import Request
from ...project import Project
from ..router import router

# TODO: have one of connect/create?
# TODO: protect against many projects creation


class Props(BaseModel):
    session: Optional[str]


class Result(BaseModel):
    session: str


@router.post("/project/connect")
def server_project_connect(request: Request, props: Props) -> Result:
    try:
        project: Project = request.app.get_project(session=props.session)
    except Exception:
        project: Project = request.app.get_project()
    # TODO: review session being optional
    return Result(session=project.session)  # type: ignore
