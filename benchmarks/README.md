# Benchmark riproducibile: target -75% token, non ancora validato

Il **75% di risparmio** è un'ipotesi da verificare, non un dato pubblicabile come fatto.

## Protocollo

1. Seleziona 10–20 task realistici (feature, bug, UI, database, documentazione) e congela il repository a uno **stesso commit di partenza**.
2. Per ogni task confronta almeno due workflow: A, Mother Skill; B, workflow di riferimento documentato (per esempio Opus orchestratore + subagenti). Stessa versione di modello se possibile, effort dichiarato, stessi strumenti e condizioni.
3. Alterna l'ordine, preferibilmente replicando ogni task più volte; documenta prompt, tempi e disponibilità cache, perché influenzano i risultati.
4. Annota `input_tokens`, `output_tokens`, `cache_creation_tokens`, `cache_read_tokens` o le metriche effettivamente riportate, **costo USD reale se disponibile**, tempo, test superati e interventi umani. Specifica se il valore è consumo lordo, consumo non-cached o costo fatturato: non mescolarli.
5. Confronta **soltanto run che soddisfano lo stesso criterio di qualità**, registrando comunque i fallimenti. I token sono una metrica, non l'unica.

Formula percentuale per una metrica token dichiarata in modo consistente:

`risparmio % = 100 × (1 - token_OpusInlineStudio / token_baseline)`.

La formula ha senso solo se i due workflow producono risultati comparabili e le metriche sono raccolte nello stesso modo. Se il risultato è negativo, la skill ha consumato **più** token.

Il file [`results-template.csv`](results-template.csv) contiene solo le intestazioni, **nessun risultato inventato**. Pubblica log anonimizzati ed eventuali costi, senza API key o dati clienti.
