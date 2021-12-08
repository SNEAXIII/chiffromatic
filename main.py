def b36_b10(str__, dict={'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11,'C': 12,'D': 13, 'E': 14, 'F': 15, 'G': 16, 'H': 17, 'I': 18, 'J': 19, 'K': 20, 'L': 21, 'M': 22, 'N': 23,'O': 24,'P': 25, 'Q': 26, 'R': 27, 'S': 28, 'T': 29, 'U': 30, 'V': 31, 'W': 32, 'X': 33, 'Y': 34, 'Z': 35}):
    nb_vide = 0
    for i, c in enumerate(str__[::-1]):
        nb_vide += dict[c] * (36 ** i)
    return nb_vide


def b10_b36(nb, __str="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ", str__=""):
    while nb != 0:
        str__ += __str[nb % 36]
        nb //= 36
    return str__[::-1]


def str_b10(str_, c=0, dicto={32: 29, 39: 30, 44: 31, 46: 32}):
    for a, b in enumerate(str_):
        if 97 <= ord(b) <= 122:
            b = ord(b) - 94
        else:
            b = dicto[ord(b)]
        c += b * 34 ** (a + 2)
    return c


def find_the_repet(phrase_, nbrepet=0, nbr_constru=0):
    while nbr_constru < phrase_:
        nbr_constru = 34 ** nbrepet
        nbrepet += 1
    return nbrepet - 2


def find_the_good(power, nb):
    for looping in range(32, 1, -1):
        nb_a_test = looping * 34 ** power
        if nb // nb_a_test == 1: return looping, nb - nb_a_test
    return 0, 0


def b10_str(phr_, mot=[], str__="", dicto={29: 32, 30: 39, 31: 44, 32: 46}):
    nb = find_the_repet(phr_)
    while phr_ != 0:
        resu = find_the_good(nb, phr_)
        phr_ = resu[1]
        mot.append(resu[0])
        nb -= 1

    for a in mot[::-1]:
        if 3 <= a <= 28:
            str__ += chr(a + 94)
        else:
            str__ += chr(dicto[a])
    return str__


def enco(phr): return b10_b36(str_b10(phr))


def deco(str___): return b10_str(b36_b10(str___))


# print(phrase_)
# phrase_chiff = str_b10(phrase_)
# print(phrase_chiff)
# str__ = b10_str(phrase_chiff)
# print(b10_b36(phrase_chiff))
# texte_a_decoder = b10_b36(phrase_chiff)
# print(enco(phrase_))
phrase_ = "hehe boi"

print(phrase_)

texte_a_decoder = enco(phrase_)

print(texte_a_decoder)

cest_decode = deco(texte_a_decoder)

print(cest_decode)
