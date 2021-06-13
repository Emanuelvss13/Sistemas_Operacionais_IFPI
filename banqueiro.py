def main():
    processos = int(input("Número de Processos: "))
    recursos = int(input("Número de Recursos: "))
    m_recursos = [int(i) for i in input("Digite os recursos disponiveis: ").split()]

    print("\n-- Recursos alocados --")
    alocados = [[int(i) for i in input(f"processo {j + 1}: ").split()] for j in range(processos)]

    print("\n-- Recurso nescessario --")
    necessarios = [[int(i) for i in input(f"process {j + 1} : ").split()] for j in range(processos)]

    alocado = [0] * recursos
    for i in range(processos):
        for j in range(recursos):
            alocado[j] += alocados[i][j]
    print(f"\ntotal de recursos alocados: {alocado}")

    disponivel = [m_recursos[i] - alocado[i] for i in range(recursos)]
    print(f"total de recursos disponiveis: {disponivel}\n")

    rodando = [True] * processos
    count = processos
    while count != 0:
        seg = False
        for i in range(processos):
            if rodando[i]:
                executando = True
                for j in range(recursos):
                    if necessarios[i][j] - alocados[i][j] > disponivel[j]:
                        executando = False
                        break
                if executando:
                    print(f"O processo {i + 1} está rodando")
                    rodando[i] = False
                    count -= 1
                    seg = True
                    for j in range(recursos):
                        disponivel[j] += alocados[i][j]
                    break
        if not seg:
            print("O processo esta em um estado não seguro")
            break

        #{disponivel}\n")

main()