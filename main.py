import random
import math
import os
import base64

def xor(a:int,b:int):
    return str((a+b) % 2)

def unicode_to_bin(txt):
    return "".join((format(ord(char),"08b")) for char in txt)

def bin_to_unicode(bin_txt):
    ans = []
    for i in range(0, len(bin_txt), 8):
         ans.append(chr(int(bin_txt[i:i+8],2)))
    return ''.join(ans)    

def bin_to_b64(bin_txt):
    b64 = base64.b64encode(int(bin_txt, 2).to_bytes((len(bin_txt)+7)//8, 'big')).decode()
    return b64

def b64_to_bin(txt):
    raw_bytes = base64.b64decode(txt)
    return ''.join(format(byte, '08b') for byte in raw_bytes)    

def generate_bin_pad(bin_txt):
    #One-time pad in binary
    pad = bin(random.randint(0,2**int(len(bin_txt))))[2:]

    #Ensure pad is same length as message
    if len(pad) < len(bin_txt):
        for x in range(0,(len(bin_txt)-len(pad))):
            pad = "0" + pad 
    return pad


def encrypt_bin(text,bin_pad):
    encryption=""

    #XOR encryption with bin_pad
    for i, letter in enumerate(text[::-1]):
        encryption = xor(int(letter),int(bin_pad[-i-1])) + encryption
    return encryption



def encrypt(txt):
    #Convert message to binary
    bin_txt = unicode_to_bin(txt)
    #Generate binary pad
    bin_pad = generate_bin_pad(bin_txt)
    
    #Encrypted text in binary
    bin_encrypted_txt = encrypt_bin(bin_txt,bin_pad)
    
    #Pad converted to unicode
    pad = bin_to_b64(bin_pad)
    
    #Encrypted text converted to unicode
    encrypted_txt = bin_to_b64(bin_encrypted_txt)
    
    return encrypted_txt+pad

def decrypt(code):
    #Remove whitespace in encrypted code
    code = code.strip()
    
    #Split code into encrypted text and pad
    encrypted_txt = code[:len(code)//2]
    pad = code[len(code)//2:]
    
    #Convert to binary 
    bin_encrypted_txt = b64_to_bin(encrypted_txt)
    bin_pad = b64_to_bin(pad)

    #Use pad to decrypt text
    bin_txt = encrypt_bin(bin_encrypted_txt,bin_pad)

    #Convert binary to unicode and return original text
    txt = bin_to_unicode(bin_txt)
    return txt


while True:
        choice = input("Would you like to \nEncrypt (1)\nDecrypt (2)\n")
        if choice == '1': #Encrypt
            txt = input("Enter your message:\n")
            print("\nEncrypted text:\n", encrypt(txt))
            input("\nPress ENTER to continue...")
            
        elif choice == '2': #Decrypt
            code = input("Enter your code:\n")

            try:
                print("\nDecrypted text:", decrypt(code))
            except:
                print("Your code is invalid!")
            input("\nPress ENTER to continue...")
            
        elif choice == '3':
            break
        elif choice == '':
            pass 
            
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
            input("\nPress ENTER to continue...")
            
    
    
if __name__ == "__main__":
    main()



#ask for string input
#converted to binary
#binary bin_pad is generated
#text encrypted in binary
#encrypted text and bin_pad converted to ascii
#user recieves unicode encrypted message and unicode bin_pad

#user enters unicode encrypted message and unicode bin_pad
#split string into encrypted message and bin_pad
#convert both bin_pad and encrypted message into binary
#decrypt encrypted message with bin_pad
#user recieves original text
