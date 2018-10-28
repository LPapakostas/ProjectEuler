def remove_same(nom,den):
    if ( (nom%10)/(den%10) == nom/den):
        return 1,1
    n_str,d_str = str(nom),str(den)
    if (n_str[0] != d_str[0]):
        d_str = d_str[::-1]
    if(n_str[0] != d_str[0]) and (n_str[1] != d_str[1]) :
        return 1,1
    else:
        if(n_str[0] == d_str[0]):
            n,d = int(n_str)%10 , int(d_str)%10
        else:
            n,d = int(int(n_str)/10) , int(int(d_str)/10)
        return n,d
    
non_trivial =[]
for nom in range(10,100):
    for den in range(10,100):
        if (nom < den) and (nom%10 != 0) and (den%10 != 0):
            r1 = float(nom/den)
            n,d = remove_same(nom,den)
            r2 = float(n/d)
            if (r1 == r2):
                non_trivial.append((nom,den))
nom_product,den_product = 1,1
for i in range(len(non_trivial)):
    nom_product*=(non_trivial[i])[0]
    den_product*=(non_trivial[i])[1]
print(den_product/nom_product)