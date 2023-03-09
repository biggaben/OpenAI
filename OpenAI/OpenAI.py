
import openai
import time

# Set up the OpenAI API client
openai.api_key = "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"

# Set up the OpenAI chat endpoint
endpoint = "https://api.openai.com/v1/completions"

# Initialize chat log
chat_log = ""

# Send a message to ChatGPT and get a response
def send_message(message):
    response = openai.Completion.create(
        engine="davinci",
        max_tokens=1024,
        n=1,
        #stop="",
        temperature=0.5,
    )
    message = response.choices[0].text.strip()

    print("ChatGPT:", response)
    return

# Loop to send and receive chat messages
while True:
    # Get user input
    user_input = input("You: ")

    # Send user input to ChatGPT
    response = send_message(user_input)

    ## Print ChatGPT's response
    #print("ChatGPT:", response)

    ## Add a delay to prevent hitting the API too frequently
    #time.sleep(1)

#___________________________________________________
#import openai
#import time

#openai.api_key = "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"

## set up the OpenAI chat endpoint
#endpoint = "https://api.openai.com/v1/engines/gpt-3.5-turbo/completions"

## send a message to ChatGPT and get a response
#def send_message(message):
#    prompt = f"User: {message}\nChatGPT:"
#    response = openai.Completion.create(
#        engine="gpt-3.5-turbo",
#        prompt=prompt,
#        max_tokens=256,
#        n=1,
#        stop=[".", "!"],
#        #stop=None,
#        temperature=0.5,
#    )
#    message = response.choices[0].text.strip()
#    return message

## loop to send and receive chat messages
#while True:
#    # get user input
#    user_input = input("You: ")
    
#    # send user input to ChatGPT
#    response = send_message(user_input)
    
#    # print ChatGPT's response
#    print("ChatGPT:", response)
    
#    # add a delay to prevent hitting the API too frequently
#    time.sleep(1)



#import os
#import openai
#import json

#openai.api_key = "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"

#openai.ChatCompletion.create(
#    model="gpt-3.5-turbo",
#    messages=[
#        {"role": "system", "content": "You are a helpful assistant."},
#        {"role": "user", "content": "Who won the world series in 2020?"},
#        {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
#        {"role": "user", "content": "Where was it played?"}
#    ]
#)

    ## list models
    #openai api models.list

    ## create a completion
    #openai api completions.create -m ada -p "Hello world"

    ## create a chat completion
    #openai api chat_completions.create -m gpt-3.5-turbo -g user "Hello world"

    ## generate images via DALLE API
    #openai api image.create -p "two dogs playing chess, cartoon" -n 1


    #import openai
    #openai.api_key = "sk-..."  # supply your API key however you choose

    #completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Hello world!"}])
    #print(completion.choices[0].message.content)


    #import openai
    #openai.api_key = "sk-..."  # supply your API key however you choose

    #image_resp = openai.Image.create(prompt="two dogs playing chess, oil painting", n=4, size="512x512")




    ## list models
    #models = openai.Model.list()

    ## print the first model's id
    #print(models.data[0].id)

    ## create a completion
    #completion = openai.Completion.create(model="ada", prompt="Hello world")

    ## print the completion
    #print(completion.choices[0].text)



    #user_in = input("Type your query(q to exit):\n==> ")
    #print()
    #if(user_in == "n"):
    #    print()
    #    print("Exiting program.")
    #    print()
    #    quit()
    #print()
    #print("Processing query. Please wait...")


    #response = openai.Completion.create(
    #    model="gpt-3.5-turbo-0301",
    #    prompt=user_in,
    #    max_tokens=512,
    #    temperature=0,       
    #    top_p=0.1,
    #    frequency_penalty=0.2,
    #    presence_penalty=0,
    #    )

    #json_obj = response["choices"][0]

    #json_str = json_obj["text"]
    
    #print("Processing finished.")
    #print()
    #print("Answer:")
    #print("----------------------------------------------------")
    #print(json_str)
    #print()
    #print()
    #print("----------------------------------------------------")
    #print()
    #print()



# wget https://api.openai.com/v1/chat/completions \
#  -H 'Content-Type: application/json' \
#  -H 'Authorization: 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' \
#  -d '{
#    "prompt": "I like to eat",
#    "max_tokens": 4000
#  }'
#  -d '{
#  "model": "gpt-3.5-turbo",
#  "messages": [{"role": "user", "content": "Say this is a test!"}],
#  "temperature": 0.7
# }'s