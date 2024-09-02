import url

with open("./data/test.txt", "r", encoding="utf-8") as file:
    txt = file.read()

mar = url.txt2title(txt)
print(mar)
