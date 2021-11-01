# DAT510 Assignment 2
## Required package
- pycryptodome </br>
For part 1.
- flask </br>
For  part 2.
- requests </br>
For  part 2.
```zsh
pip install Flask requests pycryptodome
```
## The directory
- `task1.py`: Execution file for part 1.
- `ec.py`: code for Elliptic curve.
- `ecdh.py`: code for Elliptic Curve Diffie-Hellman Key Exchange.
- `CSPRNG.py`: code for RC4.
- `DES.py`: code for DES.
- `task2Alice`: Execution file for part 2, as Alice.
- `task2Bob`: Execution file for part 2, as Bob.


## Run the program
### part 1
run `task1.py` 
### part 2
run `task2Alice.py` and `task2Bob.py` at the same time. </br>
open `http://127.0.0.1:80/` and `http://127.0.0.1:5000` in the webserver