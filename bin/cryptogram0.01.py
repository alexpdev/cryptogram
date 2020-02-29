import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

import sys
sys.path.append(BASE_DIR)

from cryptogram.decrypt import main
from cryptogram.cnf import SETTINGS

while True:
    conf = next(SETTINGS)
    main(**conf)
    break
