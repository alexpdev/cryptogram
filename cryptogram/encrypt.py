#! /usr/bin/python3
# ~*~ charset: utf8 ~*~

#############################################################################
## Copyright (C) 2020 ASPDEV.
##
## Cryptogram v0.1.1
## All rights reserved.
##
## You may use this file under the terms of the GNU AGPLv3 license:
##
## THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
## "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
## LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
## A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
## OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
## SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
## LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
## DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
## THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
## (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
## OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE."
##
#############################################################################

import random
import string

def encrypt(phrase):
    """ encrypts string with randomly generated character
    substitution cypher. returns encrypted text and key """
    alpha,cv,vc = [i for i in string.ascii_uppercase],{},{}
    txt = ""
    for char in phrase.upper():
        if char in vc:
            txt += vc[char]
        elif char.isalpha():
            if char in alpha:
                alpha.remove(char)
                let = random.choice(alpha)
                alpha.append(char)
            else:
                let = random.choice(alpha)
            alpha.remove(let)
            vc[char] = let
            cv[let] = char
            txt += let
        else:
            txt += char
    return txt,cv

def apply_cypher(phrase,cypher):
    """ encrypts string using given key previously generated
    by gen_cypher function and returns encrypted text """
    encrypted,r = "",reverse_dict(cypher)
    for i in phrase.upper():
        if i.isalpha():
            encrypted += r[i]
        else:
            encrypted += i
    return encrypted

def reverse_dict(dct):
    """ reverses dictionary; e.g. k:v --> v:k """
    reversed = {}
    for k,v in dct.items():
        reversed[v] = k
    return reversed


def gen_cypher():
    """ Creates a random charachter substitution cypher for
    the entire alphabet and returns it as a dictionary """
    alpha = [i for i in string.ascii_uppercase]
    beta, start, dct = alpha[:], 0, dict()
    while start < len(beta):
        val,r = beta[start],False
        if val in alpha:
            alpha.remove(val)
            r = True
        char = random.choice(alpha)
        dct[char] = val
        alpha.remove(char)
        if r:
            alpha.append(val)
            r = False
        start += 1
    return dct
