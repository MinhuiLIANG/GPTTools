import openai


def summary(sentence, examples, api_key):
    openai.api_key = api_key
    description = "The following is a list of sentences and the summaries of them:\n\n"
    description_and_example = description
    interface_sen = "sentence: "
    interface_tag = "\nsummary: "
    for i in range(len(examples)):
        description_and_example = description_and_example + examples[i]
    prompt = description_and_example + interface_sen + sentence + interface_tag

    response = openai.Completion.create(
      model="text-davinci-003",
      prompt=prompt,
      temperature=0,
      max_tokens=150,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0,
      stop=["\n"]
    )
    res = response.choices[0].text.strip('\n').strip(' ')
    return res


if __name__ == "__main__":
    #sentence = "Several school districts in Hampton Roads are holding classes this Presidents' Day to make up for days missed because of the snow."
    sentence = "your-sentence"

    #add your examples
    example_1 = "sentence: Maya Rudolph and longtime partner Paul Thomas Anderson have welcomed their fourth child, a source confirms to Us Weekly.\nsummary: Maya Rudolph have welcomed their fourth child.\n\n"
    example_2 = "sentence: Lindsey Vonn returned to skiing over the weekend in Chile nearly seven months after a season-ending crash that required surgery on her right knee.\nsummary: Lindsey Vonn returned to skiing over the weekend in Chile.\n\n"
    example_3 = "sentence: Two Chinese war ships, ``JING GANGSHA'' and ``HENG SHUI'' arrived at the port of Trincomalee on 13 th January 2014 on a good will visit.\nsummary: Two Chinese war ships, arrived at the port of Trincomalee will visit.\n\n"
    examples = []
    examples.append(example_1)
    examples.append(example_2)
    examples.append(example_3)

    api_key = "your-api-key"

    result = summary(sentence, examples, api_key)
    print(result)