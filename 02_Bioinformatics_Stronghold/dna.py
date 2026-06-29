def main():
    with open('dna.txt', 'r') as file:
        gene = file.read().strip()
    
    base = {'A': 0, 'C': 0,'G': 0, 'T': 0}

    for b in gene:
        if b in base:
            base[b] += 1
    
    for b in base:
        print(f"{base[b]} ", end="")

main()