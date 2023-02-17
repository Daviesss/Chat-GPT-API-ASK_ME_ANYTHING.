# import the necessary library.
#!/usr/bin/env python3
import openai
# we set up a client (openAi).
openai.api_key="This is your secret key"
# let's create a while loop that will let us ask question constantly and behave just like opanai.

while True:
    engine = "text-davinci-003"
    prompt =input(' Ask me something:')
    if 'exit' in prompt or 'quit' in prompt:
        break
    #Give me an answer.
    completion= openai.Completion.create(
        engine = engine,
        prompt = prompt,
        max_tokens =  1024,
        n=1, stop=None,
        temperature= 0.5
    )
    #let's extract useful part of the response.
    response = completion.choices[0].text
    #print the response.
    print(response)