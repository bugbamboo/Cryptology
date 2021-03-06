# COURSERA - Cryptography I - Stanford University 
# https://www.coursera.org/learn/crypto
# Week 2 - Programming assingment (implemented in Python 3 using PyCrypto)
# In this project you will implement two encryption/decryption systems, one using AES in CBC mode and another using AES in counter mode (CTR). In both cases the 16-byte encryption IV is chosen at random and is prepended to the ciphertext.
# For CBC encryption we use the PKCS5 padding scheme discussed in the lecture (14:04). While we ask that you implement both encryption and decryption, we will only test the decryption function. In the following questions you are given an AES key and a ciphertext (both are hex encoded ) and your goal is to recover the plaintext and enter it in the input boxes provided below.
# For an implementation of AES you may use an existing crypto library such as PyCrypto (Python), Crypto++ (C++), or any other. While it is fine to use the built-in AES functions, we ask that as a learning experience you implement CBC and CTR modes yourself.

import sys
import base64
import hashlib
import re
import binascii
import numpy
from operator import methodcaller
from Crypto.Cipher import AES
from Crypto.Util import Counter
from Crypto import Random


key = bytes.fromhex("140b41b22a29beb4061bda66b6747e14")
enc = bytes.fromhex('4ca00ff4c898d61e1edbf1800618fb2828a226d160dad07883d04e008a7897ee2e4b7465d5290d0c0e6c6822236e1daafb94ffe0c5da05d9476be028ad7c1d81')
iv = enc[:16]
ct1 = enc[16:]
obj = AES.new(key,AES.MODE_CBC,iv)
paddedStr = obj.decrypt(ct1)
paddingAmount = ord(paddedStr[len(paddedStr)-1:])
print (paddedStr)
print (paddedStr[:-paddingAmount])
