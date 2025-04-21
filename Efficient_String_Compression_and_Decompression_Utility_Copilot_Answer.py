compress_input = "aaabbbcccaaa"
decompress_input = "a3b3c3a3"

def compress_string(s: str) -> str:
    """Compress a string using the counts of repeated characters."""
    if not s:
        return ""

    compressed = []
    count = 1

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            compressed.append(s[i - 1] + str(count))
            count = 1

    compressed.append(s[-1] + str(count))  # Append the last character and its count
    return ''.join(compressed)

def decompress_string(s: str) -> str:
    """Decompress a string using the counts of repeated characters."""
    decompressed = []
    i = 0

    while i < len(s):
        char = s[i]
        i += 1
        count_str = ''
        
        while i < len(s) and s[i].isdigit():
            count_str += s[i]
            i += 1
        
        decompressed.append(char * int(count_str))

    return ''.join(decompressed)

print("Compressed:", compress_string(compress_input))  # Output: a3b3c3a3
print("Decompressed:", decompress_string(decompress_input))  # Output: aaabbbcccaaa
# Output: a3b3c3a3  # Output: aaabbbcccaaa
# This code provides a utility for compressing and decompressing strings using character counts.