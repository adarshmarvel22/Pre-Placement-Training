def compress(chars):
    readPtr = writePtr = 0
    count = 1

    for i in range(1, len(chars)):
        if chars[i] == chars[i-1]:
            count += 1
        if chars[i] != chars[i-1] or i == len(chars) - 1:
            chars[writePtr] = chars[readPtr]
            writePtr += 1
            if count > 1:
                digits = str(count)
                for digit in digits:
                    chars[writePtr] = digit
                    writePtr += 1
            count = 1
            readPtr = i

    return writePtr
chars = ["a", "a", "b", "b", "c", "c", "c"]
result = compress(chars)
print(result)  # Output: 6
print(chars[:result])  # Output: ["a", "2", "b", "2", "c", "3"]
