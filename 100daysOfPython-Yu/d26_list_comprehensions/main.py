"""
split name into letters
get first letter from capital_letters that is equal to letter in name
get index of that letter from capital_letters
get word in alphabet equal to index of letter in capital_letters
"""
alphabet = ['Amore', 'Bella', 'Ciao', 'Dolce', 'Elegante', 'Fragile', 'Grazie', 'Hai', 'Innamorato', 'Joviale', 'Kiss',
            'Luna', 'Mamma', 'Natura', 'Oceano', 'Pasta', 'Quando', 'Ragazzo', 'Sole', 'Terra', 'Uva', 'Vino', 'Wine',
            'Xylophone', 'Yogurt',
            'Zucchero']

name = 'Max'
nato_names = [word for letter in name for word in alphabet if word[0].lower() == letter.lower()]
print(nato_names)



#list comprehension exercise

#conditional list comprehension
names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
short_names = [name for name in names if len(name) < 5]
print(short_names)

capital_names = [name.upper() for name in names if len(name) > 4]
print(capital_names)

#squaring numbers in a list
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [num * num for num in numbers]
print(squared_numbers)

#filter even numbers from list
even_numbers = [9, 0, 32, 8, 2, 8, 7, 64, 29, 42, 99]
filtered_even_numbers = [num for num in even_numbers if num % 2 == 0]
print(filtered_even_numbers)

#dict comperehension
import random
names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
student_scores = {name: random.randint(1, 100) for name in names}
print(student_scores)

passed_students = {name: score for (name, score) in student_scores.items() if score >= 60}
print(passed_students)

#sentence to dictionary
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
sentence_split = sentence.split()
sentence_split_dict = {word: len(word) for word in sentence_split}
print(sentence_split_dict)

#weather celcius to fahrenheit
weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

weather_f = {day: (temp * 9/5) + 32 for (day, temp) in weather_c.items()}
print(weather_f)

#iterate over pandas dataframe
import pandas as pd
student_dict = {
    'student': ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie'],
    'score': [56, 78, 98, 67, 89, 92]
}

student_df = pd.DataFrame(student_dict)
for (index, row) in student_df.iterrows():
    print(row.student)

#iterate over pandas dataframe and create new column
for (index, row) in student_df.iterrows():
    student_df.at[index, 'score'] = row.score + 1
print(student_df)

#iterate over pandas dataframe and create new column
for (index, row) in student_df.iterrows():
    student_df.at[index, 'score'] = row.score + 1
print(student_df)


