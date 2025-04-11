#prompt user to generate questions and answers
filename = "gathered_quiz_data.txt"

with open(filename, 'a') as file: #used 'a' to add the gathered data
    while True:
        print('Make your desired qustion')
        question = input('Enter question: ')
        option_a = input('Enter option for A: ')
        option_b = input('Enter option for B: ')
        option_c = input('Enter option for C: ')
        option_d = input('Enter option for D: ')

#get the correct answer
while correct_answer not in ['A', 'B', 'C', 'D']:
    correct_answer = input('Enter the correct answer: ').strip().upper()

#write the question into file
file.write(f'Question: {question}\n')
file.write(f'A) {option_a}\n')
file.write(f'B) {option_b}\n')
file.write(f'C) {option_c}\n')
file.write(f'D) {option_d}\n')
file write(f'\nCorrect Answer: {correct_answer}')
#ask the user if they want to continue