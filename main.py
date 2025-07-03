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

        user_input = input("you: ")

        exitTriggers = ["exit", "quit", "q", "Q"]

        if user_input in exitTriggers:
            running  = False
        
        else: 
            response = client.chat.completions.create(
                model="deepseek-chat",
                messages=[
                    {"role": "user", "content": user_input},
                    {"role": "system", "content": "You will answers the users request"},
                ],
                stream=True
            )

            for chunk in response:
                typer.echo(chunk.choices[0].delta.content, nl=False)
                
            print()  # move to next line at end

if __name__ == "__main__":
    typer.run(run_ai)