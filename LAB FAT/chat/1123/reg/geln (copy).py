def crc(input_str, divisor):
    input_len = len(input_str)
    divisor_len = len(divisor)
    
    # Append n-1 zeros to the input string
    input_str += '0' * (divisor_len - 1)
    
    # Perform binary division
    for i in range(input_len):
        if input_str[i] == '1':
            for j in range(divisor_len):
                input_str[i+j] = '0' if input_str[i+j] == divisor[j] else '1'
    
    # The remainder is the CRC codeword
    crc_codeword = input_str[-(divisor_len - 1):]
    return crc_codeword

# Test the function with the given dataword and divisor
dataword = "101001111"
divisor = "10111"
crc_codeword = crc(dataword, divisor)
print("Dataword: ", dataword)
print("Divisor: ", divisor)
print("CRC Codeword: ", crc_codeword)

-------------------------------------------
def generate_crc(dataword, divisor):
    # Append n-1 zeros to the dataword
    n = len(divisor)
    dividend = dataword + '0' * (n - 1)
    
    # Perform binary division
    while len(dividend) >= n:
        # XOR the divisor with the leftmost n bits of the dividend
        if dividend[0] == '1':
            dividend = ''.join(['1' if dividend[i] != divisor[i] else '0' for i in range(n)]) + dividend[n:]
        else:
            dividend = dividend[1:]
    
    # The remainder is the CRC codeword
    crc = dividend.zfill(n - 1)
    return crc
    
# Test the function with the given dataword and divisor
dataword = '101001111'
divisor = '10111'
crc = generate_crc(dataword, divisor)
print("CRC codeword: ", crc)

# Append the CRC codeword to the dataword to form the transmitted message
transmitted_message = dataword + crc
print("Transmitted message: ", transmitted_message)

