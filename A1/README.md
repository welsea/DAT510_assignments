# DAT510 Assignment 1
## Required package
- flask </br>
For task 4 of part 2.
```python
pip install Flask
```
## The directory
### Part 1
- `task1.py`: Execution file for task 1.
- `decipher.py`: Contains the main decryption function. 
- `english_quadgrams.txt`: Contains the quadgrams and the count number of them in War and Peace.
- `quadgram.py`: Contains the function that generate a set consists by quadgram.
- `task1_ct.txt`: The ciphertext of task 1.
- `task2.py`: Execution file for task 2.
- `task3.py` : Execution file for task 3.
- `task3_ct.txt`: The ciphertext of task 3.
- `kasiski.py`: Contains the main funtion of Kasiski method.

### Part 2
- `task1.py`: Execution file for task 1.
- `fk.py`: Contains the <i>fk</i> function of S-DES.
- `permutaion.py`: Contains the <i>permutaion</i> function of S-DES.
- `SDES.py`: Contains the encrypt and decrypt procedures of S-DES.
- `tripleSDES.py`: Contains the encrypt and decrypt procedures of triple S-DES.
- `task2.py`: Execution file for task 2.
- `task3.py` : Execution file for task 3.
- `task4.py` : Execution file for task 4.
- `ctx1.txt` & `ctx2.txt`: Ciphertext of task 3. 

## Run the program
Use `python task*.py` to run each file.(replace * with task number.) </br>
For task 4 in part 2, use <b>http://127.0.0.1:5000/?cipher=0101110101010111110111001101110001010100</b> to test the program.