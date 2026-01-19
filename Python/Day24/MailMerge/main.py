#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
with open('./Input/Names/invited_names.txt', mode='r') as names:
    line = names.readline()
    while line:
        name = line.rstrip()

        with open('./Input/Letters/starting_letter.txt', mode='r') as letter:
            lines = letter.readlines()
            with open(f'./Output/ReadyToSend/letter_to_{name}.txt', mode='w') as send:
                for i in range(0, len(lines)):
                    lines[i] = lines[i].replace('[name]', name)
                    send.write(lines[i])
            
        line = names.readline()
