# Skill Check & personalizzazione

Dopo che l'utente ha un workspace ed è entrato nella skill, controlla `~/.claude/mother-skill/LEARNING_PROFILE.json` solo con permesso di lettura. Se esiste, proponi riuso o aggiornamento senza rifare tutto. Se non esiste, offri: «8 domande rapide, non è un esame: mi servono per evitare termini incomprensibili. Preferisci farle o partire direttamente guidato?».

Usa `data/quiz_bank.json` e, se Python è disponibile, `scripts/assess_quiz.py` (altrimenti valuta la chiave manualmente): **6 core + 2** focalizzate su web/data/motion/general, opzioni A/B/C/D ed E=non so. Domande interattive se i tool le supportano, altrimenti in chat massimo 2–4 per messaggio; non simulare widget funzionanti. Non mostrare le soluzioni prima delle risposte; possibilità di saltare. Il punteggio è indicativo, 0–2 Starter, 3–5 Explorer, 6–7 Builder, 8 Fluent (solo per basi testate). Adatta per singoli domini, non equiparare risultato a professionalità. Non fare una falsa certificazione.

Tre variabili **indipendenti**:
1. Knowledge = cosa conosco e cosa devo imparare; con evidenze, non etichette identitarie.
2. Autonomy = guided/balanced/autopilot, senza cambiare gate di sicurezza.
3. Grill Me = soft/medium/hard/extreme, profondità critica del problema, non abilità utente.

Spiega il nuovo concetto al primo incontro in 1–3 frasi: definizione concreta + perché serve proprio ora + azione. Offri «Spiegamelo meglio / Lo so già» senza chiedere ripetutamente.

Chiedi permesso prima di salvare preferenze, conserva il minimo indispensabile in `~/.claude/mother-skill/`, mai nel repo o nelle PR. Il profilo personale non deve includere nomi, email, password o risposte verbatim e non viene condiviso fra utenti o progetti. Non alterare il punteggio automaticamente sulla base di un singolo comportamento.
