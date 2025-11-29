print("You have encrypted your text. This is the script you need to decrypt it.")
#assign coefficient values (keys):
print("You've chosen some values to be the keys for your encryption. I will need them to decrypt the text.")
while True:
    try:
         a = int(input("Insert here the first number of your key, together with it's +/- signal >> "))
         b = int(input("Same steps, for the second number >> "))
         c = int(input("Now the third and last number >>> "))
    except ValueError:
        print("Please insert correct values.")
        continue
    print(f"Your key is {a}x² {'+' if b >= 0 else ''}{b}x {'+' if c >= 0 else ''}{c}.")
    confirmation = input("Is that information correct? Type yes/no, accordingly >> ")
    if confirmation == "yes":
        print("Okay. I need your text now.")
        break
    elif confirmation == "no":
        print("Re-insert the values.")
unprocessed_text_list = input("Insert the list of numbers to decrypt here, separated between commas ',' >>> ")
processed_text = [float(num) for num in unprocessed_text_list.split(',')]
import math
decrypted_values = []
for y in processed_text:
    A = a
    B = b
    C = c - y
    discriminant = B**2 - 4*A*C
    if discriminant < 0:
        print(f"Cannot decrypt value {y}: No real roots.")
        decrypted_values.append(None)
    else:
        sqrt_discriminant = math.sqrt(discriminant)
        x1 = (-B + sqrt_discriminant) / (2 * A)
        x2 = (-B - sqrt_discriminant) / (2 * A)
        # rounding up
        candidates = [round(x1), round(x2)]
        chosen = None
        for val in candidates:
            if 0 <= val <= 127:
                chosen = val
                break
        if chosen is not None:
            decrypted_values.append(chosen)
        else:
            decrypted_values.append(None)
#converting into ASCII, final part of code.
try:
    finaltext = ''.join(chr(number) for number in decrypted_values)
    print("Your decrypted text is:")
    print(finaltext)
except ValueError:
    print("Couldn't decrypt. Possibly a typo? Try again.")
input("Press enter to close this window...")
