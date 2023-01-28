import openai


def keywords_extraction(sentence, examples, api_key):
    openai.api_key = api_key
    description = "The following is a list of sentences and their key words:\n\n"
    description_and_example = description
    interface_sen = "Sentence: "
    interface_tag = "\nkey_words: "
    for i in range(len(examples)):
        description_and_example = description_and_example + examples[i]
    prompt = description_and_example + interface_sen + sentence + interface_tag

    response = openai.Completion.create(
      model="text-davinci-003",
      prompt=prompt,
      temperature=0,
      max_tokens=10,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0,
      stop=["\n"]
    )
    res = response.choices[0].text.strip('\n').strip(' ')
    return res


if __name__ == "__main__":
    #sentence = "Metaverse is a digital living space constructed by human beings using digital technology, which is a virtual world mapped by or beyond the real world and can interact with the real world, and has a new social system."
    sentence = "your-sentence"

    #add your examples
    example_1 = "Sentence: New energy vehicles refer to vehicles with advanced technical principles and new technologies and structures by using unconventional vehicle fuels as power sources (or using conventional vehicle fuels and adopting new on-board power devices) and integrating advanced technologies in power control and drive of vehicles. New energy vehicles include pure electric vehicles, extended program electric vehicles, hybrid electric vehicles, fuel cell electric vehicles, hydrogen engine vehicles, etc.\nkey_words: vehicles, new energy\n\n"
    example_2 = "Sentence: Autonomous vehicles (Self-driving automobile), also known as driverless cars, computer-driven cars, or wheeled mobile robots, are intelligent vehicles that are driven by computer systems. It has a history of several decades in the 20th century and is approaching practicality in the early 21st century. Self-driving cars rely on artificial intelligence, visual computing, radar, monitoring devices, and global positioning systems to work together to allow computers to operate motor vehicles automatically and safely without any human initiative.\nkey_words: vehicles, Autonomous, intelligent\n\n"
    examples = []
    examples.append(example_1)
    examples.append(example_2)

    api_key = "your-api-key"

    result = keywords_extraction(sentence, examples, api_key)
    print(result)