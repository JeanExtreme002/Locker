from collections import deque
from random import randint

# Get all consonants.
consonants = [chr(char) for char in range(ord("A"), ord("Z") + 1) if not chr(char) in "AEIOU"]
consonants += [chr(char) for char in range(ord("a"), ord("z") + 1) if not chr(char) in "aeiou"]

# Get all the characters that can be converted.
original = deque([char + vowel for char in consonants for vowel in "AEIOUaeiou"])
original.extend([chr(char) for char in range(ord("A"), ord("Z") + 1)])
original.extend([chr(char) for char in range(ord("a"), ord("z") + 1)])
original.extend("éúíóáÉÚÍÓÁèùìòàÈÙÌÒÀêûîôâÊÛÎÔÂõãÕÃëÿüïöäËÜÏÖÄ")
original.extend("'1234567890-=´[ç~]\,.;/\"!@#$%¨&*()_+`{Ç^}|<>:?¹²³£¢¬§ªº₢° ")

# Undesirable character codes.
excludes = (
    12439, 12440, 12441, 12544, 12545, 12546, 12547, 12548, 12588, 12589, 12590,
    12591, 12592, 12644, 12687, 12728, 12729, 12730, 12731, 12732, 12733, 12734,
    12735, 12752, 12753, 12754, 12755, 12756, 12757, 12758, 12759, 12760, 12761,
    12762, 12763, 12764, 12765, 12766, 12767, 12768, 12769, 12770, 12771, 12772,
    12773, 12774, 12775, 12776, 12777, 12778, 12779, 12780, 12781, 12782, 12783,
    12829, 12830, 12831, 12868, 12869, 12870, 12871, 12872, 12873, 12874, 12875,
    12876, 12877, 12878, 12879, 12880, 12924, 12925
)

# Get all the characters that will be used to convert the original data.
encoded = deque([chr(code) for code in range(12353, 12353 + len(original) + len(excludes)) if not code in excludes])

def decryptV1(key: int, data: str, from_hex = False) -> str:

    # Get a copy of the objects.
    original_copy = original.copy()
    encoded_copy = encoded.copy()

    # Apply the key, rotating the character list (Caesar Cipher).
    encoded_copy.rotate(key)
    data = data[::-1]

    # Transform the values ​​from hexadecimal to text.
    if from_hex: data = "".join([chr(int("0x" + hexadecimal, 16)) for hexadecimal in data.lower().split("_")])

    # Replace the encrypted characters with the original ones.
    for index in range(len(original_copy)):
        data = data.replace(encoded_copy[index], original_copy[index])

    # Return the original text.
    return data

def encryptV1(key: int, data: str, to_hex = False) -> str:

    # Get a copy of the objects.
    original_copy  = original.copy()
    encoded_copy = encoded.copy()

    # Apply the key, rotating the character list (Caesar Cipher).
    encoded_copy.rotate(key)

    # Replace the original characters with the encrypted ones.
    for index in range(len(original_copy)):
        data = data.replace(original_copy[index], encoded_copy[index])

    # Transform the data to hexadecimal.
    if to_hex: data = "_".join([hex(ord(char))[2:] for char in data]).upper()

    # Return the encrypted data, reversing its order.
    return data[::-1]

def generate_keyV1() -> int:

    # Return a random key.
    return randint(0, len(original))
