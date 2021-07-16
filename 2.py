def acuum(x):
    a = lambda x: [(x[i].upper()+x[i]*i) for i in range(len(x))] 
    return '-'.join(a(x))

print(acuum("abcd"))
