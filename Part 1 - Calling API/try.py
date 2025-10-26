import os
from google import generativeai as genai
import json

# Configure the API key 
os.environ["GOOGLE_API_KEY"] = "AIzaSyBboNa7eRaEhFkxhuLX_FhiYQhyfnal9zg"
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

file = open("./text.txt" , "r")
out = open("./response.json" , "w")

prompt_list = file.readlines()
response_list = [0 for i in range(len(prompt_list))]

# Initialize the GenerativeModel
model = genai.GenerativeModel('models/gemini-2.5-flash')

## Generating content
#response = model.generate_content(prompt_text)

#actual answer stored in (response.text)
i = 0
for prompt in prompt_list:
    response = (model.generate_content(prompt)).text
    store = {"prompt" : prompt, "response" : response}
    response_list[i] = store
    i+=1
json.dump(response_list,out,indent=4)
print("Finished.")
