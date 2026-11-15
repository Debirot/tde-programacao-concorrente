#HERERARQUIA DE RECURSOS

import threading
import time


N =5

garfos = [threading.Lock() for _ in range(N)]

print("=== HERERARQUIA DE RECURSO DOS FILOSOS ===\n")


def filosos_corrigido(id):
    garfo_esq = id
    garfo_dir = (id +1) %N

    #aqui ta o pulo do ggato
    #sempre pega o garfo de indice menor e depois o de maior

    left = min(garfo_esq,garfo_dir)
    right = max(garfo_esq, garfo_dir)

    while True:

        print(f"Filosos {id} esta penasndo;...")
        time.sleep(1)

        print(f"Fiolosos {id} esta com fome...")


        garfos[left].acquire()
        print(f"filosos {id} pegou o garfo de menor indice ({left})")

        garfos[right].acquire()
        print(f" filosos {id} pegou o garfo com maior indice ({right})")


        print(f" filososo {id} estA  comendo!!")


        garfos[right].release()
        garfos[left].release()

        print(f"o filososo {id} terminou e largou  os talheres.\n")




for i in range(N):
    t = threading.Thread(target=filosos_corrigido, args=(i,))
    t.start()
