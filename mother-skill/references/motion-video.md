# Animazioni, video, 3D: scegliere il mezzo corretto

| Strumento | Per cosa | Quando evitare |
|---|---|---|
| CSS / WAAPI | transizioni e micro-interazioni leggere nel browser | regia complessa sincronizzata su timeline |
| GSAP | timeline, ScrollTrigger, UI premium, motion browser | rendering video standalone non predisposto |
| HyperFrames | HTML/CSS/JS temporizzati → rendering video MP4 riproducibile | se servono rigging/modeling 3D avanzati |
| Remotion | video programmatici con React, componenti e rendering frame by frame | se non c'è motivo per dipendenza React/video |
| Blender | modeling 3D, materiali, luci, camera, rigging, animazioni e render | semplice animazione 2D già realizzabile con CSS/GSAP |

Prima di proporre tool, chiarire: risultato è pagina interattiva, 3D realtime, GIF, MP4 verticale/orizzontale, modello GLB/FBX, o template riutilizzabile? Un video non è automaticamente un asset 3D editabile. Concordare FPS, aspect ratio, durata, palette, audio/licenze, accessibilità/reduced motion e budget render.

Per confronti A/B/C scegliere storyboard e low-res/animatic iniziali; poi un solo render premium dopo scelta. Verifica che output esista davvero e può essere aperto. Mostra screenshot/clip reali, non mockup spacciati per prodotti finiti.

Pipeline esempio: Blender produce personaggi/scene 3D → export appropriato o render → GSAP per UI motion in browser → HyperFrames o Remotion per video finale, ma solo se la pipeline scelta lo richiede. Non installare tutti contemporaneamente. Registrare versioni tool e fonti/licenze dei media.

Fonti ufficiali da consultare per API cambiate: https://gsap.com/docs/v3/ ; https://hyperframes.app/docs/ ; https://www.remotion.dev/docs/ ; https://docs.blender.org/manual/en/latest/ .
