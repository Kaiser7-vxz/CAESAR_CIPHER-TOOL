import time

BANNER = """
 ▄████▄   ▄▄▄      ▓█████   ██████  ▄▄▄       ██▀███  
▒██▀ ▀█  ▒████▄    ▓█   ▀ ▒██    ▒ ▒████▄    ▓██ ▒ ██▒
▒▓█    ▄ ▒██  ▀█▄  ▒███   ░ ▓██▄   ▒██  ▀█▄  ▓██ ░▄█ ▒
▒▓▓▄ ▄██▒░██▄▄▄▄██ ▒▓█  ▄   ▒   ██▒░██▄▄▄▄██ ▒██▀▀█▄  
▒ ▓███▀ ░ ▓█   ▓██▒░▒████▒▒██████▒▒ ▓█   ▓██▒░██▓ ▒██▒
"""

def caesar_cipher(message, shift, decrypt=False):
    output = ""

    # Ensure that the  shift must be within 0-25
    shift = shift % 26
    if decrypt:
        shift = -shift

    for ch in message:
        if ch.isalpha():
            if ch.isupper():
                start = ord('A')
            else:
                start = ord('a')

            new_char = chr((ord(ch) - start + shift) % 26 + start)
            output += new_char
        else:
            
            output += ch

    return output


def slow_print(text, speed=0.04):
    for c in text:
        print(c, end="", flush=True)
        time.sleep(speed)
    print()


def main():
    print(BANNER)
    slow_print(" Caesar Cipher Tool", 0.03)
    print()

    mode = input("Choose mode (encrypt / decrypt): ").strip().lower()
    if mode not in ("encrypt", "decrypt"):
        print("Invalid mode. Please restart the program.")
        return

    try:
        shift = int(input("Enter shift value: "))
    except ValueError:
        print("Shift must be a number.")
        return

    text = input("Enter text: ")

    print("\nProcessing", end="")
    for i in range(3):
        time.sleep(0.4)
        print(".", end="")
    print("\n")

    result = caesar_cipher(
        text,
        shift,
        decrypt=(mode == "decrypt")
    )

    slow_print("Output:", 0.03)
    slow_print(result, 0.05)


if __name__ == "__main__":
    main()
