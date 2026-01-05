letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

user_prompt = 'yes'

while user_prompt == 'yes':
    user_choice = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()

    user_msg = input("Type your message:\n").lower()
    cipher_shift = int(input("Type the shift number:\n"))
    
    # encode
    if user_choice == 'encode':
        e_msg = ''
        for ch in user_msg:
            if ch.isalpha():
                e_msg += letters[(letters.index(ch) + cipher_shift) % 26]
            else:
                e_msg += ch
    
        print(f"Here's the {user_choice}d result: {e_msg}")
    #decode
    else:
        d_msg = ''
        for ch in user_msg:
            if ch.isalpha():
                d_msg += letters[(26 + letters.index(ch) - cipher_shift) % 26]
            else:
                d_msg += ch
        print(f"Here's the {user_choice}d result: {d_msg}")

    user_prompt = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
