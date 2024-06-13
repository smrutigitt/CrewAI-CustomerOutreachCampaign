import os
import re
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from utils import pretty_print_result
from dotenv import load_dotenv
from utils import send_email

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")
from crew import crew

os.environ["OPENAI_MODEL_NAME"] = 'gpt-3.5-turbo'
os.environ["OPENAI_API_KEY"] = openai_api_key
class LeadInfo(BaseModel):
    lead_name: str
    industry: str
    key_decision_maker: str
    position: str
    milestone: str

app = FastAPI()

@app.post("/process_lead/")
async def process_lead(lead_info: LeadInfo):
    inputs = {
        "lead_name": lead_info.lead_name,
        "industry": lead_info.industry,
        "key_decision_maker": lead_info.key_decision_maker,
        "position": lead_info.position,
        "milestone": lead_info.milestone
    }
    
    # try:
    result = crew.kickoff(inputs=inputs)
    pretty_print_result(result)

    return result
    # subject_match = re.search(r"Subject: (.+)", result)
    # subject = subject_match.group(1) if subject_match else "No Subject Found"
    # from_email = "smruti@saaragh.com"
    # to_email = "smrutirekha1999@gmail.com"
    # body = result  
        
    # send_email(subject, from_email, to_email, body)
        
    # return {"message": "Email sent successfully."}
    # except Exception as e:
    #     raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)



# import os
# from dotenv import load_dotenv
# from utils import pretty_print_result

# load_dotenv()
# openai_api_key = os.getenv("OPENAI_API_KEY")
# from crew import crew

# os.environ["OPENAI_MODEL_NAME"] = 'gpt-3.5-turbo'
# os.environ["OPENAI_API_KEY"] = openai_api_key

# inputs = {
#     "lead_name": "Tech Innovators Inc.",
#     "industry": "Artificial Intelligence Solutions",
#     "key_decision_maker": "Emily Chang",
#     "position": "CTO",
#     "milestone": "Acquisition of a Competitor"
# }

# result = crew.kickoff(inputs=inputs)

# print(pretty_print_result(result))


