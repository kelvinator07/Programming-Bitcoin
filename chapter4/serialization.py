from chapter3.secp256k1 import Signature
from chapter3.keys import PrivateKey
from chapter3.helper import encode_base58, hash256, little_endian_to_int, int_to_little_endian

# SEC For Public Keys = Standards for Efficient Cryptography
# Uncompressed SEC format
# 0x04 + x (32bytes) + y (32bytes) = (65 bytes Total)

# Compressed SEC format
# if y is even 02 otherwise 03 + x (32bytes) = (33 bytes Total)

print("Exercise 1")
# Find the uncompressed SEC format for the public key where the private key secrets are:
# * 5,000
# * 2,018^5^
# * 0xdeadbeef12345

priv = PrivateKey(5000)
print(priv.point.sec(compressed=False).hex())

priv = PrivateKey(2018**5)
print(priv.point.sec(compressed=False).hex())

priv = PrivateKey(0xdeadbeef12345)
print(priv.point.sec(compressed=False).hex())

print("\nExercise 2")
# Find the compressed SEC format for the public key where the private key secrets are:

# * 5,001
# * 2,019^5^
# * 0xdeadbeef54321
priv = PrivateKey(5001)
print(priv.point.sec().hex())

priv = PrivateKey(2019**5)
print(priv.point.sec().hex())

priv = PrivateKey(0xdeadbeef54321)
print(priv.point.sec().hex())


# DER Signatures = Distinguished Encoding Rules (DER) format.
# DER format was used by Satoshi to serialize ECDSA signatures. r and s
print("\nExercise 3")
# Find the DER format for a signature whose `r` and `s` values are:
r = 0x37206a0610995c58074999cb9767b87af4c4978db68c06e8e6e81d282047a7c6
s = 0x8ca63759c1157ebeaec0d03cecca119fc9a75bf8e6d0fa65c841c8e2738cdaec
sig = Signature(r, s)
print(sig.der().hex())

# Base58
# readability, compression, and security
# Why Base58 Is on the Way Out = What’s much better is the new Bech32 standard, which is defined in BIP0173. (Segwit)
print("\nExercise 4")
# Convert the following hex values to binary and then to Base58:
# * `7c076ff316692a3d7eb3c3bb0f8b1488cf72e1afcd929e29307032997a838a3d`
# * `eff69ef2b1bd93a66ed5219add4fb51e11a840f404876325a1e8ffe0529a2c`
# * `c7207fee197d27c618aea621406f6bf5ef6fca38681d82b2f06fddbdce6feab6`

h = '7c076ff316692a3d7eb3c3bb0f8b1488cf72e1afcd929e29307032997a838a3d'
print(encode_base58(bytes.fromhex(h)))

h = 'eff69ef2b1bd93a66ed5219add4fb51e11a840f404876325a1e8ffe0529a2c'
print(encode_base58(bytes.fromhex(h)))

h = 'c7207fee197d27c618aea621406f6bf5ef6fca38681d82b2f06fddbdce6feab6'
print(encode_base58(bytes.fromhex(h)))


# Address Format
# For mainnet addresses, start with the prefix 0x00, for testnet 0x6f.
print("\nExercise 5")
# Find the addresses corresponding to the public keys whose private key secrets are:
# * 5002 (use uncompressed SEC on testnet)
# * 2020^5^ (use compressed SEC on testnet)
# * 0x12345deadbeef (use compressed SEC on mainnet)
priv = PrivateKey(5002)
print(priv.point.address(compressed=False, testnet=True))

priv = PrivateKey(2020**5)
print(priv.point.address(testnet=True))

priv = PrivateKey(0x12345deadbeef)
print(priv.point.address())

# WIF Format = Wallet Import Format
# WIF is a serialization of the private key that’s meant to be human-readable. WIF uses Base58
# For mainnet private keys, start with the prefix 0x80, for testnet 0xef.
print("\nExercise 6")
# Find the WIF for the private key whose secrets are:
# * 5003 (compressed, testnet)
# * 2021^5^ (uncompressed, testnet)
# * 0x54321deadbeef (compressed, mainnet)
priv = PrivateKey(5003)
print(priv.wif(testnet=True))

priv = PrivateKey(2021**5)
print(priv.wif(compressed=False, testnet=True))

priv = PrivateKey(0x54321deadbeef)
print(priv.wif())

# Big- and Little-Endian Redux
print("\nExercise 7")
h = bytes.fromhex('99c3980000000000')
print(little_endian_to_int(h))

print("\nExercise 8")
n = 1
print(int_to_little_endian(n, 4))

print("\nExercise 9")
passphrase = b'kelvin@programmingblockchain.com my secret'
secret = little_endian_to_int(hash256(passphrase))
priv = PrivateKey(secret)
print(priv.point.address(testnet=True))
