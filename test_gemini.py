import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
print("Key đã load:", "Có" if api_key else "Không — kiểm tra lại file .env")

# Model mới nhất của Gemini (tháng 9/2025)
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", google_api_key=api_key)
response = llm.invoke("Say hello in one short sentence.")
print(response.content)
