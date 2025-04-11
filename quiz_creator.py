def get_filled_prompt(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        else:
            print('Input empty. Please try again.')

#prompt user to generate questions and answers
def main():
    filename = "gathered_quiz_data.txt"

    with open(filename, 'a') as file: #used 'a' to add the gathered data
        while True:
            print('Make your desired qustion')
            question = get_filled_prompt('Enter question: ')
            option_a = get_filled_prompt('Enter option for A: ')
            option_b = get_filled_prompt('Enter option for B: ')
            option_c = get_filled_prompt('Enter option for C: ')
            option_d = get_filled_prompt('Enter option for D: ') #get_filled_prompt function used to ensure there are no empty inputs

#get the correct answer
            options = {
                'A': option_a,
                'B': option_b,
                'C': option_c,
                'D': option_d,
            }   #dictionary used to map the letters into the options

            correct_answer = ''   
            while True:
                correct_answer = input('Enter the correct answer (A/B/C/D): ').strip().upper()

                if correct_answer not in options:
                    print('Option invalid, A to D only')
                    continue #to ensure valid correct answer input

                correct_answer_text = options[correct_answer]
                if not correct_answer_text:
                    print('Answer Empty, please re-check inputs.')
                else:
                    break #in case the selected answer is SOMEHOW empty

#write the question into file
            file.write(f'Question: {question}\n')
            file.write(f'A) {option_a}\n')
            file.write(f'B) {option_b}\n')
            file.write(f'C) {option_c}\n')
            file.write(f'D) {option_d}\n')
            file.write(f'\nCorrect Answer: {correct_answer}: {correct_answer_text}\n')
            file.write(f'-' * 40 + '\n')

#ask the user if they want to continue
            continue_prompt = input('Do you want to make another? (yes/any key): ').strip().lower()
            if continue_prompt != "yes":
                print(f'Exiting Program. Saving data gathered to {filename}')
                break

main()