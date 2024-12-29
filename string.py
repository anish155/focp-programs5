def input_string():
    words=input("enter the word you want:")
    return words
def encrypt_string(string):
    string=sorted(list(set(string)))
    return string
string=input_string()
result=encrypt_string(string)
print(result)