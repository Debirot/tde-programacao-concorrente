#Thread 1 e a Thread 2 pegam os locks na mesma ordem: LOCK_A e depois LOCK_B
#Mesma ordem para todos, não existe espera circular,  não trava o programa

import threading
import time

#Criando os locks 
LOCK_A = threading.Lock()
LOCK_B = threading.Lock()

def thread_1():
    LOCK_A.acquire()
    print("Thread 1 pegou o LOCK_A")
    time.sleep(0.05) #Mesma pausa da versão que trava
    print("Thread 1 esperando o LOCK_B")
    LOCK_B.acquire() #LOCK_B fica livre, porque Thread 2 precisa do LOCK_A antes
    print("Thread 1 concluiu")
    LOCK_B.release()
    LOCK_A.release()

def thread_2():
    #Thread 2 segue mesma ordem da Thread 1, A antes de B
    #Se LOCK_A ficar com Thread 1, Thread 2 vai esperar sem segurar nenhum lock
    LOCK_A.acquire()
    print("Thread 2 pegou o LOCK_A")
    time.sleep(0.05)
    print("Thread 2 esperando o LOCK_B")
    LOCK_B.acquire()
    print("Thread 2 concluiu")
    LOCK_B.release()
    LOCK_A.release()

t1 = threading.Thread(target=thread_1)
t2 = threading.Thread(target=thread_2)

t1.start()
t2.start()

#Espera no max 2 segundos por thread
t1.join(timeout=2)
t2.join(timeout=2)

#Mesmo teste da versão que trava, as duas threads terminam e cai no else
if t1.is_alive() and t2.is_alive():
    print(" as duas threads continuam travadas, ocorreu deadlock")
    print("Threads vivas:", threading.enumerate())
else:
    print("as duas threads terminaram, nao ocorreu deadlock")