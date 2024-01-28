import os
import sys
import chardet


### A map between 3-char amino-acid expressions and 1-char amino-acid expressions.
mapper_31 = {
    "Arg" : 'R',    "His" : 'H',
    "Lys" : 'K',    "Asp" : 'D',
    "Glu" : 'E',

    'Ser' : 'S',    "Thr" : 'T',
    'Asn' : 'N',    'Gln' : 'Q',

    'Cys' : 'C',    'Sec' : 'U',
    "Gly" : 'G',    'Pro' : 'P',
    
    "Ala" : 'A',    "Val" : 'V',
    "Ile" : 'I',    "Leu" : 'L',
    "Met" : 'M',    "Phe" : 'F',
    "Tyr" : 'Y',    "Trp" : 'W',
}
mapper_13 = {v: k for k, v in mapper_31.items()}


def translate_3_to_1(amino_text):
    """Tranlate 3-char amino-acid expression text into 1-char one."""
    aminos = amino_text.split()
    aminos = [mapper_31.get(amino, amino) for amino in aminos if not amino.startswith('<') and amino.endswith('>')]
    return "".join(aminos)


def translate_1_to_3(amino_text):
    """Tranlate 1-char amino-acid expression text into 3-char one."""
    aminos = [mapper_13.get(amino, amino) for amino in amino_text if not amino.startswith('<') and amino.endswith('>')]
    return " ".join(aminos)


def read_file(filepath):
    """Read an amino-acid sequence file as text."""
    with open(filepath, mode='rb') as fr:
        rawdata = fr.read()
    result = chardet.detect(rawdata)
    encoding = result['encoding']
    with open(filepath, mode='r', encoding=encoding) as fr:
        text = fr.read()
    return text


def write_file(filepath, text, encoding='utf8'):
    """Write text on an amino-acid sequence file."""
    with open(filepath, encoding=encoding, mode='w') as fw:
        fw.write(text)
    return 


if __name__ == '__main__':
    filenames = sys.argv[1:]

    if filenames and filenames[0] in ('-h', '--help'):
        print("< Example Code >")
        print("python amino_translator.py seq1.txt seq2.txt ...")
        exit()

    if not filenames:
        filenames = [each for each in os.listdir() if each.endswith('.txt') and not each.endswith('_trsld.txt')]
        if not filenames:
            print("<Error-Notice> :: No target files in the current directory.")
            exit()
    
    for filename in filenames:
        if not filename.endswith('.txt'): continue
        if filename.endswith('_trsld.txt'): continue
        text = read_file(filename)
        text = translate_3_to_1(text)
        new_filename = f"{filename.split('.')[0]}_trsld.{filename.split('.')[1]}"
        write_file(new_filename, text)
        print(f"<Process-Notice> :: The file '{filename}' has been tranlated into 1-char amino-acid sequence.")
        print(f"\t\t    New file '{new_filename}' has been created.")


'''
if __name__ == '__main__':
    amino3 = "Met Val Asn Leu Glu Pro Met His Thr Glu Ile"
    amino1 = convert_31(amino3)
    amino13 = convert_13(amino1)
    print(amino3)
    print(amino1)
    print(amino13)
    assert amino13 == amino3
'''
