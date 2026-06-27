def main():
    with open("ini_5_input.txt", "r") as file, open("ini_5_output.txt", "w") as output:
        lines = file.readlines()

        for line in range(len(lines)):
            if (line + 1) % 2 == 0:
                output.writelines(lines[line])

main()