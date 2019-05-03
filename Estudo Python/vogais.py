def vogal(c):
    vogais = ['a','e','i','o','u','A','E','I','O','U']
    évogal = False
    for vog in vogais:
        if c == vog:
            évogal = True
            break
    return évogal

print(vogal('U'))