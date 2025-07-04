import os
import time
from dotenv import load_dotenv
from openai import OpenAI
import typer

load_dotenv()

# app = typer.Typer()


def run_ai():
    client = OpenAI(api_key=os.getenv('DEEPSEEK_API_KEY'), base_url="https://api.deepseek.com")

    running = True

    while running == True:

        user_input = input("Paste your code that you would like deco to explain line by line: ")

        exitTriggers = ["exit", "quit", "q", "Q"]

        if user_input in exitTriggers:
            running  = False
        
        else: 
            response = client.chat.completions.create(
                model="deepseek-chat",
                messages=[
                    {"role": "user", "content": user_input},
                    {"role": "system", "content": "You will explain the users code they have given you it may be in any coding language. Explain to the user in very simple launguage. If they past lots of code but request to you to explain one line explain only one line."},
                ],
                stream=True
            )

            for chunk in response:
                typer.echo(chunk.choices[0].delta.content, nl=False)
                
            print()  # move to next line at end

if __name__ == "__main__":
    typer.run(run_ai)