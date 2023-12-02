# importing the module
import base64

# assign the string from challenge
string = "==gC9FSI5tGMwA3cfRjd0o2Xz0GNjNjYfR3c1p2Xn5WMyBXNfRjd0o2eCRFS"

# assign variable and reverse it with a slice method then print
print("This is the string reversed:\n") 
convert_string = print(string[::-1])
print("\n")
convert_string = "SFRCe2o0djRfNXByMW5nX2p1c3RfYjNjNG0zX2o0djRfc3AwMGt5ISF9Cg=="

# converting the base64 code into ascii characters as each character in B64 is 6 bits
convert_bytes = convert_string.encode("ascii")

# converting into bytes from base64 system
converted_bytes = base64.b64decode(convert_bytes)

# decoding the ASCII characters into alphabets
decoded_sample = converted_bytes.decode("ascii")

# displaying the result
print(f"The string after decoding is: {decoded_sample}") 
