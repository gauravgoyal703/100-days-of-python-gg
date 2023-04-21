student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
#{"A": "Alfa", "B": "Bravo"}

with open("nato_phonetic_alphabet.csv") as file:
    word_dict = {line.split(",")[0]:line.split(",")[1].split()[0] for line in file.readlines()[1:]}

word_data = pandas.read_csv("nato_phonetic_alphabet.csv")
word_dict_2 = {value.letter:value.code for (index, value) in word_data.iterrows()}
print(word_dict_2)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

word = input("Please add a word: ").upper()

word_list = [word_dict_2[wchar] for wchar in word]
print(word_list)

