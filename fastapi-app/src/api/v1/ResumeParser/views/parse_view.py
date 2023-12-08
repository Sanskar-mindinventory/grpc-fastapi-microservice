from typing import Any
from fastapi import APIRouter, Depends, UploadFile
from src.api.v1.ResumeParser.services.parse_service import ParserServices
from src.api.v1.ResumeParser.utils.auth_utils import verify_token



resume_parser = APIRouter(prefix="/resume")


@resume_parser.get('/')
def resume_get_view():
    return {"Response": "Resume Service is working perfectly"}

@resume_parser.post('/upload')
def resume_uploader(file: UploadFile, job_desc:str, token: Any = Depends(verify_token)):
    print(f"Welcome ======================================= {token.user.username}")
    file_obj = ParserServices().create_file(resume=file)
    response = ParserServices().show_parser_result(resume=file, job_description=job_desc)
    return response