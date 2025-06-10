def most_frequent_char(s):
    freq = {}
    max_char = ''
    max_count = 0

    for char in s:
        if char != ' ':  # ignore spaces
            freq[char] = freq.get(char, 0) + 1
            if freq[char] > max_count:
                max_count = freq[char]
                max_char = char

    return max_char, max_count

input_str = 'mississippi'
char, count = most_frequent_char(input_str)
print(f"Most frequent character: '{char}' (occurs {count} times)")