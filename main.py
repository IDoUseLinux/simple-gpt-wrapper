import openai

try :
    with open("API.KEY", 'r') as API_KEY :
        openai.api_key = API_KEY.read()
except FileNotFoundError :
    openai.api_key = input("Please copy and paste your API key or put it in the file 'API.KEY' in the program directory.")

with open("systemprompt.txt", 'r') as SYSTEM_PROMPT :
    system_prompt = SYSTEM_PROMPT.read()

chat_history = [
    {"role" : "system", "content" : system_prompt}    
]

print("Enter anything you want to ask me!")
output = ""

while True :
    try :
        user_input = input(output+"\n")
        chat_history.append({"role" : "user", "content" : user_input})
        response = openai.chat.completions.create(
            model="gpt-4o",
            messages=chat_history,
            max_tokens=300,
            n=1,
            stop=None,
            temperature=0.7
        )

        output = response.choices[0].message.content
    except KeyboardInterrupt :
        break
    except Exception as e :
        print(f"An error occurred: {str(e)}")
    