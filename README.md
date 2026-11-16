

# TDE - Programação Concorrente - GRUPO 1 TDE2 

===

https://github.com/Debirot/tde-programacao-concorrente/tree/main



# Vídeo: (link do YouTube)

# 

# \## Integrantes

Mateus de Brito Gomes

Júlio Cesar Stein

Thiago Oliveira

# 

# \## Linguagem

Python 3.11

# 

# \## Parte 1 - Jantar dos Filósofos



!\[versao ingenua com deadlock](parte1-filosofos/evidencias/ingenua/deadlock.png)

!\[versao corrigida](parte1-filosofos/evidencias/corrigida/versaacorrigidaa.png)



Cenario 1 - Versaso ingenua e Ocorrencia de deadlock



No jantar dos filosofos(N = 5) na versao ingenua cada filosofo executa o seguinte ciclo repetitivo:





1- pensa(time.sleep)

2- sentir fome

3 - pega garfo esquerdo (garfo\_esq.acquire())

4 - pausa (time.sleep(x))

5 - adquite garfo direito(garfo\_dir.acquire())

6 - comer e libera os talheres.





Analise dos reesultados e comportamento do (Scheduler) que e o agendamento



\- timesleep aleatorio ou maior que 0.5:

De inicio o sistema ocorreu sem trava aparente,porque o escalonamnto nativo do SO gerencia as trocas de contexto das threads de forma que, eventualmente, um filosofo consegue adquirir ambos os talheres, comer e liberaros antes que um vizinho alcancem o mesmo pronto critico.



\- impacto do timesleep(0.5) e o papel do escalonador :

Ao chamar time.sleep(0.5), logo apos o primeiro garfo, a thread desiste voluntariamente da CPU e entra em estado de espera. Isso forca o escalonador do SO a alternar o processamento para as demais threads sem que estejam na sequenica, criando uma janela temporal necessssaria para que o agendador de oportunidade a todas as threads de xecutarem,pegar os garfos esquerdos e ficarem no mesmo estado vulneravel q e com o garfo na mao antes de tentar pegar o proximo;

\-DEADLOCK: Com todos os garfos esquerdos ocupados,cada filosofo tenta pegar o direito porem esta ocupado pelo vizinho. Como a thread nao libera o recurso  ,elas ficam blloqueado e aguardando alguem liberaar,gerar espera circular. O programa para o progresso pois as threads ficam bloquedas,gerando DEADLOCK classico verificado nos logs de execucao, mesmo com o SO e os outros aplicativos funcionaando normalmente.





\-Cenario 2 - versao corrigida utilizando hirerarquia de recursos para eliminar DEADLOCK



Para resolver o problema de deadlock observado na versao ingenua, o algoritmo foi modificado aplicando hirerarquia de recursos.Essa estrageria consiste em impor uma ordenacao global e estrita  sobre a aquisicao dos recurso compartilhados que sao os garfos.

No modelo corrigido

1\. cada garfo possui um indice numero fixo que vvai de 0 ate N -1.

2\. Para cada filosofo identificam-se os garfos adjacentes(esquerda e direita).

3\. Ao invez de sempre pegar o garfo esquerdo primeiro foi modificado a regra, a nova regra e a seguinte no codigo emos left = min(garfo\_esq, garfo\_dir) ( pega o garfo de menor indice primeiro), right = max(garfo\_esq, garfo\_dir) (pega o garfo de maior indice ).

4\.  Apos comer libera os garfos e se inicia o ciclo novamente.





Para que ocorra um \*deadlock\* a  \*\*coexistencia simultanea das quatro condicoes de coffman\*\*(exclusao mutua, posso e espera. nao-preempcao e espera circular). Na versao ingenua todas as quatro aparecem.



O metodos utilizado(hirerarquia de recursos) atua diretamente sobre a \*\*espera circular\*\* . Ao impor uma ordem globa  de menor e maior ,torna-se matematiamente impossivel a formacao de um ciclo fechado de espera entre os filosofos. O sistema ganha progresso continuo e as \*\*threads\*\* podem sofrer breves espera por conter recursos, mas o travamento sistemico (deadlock) nao ocorre,cono foi mostrados os prints da execucao do vscode.





3\. Starvation e justica



Esse metodo garante a quebra do deadlock ,mas nao garante justica total, pois ha espera para comer, podendo deixar algum outro com fome  caso o tempo de espera seja muito longo,na espera para liberar um recurso, ou starvation q e um filoso esperar indefinitivamente  um recurso  enquanto os outros conseguem comer.Como hirerarquia apenas elimina o travamento sistemico e nao gerencia fila de prioridades ou vez de atendimento, umfilosofo pode acabar sofrendo esperas prolongadas caso os vizinhos acesem os recursos repetidamente.





4\. PSEUDO CODIGOS

4.1- parte ingenua



N = 5 filosofos

Garfos 0..N-1 (garfo i fica entre filosos i e (i+1) mod N)



filosofo(id)

&#x20;   garfo\_esq = id

&#x20;   garfo\_dir = (id+1) mod N



&#x20;   enquanto verdadeiro faca:

&#x20;       //comeca pensar:

&#x20;       imprimir("filosofo",id, "esta pensando!!!")

&#x20;       aguarda(1 segundo)



&#x20;       //deu fome

&#x20;       imprimir("filosofo", id, "esta com fome")



&#x20;       //pega o garfo esquerdo

&#x20;       garfos\[gardo\_esq].adquirir()

&#x20;       imprimir("filosofo",id."pegou garfo",garfo\_esq,"(esquerda).")



&#x20;       aguardaar(0.5 segundos)//pausa para favorecer o deadlock



&#x20;       //pega o garfo direto

&#x20;       garfos\[garfo\_dir].adquirir()

&#x20;       imprimir("filosofo",id."pegou o garfo",garfo\_dir,"(direita)")



&#x20;       //comer

&#x20;       imprimir("filosofo",id,"estacomendo!!!")

&#x20;       aguardar(1 segundo)



&#x20;       //terminou e comer e libera os talheres

&#x20;       garfos\[garfo\_dir].liberar()

&#x20;       garfo\[garfo\_esq].liberar()



&#x20;       imprimir("filosofo",id."terminou e largou os talheres.\\n")



&#x20;fim da funcao



&#x20;//executa o main

&#x20;para i ate 0 e N-1 faca:

&#x20;   cria thread t para exeutar filosofo(i)

&#x20;   inicia thread t

&#x20;fim para





4.2 pseudo codigo da versao corrigida



N = 5 filósofos

Garfos 0..N-1 (garfo i fica entre filósofos i e (i+1) mod N)



funcao filosofo (id):

&#x20;   garfo\_esq =id

&#x20;   garfo\_dir = (id+1) mod N





enquanto verdadeiro faca:



&#x20;   //comeca pensar

&#x20;   imprimir("filoso",id,"esta pensando!!!")

&#x20;   aguardar(1 segundo)



&#x20;   //deu fome

&#x20;   impriiir("filosofo",id,"esta com fome")



&#x20;   //aqui entra hirerarquia de recurso contra deADLOCK



&#x20;   primeiro = min(garfo\_esquerda, garfo\_direita)

&#x20;   segundo = max(garfo\_esquerda, garfo\_direita)





&#x20;   //pega primeir garfo(menor indice)

&#x20;   garfos\[primeiro].adquirir()

&#x20;   imprimir("fillosos",id,"pegou o garfo",primeiro)



&#x20;   //segundo garfo(maior indice)

&#x20;   garfos\[segundo].adquirir()

&#x20;   imprimir("filosofo",id,"pegou o garfo",segundo)



&#x20;   //comer

&#x20;   imprimir("filosofo",id,"esta comendo!!")

&#x20;   aguarda(1 segundo)



&#x20;   //terminou de comer e libera os talher

&#x20;   garfo\[segundo].liberar()

&#x20;   garfo\[primeira].liberar()

&#x20;   imrprimir("filosofo",id,"terminou e largou os talheres\\n")



fim da funcao



//execucao principal

para i de 0 ate N -1 faca:

&#x20;   criar thread t para executar filosofo(i)

&#x20;   iniciar thread t

fim para

# 

# \## Parte 2 - Threads e semáforos

!\[sem semaforo 1](parte2-semaforo/prints/sem\_semaforo\_1.png)

!\[sem semaforo 2](parte2-semaforo/prints/sem\_semaforo\_2.png)

!\[sem semaforo 3](parte2-semaforo/prints/sem\_semaforo\_3.png)

!\[com semaforo 1](parte2-semaforo/prints/com\_semaforo\_1.png)

!\[com semaforo 2](parte2-semaforo/prints/com\_semaforo\_2.png)

!\[com semaforo 3](parte2-semaforo/prints/com\_semaforo\_3.png)



Como executar:



cd parte2-semaforo

python contador\_sem\_semaforo.py

python contador\_com\_semaforo.py



Funcionamento:

8 threads incrementam um contador compartilhado 200,000 vezes cada. O valor esperado é 8 × 200,000 = 1,600,000.



Sem semáforo: as threads leem e gravam o contador ao mesmo tempo e o resultado sai errado.

Com semáforo: threading.Semaphore(1) deixa só uma thread por vez mexer no contador e o resultado sai certo.



O for j in range(10): pass entre a leitura e a escrita existe por causa do GIL do Python. Sem ele, a troca de thread quase nunca acontece no meio do incremento e a corrida não aparece.



Resultados

Versão	     Tentativa	Esperado	Obtido	Tempo (segundos)

Sem semáforo	1	1600000	        865337	 0.469

Sem semáforo	2	1600000	        1101351	 0.255

Sem semáforo	3	1600000	        887445	 0.367

Com semáforo	1	1600000	        1600000	 1.388

Com semáforo	2	1600000	        1600000	 1.401

Com semáforo	3	1600000	        1600000	 1.392



Discussão:

Duas threads leem o mesmo valor (ex: 100), as duas gravam 101, e um incremento some, por isso há perda de incremento



Só uma thread por vez lê e grava o contador, então nenhuma lê um valor desatualizado. O semáforo resolve o problema.



Throughput: com semáforo ficou quase 4 vezes mais lento, porque as threads esperam a vez. Perde velocidade, mas o resultado fica correto.



Justiça: o Semaphore do Python não garante ordem de chegada (FIFO), mas isso não muda o resultado, porque todas as threads terminam.



O acquire() e o release() funcionam como barreiras o que uma thread gravou antes do release() é visto pela próxima que fizer acquire(), garantindo visibilidade.



# \## Parte 3 - Deadlock



!\[deadlock](parte3-deadlock/prints/deadlock\_print.jpeg)

!\[sem deadlock](parte3-deadlock/prints/sem\_deadlock\_print.jpeg)



\### Como executar



cd parte3-deadlock

python deadlock.py

python deadlock\_corrigido.py





\### Cenário



Duas threads e dois locks (A e B):



\- Thread 1 pega o LOCK\_A e depois o LOCK\_B

\- Thread 2 pega o LOCK\_B e depois o LOCK\_A



O time.sleep(0.05) entre as duas aquisições dá tempo para cada thread pegar o seu primeiro lock antes de pedir o segundo. Assim o deadlock acontece em toda execução.



\### Condições de Coffman



\- Exclusão mútua: cada lock só pode ficar com uma thread por vez.

\- Manter e esperar: a Thread 1 segura o A e espera o B; a Thread 2 segura o B e espera o A.

\- Não preempção: nenhuma thread tira o lock da outra; só quem pegou pode liberar.

\- Espera circular: a Thread 1 espera a Thread 2, e a Thread 2 espera a Thread 1.



As quatro aconteceram ao mesmo tempo, por isso houve deadlock.



\### Correção



Ordem global de aquisição: todas as threads pegam o LOCK\_A antes do LOCK\_B. A única mudança foi na Thread 2:



python

def thread\_2():

&#x20;   LOCK\_A.acquire()

&#x20;   print("Thread 2 pegou o LOCK\_A")

&#x20;   time.sleep(0.05)

&#x20;   print("Thread 2 esperando o LOCK\_B")

&#x20;   LOCK\_B.acquire()

&#x20;   print("Thread 2 concluiu")

&#x20;   LOCK\_B.release()

&#x20;   LOCK\_A.release()





Isso quebra a espera circular. Se o LOCK\_A está com a Thread 1, a Thread 2 espera sem segurar nenhum lock, então a Thread 1 consegue pegar o LOCK\_B, terminar e liberar os dois. As outras três condições continuam existindo, mas basta quebrar uma para o deadlock não acontecer.

