def main():
    with open("rna.txt", "r") as file:
        seq = file.read().strip()
    
    rna = ""

    for b in seq:
        if b == 'T':
            rna = rna + 'U'
        else:
            rna = rna + b

    print(rna)

main()