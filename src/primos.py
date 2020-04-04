def verifica_se_eh_primo(numero):
    verdadeiro = True
    if numero == 1:
        return verdadeiro
    else:
        for i in range(2, numero):
            if numero % i == 0:
                verdadeiro = False
                break
        return verdadeiro


def preenche_lista_primo(lista):
    cont = 1
    while len(lista) < 100:
        res = verifica_se_eh_primo(cont)
        if res:
            lista.append(cont)
        cont += 1
    return lista


def print_primos(lista):
    cont = 0
    cont2 = 10
    primos = ''
    for i in lista_primos:
        if lista_primos[cont:cont2] != []:
            primos += str(lista_primos[cont:cont2])
        else:
            break
        cont += 10
        cont2 += 10
    return primos


lista_primos = []
lista_primos = preenche_lista_primo(lista_primos)
print(print_primos(lista_primos))
