from openai import OpenAI
import cvlatex
from dotenv import load_dotenv
import os

load_dotenv(override=True)
key = os.getenv("OPENAI_API_KEY")
print(key)