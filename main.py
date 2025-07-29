import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types





def main():
    #loads information from the dotenv file
    load_dotenv()
    #accesses the api key
    api_key = os.environ.get("GEMINI_API_KEY")
    #operating the gemini client with the api key
    client = genai.Client(api_key=api_key)


    print("Hello from ai-agent-project!")

    verbose = "--verbose" in sys.argv
    args = []
    for arg in sys.argv[1:]:
        if not arg.startswith("--"):
            args.append(arg)
    #calling the sys import to grab user input from the CLI
    if not args:
        print(f"AI Code Assistant")
        print(f'\nUsage: python main.py "your prompt here" [--verbose]')
        print(f'Example: python main.py "How do I build a calculator app?"')
        sys.exit(1)
    #saves user prompt from the CLI
    user_prompt = " ".join(args)

    if verbose:
        print(f"User prompt: {user_prompt}\n")
    #keeping track of mulitple messages from the user
    messages = [
    types.Content(role="user", parts=[types.Part(text=user_prompt)]),
]
    
    generate_content(client, messages, verbose)

def generate_content(client, messages, verbose):
       
    #generating the response from the LLM
    response = client.models.generate_content(
        model='gemini-2.0-flash-001', contents=messages,
    )
    if verbose:
        prompt_tokens = response.usage_metadata.prompt_token_count
        candidates_tokens = response.usage_metadata.candidates_token_count
        print(f"Prompt tokens: {prompt_tokens}")
        print(f"Response tokens: {candidates_tokens}")
    print("Response:")
    print(response.text)
    


if __name__ == "__main__":
    main()
