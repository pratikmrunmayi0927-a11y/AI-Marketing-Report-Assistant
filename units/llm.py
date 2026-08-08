import os
from groq import Groq
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Create OpenAI client
api_key = os.getenv("GROQ_API_KEY")

# Create Groq Client
client = Groq(api_key=api_key)

def generate_marketing_insights(prompt):
    print("Function is running")
    return "Test Successful"

    try:
        response = client.chat.completions.create(
            model="gpt-4.1-mini",   # You can also use "gpt-5.5-mini" if your account has access
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are an expert digital marketing analyst. "
                        "Analyze the marketing campaign data and provide "
                        "clear insights, strengths, weaknesses, and recommendations."
                    ),
                },
                {
                    "role": "user",
                    "content": prompt,
                },
            ],
            temperature=0.7,
            max_tokens=500,
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"❌ Error generating insights:\n\n{str(e)}"