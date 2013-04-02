#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

    Copyright 2011 Vince Spicer <vinces1979@gmail.com>

    As long as you retain this notice you can do whatever you want with this stuff.
    If we meet some day, and you think this stuff is worth it, you can buy me a
    beer in return Regina, SK Canada

"""
import re
import string
from random import SystemRandom


def pwgen(length=10, count=5, capitalize=False, numerals=True, symbols=False, allowed_symbols=None, ambiguous=False):
    """Generate a random password.

    @param pw_length: The length of the password to generate [default: 20]
    @param num_pw: The number of passwords to generate [default: 1]
    @param numerals: Enforce at least one number to be in the password [default: False]
    @param capitalize:  Enforce at least one capital letter to be in the password [default: False]
    @param symbols: Enforce at least one symbol to be in the password [default: False]
    @param allowed_symbols: a string containing allowed symbols [default: string.punctuation]
    @param ambiguous: Don't include ambigous characters [default: False ]

    """
    Digits = string.digits
    baseSymbols = string.punctuation
    AmbigousLetters = "B8G6I1l|0OQDS5Z2"
    HasCaps = re.compile(r"[A-Z]")
    HasNumerals = re.compile(r"[0-9]")
    HasAmbiguous = re.compile(r"[%s]" % AmbigousLetters)
    choice = SystemRandom().choice

    letters = string.ascii_lowercase

    if capitalize:
        letters += string.ascii_uppercase
    if numerals:
        letters += Digits
    if symbols:
        if allowed_symbols is not None:
            baseSymbols = allowed_symbols
            HasSymbols = re.compile(r"[%s]" % re.escape(baseSymbols))
        else:
            HasSymbols = re.compile(r"[%s]" % re.escape(baseSymbols))
        letters += baseSymbols
    if not ambiguous:
        letters = re.sub(HasAmbiguous, "", letters)

    passwds = []
    while len(passwds) < int(count):
        passwd = "".join(choice(letters) for x in range(length))
        if capitalize and not HasCaps.search(passwd):
            passwd = replaceRandomChar(choice(string.ascii_lowercase), passwd)
        if numerals and not HasNumerals.search(passwd):
            passwd = replaceRandomChar(choice(Digits), passwd)
        if symbols and not HasSymbols.search(passwd):
            passwd = replaceRandomChar(choice(baseSymbols), passwd)
        if ambiguous and not HasAmbiguous.search(passwd):
            continue
        passwds.append(passwd)

    return len(passwds) == 1 and passwds[0] or passwds


def replaceRandomChar(letter, word, pos=None):
    randint = SystemRandom().randint
    if not pos:
        pos = randint(0, len(word))
    word = list(word)
    word[pos] = letter
    return "".join(word)

