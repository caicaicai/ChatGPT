import requests
import json
import os

url = "https://api.openai.com/v1/completions"
OpenAiToken = os.getenv('OpenAiToken') # None

def doChat(t):

  payload = json.dumps({
    "model": "text-davinci-003",
    "prompt": t,
    "temperature": 0,
    "max_tokens": 4000
  })
  headers = {
    'Authorization': 'Bearer ' + OpenAiToken,
    'Content-Type': 'application/json'
  }

  response = requests.request("POST", url, headers=headers, data=payload)

  return response.json()


if __name__ == "__main__":
    message = doChat("hello")
    print(message)