import json

with open("messages.json", "r") as file:
    messages = json.load(file)

print(messages)
while True:
    message = input("Write your message: ")
    if message.lower() == "exit":
        break
    messages.append(message)

with open("messages.json", "w") as file:
    json.dump(messages, file)


