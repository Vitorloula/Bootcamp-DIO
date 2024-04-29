import timeit
def pesquisa_binaria(lis, it):
    baixo = 0
    alto = len(lis) - 1

    while baixo <= alto:
        meio = (alto + baixo) // 2
        chute = lis[meio]

        if(chute == it):
            return meio
        if(chute > it):
            alto = meio - 1
        else:
            baixo = meio + 1
    return None 

tamanho = int(input("Coloque o tamanho da lista: "))
item = int(input(f"Coloque um valor entre 1 e {tamanho}: "))
lista = [i for i in range(1,tamanho + 1)]

# Medição de tempo: início
inicio_tempo = timeit.default_timer()

pesquisa_binaria(lista, item)

fim_tempo = timeit.default_timer()

print(f"O item {item} ta na posição : {pesquisa_binaria(lista,item)}")
print(f"Tempo de execução: {fim_tempo - inicio_tempo:.10f} segundos")
