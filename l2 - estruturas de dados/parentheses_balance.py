def is_correct_sequence(s):
    stack = []
    matching_bracket = {')': '(', ']': '['}

    for char in s:
        if char in '([':
            # Push opening brackets onto the stack
            stack.append(char)
        elif char in ')]':
            # Check for closing brackets
            if stack and stack[-1] == matching_bracket[char]:
                stack.pop()
            else:
                return "No"

    # If the stack is empty, all brackets are matched
    return "Yes" if not stack else "No"


def main():
    n = int(input().strip())

    results = []
    for _ in range(n):
        string = input().strip()
        result = is_correct_sequence(string)
        results.append(result)

    for result in results:
        print(result)


if __name__ == "__main__":
    main()
