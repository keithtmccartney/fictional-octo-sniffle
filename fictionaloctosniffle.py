import os

os.environ["OPENAI_API_KEY"] = "your-api-key-here"

from langchain.llms import OpenAI

llm = OpenAI(model_name="text-davinci-003") # The meaning of life is subjective and can vary from person to person, but is generally thought of as a purpose or reason to live. It can involve finding fulfillment, developing personal connections, and achieving goals. Ultimately, it is up to each individual to discover and decide what their own meaning of life is.

question = "What is the meaning of life?"

print(llm(question))
