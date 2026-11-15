import threading, time
#versao ingenua
N = 5

garfos = [threading.Lock() for _ in range(N)]



def filosos(id):

    garfo_esq = id
    garfo_dir = (id + 1) % N

    while True:
        #comeca pensar o filoso
        print(f"Filoso {id} esta pensando!!")
        time.sleep(1)
        #deu fome
        print(f"Filoso {id} esta com fome")

        #pega garfo esqueta (com time sleep nao deu  deadlock,assim foi reduzido para 0.1)
        garfos[garfo_esq].acquire()
        print(f"Filoso {id} pego o garfo {garfo_esq} (esquerda).")

        time.sleep(0.5)

        #seguindo pega o direito
        garfos[garfo_dir].acquire()
        print(f"Filoso {id} pegou garfo{garfo_dir} (direita)")

        #comer
        print(f"filosofo {id} esta COMENDO!!!")
        time.sleep(1)

        #termiinq comer  e libera garfo
        garfos[garfo_dir].release()
        garfos[garfo_esq].release()
        print(f"Filosos {id} terminou e largo os talheres.\n")

for i in range(N):
    t = threading.Thread(target= filosos, args =(i,)) #a virgula no argd e pra dizer q e uma tupla de um elemento
    t.start()

