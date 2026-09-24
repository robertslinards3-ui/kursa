# Darba plāns: Kursa (LU pirmsinkubācija, "Idea to Impact")

> Plāns seko komandas pieteikuma anketai [Kursa_PieteikumaAnketa.docx](Kursa_PieteikumaAnketa.docx).
> Ja anketa mainās, jāmaina arī šis plāns.
> - **Lēmumi un atvērtie jautājumi:** [PROJECT.md](PROJECT.md)
> - **Konkurenti:** [TIRGUS_IZPETE.md](TIRGUS_IZPETE.md)
> - **Nauda:** [BUDZETS.md](BUDZETS.md)
>
> Iepriekšējie plāni (pilns TMS, pēc tam "CMR foto → rēķins") ir mapē `pieteikums/arhivs/`.

## 1. Mērķi 4 mēnešos (tādi paši kā anketā)

1. **Vismaz 15 intervijas** ar pārvadātājiem un ekspeditoriem. Jāapstiprina galvenās problēmas un gatavība maksāt par risinājumu.
2. **Pirmais prototips** platformas galvenajām funkcijām. MVP sākas ar **1–2 funkcijām, kas dod vislielāko ietaupījumu**, nevis ar visu platformu.
3. **Testēšana ar 2–3 pārvadātājiem** reālos darba apstākļos.
4. **Biznesa modelis un cenu struktūra**, balstoties uz testēšanas rezultātiem.

Pilotā mērām to, ko nosauc anketa:

| Rādītājs | Kā mērām |
|---|---|
| Vienas kravas apstrādes laiks | Minūtes no pieprasījuma līdz apstiprinātam pasūtījumam / rēķinam, pirms un pēc |
| Kļūdu skaits dokumentos | Laboti lauki un atgriezti rēķini |
| Dienas no piegādes līdz rēķinam | Datums piegādē un datums rēķinā |

## 2. Kā izvēlēties 1–2 MVP funkcijas

Anketā ir 6 platformas daļas. 4 mēnešos būvējam tikai tās 1–2, kurām intervijās un dispečera vērošanā ir lielākā sāpe. Kandidāti:

| Funkcija | Ko ietaupa | Kas pārbaudāms intervijās |
|---|---|---|
| **Pasūtījuma apstrāde:** e-pasts/PDF → strukturēts pasūtījums | Dispečera laiku, pārrakstīšanas kļūdas | Cik pieprasījumu dienā, kādās valodās, cik minūšu katrs |
| **Cenas aprēķins:** maršruts, nodevas, degviela, peļņa | Laiku cenas piedāvājumam | Kā šodien rēķina, cik piedāvājumu nedēļā |
| **Rēķins no piegādes:** CMR foto → rēķins → atgādinājumi | Dienas līdz naudai | Cik dienu līdz rēķinam, kā CMR nonāk birojā |
| Plānošana, atbilstība (darba laiks, kabotāža, dienas nauda, CO2) | | Visticamāk pēc programmas: sarežģīti un to jau dara TMS (Planlogi, Mapon) |

**Lēmums 1. mēneša beigās:** kuras 1–2 funkcijas būvējam. Pamats: intervijās visbiežāk minētā un vērošanā izmērītā sāpe.

## 3. Lomas (priekšlikums, jo anketā "Pienākumi komandā" vēl ir tukšs)

| | Roberts Kaņepons (Finanšu menedžments) | Roberts Linards (E-bizness) |
|---|---|---|
| Galvenā atbildība | Rēķinu un cenu loģika, biznesa modelis un cenas, sarunas ar grāmatvežiem, LU atskaites un izdevumu žurnāls | Produkts un prototips, digitālie procesi un integrācijas (e-pasts, grāmatvedības programmas), testēšana ar pilota klientiem |
| Kopā | Intervijas, dispečera vērošana, MVP funkciju izvēle, Demo diena | |

Kurš galvenokārt programmē, jāizlemj jums abiem. No tā atkarīgs arī Claude Max plāns (20x galvenajam izstrādātājam).

## 4. Darba ritms

- **Pirmdienās 1 h:** ko izdarījām, ko darām šonedēļ, kas traucē.
- **Kopīgais darbu saraksts** ar atzīmēm: https://claude.ai/artifact/8Cufb9nBRmZk6ppiHixwkW (jāatjauno pēc šī plāna).
- **Izdevumu žurnāls (LU!):** mape `izdevumi/` (tabula + rēķinu PDF). Iegrāmato tajā pašā dienā, katra mēneša beigās salīdzina ar BUDZETS.md.
- **Intervijas:** pieraksts uzreiz pēc sarunas pēc veidnes (6. sadaļa), mapē `intervijas/` (nav repozitorijā, jo tajā ir personas dati).

## 5. Posmi pa mēnešiem

### 1. mēnesis: problēmas apstiprināšana
- **Kontaktu saraksts:** 40 kontakti, gan pārvadātāji (5–100 auto, starptautiskie, īpaši Baltija–Ziemeļvalstis), gan ekspeditori.
- **Intervijas:** 15 ar īpašniekiem, dispečeriem un grāmatvežiem. Pirmās 3 abi kopā.
- **Dispečera vērošana:** vismaz 1–2 dienas pie dispečera. Pierakstām katru kravu: kas pienāk, cik laika katrs solis aizņem, kur dati tiek pārrakstīti.
- **Paraugi:** savācam anonimizētus pieprasījumu e-pastus, cenu piedāvājumus un CMR foto, lai tos izmantotu prototipā.
- **Mēneša beigās:** izvēlamies 1–2 MVP funkcijas (2. sadaļa). Ja intervijās neviens negrib maksāt, apstājamies un pārdomājam.

### 2. mēnesis: prototips
- 1–2 izvēlētās funkcijas uz īstiem paraugiem.
- Princips "cilvēks apstiprina": AI sagatavo, dispečers pārbauda un apstiprina.
- Mēneša vidū iekšējais demo, beigās vienošanās ar 2–3 pilota pārvadātājiem.

### 3. mēnesis: testēšana ar 2–3 pārvadātājiem
- Reālas kravas, paralēli ierastajam darbam.
- Katru nedēļu saruna ar katru pilota klientu. Labojam to, kas traucē.
- Mērām 3 rādītājus (1. sadaļa): pirms pilota un pilota laikā.

### 4. mēnesis: biznesa modelis un Demo diena
- Cenu struktūra no pilota rezultātiem, piemēram, maksa par auto mēnesī vai par apstrādātu kravu. Sarunas par cenu ar pilota klientiem.
- Biznesa modelis: kam pārdodam pirmos, kā, par cik, kas ir nākamās funkcijas.
- Demo dienas prezentācija ar pilota skaitļiem, LU atskaite.

## 6. Intervijas

### Kur atrast
1. Personīgie kontakti un paziņu uzņēmumi.
2. Grāmatveži, kas apkalpo pārvadātājus.
3. firmas.lv / Lursoft: NACE 49.41 (kravu autopārvadājumi) un 52.29 (ekspedīcija).
4. Nozares asociācijas (piem., "Latvijas Auto"), loģistikas grupas Facebook/LinkedIn.

### Jautājumi (neko nepārdodam, jautājam par pagātni)
1. Pastāstiet par pēdējo kravu no pieprasījuma līdz naudai kontā. Kas notika katrā solī?
2. Kā pienāk kravu pieprasījumi (e-pasts, PDF, birža, telefons)? Kādās valodās? Cik dienā?
3. Kā sagatavojat cenas piedāvājumu? Cik laika tas aizņem? Kā rēķināt nodevas un degvielu?
4. Kā izvēlaties auto un vadītāju? Kā vadītājs saņem norādījumus?
5. Kā parakstītais CMR nonāk birojā? Pēc cik dienām tiek izrakstīts rēķins? Cik ilgi līdz samaksai?
6. Kādos formātos jāizraksta rēķini (Latvija, Norvēģija u.c.)? Vai esat dzirdējuši par e-rēķinu termiņiem?
7. Kā sekojat darba laikam, kabotāžai, dienas naudai?
8. Kādus rīkus jau lietojat (TMS, Mapon, kravu biržas, Excel, grāmatvedības programma)? Ko esat mēģinājuši un atmetuši? Kāpēc?
9. Kurš no šiem soļiem jums sāp visvairāk? Cik tas izmaksā laikā vai naudā?
10. *(Beigās)* Vai varam kādu dienu pavērot, kā strādā dispečers? Vai varat iedot dažus anonimizētus paraugus?

### Pieraksta veidne
- **Uzņēmums, auto skaits, virzieni, kas runāja (loma).** **Rīki:** __
- **Kravas ceļš un laiks katrā solī:** __
- **3 lielākās sāpes (citāti):**
- **Gatavība maksāt / pilotam:** jā / varbūt / nē. **Nākamais solis:**

## 7. Tehniskie principi (no anketas)

- **LLM** pieprasījumu, e-pastu un dokumentu nolasīšanai dažādās valodās. **Attēlu atpazīšana** papīra CMR foto.
- **Karšu un ceļu nodevu datu pakalpojumi** maršrutam un izmaksām. **Optimizācija** auto piešķiršanai (tikai ja to izvēlamies MVP).
- **Integrācijas** ar e-pastu, telemātiku, kravu biržām, grāmatvedības programmām (kur pieejamas).
- **E-rēķini:** Peppol BIS Billing 3.0 un Norvēģijas EHF, caur sertificētu Peppol pakalpojumu sniedzēju.
- **Mobilā tīmekļa lietotne** vadītājiem bez instalēšanas. **Mākonis ES**, VDAR.
- **Cilvēks apstiprina:** AI sagatavo, lēmumu pieņem dispečers.
- **Izvēlamies to, ko jau protam:** viens repozitorijs, viens serveris, viena datubāze.

## 8. Riski

| Risks | Ko darām |
|---|---|
| Pilnu TMS jau piedāvā Planlogi (Igaunija), Mapon (Rīga), Dashdoc u.c. | Žūrijai skaidri pasakām atšķirību: AI automatizācija, nevis datu ievade; Baltija–Ziemeļvalstis ar e-rēķinu formātiem. Pārbaudām intervijās, ko viņi jau lieto |
| 6 funkcijas ir par daudz 2 cilvēkiem 4 mēnešos | MVP = tikai 1–2 funkcijas, pārējais ir ceļa karte |
| Intervijās neviens negrib maksāt | Lēmums 1. mēneša beigās, pirms būvējam |
| AI slikti lasa rokrakstu vai netipiskus e-pastus | "Cilvēks apstiprina" un testi uz īstiem paraugiem 1.–2. mēnesī |
| Norvēģijas EHF un Peppol pakalpojuma izmaksas | Pilotā pietiek ar PDF + eksportu. Peppol sniedzēju izvēlamies, kad ir klients, kam tas vajadzīgs |

## 9. Ko programmas laikā NEDARĀM

- Visas 6 platformas daļas.
- Savu Peppol piekļuves punktu.
- eFTI sertifikāciju.
- Dzelžus.
- Sadarbības vidi ekspeditoriem un nosūtītājiem (ilgtermiņa vīzija anketā).
