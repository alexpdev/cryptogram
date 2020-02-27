# Cryptogram

**Program for solving cryptograms.**
Cryptograms are encrypted text. Solving them requires discovering encryption key and unencrypting.
For example: we are given the encrypted text, and part of the key might be provided.

`phrase = 'QIVQOZ QFXQOT QIKQVZ UKKQVZ QIVQKZ'`
`key = { 'I' : 'X' }`

> the code will print possible matches to stdout for,
> and you will be given the option to end if it comes across a good match.
`phrase = "EXPERT ELDERS EXCEPT ACCEPT EXPECT"`
`key = {'Q': 'E', 'I': 'X', 'F': 'L', 'U': 'A', 'V': 'P', 'O': 'R', 'X': 'D', 'T': 'S', 'Z': 'T', 'K': 'C'}`
---

## Instructions

- Open *config.py*
- Put cryptogram text in the *phrase* field
- (optional) put known `key : value` pairs in the *key* field
- run **decrypt.py**
