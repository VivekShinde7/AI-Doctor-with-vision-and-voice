import os
from langchain_groq import ChatGroq
from groq import Groq
from dotenv import load_dotenv
import base64

# Configure the LLM
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

def analyze_image_with_query(query, model, encoded_image):
    load_dotenv()
    groq_api_key = os.getenv("GROQ_API_KEY")
    client = Groq()
    
    messages = [
        {
            "role": "user",
            "content": [
                {"type": "text", "text": query},
                {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{encoded_image}"}},
            ],
        }
    ]
    
    
    chat_completion = client.chat.completions.create(
        messages=messages,
        model=model
    )

    return chat_completion.choices[0].message.content


