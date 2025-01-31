#!/usr/bin/env python3
import argparse

def coding(text, mixing=9, key=9, show_values=False):
    final = ""
    for i in text:
        coding_word = ord(i) + int(mixing)
        coded_word = str(coding_word) + str(key)
        final += chr(int(coded_word))
    if show_values:
        print(f"{final} mixing: {mixing}, key: {key}")
    else:
        print(final)

def decoder_main(text, mixing=9, key=9):
    message = ""
    for i in text:
        decoded = str(ord(i))
        decodedminone = decoded[:-1]
        final = int(decodedminone) - int(mixing)
        message += chr(final)
    print(message)

def search_mix_and_key(text):
    parts = text.split(" mixing: ")
    if len(parts) == 2:
        main_text, mix_key = parts
        mix_key_parts = mix_key.split(", key: ")
        if len(mix_key_parts) == 2:
            mixing, key = mix_key_parts
            decoder_main(main_text, int(mixing), int(key))
    else:
        decoder_main(text, 9, 9)

def main():
    parser = argparse.ArgumentParser(description="AHcoder v2.0 CLI tool")
    parser.add_argument("text", nargs="?", help="Text to encode or decode")
    parser.add_argument("--decrypt", "-d", action="store_true", help="Decrypt the provided text")
    parser.add_argument("--decrypt-values", "-dv", action="store_true", help="Decrypt text with embedded mixing and key values")
    parser.add_argument("--mixing", "-m", type=int, default=9, help="Mixing value (default: 9)")
    parser.add_argument("--key", "-k", type=int, default=9, help="Key value (default: 9)")
    
    args = parser.parse_args()
    
    if args.text:
        if args.decrypt_values:
            search_mix_and_key(args.text)
        elif args.decrypt:
            decoder_main(args.text, args.mixing, args.key)
        else:
            show_values = args.mixing != 9 or args.key != 9
            coding(args.text, args.mixing, args.key, show_values)
    else:
        parser.print_help()
        
if __name__ == "__main__":
    main()
