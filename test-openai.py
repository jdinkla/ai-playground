import os
import openai

model="text-davinci-003"

openai.api_key = os.getenv("OPENAI_API_KEY")
response = openai.Completion.create(model=model, prompt="Create a nice name that consist of two words for a brand selling fake and bad tasting cigarettes", temperature=0.2, max_tokens=20)
print(response)