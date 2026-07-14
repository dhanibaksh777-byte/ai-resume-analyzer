from fastapi import FastAPI,HTTPException
from groq import AuthenticationError
from llm_client import ai_resume_analyzer
from schemas import ResumeRequest, ResumeAnalysis
from prompt import system_prompt
import json 


app = FastAPI(title="Ai Resume Analyzer")



from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/analyze-resume", response_model=ResumeAnalysis)
def analyze_resume(request : ResumeRequest):
    messages = [{"role" : "system" , "content" : system_prompt},
                {"role" : "user", "content" : request.resume_text}]
    try:
        reply = ai_resume_analyzer(messages)
        result = json.loads(reply)

        return result
    
    except json.JSONDecodeError:
        raise HTTPException(status_code=500,detail="Ai returned invalid json")
    except AuthenticationError:
        raise HTTPException(status_code=500,detail="Invalid Groq API key. Check your .env file")
    except Exception:
        raise HTTPException(status_code = 500,detail="chatbot is currently unavailable")
    
   
        

        
        

    
