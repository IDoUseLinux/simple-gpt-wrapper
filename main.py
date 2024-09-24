import openai

with open("API.KEY", 'r') as API_KEY :
    openai.api_key = API_KEY.read()

with open("systemprompt.txt", 'r') as SYSTEM_PROMPT :
    system_prompt = SYSTEM_PROMPT.read()

chat_history = [
    {"role" : "system", "content" : system_prompt}    
]

print("Enter anything you want to ask me!\n")
output = ""

while True :
    user_input = input(output)
    try :
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
    except Exception as e :
        print(f"An error occurred: {str(e)}")
    