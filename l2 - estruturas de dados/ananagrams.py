import sys
from collections import defaultdict


def main():
    canonical_map = defaultdict(list)

    # Read input lines
    for line in sys.stdin:
        line = line.strip()
        if line == '#':
            break
        words = line.split()
        for word in words:
            canonical_form = ''.join(sorted(word.lower()))
            canonical_map[canonical_form].append(word)
  
    # List to store ananagrams
    ananagrams = []

    # Determine which words are ananagrams
    for word_list in canonical_map.values():
        if len(word_list) == 1:
            ananagrams.append(word_list[0])

    # Sort the ananagrams lexicographically
    ananagrams.sort()

    for ananagram in ananagrams:
        print(ananagram)


if __name__ == "__main__":
    main()
