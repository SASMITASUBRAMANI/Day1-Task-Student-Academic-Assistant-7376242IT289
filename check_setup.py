"""Check the environment and Groq connection."""
import sys
from config import client, MODEL, PROVIDER

print("Python version :", sys.version.split()[0])
print("Provider       :", PROVIDER)
print("Model          :", MODEL)
print("Calling the model ...")

response = client.chat.completions.create(
    model=MODEL,
    messages=[{"role": "user", "content": "Reply with exactly: SETUP OK"}],
    temperature=0,
)

print("Model replied  :", response.choices[0].message.content.strip())
print("Setup check finished.")
