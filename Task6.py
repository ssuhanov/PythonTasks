catColors = {"0": "white",
             "1": "white",
             "2": "white",
             "3": "red",
             "4": "red",
             "5": "grey",
             "6": "grey",
             "7": "grey",
             "8": "black",
             "9": "black"}

catSizes = {"0": "small",
            "1": "small",
            "2": "small",
            "3": "medium",
            "4": "medium",
            "5": "big",
            "6": "big",
            "7": "big",
            "8": "huge",
            "9": "huge"}

catCharacters = {"0": "lazy",
                 "1": "lazy",
                 "2": "calm",
                 "3": "calm",
                 "4": "calm",
                 "5": "active",
                 "6": "active",
                 "7": "active",
                 "8": "hyperactive",
                 "9": "hyperactive"}

catTypes = {"0": "bald",
            "1": "bald",
            "2": "bald",
            "3": "shorthaired",
            "4": "shorthaired",
            "5": "shorthaired",
            "6": "longhaired",
            "7": "longhaired",
            "8": "extra longhaired",
            "9": "extra longhaired"}

def catParameter(parameterNumber, parametersDictionary, unknownPhrase):
    if parameterNumber in parametersDictionary.keys():
        return parametersDictionary[parameterNumber]
    else:
        return unknownPhrase

catNumber = input("Please enter the cat number: ")
if len(catNumber) >= 4:
    catArray = []
    catArray.append(catParameter(catNumber[0], catColors, "unknown color"))
    catArray.append(catParameter(catNumber[1], catSizes, "unknown size"))
    catArray.append(catParameter(catNumber[2], catCharacters, "unknown character"))
    catArray.append(catParameter(catNumber[3], catTypes, "unknown type"))
    catDescription = " ".join(catArray)
    print("This is a %s cat" % catDescription)
else:
    print("Incorrect input, sorry :(")
