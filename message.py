def message():
    string=input("write whatever message you want:")
    return string
def count(message_call):
    letter_counts = {chr(i): 0 for i in range(ord('a'), ord('z') + 1)}

    for char in message_call:
        if char.isalpha():  
            letter_counts[char] += 1

    print("letter and their count:")

    for word, count in letter_counts.items():
        if count>0:
            print(f"{word}:{count}")

message_call=message().lower()
count(message_call)