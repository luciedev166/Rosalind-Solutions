def main():

    with open("rosalind_ini6.txt", "r") as file:
        s = file.read().strip().split()
    words = {}

    for w in s:
        if not w in words:
            words[w] = 1
        else:
            words[w] += 1
    
    for k in words:
        print(f"{k} {words[k]}")
main()