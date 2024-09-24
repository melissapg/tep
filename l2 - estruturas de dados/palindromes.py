def is_palindrome(s):
    return s == s[::-1]


def is_mirrored(s, mirror_map):
    mirrored = ''.join(mirror_map.get(c, '') for c in s[::-1])
    return mirrored == s


def main():
    mirror_map = {
        'A': 'A', 'B': '', 'C': '', 'D': '', 'E': '3', 'F': '', 'G': '', 'H': 'H', 'I': 'I',
        'J': 'L', 'K': '', 'L': 'J', 'M': 'M', 'N': '', 'O': 'O', 'P': '', 'Q': '', 'R': '',
        'S': '2', 'T': 'T', 'U': 'U', 'V': 'V', 'W': 'W', 'X': 'X', 'Y': 'Y', 'Z': '5', '0': '',
        '1': '1', '2': 'S', '3': 'E', '4': '', '5': 'Z', '6': '', '7': '', '8': '8', '9': 'W'
    }

    while True:
        try:
            line = input().strip()
            if not line:
                continue

            is_pal = is_palindrome(line)
            is_mrrd = is_mirrored(line, mirror_map)

            if is_pal and is_mrrd:
                result = f"{line} -- is a mirrored palindrome."
            elif is_pal:
                result = f"{line} -- is a regular palindrome."
            elif is_mrrd:
                result = f"{line} -- is a mirrored string."
            else:
                result = f"{line} -- is not a palindrome."

            print(result)
            print()  # Print an empty line after each result

        except EOFError:
            break

if __name__ == "__main__":
    main()
