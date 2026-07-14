from pydantic import BaseModel,Field
from typing import List


class ResumeRequest(BaseModel):
    resume_text : str = Field(min_length=50,max_length=8000)

class ResumeAnalysis(BaseModel):
    summary : str
    skills : List[str]
    strengths : List[str]
    improvements : List[str]

