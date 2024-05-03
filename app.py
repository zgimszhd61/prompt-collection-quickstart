from openai import OpenAI
import os

os.environ["OPENAI_API_KEY"] = "sk-"
client = OpenAI()
completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Hello!"}
  ]
)

print(completion.choices[0].message.content)
