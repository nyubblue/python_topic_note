import  pandas

student_dict = {
    "Student" : ["Buyn", "Hung", "Dat"],
    "Score": [80, 80, 80]
}
for (key, value) in student_dict.items():
    print(value)

print("\n\n")
student_data_frame = pandas.DataFrame(student_dict)

#Loop through a data frame
for (key, value) in student_data_frame.items():
    print(key)

print("\n\n\n")
#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    print(row.student)
    print("\n")