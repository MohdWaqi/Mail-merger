############################ Opening the names file that needs to be invited. #################################

with open("Input/Names/invited_names.txt", "r") as names:
    invitation_to = names.readlines()
new_names = []
for name in invitation_to:
    person = name.strip("\n")
    new_names.append(person)

############################## replacing the name in the example letter to invited names ##############################

with open("Input/Letters/starting_letter.txt", "r") as doc:
    letter = doc.readlines()
for characters in new_names:
    persons = letter[0].replace("[name]", f"{characters}")
    with open(f"Output/ReadyToSend/letter_for_{characters}.txt", "w") as invitation:
        invitation.write(f"{persons}{letter[1]}{letter[2]}{letter[3]}{letter[4]}{letter[5]}{letter[6]}")


