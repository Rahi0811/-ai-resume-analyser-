from google import genai
from google.genai import types

try:

    client=genai.Client(api_key="AIzaSyDFb6LfuoA2ZUhODuhKs8ey2eGNnVicL78" \
    "")

    prompt = input("Enter your prompt...")

    response = client.models.generate_content( 
        model="gemini-2.5-flash",
        contents = prompt,
        config = types.GenerateContentConfig(
            system_instruction=("Answer within 200 words"),
            temperature=0.1,
        )
        )

    print(response.text)

except Exception as e:
    print(f"An error occurred: {e}")