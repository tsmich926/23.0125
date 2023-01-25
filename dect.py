def dec_to_bin(n):
    if n==1:
        return '1'
    res = dec_to_bin(n//2) + str(n%2)
    return res

print(dec_to_bin(55))
