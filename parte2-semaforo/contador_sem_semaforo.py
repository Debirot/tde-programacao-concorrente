import threading
import time

# quantidade de threads
T = 8
# quantidade de incrementos por thread
M = 200000

# contador compartilhado entre as threads
count = 0


def tarefa():
    global count
    for i in range(M):
        valor = count
        # pequeno trabalho para a troca de thread acontecer aqui
        for j in range(10):
            pass
        # grava o valor + 1 
        count = valor + 1


# cria as threads
threads = []
for i in range(T):
    t = threading.Thread(target=tarefa)
    threads.append(t)

# começa a contar o tempo
inicio = time.time()

# inicia as threads
for t in threads:
    t.start()
# espera todas terminarem
for t in threads:
    t.join()

print("Esperado:", T * M)
print("Obtido:", count)
print("Tempo:", time.time() - inicio)