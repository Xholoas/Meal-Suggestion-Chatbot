import openai

openai.api_key = "KEY"
# Giving a prompt to ChatGPT with our 'API Key' to get an output.
completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Generate a 600 kcal breakfast suggestion."}])
print(completion.choices[0].message.content)
