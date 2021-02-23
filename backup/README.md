# Un-Cryptogram v0.1

Un-Cryptogram is a small application for decrypting and solving simple character substitution encrypted text,
commonly called a *Cryptogram*.
------------

## Getting Started

In order to try out Cryptogram, simply clone the repo, or download and unzip the package into an empty directory.
Open up a terminal, navigate to the newly created directory, and enter `python cryptogram/window.py`
or on *Windows* `python cryptogram\window.py`.

### Prerequisites

Before you attempt to follow the instructions above you will need to have python installed on your system.
You will also need to install the PyQt5 package from PyPa.  You may also wish to create a virtual enviornment
for this specific project.

```python
Python 3.*
PyQt5~=*
```

### Installing

**Step - by - Step.**

- Clone the repo with git or download and Unzip into an empty directory.
- ensure Python 3.* is installed and functioning properly.
- Open a terminal and navigate to the directory containing the project.
- enter `$ python -m venv venv #<-(or desired name for your virtual python enviornment)`
- activate your virtual enviornment, this is done by invoking a activate.bat script on windows or with the "source" command on unix
- run `python -m pip install --upgrade pip`.
- run `pip install requirements.txt`
- run `python cryptogram/window.py`.
- That's it.

### Example

The following is an example of a simple cryptogram.

Cryptogram = "YNAAX TXWAQ"

The goal is to guess the key used to encrypt the phrase and the unencrypted message.
A key such as a dictonary mapping the encrypted letter to the unencrypted one is a common format for keys.
The solution for the example above uses the following key.

Solution Key = `{"Y" : "H", "N" : "E", "A" : "L", "X" : "O", "T" : "W", "W" : "R", "Q" : "D"}`

Applying the key to the cryptogram gives the message = `"HELLO WORLD"`.

This program's purpose is to take out the guesswork and output the answer or as close to it as possible withing seconds.

Try it out!

### Contributing

For suggestions or feature requests open an issue.  If you would like to help in the development submit a pull request with a description for review.

FYI. This is one of many simple projects that I do in my free time...

See the License file for copyright information.

Happy Coding.

