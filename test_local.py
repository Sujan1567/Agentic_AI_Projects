import json 
from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama",
)  

model="llama3.2:latest"
# model="gpt-4o-mini"
messages=[
    {"role": "system", "content": "You are a terse travel assistant for Nepal."},
    {"role": "user",   "content": 'Extract the name and city. Respond with JSON only.\n'
         'Text: "Ram Thapa runs a trekking shop in Pokhara."'},
]
temperature=0,

resp = client.chat.completions.create(
    model=model,
    messages=messages,
)
print(resp.choices[0].message.content)
