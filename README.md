# robot-guide
robot guide through a 2d map with polygon obstacles using searching algorithms

Per usare questo programma occorre innanzitutto scaricare la libreria https://github.com/scikit-geometry/scikit-geometry disponibile su conda. Lavorando su linux ho utilizzato un virtual environment per usare il comando conda:

Questa libreria permette di utilizzare vari costrutti della geometria utilizzati nell'esercizio.

I test si possono fare dalla classe main, un input richiederà quale mappa utilizzare (in questo caso ce ne sono 2), inserendo 0 si accede alla prima mappa, inserendo qualsiasi altro valore si accede alla seconda mappa. scelta la mappa Il programma  mostrarà un plot: lo stato di inizio(punto blu), lo stato di goal(punto giallo) e tutti i vari ostacoli presenti nella mappa(poligoni). Non appena si chiuderà la finestra del plot(in caso si utilizzi python su terminale, questo aspetterà di eseguire le prossime istruzioni finché la finestra del plot è chiusa), Il programma chiederà quale algoritmo di ricerca usare: 1 - A*, 2 - Best first search (graph), 3 o qualsiasi altro numero - Breadth first search (graph). una volta scelto l'algoritmo,verrà eseguito e verrà mostrato un plot della mappa con il percorso trovato dall'algoritmo. Nel terminale verrà poi scritta la lista dei segmenti che compongono il cammino da inizio a goal e la sua lunghezza.
Ad esempio:![mappa 0](https://github.com/emanuelenencioni/robot-guide/blob/main/Figure_1.png)

dopo aver eseguito A*:![mappa 1](https://github.com/emanuelenencioni/robot-guide/blob/main/Figure_2.png)

Il codice del file utils.py, come il codice di astar e best first search è stato preso dalla repository https://github.com/aimacode.
