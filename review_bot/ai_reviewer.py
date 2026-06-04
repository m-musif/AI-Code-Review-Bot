from groq import Groq

from review_bot.config import MODEL_NAME


def generate_ai_review(api_key: str, prompt: str) -> str:
    client = Groq(api_key=api_key)

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content
