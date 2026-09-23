# Darba plāns — pārvadājumu platforma (LU inkubācija)

> Kā mums abiem (tev un Robertam) rīkoties 4 mēnešu LU pirmsinkubācijas programmā (MoneyLab).
> Pieteikuma faili un iesniegšanas saraksts: [pieteikums/IESNIEGSANA.md](pieteikums/IESNIEGSANA.md). Lēmumi un atvērtie jautājumi ir
> [PROJECT.md](PROJECT.md), nauda ir [BUDZETS.md](BUDZETS.md).

## 1. Ko gribam sasniegt programmas beigās (4. mēnesis, Demo diena)

Jābūt izmērāmam rezultātam, ne tikai "uzbūvējām sistēmu":

| Mērķis | Skaitlis |
|---|---|
| Intervijas ar pārvadātājiem (5–50 auto) | **15** |
| Pārvadātāji, kas lieto sistēmu pilotā ar īstām kravām | **2–3** |
| Dienas no piegādes līdz rēķinam pilota klientiem | no **5–15 dienām → 0–1 diena** |
| Klienti, kas rakstiski apņemas maksāt pēc pilota (LOI vai priekšapmaksa) | **≥ 1** |

Ja pēc 1. mēneša (15 intervijām) **mazāk par 3** pārvadātājiem piekrīt bezmaksas pilotam,
apstājamies un pārdomājam. Tas ir lēmuma punkts PROJECT.md.

## 2. Līdz 27. septembrim (pieteikums)

| Diena | Kas | Kurš |
|---|---|---|
| 23.09 (tr) | Izlasīt PROJECT.md, PLAN.md, BUDZETS.md un `pieteikums/`. Nosūtīt jautājumus LU | abi |
| 24.09 (ce) | Vienoties par komandas nosaukumu, virzienu (MoneyLab) un budžetu. Ekrānšāviņi cenu izpētei | abi |
| 25.09 (pk) | Personīgie dati veidlapā, savi vārdi motivācijā, ekrānšāviņi budžeta pielikumiem (melnraksti jau ir `pieteikums/`) | tu |
| 26.09 (se) | Roberts pārlasa, labojumi, gala versija | Roberts, tad tu |
| 27.09 (sv) | Iesniegt līdz pusdienlaikam, nevis pusnaktī | tu |

Pieteikumā godīgi jāparāda:
- **Obligātais termiņš:** e-rēķini no 2028. gada.
- **Iespēja, nevis pienākums:** eFTI.
- **Validācija:** 15 intervijas ar skaidru lēmuma punktu. Žūrijai tas izskatās nopietni.

Precīzs darāmo saraksts (faili, ekrānšāviņi, jautājumi LU) ir [pieteikums/IESNIEGSANA.md](pieteikums/IESNIEGSANA.md).

## 3. Lomas (priekšlikums, galīgi lemjam pēc pieteikuma)

| | Tu: produkts un klienti | Roberts: tehnoloģija |
|---|---|---|
| Galvenā atbildība | Intervijas, pilota klienti, rēķinu un grāmatvedības loģika (tava finanšu pieredze), LU atskaites un izdevumu žurnāls | Arhitektūra, serveris, datubāze, šofera PWA, izvietošana, drošība |
| Kodē arī | Rēķinu ģenerēšanu (PDF + Peppol XML), maksājumu atgādinājumus | Dispečera paneli, e-CMR, parakstu, foto |
| Kopā | Pirmās 3 intervijas ejam abi. Roberts dzird problēmas pats, nevis no pierakstiem. |

Ja Roberts ir stiprāks citur (piemēram, frontend vai sarunas ar klientiem), sadali pielāgojam.
Princips: **katram ir sava atbildības joma, par kuru viņš atskaitās.**

## 4. Darba ritms

- **Pirmdienās 1 h sanāksme:**
  1. Ko izdarījām?
  2. Ko darām šonedēļ?
  3. Kas traucē?
- **Uzdevumu dēlis:** GitHub Projects (vai Trello). Katram uzdevumam ir viens atbildīgais.
- **Lēmumi:** ierakstām PROJECT.md tajā pašā dienā.
- **Izdevumu žurnāls (LU!):**
  - Kopīga mape `izdevumi/` ar tabulu (datums, kas, summa, BUDZETS.md pozīcija, kurš maksāja) un čeku/rēķinu PDF.
  - Čeku iegrāmatojam **tajā pašā dienā**.
  - Katra mēneša beigās tabulu salīdzinām ar BUDZETS.md.
- **Intervijas:** pieraksti uzreiz pēc sarunas, vienā veidnē (sk. 6. sadaļu), mapē `intervijas/`.

## 5. Posmi pa mēnešiem

### 0. nedēļa: sagatavošanās (uzreiz pēc pieteikuma)
- [ ] Kopīgs GitHub repo, uzdevumu dēlis, izdevumu žurnāls
- [ ] Claude Max abiem (5x, 4 mēneši)
- [ ] 40 pārvadātāju saraksts intervijām (sk. 6. sadaļu)
- [ ] Intervijas jautājumi (sk. 6. sadaļu)
- [ ] Abi piesakāmies LU stipendijai (€280/mēn.), ja atbilstam

### 1. mēnesis: intervijas un validācija
- 15 intervijas (~5 nedēļā), pārsvarā attālināti (telefons/Teams). Klātienē tikai pilota ieviešana.
- **Pirmajās 10 intervijās produktu nerādām**, tikai jautājam, kā viņi strādā tagad.
- 4.–10. intervijas laikā uzzīmējam ekrānus uz papīra vai Figma. Intervijās 11–15 rādām
  klikšķināmu maketu.
- Juridiskie jautājumi (e-CMR paraksts, GDPR šoferu datiem, pilota vienošanās): mentori + Datu valsts inspekcijas vadlīnijas. Jurists vajadzīgs tikai pēc programmas, kad e-CMR aizstās papīru.
- Tehniskais pamats, kamēr notiek intervijas: repo, serveris, datubāze, pieteikšanās, izvietošana.
  **Funkcijas vēl nebūvējam.**
- **1. mēneša beigās lēmuma punkts:** ≥ 3 piekrišanas pilotam → turpinām. Ja mazāk, apstājamies un pārdomājam.

### 2. mēnesis: MVP būvēšana
Secība ir svarīga. Katrs solis ir lietojams pats par sevi:
1. **Datu modelis:** klients, krava, auto, šoferis, piegāde, e-CMR, rēķins.
2. **Dispečera panelis:**
   - kravas ievade;
   - auto un šofera piešķiršana;
   - statusi.
3. **Šofera PWA:**
   - redz uzdevumu;
   - aizpilda e-CMR;
   - saņēmējs paraksta uz ekrāna;
   - foto ar laika zīmogu;
   - GPS paraksta brīdī;
   - darbojas arī ar sliktu internetu (sinhronizē vēlāk);
   - valoda: LV un RU (LT un UA vēlāk).
4. **Rēķins no parakstītas piegādes:** PDF + Peppol BIS 3.0 XML, eksports grāmatvedībai.
5. **Maksājumu atgādinājumi:** e-pasts klientam pēc termiņa.

- **2. mēneša vidū:** iekšējais demo. Viss scenārijs no sākuma līdz beigām ar izdomātiem datiem.
- **2. mēneša beigās:** pirmais pilota klients sāk lietot sistēmu **paralēli papīram**, lai viņš
  neriskē.

### 3.–4. mēnesis: pilots ar 2–3 pārvadātājiem
- Katru nedēļu īsa saruna ar katru pilota klientu. Labojam to, kas traucē.
- Mērām:
  - dienas no piegādes līdz rēķinam;
  - cik e-CMR aizpildīti bez kļūdām;
  - vai šoferi lieto sistēmu bez atgādināšanas.
- 4. mēnesī runājam par cenu: "Vai maksātu €X par auto mēnesī?" Mērķis ir LOI vai priekšapmaksa.

### 4. mēneša beigas: rezultāti un Demo diena
- Demo video: īsta piegāde → paraksts → rēķins tajā pašā minūtē.
- Rezultātu apkopojums (tabula 1. sadaļā ar reāliem skaitļiem).
- Demo dienas prezentācija (balvu fonds €5 000).
- LU atskaite: izdevumu žurnāls + čeki.
- Lēmums, ko darām tālāk (turpinām / SIA / finansējums).

## 6. Intervijas

### Kur atrast pārvadātājus
1. **Personīgie kontakti:** radi, draugi, draugu uzņēmumi. Siltais kontakts atbild 5× biežāk.
2. **Grāmatveži, kas apkalpo pārvadātājus.** Viņi pazīst desmitiem klientu, un viņiem pašiem
   sāp papīra CMR. Tas var būt arī nākotnes pārdošanas kanāls.
3. **firmas.lv / Lursoft:** NACE kods **49.41** (kravu autopārvadājumi), filtrs pēc darbinieku skaita.
4. **Nozares asociācijas**, piemēram, "Latvijas Auto". Biedru saraksti un pasākumi.
5. **Facebook/LinkedIn šoferu un loģistikas grupas.**

Sarakstā 40 kontakti, jo gaidām, ka atbildēs ~40%.

### Jautājumi (neko nepārdodam, jautājam par pagātni un faktiem)
1. Pastāstiet par pēdējo kravu no pasūtījuma līdz naudai kontā. Kas notika katrā solī?
2. Cik ilgi parasti paiet no piegādes līdz rēķina izrakstīšanai? Un līdz samaksai?
3. Kā parakstītais CMR nonāk birojā? Cik bieži tas pazūd vai kavējas?
4. Kas izraksta rēķinus? Kādā programmā? Cik laika tas aizņem nedēļā?
5. Kā izlemjat, kurš auto un šoferis brauc? Kas to dara?
6. Kā klienti uzzina, kur ir krava? Cik zvanu dienā?
7. Ko jau lietojat (programmas, lietotnes, Excel, WhatsApp)? Ko esat mēģinājuši un atmetuši? Kāpēc?
8. Vai esat dzirdējuši par obligātajiem e-rēķiniem no 2028. gada? Kā plānojat to risināt?
9. Kas jūsu darbā šobrīd sāp visvairāk? (Ja atbilde nav par papīriem vai rēķiniem, tas ir svarīgi zināt!)
10. Ja būtu risinājums X, vai būtu gatavi to izmēģināt 4 nedēļas ar vienu vai diviem auto? (Tikai beigās.)

### Pieraksta veidne (katrai intervijai)
- **Uzņēmums, auto skaits, kas runāja (loma).**
- **Dienas no piegādes līdz rēķinam:** __. **Programmas:** __.
- **3 lielākās sāpes (citāti):**
- **Pilotam:** jā / varbūt / nē. **Nākamais solis:**

## 7. Tehniskie principi

- **Izvēlamies to, ko jau protam.** 4 mēnešos nav laika mācīties jaunu ietvaru. Ieteikums
  (ja abiem der):
  - TypeScript;
  - viens tīmekļa ietvars (piem., Next.js) gan panelim, gan šofera PWA;
  - PostgreSQL;
  - Docker uz viena Hetzner servera.
- **Viens serveris, viena datubāze, viens repo.** Mikroservisus nelietojam.
- **Bezmaksas servisi, kur vien var:**
  - OpenRouteService maršrutiem (kravas auto profils);
  - OpenStreetMap kartēm;
  - Resend e-pastiem;
  - Sentry kļūdām.
- **Dati ir klienta nauda:** katru nakti rezerves kopija, šifrēts savienojums, piekļuve pēc lomām.
  Šofera atrašanās vieta tiek fiksēta **tikai** parakstīšanas brīdī, nevis visu laiku (GDPR; pirms komerciālas lietošanas pārbauda jurists).
- **e-CMR un rēķina dati "eFTI-ready":** lauki atbilst e-CMR standartam, lai vēlāk varētu
  pieslēgties sertificētai eFTI platformai.
- **Claude Max** kodēšanai (Claude Code), testiem, dokumentācijai. Arī interviju pierakstu
  apkopošanai.

## 8. Riski

| Risks | Pazīme | Ko darām |
|---|---|---|
| Pārvadātāji negrib mainīt ieradumus | Intervijās "mums viss ok" | Lēmuma punkts 1. mēneša beigās. Meklējam šaurāku sāpi (piem., tikai rēķini no CMR) |
| Šoferi nelieto lietotni | Pilotā e-CMR netiek aizpildīti | Maksimāli vienkāršs ekrāns, krievu valoda, apmācība uz vietas, pirmās nedēļas paralēli papīram |
| e-CMR juridiskais spēks | Pēc programmas jurists saka, ka vajag kvalificētu parakstu | Dokobit integrācija (izmaksas BUDZETS.md), vai sākumā e-CMR kā "kopija" blakus papīram |
| Grāmatvedības programmu dažādība | Katram klientam cita programma | v1 eksportē standarta Peppol XML + CSV. Integrācijas tikai tām programmām, ko lieto pilota klienti |
| Konkurenti (Planlogi, Impargo, grāmatvedības programmas ar e-rēķiniem) | Klients jau lieto ko līdzīgu | Mūsu priekšrocība: automātisks rēķins no piegādes, latviešu specifika, ātrs atbalsts latviski |
| Laiks: divi cilvēki, 4 mēneši | Nedēļas mērķi netiek izpildīti 2× pēc kārtas | Griežam funkcijas, nevis kvalitāti. Viss ārpus v1 saraksta paliek ceļa kartē |

## 9. Ko programmas laikā NEDARĀM

- Maršrutu optimizāciju
- Ceļa nodevu aprēķinu
- Atpakaļkravu meklēšanu
- Tahogrāfu
- Komandējumu deklarācijas
- Kabotāžu
- Dienas naudu
- Degvielas kartes
- CO2 atskaites
- Robežu rindas
- Apkopes atgādinājumus
- Klientu portālu
- Rentabilitātes analītiku
- GPS/kameras kasti
- eFTI sertifikāciju
- Savu Peppol piekļuves punktu

Tas viss paliek pieteikumā kā **ceļa karte pēc inkubatora**. Tas parāda, ka mērogs ir liels, bet
mēs apzināti sākam ar vienu lietu, ko izdarām labi.
