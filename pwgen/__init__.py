#!/usr/bin/env python
"""

    Copyright 2011 Vince Spicer <vinces1979@gmail.com>

    As long as you retain this notice you can do whatever you want with this stuff.
    If we meet some day, and you think this stuff is worth it, you can buy me a
    beer in return Regina, SK Canada

"""

from random import choice, randint
import string
import re

LowercaseLetters = string.lowercase
UpperCase = string.uppercase
Digits = string.digits
Symbols = string.punctuation

HasCaps = re.compile("[A-Z]")
HasNumerals = re.compile("[0-9]")
HasSymbols = re.compile(r"[%s]" % re.escape(Symbols))

def replaceRandomChar(letter, word, pos=None):
    if not pos:
        pos = randint(0, len(word))
    word = list(word)
    word[pos] = letter
    return "".join(word)

def pwgen(pw_length=20, num_pw=1, no_numerals=False, no_capitalize=False, capitalize=False,
                         numerals=False, no_symbols=False, symbols=False, allowed_symbols=None):
    """Generate a random password.

    @param pw_length: The length of the password to generate [default: 20]
    @param num_pw: The number of passwords to generate [default: 1]
    @param no_numerals:  Don't include numbers in the passwords [default: False]
    @param numerals: Enforce at least one number to be in the password [default: False]
    @param no_capitalize: Don't include capital letters in the password [default: False]
    @param capitalize:  Enforce at least one capital letter to be in the password [default: False]
    @param no_symbols: Don't include symbols in the password [default: False]
    @param symbols: Enforce at least one symbol to be in the password [default: False]
    @param allowed_symbols: a string containing allowed symbols [default: string.punctuation]

    """

    global Symbols, HasSymbols
    letters = LowercaseLetters
    if not no_capitalize:
        letters += UpperCase
    if not no_numerals:
        letters += Digits
    if not no_symbols:
        if allowed_symbols is not None:
            Symbols = allowed_symbols
            HasSymbols = re.compile(r"[%s]" % re.escape(Symbols))
        letters += Symbols

    passwds = []
    while len(passwds) < int(num_pw):
        passwd = "".join(choice(letters) for x in range(pw_length))
        if capitalize and not HasCaps.search(passwd):
            passwd = replaceRandomChar(choice(UpperCase), passwd)
        if numerals and not HasNumerals.search(passwd):
            passwd = replaceRandomChar(choice(Digits), passwd)
        if symbols and not HasSymbols.search(passwd):
            passwd = replaceRandomChar(choice(Symbols), passwd)
        passwds.append(passwd)

    if len(passwds) == 1:
        return passwds[0]

    return passwds
