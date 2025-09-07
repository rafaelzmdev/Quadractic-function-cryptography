print("I will encrypt the text you submit to me. At the end of the encryption, I will also give you a key.")
rawtext = str(input("Write your text here >>> "))
#Dictionary:
asciivalue = []
for char in rawtext:
    lettervalue = ord(char)
    if lettervalue > 127:
        raise ValueError (f"Script only works with 7 bit ASCII characters. Replace following: '{char}'")
    asciivalue.append(float(lettervalue))
#Asking for the users' personal key
while True:
    try:
        print("Okay. So now that I have your text, I will be giving you the opportunity to choose a quadractic function to encrypt your text. WARNING! Save the function, as it will be the key for decrypting your text.")
        a = int(input("Type the 'a' coefficient of the function [+-ax²] [don't use a value over 20 if you want to preserve this code's sanity, don't use zero aswell] as following >> "))
        b = int(input("Type the 'b' coefficient of the function [+-bx] as following >> "))
        c = int(input("Type the 'c' coefficient of the function [+-z] as following >> "))
    except ValueError:
        print("You can only assign integers as coefficients.")
        continue
    print(f"Your key is now assigned as: {a}x² {'+' if b >= 0 else ''}{b}x {'+' if c >= 0 else ''}{c}. Save this key.")
    confirmation = input("Do you want to proceed or did you not like the key? Type 'proceed' or 'restart', as following >> ")
    if confirmation == "proceed":
        break
    elif confirmation == "restart":
        print("Follow the same steps you did before. Don't mess up this time! ;)")
#Applying the quadratic equation over the ASCII value to be encrypted
encryptedascii = [a * x**2 + b * x + c for x in asciivalue]
print(f"Your text is now encrypted. Save it. In order to decrypt, use the decrypting script. Write this down, together with your coefficients (keys). The second script will ask for both. Here is your text: {(encryptedascii)}")
input("Press Enter to close the window...")



