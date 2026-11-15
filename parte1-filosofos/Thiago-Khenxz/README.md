Cenario 1 - Versaso ingenua e Ocorrencia de deadlock

No jantar dos filosofos(N = 5) na versao ingenua cada filosofo executa o seguinte ciclo repetitivo:


1- pensa(time.sleep)
2- sentir fome
3 - pega garfo esquerdo (garfo_esq.acquire())
4 - pausa (time.sleep(x))
5 - adquite garfo direito(garfo_dir.acquire())
6 - comer e libera os talheres.


Analise dos reesultados e comportamento do (Scheduler) que e o agendamento 

- timesleep aleatorio ou maior que 0.5:
De inicio o sistema ocorreu sem trava aparente,porque o escalonamnto nativo do SO gerencia as trocas de contexto das threads de forma que, eventualmente, um filosofo consegue adquirir ambos os talheres, comer e liberaros antes que um vizinho alcancem o mesmo pronto critico.

- impacto do timesleep(0.5) e o papel do escalonador :
Ao chamar time.sleep(0.5), logo apos o primeiro garfo, a thread desiste voluntariamente da CPU e entra em estado de espera. Isso forca o escalonador do SO a alternar o processamento para as demais threads sem que estejam na sequenica, criando uma janela temporal necessssaria para que o agendador de oportunidade a todas as threads de xecutarem,pegar os garfos esquerdos e ficarem no mesmo estado vulneravel q e com o garfo na mao antes de tentar pegar o proximo;
-DEADLOCK: Com todos os garfos esquerdos ocupados,cada filosofo tenta pegar o direito porem esta ocupado pelo vizinho. Como a thread nao libera o recurso  ,elas ficam blloqueado e aguardando alguem liberaar,gerar espera circular. O programa para o progresso pois as threads ficam bloquedas,gerando DEADLOCK classico verificado nos logs de execucao, mesmo com o SO e os outros aplicativos funcionaando normalmente.




-Cenario 2 - versao corrigida utilizando hirerarquia de recursos para eliminar DEADLOCK

Para resolver o problema de deadlock observado na versao ingenua, o algoritmo foi modificado aplicando hirerarquia de recursos.Essa estrageria consiste em impor uma ordenacao global e estrita  sobre a aquisicao dos recurso compartilhados que sao os garfos. 
No modelo corrigido  
1. cada garfo possui um indice numero fixo que vvai de 0 ate N -1.
2. Para cada filosofo identificam-se os garfos adjacentes(esquerda e direita).
3. Ao invez de sempre pegar o garfo esquerdo primeiro foi modificado a regra, a nova regra e a seguinte no codigo emos left = min(garfo_esq, garfo_dir) ( pega o garfo de menor indice primeiro), right = max(garfo_esq, garfo_dir) (pega o garfo de maior indice ).
4.  Apos comer libera os garfos e se inicia o ciclo novamente.


Para que ocorra um *deadlock* a  **coexistencia simultanea das quatro condicoes de coffman**(exclusao mutua, posso e espera. nao-preempcao e espera circular). Na versao ingenua todas as quatro aparecem.

O metodos utilizado(hirerarquia de recursos) atua diretamente sobre a **espera circular** . Ao impor uma ordem globa  de menor e maior ,torna-se matematiamente impossivel a formacao de um ciclo fechado de espera entre os filosofos. O sistema ganha progresso continuo e as **threads** podem sofrer breves espera por conter recursos, mas o travamento sistemico (deadlock) nao ocorre,cono foi mostrados os prints da execucao do vscode. 


3. Starvation e justica

Esse metodo garante a quebra do deadlock ,mas nao garante justica total, pois ha espera para comer, podendo deixar algum outro com fome  caso o tempo de espera seja muito longo,na espera para liberar um recurso, ou starvation q e um filoso esperar indefinitivamente  um recurso  enquanto os outros conseguem comer.Como hirerarquia apenas elimina o travamento sistemico e nao gerencia fila de prioridades ou vez de atendimento, umfilosofo pode acabar sofrendo esperas prolongadas caso os vizinhos acesem os recursos repetidamente.


4. PSEUDO CODIGOS
4.1- parte ingenua

N = 5 filosofos
Garfos 0..N-1 (garfo i fica entre filosos i e (i+1) mod N)

filosofo(id)
    garfo_esq = id
    garfo_dir = (id+1) mod N

    enquanto verdadeiro faca:
        //comeca pensar:
        imprimir("filosofo",id, "esta pensando!!!")
        aguarda(1 segundo)

        //deu fome
        imprimir("filosofo", id, "esta com fome")

        //pega o garfo esquerdo
        garfos[gardo_esq].adquirir()
        imprimir("filosofo",id."pegou garfo",garfo_esq,"(esquerda).")

        aguardaar(0.5 segundos)//pausa para favorecer o deadlock

        //pega o garfo direto
        garfos[garfo_dir].adquirir()
        imprimir("filosofo",id."pegou o garfo",garfo_dir,"(direita)")

        //comer
        imprimir("filosofo",id,"estacomendo!!!")
        aguardar(1 segundo)

        //terminou e comer e libera os talheres
        garfos[garfo_dir].liberar()
        garfo[garfo_esq].liberar()

        imprimir("filosofo",id."terminou e largou os talheres.\n")

 fim da funcao

 //executa o main
 para i ate 0 e N-1 faca:
    cria thread t para exeutar filosofo(i)
    inicia thread t
 fim para   


4.2 pseudo codigo da versao corrigida

N = 5 filósofos
Garfos 0..N-1 (garfo i fica entre filósofos i e (i+1) mod N)

funcao filosofo (id):
    garfo_esq =id
    garfo_dir = (id+1) mod N


enquanto verdadeiro faca:

    //comeca pensar
    imprimir("filoso",id,"esta pensando!!!")
    aguardar(1 segundo)

    //deu fome
    impriiir("filosofo",id,"esta com fome")

    //aqui entra hirerarquia de recurso contra deADLOCK

    primeiro = min(garfo_esquerda, garfo_direita)
    segundo = max(garfo_esquerda, garfo_direita)


    //pega primeir garfo(menor indice)
    garfos[primeiro].adquirir()
    imprimir("fillosos",id,"pegou o garfo",primeiro)

    //segundo garfo(maior indice)
    garfos[segundo].adquirir()
    imprimir("filosofo",id,"pegou o garfo",segundo)

    //comer
    imprimir("filosofo",id,"esta comendo!!")
    aguarda(1 segundo)

    //terminou de comer e libera os talher
    garfo[segundo].liberar()
    garfo[primeira].liberar()
    imrprimir("filosofo",id,"terminou e largou os talheres\n")

fim da funcao

//execucao principal
para i de 0 ate N -1 faca:
    criar thread t para executar filosofo(i)
    iniciar thread t
fim para    




