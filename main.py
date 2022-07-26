import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
#print(data.to_dict())

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#1. Create a dictionary in this format:
#{"A": "Alfa", "B": "Bravo"}
data_dict = {row.letter:row.code for (index, row) in data.iterrows()}
#print(data_dict)
# 2. Create a list of the phonetic code words from a word that the user inputs.
word = "AB"
#data_list = [  item. for (key, value) in data_dict.items()]
#cach 1
data_list = [data_dict[letter] for letter in word]
print(data_list)

#cach 2
data_list1 = [value for (key, value) in data_dict.items() if key in word]
print(data_list1)