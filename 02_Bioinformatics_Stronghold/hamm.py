def main():
    # p = "GAGCCTACTAACGGGAT"
    # q = "CATCGTAATGACGGCCT"

    with open("hamm_1.txt", "r") as file:
        p = file.read().strip()

    with open("hamm_2.txt", "r") as file:
        q = file.read().strip()

    print(HammingDistance(p, q))

def HammingDistance(p, q):
    count = 0

    for i in range(len(p)):
        if p[i] != q[i]:
            count += 1
    return count
main()