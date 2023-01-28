import openai


def paraphrase(sentence, examples, api_key):
    openai.api_key = api_key
    description = "The following is a list of sentences and their paraphrased sentences:\n\n"
    description_and_example = description
    interface_sen = "Sentence: "
    interface_tag = "\nParaphrase: "
    for i in range(len(examples)):
        description_and_example = description_and_example + examples[i]
    prompt = description_and_example + interface_sen + sentence + interface_tag

    response = openai.Completion.create(
      model="text-davinci-003",
      prompt=prompt,
      temperature=0,
      max_tokens=100,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0,
      stop=["\n"]
    )
    res = response.choices[0].text.strip('\n').strip(' ')
    return res


if __name__ == "__main__":
    #sentence = "The history of Western scholarship shows that science is a derivative of philosophy."
    sentence = "your-sentence"

    example_1 = "Sentence: The need for investors to earn a commercial return may put upward pressure on prices.\nParaphrase: The need for profit is likely to push up prices.\n\n"
    example_2 = "Sentence: What should I learn to become a data scientist?\nParaphrase: How can I start learning data science?\n\n"
    #add your examples
    examples = []
    examples.append(example_1)
    examples.append(example_2)

    api_key = "your-api-key"

    result = paraphrase(sentence, examples, api_key)
    print(result)