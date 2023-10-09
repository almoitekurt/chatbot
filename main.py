import openai

openai.api_key = "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"

def chatbot(prompt):
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = [{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content.strip()

if __name__ == '__main__':
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            break

        response = chatbot(user_input)
        print ("Chatbot:", response)