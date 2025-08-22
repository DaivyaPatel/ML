import json
import os

emoji_dictionary1 = {
    'a': ['🦄','🌟','🍀'], 'b': ['🛸','🔥','💧'], 'c': ['🍄','🌙','⚡'], 'd': ['🕹️','🍎','🎯'], 'e': ['🎃','🍇','🍋'],
    'f': ['🪐','🌈','🥝'], 'g': ['🐉','🌹','🥑'], 'h': ['🦖','🍒','🥥'], 'i': ['🧊','🍉','🥔'], 'j': ['🪓','🍌','🍓'],
    'k': ['🧿','🥭','🥕'], 'l': ['🪁','🌽','🥦'], 'm': ['🦥','🥬','🫐'], 'n': ['🐙','🍍','🛷'], 'o': ['🪲','⚡','💎'],
    'p': ['🛶','🌟','🎃'], 'q': ['🪀','🍎','🍋'], 'r': ['🦚','🌈','🍇'], 's': ['🛡️','🥝','🥑'], 't': ['🪞','🍒','🥥'],
    'u': ['🧸','🍉','🥔'], 'v': ['🪨','🍌','🍓'], 'w': ['🕊️','🥭','🥕'], 'x': ['🪤','🌽','🥦'], 'y': ['🛷','🥬','🫐'], 'z': ['🦩','🍍','🦄'],
    'A': ['🌈','🔥','💎'], 'B': ['🔥','🌟','🍀'], 'C': ['💎','🌙','⚡'], 'D': ['⚡','🍎','🎯'], 'E': ['🍀','🍇','🍋'],
    'F': ['🎯','🌈','🥝'], 'G': ['🍎','🌹','🥑'], 'H': ['🌹','🍒','🥥'], 'I': ['🌙','🍉','🥔'], 'J': ['🍇','🍌','🍓'],
    'K': ['🥝','🥭','🥕'], 'L': ['🥑','🌽','🥦'], 'M': ['🍒','🥬','🫐'], 'N': ['🥥','🍍','🛷'], 'O': ['🍉','⚡','💎'],
    'P': ['🍋','🌟','🎃'], 'Q': ['🥭','🍎','🍋'], 'R': ['🍌','🌈','🍇'], 'S': ['🍓','🥝','🥑'], 'T': ['🥔','🍒','🥥'],
    'U': ['🥕','🍉','🥔'], 'V': ['🌽','🍌','🍓'], 'W': ['🥦','🥭','🥕'], 'X': ['🥬','🌽','🥦'], 'Y': ['🫐','🥬','🛷'], 'Z': ['🍍','🦄','🌈'],
    ' ': ['⬛'], '.': ['⚫'], ',': ['⚪'], '!': ['❗'], '?': ['❓']
}

reverse_map = {}
for c, emj_list in emoji_dictionary1.items():
    for v in emj_list:
        reverse_map[v] = c

def load_custom_mappings(filename="custom_emoji.json"):
    global emoji_dictionary1, reverse_map
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as f:
            custom_map = json.load(f)
        for k, v in custom_map.items():
            if isinstance(v, list):
                emoji_dictionary1[k] = v
            else:
                emoji_dictionary1[k] = [v]
        reverse_map = {}
        for k, v_list in emoji_dictionary1.items():
            for v in v_list:
                reverse_map[v] = k

def save_custom_mappings(filename="custom_emoji.json"):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(emoji_dictionary1, f, ensure_ascii=False)
    print("Mappings saved")

def encrypt(text):
    result = ''
    for idx, char in enumerate(text):
        emojis = emoji_dictionary1.get(char, [char])
        emoji = emojis[idx % len(emojis)]
        result += emoji
    return result

def decrypt(emoji_text):
    result = ''
    for char in emoji_text:
        result += reverse_map.get(char, char)
    return result

def add_custom_mapping():
    global reverse_map
    while True:
        char = input("Enter character to map (or 'exit' to stop): ")
        if char.lower() == 'exit':
            break
        if len(char) != 1:
            print("Please enter a single character.")
            continue
        emojis = input(f"Enter emojis for '{char}': ")
       # emojis = [e.strip() for e in emojis if e.strip()]
        emoji_dictionary1[char] = emojis
        reverse_map = {}
        for k, v_list in emoji_dictionary1.items():
            for v in v_list:
                reverse_map[v] = k
        print(f"Mapping '{char}' -> {emojis} added!")

def encrypt_file(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        text = f.read()
    encrypted_text = encrypt(text)
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(encrypted_text)
    print(f"File encrypted and saved as '{output_file}'")

def decrypt_file(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        text = f.read()
    decrypted_text = decrypt(text)
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(decrypted_text)
    print(f"File decrypted and saved as '{output_file}'")

if __name__ == "__main__":
    load_custom_mappings()
    while True:
        print("\n1. Encrypt Message")
        print("2. Decrypt Message")
        print("3. Add Custom Mapping")
        print("4. Save Custom Mappings")
        print("5. Encrypt File")
        print("6. Decrypt File")
        print("7. Exit")
        choice = input("Choose: ")

        if choice == '1':
            text = input("Enter text: ")
            print("Encrypted:", encrypt(text))
        elif choice == '2':
            emoji_text = input("Enter emoji text: ")
            print("Decrypted:", decrypt(emoji_text))
        elif choice == '3':
            add_custom_mapping()
        elif choice == '4':
            save_custom_mappings()
        elif choice == '5':
            in_file = input("Enter input file path: ")
            out_file = input("Enter output file path: ")
            encrypt_file(in_file, out_file)
        elif choice == '6':
            in_file = input("Enter input file path: ")
            out_file = input("Enter output file path: ")
            decrypt_file(in_file, out_file)
        elif choice == '7':
            break
        else:
            print("Invalid choice")

