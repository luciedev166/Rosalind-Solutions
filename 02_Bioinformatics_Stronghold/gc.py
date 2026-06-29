def main():
    with open("gc.txt", "r") as file:
        fasta = [line.strip() for line in file.readlines()]
    
    id = {}
    for line in fasta:
        if line.startswith('>'):
            id[line[1:].strip()] = ["", 0]
            key = line[1:].strip() 
        else:
            id[key][0] = id[key][0] + line

    for i in id:
        id[i][1] =((id[i][0].count('C') + id[i][0].count('G')) / len(id[i][0])) * 100

    high = max(id, key=lambda i: id[i][1])
    print(high)
    print(id[high][1])

main()