################################################################################
## Copyright (C) 2020 ASPDEV.
##
## Cryptogram v0.1.1
## All rights reserved.
##
##
## You may use this file under the terms of the GNU AGPLv3 license as follows:
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
################################################################################
import os
import sys
##
version = "0.1.1"
##
## Only uncomment the items you want to customize...
################################################################################
## Verbosity describes the level of output to logfiles or stdout (0-3)
# VERBOSITY = 1
################################################################################
## If a portion of the encryption key is known, you can enter it here as
## {Key:Value} pairs, where key is the current encrypted character and value is
## decrypted character
KEY = {"Q":"V"}  #{"I":"X"}
################################################################################
## A phrase can be a string of any size. non alphanumeric characters are
## are filtered out for you and re-inserted in the final output
PHRASE =  "ICJ BTHVFJL ZNIC BJHBFJ ZCH CWQJ PH QNOJG NG ICWI AJPJTWFFU UHD OWP VJ BTJIIU GDTJ ICJU'TJ AHNPA ID CWQJ GHLJ BTJIIU WPPHUNPA QNTIDJG. - JFNEWVJIC IWUFHT" #'QIVQOZ QFXQOT QIKQVZ UKKQVZ QIVQKZ'
################################################################################
## The phrase path should be an absolute path to a json file containing
## containing multiple phrases for decryption. this value is ignored if
## the phrase field evaluates to True. The json file format is:
## { phrase1 : key1 , phrase2 : key2 }.  keys can be empty {}
# PHRASE_PATH = None
################################################################################
## The BASE_DIR is the toplevel directory for cryptogram program. Only edit if
## using non default application directory structure.
# BASE_DIR = None
################################################################################
## The default words_file is in the data directory, and contains a list of
## English words used for decryption. Only edit if providing a custom list.
# WORDS_PATH = None
################################################################################
## Output specifies where logging data and results are printed to.
# OUTPUT = sys.stdout
################################################################################
