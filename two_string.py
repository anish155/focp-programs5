def first_string():
    first_word=input("enter your word:")
    set1=set(first_word)
    return set1
def second_string():
    second_word=input("enter your word:")
    set2=set(second_word)
    return set2
def same_one_string(string1,string2):
    one_same=string1 | string2
    print("letter that appear in at least one of two words:",one_same)
def both_same_string(string1,string2):
    both_same=string1 & string2
    print("letter that appear in both words:",both_same)
def not_both_string(string1,string2):
    not_same=string1 ^ string2
    print("letter that donot appear in both words:",not_same)
string1=first_string()
string2=second_string()
same_one_string(string1,string2)
both_same_string(string1,string2)
not_both_string(string1,string2)