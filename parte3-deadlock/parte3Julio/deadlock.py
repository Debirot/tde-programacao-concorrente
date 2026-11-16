#Thread 1 pega o LOCK_A e depois o LOCK_B
#Thread 2 faz inversa: LOCK_B e depois LOCK_A
#cada uma segura um lock e esperando o outro
 
import threading
import time

#Criando os locks 
LOCK_A = threading.Lock()
LOCK_B = threading.Lock()

def thread_1():
    LOCK_A.acquire()
    print("Thread 1 pegou o LOCK_A")
    #Pausa 50 ms segurando o LOCK_A
    time.sleep(0.05) #Dá tempo pra Thread 2 pegar o LOCK_B
    print("Thread 1 esperando o LOCK_B")
    #Segura o LOCK_A e espera o LOCK_B 
    LOCK_B.acquire() #Trava o LOCK_B fica com a Thread 2
    print("Thread 1 concluiu")
    LOCK_B.release()
    LOCK_A.release()

def thread_2():
    #Inverso em relação a Thread 1 que cria o deadlock
    LOCK_B.acquire()
    print("Thread 2 pegou o LOCK_B") #Garante que a Thread 2 segure o LOCK_B enquanto
    time.sleep(0.05)  #Dá tempo da Thread 1 pegar o LOCK_A
    print("Thread 2 esperando o LOCK_A")
    #Thread 1 espera 2 e a 2 espera a 1 gerando a espera circular
    LOCK_A.acquire()  #Trava aqui o LOCK_A fica com a Thread 1
    print("Thread 2 concluiu")
    LOCK_A.release()
    LOCK_B.release()

t1 = threading.Thread(target=thread_1)
t2 = threading.Thread(target=thread_2)

t1.start()
t2.start()

#Espera no máximo 2 segundos por cada thread para mostrar que travaram
t1.join(timeout=2)
t2.join(timeout=2)

#Se as duas ainda estão ativa depois do prazo estão travadas
#is_alive() mostra que as threads não terminaram e threading.enumerate() lista threads ativas
if t1.is_alive() and t2.is_alive():
    print(" as duas threads continuam travadas, ocorreu deadlock")
    print("Threads vivas:", threading.enumerate())