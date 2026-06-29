def main():
    n = 35
    k = 4
    adults = 0
    babies = 1

    for _ in range(n - 1):
        next_adoles = adults + babies #adults next month, current adults are already adolescents so they count ..
        next_babies = adults * k #babies next month, made by official adults

        adults = next_adoles #adolescents become adults
        babies = next_babies
    
    print(adults + babies)

main()