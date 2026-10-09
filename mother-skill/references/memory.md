# Second Brain v2: ripresa veloce, meno riletture

Tre livelli: `CLAUDE.md` breve e stabile (istruzioni, comandi, link), `.claude/mother-skill/STATE.json` e `HANDOFF.md` (stato corrente), `docs/wiki/` e `docs/decisions/` (approfondimenti su richiesta); archivio `docs/archive/YYYY-MM/` per handoff storici. Non leggere tutta la wiki all'avvio: prima `STATE.json`, poi HANDOFF, poi riferimenti necessari.

Dopo ~7 giorni di lavoro sullo stesso progetto **oppure** quando aumenta la ridondanza, proponi una compattazione basata su verifica: confronta note con stato reale e Git, elimina duplicazioni, archivia handoff obsoleti, aggiorna indice. Mai cancellare decisioni, contesto di bug aperti, credenziali (che non dovrebbero mai stare qui) o lavoro altrui. Chiedi consenso prima di cancellazioni/archiviazioni che modificano file.

Handoff massimo una pagina utile: SHA/branch, task appena concluso, ciò che funziona, test reali, rischi/bug, cosa fare subito, link alle decisioni. `STATE.json` è la fonte strutturata; `HANDOFF.md` è la sintesi umana. Profilo didattico personale **fuori repo** `~/.claude/mother-skill/LEARNING_PROFILE.json` con consenso.

Ottimizzazione token reale: caricare un indice prima del contenuto; niente screenshot serializzati in markdown, niente log CI lunghi, niente transcript copiati. Non promettere numeri di token risparmiati senza misurazione.

## Handoff a 70%

La manutenzione settimanale non sostituisce il protocollo del contesto: consulta `context-budget.md`. **Al 60% osservato prepara, al 70% salva e riparti in nuova conversazione**, senza delegare ricostruzioni o leggere tutti gli MD. Se l'indicatore non è disponibile, non inventare percentuali.
