def _main():
    processos = [int(i) for i in input("Digite os numeros dos processos: ").split()]
    tempo = [int(i) for i in input("Digite os tempos de cpu desses processos: ").split()]

    q = int(input("Agora digite o tempo de quantum: "))
    t = int(input("E tambem o tempo de troca de contexto: "))  
    
    dados = calc_bruto(processos, tempo, q, t)
    show(dados)



def calc_bruto(processos, tempo, quantum, troca):
    turn = []
    tme = []
    tme = [0] * len(processos) 
    t = 0
    i = 0
    while(1):
        
        if(len(turn) == len(tempo)):
            return [tme, turn]

        if(tempo[i] == 0):
            i += 1
            if(i >= len(tempo)):
                i = 0

        if(tempo[i] == 0):
            i += 1
            if(i >= len(tempo)):
                i = 0

        tempo[i] -= quantum

        if(tempo[i] == 0):
            a = quantum - tempo[i]
            t += a
            obj = {
                'Processo': processos[i],
                'tempo': t
            }
            turn.append(obj)
            t += troca
            e = 0
            while(1):
                a = quantum - tempo[i]

                if(e >= len(tme)):
                    break

                if(i == e):
                    e+=1
                    continue
                else:
                    if(tempo[e] == 0):
                        e+=1
                        continue
                    else:
                        tme[e] += troca
                        tme[e] += a
                        e+=1
            tempo[i] -= tempo[i]
        elif(tempo[i] < 0):
            a = tempo[i] * -1
            t += a 
            obj = {
                'Processo': processos[i],
                'tempo': t
            }
            turn.append(obj)
            t += troca
            e = 0
            while(1):
                a = tempo[i] * -1
                if(e >= len(tme)):
                    break

                if(i == e):
                    e+=1
                    continue
                else:
                    if(tempo[e] == 0):
                        e+=1
                        continue
                    else:
                        tme[e] += troca
                        tme[e] += a
                        e+=1
            tempo[i] -= tempo[i]
        else:
            t += quantum
            t += troca
            e = 0
            while(1):
                if(e >= len(tme)):
                    break

                if(i == e):
                    e+=1
                    continue
                else:
                    if(tempo[e] == 0):
                        e+=1
                        continue
                    else:
                        tme[e] += troca
                        tme[e] += quantum
                        e+=1
            

        i += 1
        if(i == len(tempo)):
            i = 0


def show(dados):
    const = 0
    totaltme = 0
    totaltra = 0
    tme = dados[0]
    tra = dados[1]

    for i in tra:
        print("\nO processo", i["Processo"], "teve um turnaround de:", i["tempo"], sep=" ")
        totaltra += i["tempo"]

    print('\n')
    while(1):
        if(const >= len(tme)):
            break
        else:
            print(f"\nO processo {const+1} teve um tempo de espera de: {tme[const]}")
            totaltme += tme[const]
            const += 1

    mediatme = totaltme / len(tme)    
    mediatra = totaltra / len(tra)

    print(f"\nO tempo médio de turnaround foi: {mediatra}")    
    print(f"O tempo médio de espera foi: {mediatme}") #   

    
_main()
