import openai

openai.api_key = 'your openaiAPI'

def chat(input_message):
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": input_message},
        ]
    )
    chat_response = response['choices'][0]['message']['content']
    return chat_response


user_input = input("Вы: ")
while user_input.lower() != 'stop':
    response = chat(user_input)
    print("AI: " + response)
    user_input = input("Вы: ")
