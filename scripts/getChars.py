


def chars(txt_file):
    chars=[]
    with open(txt_file, "r", encoding="utf-8") as ttf:
        for line in ttf:
            chars+=[*line]
    output = set()

    for x in chars:
        output.add(x)

    chars = list(output)
    return chars

path = r"name.csv"
charList = chars(path)
print("".join(charList).replace("\n",""))