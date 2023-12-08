import shutil
from pyresparser import ResumeParser
from src.api.v1.ResumeParser.utils.parser_utils import Preprocessfile, find_score, predictResume

class ParserServices:

    @staticmethod
    def show_parser_result(resume, job_description):      
        processed_job_des = Preprocessfile(job_description)
        score = find_score(processed_job_des,resume.filename)
        user_info = ResumeParser(f"/home/mind/PyCharm_projects/ML/resume_parser/files/{resume.filename}").get_extracted_data()
        user_info['predicted']=predictResume(resume.filename)
        response = {
                'resumeId': resume.filename,
                'score': score,
                'userInfo': user_info,
            }
        return response
    
    @staticmethod
    def create_file(resume):
        file_location = f"files/{resume.filename}"
        with open(file_location, "wb+") as file_object:
            shutil.copyfileobj(resume.file, file_object)
