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

__version__ = "0.1.1"

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from cryptogram.init import SETTINGS
from cryptogram.manager import UpdateKey,Solved,EndDecrypt
from cryptogram.GUI.CryptoUI import GraphicalManager

def start(conf):
    try:
        man = GraphicalManager(**conf)
        man.mainloop()
    except UpdateKey:
        return start(conf)
    except Solved:
        return
    except EndDecrypt:
        return

for conf in SETTINGS:
    start(conf)

print("Goodbye")
