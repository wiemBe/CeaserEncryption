def encryptToCaesar(text, shift):
    encodedText = ""
    shift = int(shift)  # Convert shift to integer
    for char in text:
        if char.isalpha():
            shiftBase = ord("A") if char.isupper() else ord("a")
            encodedText += chr((ord(char) - shiftBase + shift) % 26 + shiftBase)
        else:
            encodedText += char
    return encodedText

def decryptFromCaesar(text):
    possible_decodings = []
    for shift in range(26):
        decodedText = ""
        for char in text:
            if char.isalpha():
                shiftBase = ord("A") if char.isupper() else ord("a")
                decodedText += chr((ord(char) - shiftBase - shift) % 26 + shiftBase)
            else:
                decodedText += char
        possible_decodings.append(decodedText)
    return possible_decodings

if __name__ == "__main__":
    keyboardInput = "R"

    while keyboardInput.upper() == "R":
        keyboardInput = input("decrypt or encrypt (d/e): ")

        if keyboardInput.upper() == "E":
            plainText = input("what's the text you wanna encrypt with Caesar cipher: ")
            shift = input("how many times you wanna shift: ")
            print(encryptToCaesar(plainText, shift))

        elif keyboardInput.upper() == "D":
            decryptedText = input("What is the text you wanna decrypt: ")
            print("Brute forcing..")
            possible_decodings = decryptFromCaesar(decryptedText)
            for decoding in possible_decodings:
                print(decoding)
            print("One of them is correct.")

        else:
            raise ValueError("unexpected input")

        keyboardInput = input("R/Q for program: ")
