#############################################################################
##
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
##
#############################################################################
import os
import sys

"""
This file contains default configuration values and should not be edited
directly. Updates can be made to the setup.py file in the root directory.
directory. All values read in the root config.py file will overwrite values listed here.
"""
version_ = "0.1.1"

# VARIABLES
PHRASE = None #'QIVQOZ QFXQOT QIKQVZ UKKQVZ QIVQKZ'
KEY = None #{"I":"X"}

# PATHS
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WORDS_PATH = os.path.join(ROOT,"data","words.pickle")
PHRASE_PATH = None #os.path.join(ROOT,"data","phrases.json")

# OPTIONS
VERBOSITY = 1
INTERACTIVE = True
OUTPUT = sys.stdout


# ALL SETTINGS
EXPORT = {
    "BASE_DIR" : ROOT,
    "words_file" : WORDS_PATH,
    "key" : KEY,
    "phrase" : PHRASE,
    "phrase_path" : PHRASE_PATH,
    "verbosity" : VERBOSITY,
    "output" : OUTPUT,
}
