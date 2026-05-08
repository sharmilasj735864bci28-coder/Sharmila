n = int(input())
numbers = list(map(int, input().split()))
result = tuple(x**2 if x % 2 == 0 else x**3 for x in numbers)
print(result)




text = input("Enter a string: ")
words = text.split()
longest_word = max(words, key=len)
print(longest_word)


def compress_string(s):
    if not s:
        return ""

    compressed = []
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            count += 1
        else:
            compressed.append(s[i-1] + str(count))
            count = 1
            compressed.append(s[-1] + str(count))
            return "".join(compressed)
        input_str = input("Enter a string: ")
        print(compress_string(input_str))

