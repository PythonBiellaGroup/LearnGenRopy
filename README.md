# Repository delle lezioni

Ogni cartella conterrà il progetto completo allo stato di avanzamento della lezione. Per la corretta esecuzione, è necessario trascinare il file nella directory dei progetti Genropy specificata nel corso dell'installazione (di default ``sviluppo/genropy_projects``). Si consiglia di rinominare di volta in volta la versione in uso semplicemente *blood_donor*.

Per l'installazione di Genropy si faccia riferimento a questa guida: https://www.genropy.org/docs/installation_guide/framework_installation.html

# Pre-requisiti

Una volta clonato il progetto, eseguire in una finestra di terminale lo script ``gnrdbsetup bd_test`` per generare database, tables e colonne partendo dal model.

Eseguendo la **gnrdbsetup** con l'attributo ``-u`` è possibile generare anche i *sysRecord*, ovvero i record di sistema predefiniti (si veda in proposito la tabella ``donor.donator_blood_group``).

È a questo punto possibile avviare il software: in una finestra di terminale lanciare il ``gnrdaemon`` e in una finestra separata avviare l'applicativo con lo script ``gnrwsgiserve bd_test``.

Una volta entrati nell'applicativo, entrare nelle preferenze di sistema (bottone in basso a destra con etichetta *Preferences*) e dal tab **Geo Italia** cliccare su ``Load data`` per popolare le tabelle geografiche.

È ora possibile creare i record dei donatori, delle analisi e delle donazioni!

# Restore dei dati

Nella cartella *data* del progetto è contenuto un database di record generati casualmente a scopo didattico. Il database è in PostgreSQL, di conseguenza per l'eventuale restore occorre aver configurato Genropy seguendo questa guida:

https://www.genropy.org/docs/installation_guide/config_db.html

Per eseguirne il restore, eseguire lo script ``gnrwsgiserve bd_test --restore bd_test_dump_.zip`` dall'interno della cartella *data* (o in alternativa trascinare il file nella finestra per copiare l'intero percorso).

# References e materiale didattico

A questo link è possibile reperire il materiale didattico delle serate: https://github.com/PythonBiellaGroup/MaterialeSerate/tree/master/Genropy

## Documentazione e link utili per approfondire Genropy

Repository ufficiale su Bitbucket
➡️  https://bitbucket.org/genropy/genropy/src/py3/

Blog di Genropy
➡️ https://www.genropy.org/blog

Tutorial Fatturazione
➡️ https://genropy.org/docs/tutorial_fatturazione

Corso Base di Genropy
➡️ https://www.genropy.org/docs/corso_genropy/index.html 

Learn Genropy su YouTube
➡️ https://www.youtube.com/playlist?list=PLNVV7kKSGQW845Qhpu8pB-SPeq6aa9ZZf