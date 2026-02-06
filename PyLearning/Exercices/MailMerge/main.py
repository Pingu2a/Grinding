
#Taking the template letter
with open("./Input/Letters/starting_letter.txt") as letter:
    myLtr = letter.read()

#Taking the names
with open("./Input/Names/invited_names.txt") as Names:
    name_list = Names.readlines()

#Strip the names inside the list to remove '\n', then replace [name] by real name
#Finally creating a new file with each names
for i in name_list:
    name_strip = i.strip()
    new_ltr = myLtr.replace("[name]", name_strip)

    with open(f"./Output/ReadyToSend/letter_for_{name_strip}.txt", mode="w") as finalLetter:
        finalLetter.write(new_ltr)
print(myLtr)