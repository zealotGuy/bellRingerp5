def caesar(word):
    changed = ""
    for x in word:
        changed += chr(((ord(char)-ord('a')+1)%26)+ord("a"))
    return changed
print(caesar("Mr.Baez"))
