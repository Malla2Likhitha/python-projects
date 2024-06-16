# TODO: Create a letter using starting_letter.txt

with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

for i in range(0, len(names)):
    with open('./Input/Letters/starting_letter.txt') as start:
        contents = start.readlines()
    # print(contents[0].strip("Dear"))
    contents[0] = contents[0].replace(contents[0].strip("Dear"), f' {names[i]}')
    # print(contents[0])

    with open(f"./Output/ReadyToSend/letter_for_{names[i].strip('\n')}.txt", mode='w') as letter:
        letter.writelines(contents)
