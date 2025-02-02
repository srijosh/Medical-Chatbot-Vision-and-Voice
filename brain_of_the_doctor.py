import os
import base64
from groq import Groq
from dotenv import load_dotenv
load_dotenv()

#Step1: Setup GROQ API key
GROQ_API_KEY=os.environ.get("GROQ_API_KEY")

#Step2: Convert image to required format
def encode_image(image_path):   
    image_file=open(image_path, "rb")
    return base64.b64encode(image_file.read()).decode('utf-8') # final result is a Base64 string, but it is stored as a UTF-8 text representation.

#Step3: Setup Multimodal LLM 
# query="Is there something wrong with my hand?"
# model="llama-3.2-90b-vision-preview"

def analyze_image_with_query(query, model, encoded_image):
    client=Groq()  
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text", 
                    "text": query
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{encoded_image}",
                    },
                },
            ],
        }]
    chat_completion=client.chat.completions.create(
        messages=messages,
        model=model
    )

    return chat_completion.choices[0].message.content

# analyze_image_with_query(query=query, model=model, encoded_image=encode_image("rash.png"))