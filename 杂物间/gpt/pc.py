import openai 

openai.api_key = "sk-VdYpVgHEHGTd9NDnV7CCd0F4LMxE7mbuJuEhrhx6sMwHS8cF"
openai.api_base = "https://api.chatanywhere.tech"
response = openai.Image.create(
  model="dall-e-3",
  prompt="A cute baby sea otter",
  n=1,
  size="1024x1024"
)
print(1)
image_url = response['data'][0]['url']
 
print(image_url)