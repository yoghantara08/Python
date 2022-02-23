print("Phrase Translator")
print("Any vowel will replaced by \"g\"")
def translator(phrase):
    translation = ""
    for letter in phrase:
        if letter in "AIUOE":
            translation = translation + "G"
        elif letter in "aiuoe":
            translation = translation + "g"
        else:
            translation = translation + letter
    return translation

print(translator(input("Enter a phrase : ")))