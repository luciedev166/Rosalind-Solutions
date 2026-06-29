def main():
    with open("revc.txt", "r") as file:
        seq = file.read().strip()
    
    base = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    comp = ""

    for b in seq:
        comp = comp + base[b]
    
    rev_comp = comp[::-1]

    print(rev_comp)

main()