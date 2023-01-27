import openai


def senti_analysis(sentence, examples, api_key):
    openai.api_key = api_key
    description = "The following is a list of sentences and the emotions they have:\n\n"
    description_and_example = description
    interface_sen = "sentence: "
    interface_tag = "\nEmotion: "
    for i in range(len(examples)):
        description_and_example = description_and_example + examples[i]
    prompt = description_and_example + interface_sen + sentence + interface_tag

    response = openai.Completion.create(
      model="text-davinci-003",
      prompt=prompt,
      temperature=0,
      max_tokens=6,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0,
      stop=["\n"]
    )
    res = response.choices[0].text.strip('\n').strip(' ')
    return res


if __name__ == "__main__":
    sentence = "I really love to watch movies in cinema"

    example_positive = "Sentence: I am feeling so good watching a movie.\nEmotion: Positive\n\n"
    example_neutral = "Sentence: I want to watch movies in my leisure time.\nEmotion: Neutral\n\n"
    example_negative = "Sentence: I think watching movies is a waste of time.\nEmotion: Negative\n\n"
    examples = []
    examples.append(example_positive)
    examples.append(example_neutral)
    examples.append(example_negative)

    api_key = "your-api-key"

    result = senti_analysis(sentence, examples, api_key)
    print(result)

