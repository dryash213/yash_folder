# main.py (or your FastAPI app file)
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
    
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pandas as pd

import os


from groq import Groq

class DropdownRequest(BaseModel):
    dropdown1: str
    dropdown2: str
    dropdown3: str
    dropdown4: str



# Load the CSV file
csv_file_path = 'static/text_files_data.csv'  # Replace with your actual CSV file path
df_content = pd.read_csv(csv_file_path)
csv_file_path = 'static/prompt_data.csv'  # Replace with your actual CSV file path
df_prompt = pd.read_csv(csv_file_path)

app = FastAPI()

origins = [
    "http://localhost:8000",
    "http://127.0.0.1:8000",
    "http://0.0.0.0:8000",
    "http://localhost:1234",
    "http://127.0.0.1:1234",
    "http://0.0.0.0:1234",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def prepare_message(prompt:str, document_content:str,query_type:str) -> list:


    user_prompt = prompt.format(**{'Document_content':document_content,"Mock Paper":query_type})
    
    msg = []
    msg.append({"role": "user", "content": user_prompt})

    return msg


def generate_response(system_prompt=str, user_prompt=str, model=str):
    # print(model, system_prompt, user_prompt)

    client = Groq(
        api_key="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",
    )

    chat_completion = client.chat.completions.create(
        messages=prepare_message(system_prompt, user_prompt),
        model=model,
    )

    return chat_completion.choices[0].message.content
def get_response(category_1,category_2,category_3,category_4):
        # Filter the DataFrame based on the dropdown selections
    
    prompt_df  =  df_prompt[
        (df_prompt['Parent Folder'] == category_1) &
        (df_prompt['File Name'] == category_4) 
    ]
    
    document_content_df = df_content[
        (df_content['Parent Folder'] == category_1) &
        (df_content['Sub Folder'] == category_2) &
        (df_content['File Name'] == category_3)
    ]
    
    query_type_df = df_content[
        (df_content['Parent Folder'] == category_1) &
        (df_content['Sub Folder'] == category_2) &
        (df_content['File Name'] == category_4)
    ]


    if document_content_df.empty:
        raise HTTPException(status_code=404, detail="No matching records found")
    
    if query_type_df.empty:
        raise HTTPException(status_code=404, detail="No matching records found")
    
    if prompt_df.empty:
        raise HTTPException(status_code=404, detail="No matching records found")
    
    
    
    prompt = df_prompt['File Data'].values[0]
    document_content = document_content_df['File Data'].tolist()[0]
    query_type = query_type_df['File Data'].tolist()[0]
    
    msg = prepare_message(prompt,document_content,query_type)
    response = generate_response(msg)
    # Convert the filtered DataFrame to a list of dictionaries
    return response

@app.post("/api/endpoint/")
async def api_endpoint(request: DropdownRequest):

    # Process the data and generate a response  
    response_data = {
        'message': f'Selected options: {request.dropdown1}, {request.dropdown2}, {request.dropdown3}, {request.dropdown4}'
    }
    response = get_response(request.dropdown1,request.dropdown2,request.dropdown3,request.dropdown4)
    return response

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=1234)
    
    
