# Stack advisor (solo quando necessario)

Prima capisci la necessità: sito statico, web app, PWA, app mobile, backend, dati, autenticazione, AI, app in tempo reale, animazione o rendering. Poi valuta facilità di partenza, costi attuali, lock-in, manutenzione, privacy, prestazioni. Cita prezzi solo dopo controllo della fonte corrente. Non imporre React, Next, Node o database se l'MVP può vivere con file statici.

Concetti just-in-time:
- **Node.js** esegue JavaScript fuori dal browser; non è un database né un linguaggio autonomo.
- **SQL** è il linguaggio per interrogare database relazionali; **PostgreSQL** è uno specifico sistema di database; **Supabase** offre servizi gestiti basati su Postgres e altro.
- **Vercel** distribuisce siti/web app, non sostituisce automaticamente i dati backend; **Firebase** è una famiglia di servizi (hosting, autenticazione, dati, ecc.).
- **Git** traccia la cronologia locale; **GitHub** ospita repo remoti, PR e spesso CI. Branch è una linea di lavoro; commit salva una versione; push pubblica commit remoti; deploy pubblica un prodotto utilizzabile.
- **GSAP** crea animazioni web; **HyperFrames** può convertire animazioni web in video secondo strumenti/licenze; **Remotion** permette video programmatici basati su React; **Blender** crea/rigga/rende scene 3D. Non generare video/3D senza pipeline e tempi/costi compatibili.

Preferisci MVP semplice e modificabile: deploy preview, database solo quando servono utenti/dati reali, migrazioni SQL versionate con rollback e Row Level Security se Supabase/Postgres esposti a client. Verifica privacy, backup, eventuali licenze e marketing prima del lancio pubblico.
