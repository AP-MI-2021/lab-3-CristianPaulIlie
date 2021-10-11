import math


def printMenu():
    print("1. Citire lista")
    print("2. Determinare cea mai lungă subsecvență cu proprietatea 1")
    print("3. Determinare cea mai lungă subsecvență cu proprietatea 2")
    print("4. Ieșire")


def citireLista():
    l = []
    n= int(input("Dati numarul de elemente: "))
    for i in range(n):
        l.append(int(input("L[" + str(i)  + "]=")))
    return l


def get_longest_subsequence(lst: list[int], has_property: callable) -> list[int]:
    """Returneaza cea mai lunga subsecventa a unei liste, cu o proprietate specifica
        param:   lst (list[int]): Lista principala
        return: list[int]: Cea mai lunga lista cu o proprietate specifica
        """
    returned_subsequence = []
    max_length = 0

    for i in range(len(lst)):
        for j in range(i, len(lst)):
            current_subsequence = lst[i:j + 1]
            if len(current_subsequence) > max_length and has_property(current_subsequence):
                max_length = len(current_subsequence)
                returned_subsequence = current_subsequence

    return returned_subsequence


def are_perfect_squares(lst: list[int]) -> bool:
    """Verifica daca o lista este formata doar din patrate perfecte
        param:    lst (list[int]): Lista verifiata
        return: True daca e formata doar din patrate perfecte, False in caz contrar.
        """
    for x in lst:
        if x != int(math.sqrt(x)) ** 2:
            return False

        return True


def test_are_perfect_squares():
    assert are_perfect_squares([9]) == True
    assert are_perfect_squares([2,5,64,9]) == False
    assert are_perfect_squares([36,16,36,9]) == True
    assert are_perfect_squares([49, 64]) == True


def get_longest_all_perfect_squares(lst: list[int]) -> list[int]:
    """Returneaza cea mai lunga subsecventa a unei liste date, continand doar elementele care sunt patrate perfecte.
        param:   lst (list[int]): Lista principala
        return:  list[int]: Subsecventa ta cu patratele perfecte
       """
    return get_longest_subsequence(lst, are_perfect_squares)


def test_get_longest_all_perfect_squares():
    assert get_longest_all_perfect_squares([23,45,91,81,36,25,6,25,16,58,9]) == [81,36,25]
    assert get_longest_all_perfect_squares([17,21,48]) == []
    assert get_longest_all_perfect_squares([49, 6, 9, 21, 25, 25]) == [25,25]
    assert get_longest_all_perfect_squares([]) == []


def get_bytes1(n: int) -> int:
    """Returneaza numarul de biti cu valoare 1 al unui numar
    param:   n (str): Numarul verificat
    return:    int: Numarul de biti cu valoarea 1
    """

    bytes1 = 0
    while n:
        if n % 2 == 1:
            bytes1+=1
        n //= 2

    return bytes1


def test_get_bytes1():
    assert get_bytes1(7) == 3
    assert get_bytes1(64) == 1
    assert get_bytes1(0) == 0
    assert get_bytes1(9) == 2


def same_bit_counts(lst: list[int]) -> bool:
    """Verifica daca toate numerele din lista au acelasi numar de biti de 1 in reprezentarea binara
    param:    lst (list[int]): Lista verificata
    return:    bool: True daca toate numerele au acelasi numar de biti de 1, False in caz contrar
    """
    for i in range(1, len(lst)):
        if get_bytes1(lst[i]) != get_bytes1(lst[i-1]):
            return False

    return True


def test_same_bit_counts():
    assert same_bit_counts([7, 21, 76]) == True
    assert same_bit_counts([2,8,16]) == True
    assert same_bit_counts([]) == True
    assert same_bit_counts([0,1]) == False


def get_longest_same_bit_counts(lst: list[int]) -> list[int]:
    """Returneaza cea mai lunga subsecventa cu elemente ce au acelasi numar de biti de 1 in reprezentarea lor binara
    param:    lst (list[int]): Lista principala
    rerurn:    list[int]: Subsecventa
    """
    return get_longest_subsequence(lst, same_bit_counts)


def test_get_longest_same_bit_counts():
    assert get_longest_same_bit_counts([5,9,2,1,7,21,76,48]) == [7,21,76]
    assert get_longest_same_bit_counts([12,4,16,91,5]) == [4,16]
    assert get_longest_same_bit_counts([]) == []
    assert get_longest_same_bit_counts([0]) == []


def is_palindrome(x: int) -> bool:
    """Verifica daca un numar e palindrom
    Args:
        x (int): Numarul verificat
    Returns:
        bool: True daca e palindrom, False in caz contrar
    """
    return str(x) == str(x)[::-1]

def test_is_palindrome():
    assert is_palindrome(7) == True
    assert is_palindrome(121) == True
    assert is_palindrome(1432) == False
    assert is_palindrome(23935943) == False


def are_all_palindromes(lst: list[int]) -> bool:
    """Verifica daca toate numerele dintr-o lista sunt palindroame
    Args:
        lst (list[int]): Lista verificata
    Returns:
        bool: True daca toate numerele din lista sunt palindroame, False in caz contrar
    """
    for x in lst:
        if not is_palindrome(x):
            return False

    return True


def test_are_all_palindromes():
    assert are_all_palindromes([101,23432, 515]) == True
    assert are_all_palindromes([54,23,818]) == False
    assert are_all_palindromes([]) == True
    assert are_all_palindromes([1,0,9,2]) == True


def get_longest_all_palindromes(lst: list[int]) -> list[int]:
    """Returneaza cea mai lunga subsecventa de numere care sunt palindroame dintr-o lista
    Args:
        lst (list[int]): Lista cu toate elementele
    Returns:
        list[int]: Subsecventa cu palindroame
    """
    return get_longest_subsequence(lst, are_all_palindromes)

def test_get_longest_all_palindromes():
    assert get_longest_all_palindromes([54,21,636,666,21812, 53,14]) == [636,666,21812]
    assert get_longest_all_palindromes([0,1,2,3,4]) == [0,1,2,3,4]
    assert get_longest_all_palindromes([14]) == []
    assert get_longest_all_palindromes([2]) == [2]


def main():
    test_are_perfect_squares()
    test_get_longest_all_perfect_squares()
    test_get_bytes1()
    test_same_bit_counts()
    test_get_longest_same_bit_counts()
    test_is_palindrome()
    test_are_all_palindromes()
    test_get_longest_all_palindromes()
    lst = []
    while True:
        printMenu()
        optiune = input("Dati optiune:  ")
        if optiune == "1":
            lst = citireLista()
        elif optiune == "2":
            print(get_longest_all_perfect_squares(lst))
        elif optiune == "3":
            print(get_longest_same_bit_counts(lst))
        elif optiune == "4":
            break
        else:
            print("Optiune gresita: Reincercati!")

main()




