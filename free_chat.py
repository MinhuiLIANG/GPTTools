import openai as ai
completion = ai.Completion()


def chatbot_interface(description, history, sentence, api_key):
    ai.api_key = api_key
    chat_log = description + "\n" + history + "\n"
    prompt = f"{chat_log}Human: {sentence}\nAI:"
    response = completion.create(
        model="text-davinci-002",
        prompt=prompt,
        temperature=0.85,
        max_tokens=100,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
        stop=[" Human:", " AI:"])
    res = response.choices[0].text.strip('\n')

    return res


if __name__ == "__main__":
    history = ""

    #description = "This is a conversation with an AI assistant. This assistant is very kind, helpful and humorous."
    description = "your-description"

    #user_sentences = ["Hi, do you know the Avengers?", "What's your favourite character of the Avengers?"]
    user_sentences = "your-sentences"

    api_key = "your-api-key"

    #an example of usage, the user_sentences can be obtained from other interface(e.g. front-end of a softerware, user input)
    #while fit your conditions
    for i in range(2):
        res = chatbot_interface(description, history, user_sentences[i], api_key)
        print(f"user: {user_sentences[i]}\nchatbot: {res}")
        user_history = "Human: " + user_sentences[i] + "\n"
        chatbot_history = "AI: " + res
        history = history + user_history + chatbot_history



