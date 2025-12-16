from openai import AzureOpenAI
import os


client = AzureOpenAI(
    api_version="2024-12-01-preview",
    azure_endpoint="https://ajitk-mj8s6u4e-eastus2.cognitiveservices.azure.com/",
    api_key="FEkcFMpvuu9CjMmUXo4wlyG5ZFvrwhXycc2VBK1Kj6y8yu3FAd9IJQQJ99BLACHYHv6XJ3w3AAAAACOG00pG"
)

prompt = (
    "Translate the English to Korean:\n"
    "English: Hello. \n Korean: 안녕하세요.\n"
    "English: I love programming. \n Korean:"
)

response = client.chat.completions.create(
    messages=[{"role": "user", "content": prompt}],
    max_completion_tokens=100000,
    model="o3-mini"
)



print(response.choices[0].message.content)

