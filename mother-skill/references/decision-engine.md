# Decision Engine: una decisione utile al momento giusto

## Grill Me
- SOFT: 1–3 domande essenziali e ipotesi concrete.
- MEDIUM: 4–6 domande mirate su utenti, requisiti e compromessi.
- HARD: 7–10 domande in piccoli gruppi; architettura, regressioni, dati, test, performance.
- EXTREME: stress test mirato 10–16 domande organizzate in turni, minacce, lock-in, scalabilità, recoverability, costi, compliance.
Suggerisci livello proporzionato, ma l'utente sceglie; non trasformare un principiante in interrogatorio.

## Selettore formato decisionale
| Intento | Formato consigliato |
|---|---|
| Nuova pagina o brand | 3 prototipi A/B/C, preferibilmente navigabili |
| Singolo widget | 3 demo isolabili |
| Motion/video | 3 clip vere, solo con tool/risorse disponibili; altrimenti 3 storyboard espliciti |
| Database/auth/API | comparazione tecnica 2–3 architetture con trade-off e test, nessun video |
| Bug | ipotesi → osservazioni → test riproduttivo → fix; NON A/B/C decorative |
| Piccolo fix ovvio | 1 proposta, test, avanti |

Per A/B/C specifica una differenza reale, vantaggio/svantaggio, preferenza motivata e scelta dell'utente. Non generare tre video renderizzando costi alti senza consenso. Quando la preview è solo un'immagine, dirlo; non fingere che sia un sito cliccabile. Mostra screenshot intermedie quando hai renderer/browser/preview reale; sono feedback **non bloccanti** finché l'utente non interviene.
