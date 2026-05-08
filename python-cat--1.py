def compress_string(text):
    if not text:
        return ""

    compressed = []
    count = 1

   
    for i in range(1, len(text)):
        if text[i] == text[i - 1]:
            count += 1
        else:
            
            compressed.append(text[i - 1] + str(count))
            count = 1
    
    
    compressed.append(text[-1] + str(count))

    return "".join(compressed)


input_str = "aaabbccccd"
print(f"Original: {input_str}")
print(f"Compressed: {compress_string(input_str)}")



