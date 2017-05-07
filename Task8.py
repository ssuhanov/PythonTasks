letters = {'а': 'a',
           'б': 'b',
           'в': 'v',
           'г': 'g',
           'д': 'd',
           'е': 'e',
           'ё': 'e',
           'ж': 'zh',
           'з': 'z',
           'и': 'i',
           'й': 'y',
           'к': 'k',
           'л': 'l',
           'м': 'm',
           'н': 'n',
           'о': 'o',
           'п': 'p',
           'р': 'r',
           'с': 's',
           'т': 't',
           'у': 'u',
           'ф': 'f',
           'х': 'h',
           'ц': 'c',
           'ч': 'ch',
           'ш': 'sh',
           'щ': 'sch',
           'ь': " ' ",
           'ы': 'y',
           'ъ': " ' ",
           'э': 'e',
           'ю': 'ju',
           'я': 'ya'}

userInput = input("Please enter some sentence in russian: ")

resultString = ""
for inputLetter in userInput:
    lowerLetter = inputLetter.lower()
    if lowerLetter in letters.keys():
        translitLetter = letters[lowerLetter]
        if inputLetter == lowerLetter:
            resultString += translitLetter
        else:
            resultString += translitLetter.upper()
    else:
        resultString += inputLetter

print(resultString)
