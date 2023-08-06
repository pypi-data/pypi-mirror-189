from typing import Optional
from pydantic import BaseModel
from fastapi import Request
from ...project import Project, ITable
from ..router import router


class Props(BaseModel):
    session: Optional[str]
    path: str
    valid: Optional[bool]
    limit: Optional[int]
    offset: Optional[int]


class Result(BaseModel):
    table: ITable


@router.post("/resource/read-table")
def server_resource_read_table(request: Request, props: Props) -> Result:
    project: Project = request.app.get_project(props.session)
    table = project.resource_read_table(
        props.path,
        valid=props.valid,
        limit=props.limit,
        offset=props.offset,
    )
    return Result(table=table)
