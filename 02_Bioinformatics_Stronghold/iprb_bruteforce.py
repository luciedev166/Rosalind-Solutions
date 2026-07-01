def main(): #This is brute force. I myself am shocked it works. This is my first try. Will probably redo.
    k_l = 24 #AA
    m_l = 16 #Aa
    n_l = 28 #_aa
    
    k = "AA"
    m = "Aa"
    n = "aa"
    
    count = 0
    recessive = 0
    
    l = count_pairs(k, m, n, k_l,m_l,n_l)
    count += l[0]
    recessive += l[1]
    
    l = count_pairs(m, k, n,m_l,k_l,n_l)
    count += l[0]
    recessive += l[1]
    
    l =count_pairs(n, k, m,n_l,k_l,m_l)
    count += l[0]
    recessive += l[1]
    
    # print(count)
    # print(recessive)
    print(1 - (recessive / count))
    

def count_pairs(k, m, n,k_l, m_l, n_l):#k is lead, m and n are followers 
    c = 0
    r = 0
    for x in range(k_l):
        for i in range(2):
            p = ""
            for _ in range(m_l):
                for j in range(2):
                    p = k[i] + m[j]
                    if(p == "aa"):
                        r+=1
                    c+=1
                    
            for _ in range(n_l):
                for j in range(2):
                    p = k[i] + n[j]
                    if(p == "aa"):
                        r+=1
                    c+=1
                    
            for _ in range(k_l - 1):
                for j in range(2):
                    p = k[i] + k[j]
                    if(p == "aa"):
                        r+=1
                    c+=1
    return [c, r]
main()