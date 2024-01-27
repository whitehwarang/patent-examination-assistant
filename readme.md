
# Amino Translator
Amino Translator is a small python program for converting 3-char amino-acid sequence into 1-char amino-acid sequence.


# When To Use
When examining a patent application with amino-acid sequence, 3-char amino-acid sequence need to be compared to 1-char amino-acid sequence. However, it is very cumbersome because the sequences are generally too long to compare. In order to make it easier, I made a small program that helps to translate 3-char amino-acid sequence into 1-char amino-acid sequence.


# How To Use
1. Use with python.

    1) pre-requirement
        - python interpreter
        - chardet package 
        ```bash
        pip install chardet
        ```

    2) how to use
        ```bash
        python amino-translator.py seq1.txt seq2.txt ...
        ```
    
    3) result
        - seq1_trsld.txt, seq2_trsld.txt, ...

2. Use as executable file(exe file).
    1) pre-requirement
        - prepare both executable file(amino_translator.exe) and amino-sequence files to be translated(seq1.txt, seq2.txt, ...).
        - the executable file has already been made through 'pyinstaller' package and is provided with python-code.

    2) how to use
        - put the amino-sequence files into the same directory where the executable file is.
        - execute the executable file.
        - then, it will translate and create new tranlated files.
    
    3) result
        - eq1_trsld.txt, seq2_trsld.txt, ...