
text = ""

for i in range(1,100):
    text = f"{text} ![{i}](images/{i}.png)\n"
print(text)