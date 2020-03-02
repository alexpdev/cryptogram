# ~*~ charset: utf8 ~*~
# Cryptogram: version 0.1.1
try:
    from . import (config,
                    decrypt,
                    encrypt,
                    init,
                    manager,
                    phraseMap,
                    GUI)
except:
    import config,decrypt,encrypt,init,manager,phraseMap,GUI
