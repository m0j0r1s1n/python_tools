# python_tools

___


Along the way I stumble across so many pre-written python tools. From tools
that create a password to tools that will crack a password.  I never study 
and copy and delve into the coding of them to re-inforce my own knowledege 
of Python.  

See, I know lots of Python but I never have the chance to keep using and doing
the "rinse and repeat" method I did in previous occupations so I think it
is about time I put all the little (I mean that) fragments off knowledege together.

I was doing a very easy challenge on HTB just recently and it got to the flag.
The flag happened to be a string of Base64 but reversed so I stuffed into an
online tool and got the challenge complete. I knew when I was doing this I could 
produce a tool in Python to do this so went back and with the help if Google
crested a tool that worked.

### <samp>The Base64 Encoded Reverse String Converter.</samp>

```python
# importing the module
import base64

# assign the string from challenge
string = "==gC9FSI5tGMwA3cfRjd0o2Xz0GNjNjYfR3c1p2Xn5WMyBXNfRjd0o2eCRFS"

# assign variable and reverse it with a slice method then print
print("This is the string reversed:\n") 
# this is when the string gets reversed 
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
print(f"Here is the flag: {decoded_sample}")
# Here is the flag: HTB{j4v4_5pr1ng_just_b3c4m3_j4v4_sp00ky!!}  
```

It worked (: so if you stumble upon this you can tweak to suit or so can I.
