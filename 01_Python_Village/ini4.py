def main():
    a = 4437
    b = 9194

    count = 0    
    for i in range(a, b + 1):
        if i % 2 != 0:
            count += i

    print(count)
main()