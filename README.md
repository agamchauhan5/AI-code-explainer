# Deco — AI Code Explainer (CLI)

**Deco** is your personal AI code decoder that explains any code you paste — in simple, beginner-friendly language — right from your terminal.

---

## 💡 What It Does

Just paste your code and Deco will break it down step-by-step using DeepSeek's powerful AI models.

Works with:
- Python 🐍
- JavaScript ⚙️
- HTML/CSS 🌐
- Any other programming language

---

## 🧠 Features

- Line-by-line code explanations
- Beginner-friendly language
- Works in any terminal
- Supports multiline code blocks
- Explains single lines on request
- Streamed AI responses

---

## 🚀 Setup Guide (1-File Copy & Go)

### 1. 💻 Create a project folder

```bash
mkdir deco
cd deco
2. 📄 Create a file main.py and paste this code:
python
Copy
Edit
import os
import time
from dotenv import load_dotenv
from openai import OpenAI
import typer

load_dotenv()

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
3. 📦 Install the required packages
Mac/Linux:
bash
Copy
Edit
python3 -m venv _venv
source _venv/bin/activate
pip install openai python-dotenv typer
Windows:
cmd
Copy
Edit
python -m venv _venv
_venv\Scripts\activate
pip install openai python-dotenv typer
4. 🔐 Create a .env file in the same folder:
ini
Copy
Edit
DEEPSEEK_API_KEY=your_deepseek_api_key_here
✅ 5. Run the app:
Mac/Linux:
bash
Copy
Edit
python main.py
Windows:
cmd
Copy
Edit
python main.py
🧪 Example
pgsql
Copy
Edit
Paste your code that you would like deco to explain line by line:
for i in range(3):
    print(i)
Output:

This loop prints numbers from 0 to 2, increasing one by one...

🙋‍♂️ Author
Made with ❤️ by Agam — for beginner coders who want a little help from AI.