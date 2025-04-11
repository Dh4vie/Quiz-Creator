#prompt user to generate questions and answers
print('Make your desired qustion')
question = input('Enter question: ')
option_a = input('Enter option for a: ')
option_b = input('Enter option for b: ')
option_c = input('Enter option for c: ')
option_d = input('Enter correct answer for d: ')

#get the correct answer
while correct_answer not in ['a', 'b', 'c', 'd']:
    correct_answer = input('Enter the correct answer: ').strip().lower()

#write the question into file
#ask the user if they want to continue