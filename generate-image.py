from openai import Image

#prompt = "Hänsel and Gretel stand in awe, their eyes wide with wonder as they take in the sight of the witch's house for the first time. The house appears to be made of gingerbread and frosting, with a large, brightly-colored candy roof. The front door is a large, wooden door with a golden handle. The windows are lollipops, and the garden is full of brightly-colored flowers and vegetables. The air is filled with the smell of freshly-baked cookies."
prompt = "Ernie and Bert eat cookies"

response = Image.create(
  prompt=prompt,
  n=1,
  size="1024x1024"
)

print(response)

image_url = response['data'][0]['url']

print(image_url)
