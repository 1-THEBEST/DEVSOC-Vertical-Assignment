from google import generativeai as genai

# Make sure API key is configured
genai.configure(api_key="AIzaSyBboNa7eRaEhFkxhuLX_FhiYQhyfnal9zg")

# List all models
models = genai.list_models()
for model in models:
    print(model)
