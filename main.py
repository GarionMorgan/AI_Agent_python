import os
import sys
from dotenv import load_dotenv
from google import genai
#loads information from the dotenv file
load_dotenv()
#accesses the api key
api_key = os.environ.get("GEMINI_API_KEY")
#operating the gemini client with the api key
client = genai.Client(api_key=api_key)


def main():
    print("Hello from ai-agent-project!")
    #calling the sys import to grab user input from the CLI
    if len(sys.argv) < 2:
        print(f"Usage: python3 main.py <User request>")
        sys.exit(1)
    #saves user prompt from the CLI
    user_prompt = sys.argv[1]

    response = client.models.generate_content(
        model='gemini-2.0-flash-001', contents=user_prompt
    )

    print(response.text)
    prompt_tokens = response.usage_metadata.prompt_token_count
    candidates_tokens = response.usage_metadata.candidates_token_count
    print(f"Prompt tokens: {prompt_tokens}")
    print(f"Response tokens: {candidates_tokens}")


if __name__ == "__main__":
    main()
