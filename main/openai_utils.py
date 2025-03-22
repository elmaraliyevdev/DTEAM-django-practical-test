import openai
from django.conf import settings

openai.api_key = settings.OPENAI_API_KEY

def ask_openai(prompt):
    """Send a prompt to OpenAI and return the response."""
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "You are a career advisor."},
                  {"role": "user", "content": prompt}]
    )
    return response["choices"][0]["message"]["content"]