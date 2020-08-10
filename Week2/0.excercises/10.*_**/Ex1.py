# Napisz funkcję która przyjmie dowolną liczbę argumentów pozycyjnych i zwróci napis
# powstały z połączenia ich z wykorzystaniem myślnika jako łącznika pomiędzy poszczególnymi argumentami


def num(*words):
    result = ""
    for word in words:
        result += str(word)
        result += "-"
    return result[:-1]

    # with only string we could use this
    # return "-".join(words)



print(num("co", "jest", "grane"))




