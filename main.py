import pyperclip as pc

names = ["Apple", "Banana", "Cherry", "Dog", "Elephant"]
present = []
absent = []
not_audio = []
asking = True
number = 0

while asking:
    question = names[number]
    answer = input(question + ": ")
    if answer == "p":
        present.append(question)
    if answer == "a":
        absent.append(question)
    if answer == "n":
        not_audio.append(question)

    if number == 38:
        asking = False
    number += 1

correction = input("Names to be removed: ")
correction_list = correction.split(",")
for i in correction_list:
    absent.remove(i)

counter = 1
absentees = ''
for x in absent:
    temp = f"{counter}.{x}"
    absentees = absentees + temp + "\n"
    counter += 1
count2 = 1
not_audio_names = ''
for i in not_audio:
    tempo = f"{count2}.{i}"
    not_audio_names = not_audio_names + tempo + "\n"
    count2 += 1
if not_audio_names == '':
    not_audio_names = "Nil"
not_audio_msg = f"Students not connected to audio: {not_audio}"
present_length = len(present)
absent_length = len(absent)
message = f"Good Morning Ma'am, the attendance of IX-G for today is as follows: \nAbsentees: \n{absentees} \nStudents not connected to audio:\n{not_audio_names}.\nThe total strength today was {5 - absent_length}/5."
pc.copy(message)
print(message)
