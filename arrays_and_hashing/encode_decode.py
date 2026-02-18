data = ["Hello", "World"]


def encode(strs: list):
    message = []
    for i, j in enumerate(strs):
        message.append(f"{len(j)}#{j}")
    print(message)
    return "".join(message)


def decode(s: str):
    message = []
    start = 0
    while len(s) > start:
        stop = s.find("#", start)
        num = int(s[start:stop])
        message.append(s[stop + 1 : stop + num + 1])
        start = stop + num + 1
    return message


print(decode(encode(data)))
