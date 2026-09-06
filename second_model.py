import json 
from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama",
)  

model="travel-nepal:latest "
# model="gpt-4o-mini"
messages=[
    {"role": "system", "content": "You are a terse travel assistant for Nepal."},
    {"role": "user",   "content": 'You may answer the question of the mathmatics as your the math te.\n'
         'Text: "Tell the different equation of the mathmatics."'},
]
temperature=0,

resp = client.chat.completions.create(
    model=model,
    messages=messages,
)
print(resp.choices[0].message.content)
