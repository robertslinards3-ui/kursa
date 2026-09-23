# LU pirmsinkubācijas pieteikums: teksta avots

> Šis ir pieteikuma veidlapas ([Pieteikuma_Anketa.docx](Pieteikuma_Anketa_AIZPILDITA.docx))
> teksts pa sadaļām. Labojumus veic šeit, tad pārģenerē .docx (`python aizpildit.py`).
> `[KVADRĀTIEKAVĀS]` ir lauki, kas jāaizpilda jums pašiem. Iepriekšējā versija (pilns TMS)
> ir mapē `arhivs/`. Kāpēc versiju mainījām, sk. ../TIRGUS_IZPETE.md.

## Programmas virziens
Tematiskā finanšu tehnoloģiju pirmsinkubācijas programma "MoneyLab"

## Komandas nosaukums
[KOMANDAS NOSAUKUMS]

## RIS3 joma
Informācijas un komunikācijas tehnoloģijas

## Kopsavilkums un mērķi
Veidojam rīku maziem kravu autopārvadātājiem (5–50 kravas automašīnas). Tas saīsina ceļu no piegādes līdz naudai kontā. Šoferis vai birojs nofotografē parakstīto CMR pavadzīmi. Mākslīgais intelekts nolasa datus, un sistēma sagatavo rēķinu, nodod to uzņēmuma grāmatvedības programmai un seko līdzi samaksai. Rīks strādā ar papīra CMR, ko šodien izmanto lielākā daļa pārvadājumu, tāpēc šoferim un dispečeram nav jāmaina savs darbs.

Mērķi četru mēnešu programmā:
1. Validēt problēmu: 15 intervijas ar pārvadātāju īpašniekiem, dispečeriem un grāmatvežiem.
2. Tehniski pārbaudīt risinājumu: no 30 īstiem CMR foto pareizi nolasīt ≥ 90% rēķinam vajadzīgo lauku.
3. Izstrādāt MVP ar četrām daļām: CMR foto augšupielāde, datu nolasīšana, rēķins, maksājumu uzraudzība.
4. Pilots ar 2–3 pārvadātājiem, izmantojot reālus pārvadājumus. Izmērīt, cik dienu paiet no piegādes līdz rēķinam.
5. Vismaz 1 rakstisks apliecinājums par gatavību maksāt (LOI) un biznesa modelis.

## Idejas aktualitātes pamatojums
- **Papīrs joprojām dominē.** Elektronisko CMR (e-CMR) izmanto mazāk nekā 1% pārvadājumu. Latvijas pārvadātāji gadā aizpilda ap 2 miljoniem CMR pavadzīmju (Satiksmes ministrijas aplēse). Rēķinu var izrakstīt tikai tad, kad parakstītais CMR nonāk birojā.
- **Obligāti e-rēķini no 2028. gada 1. janvāra.** B2B darījumos Latvijā būs obligāti strukturēti e-rēķini, un to dati būs jāziņo VID (Finanšu ministrija). Pārvadātājiem tik un tā būs jāsakārto rēķinu process. Tas ir dabisks brīdis, kad pāriet uz jaunu rīku.
- **Naudas plūsmas spiediens.** 2026. gada septembrī degvielas cenas tuvojas rekordiem, tāpēc peļņas marža ir zema. Rēķins aizkavējas par dienām vai nedēļām, un tad vēl ir 30–60 dienu apmaksas termiņš. Mazam uzņēmumam tas nozīmē, ka trūkst naudas degvielai un algām.
- **Tirgus apjoms.** Latvijā ir ~4 150 licencētu starptautisko kravu pārvadātāju un ~22 000 licencētu kravas transportlīdzekļu (ATD, 30.09.2025.).

## Problēmas un risinājuma raksturojums
**Problēma.** Maza pārvadātāja naudas plūsmu bremzē papīrs:
- parakstītais CMR ceļo kopā ar šoferi un birojā nonāk pēc dienām vai nedēļām. Bieži vispirms atnāk tā foto WhatsApp (šo pieņēmumu pārbaudīsim intervijās);
- grāmatvede no CMR ar roku pārraksta datus rēķinā. Tas ir lēni, rodas kļūdas, un reizēm kāds CMR pazūd;
- par kavētiem maksājumiem neviens sistemātiski neatgādina, un īpašniekam trūkst pārskata, kurš cik ir parādā.

**Risinājums: "CMR foto → rēķins → samaksāts".**
1. **Foto augšupielāde.** Šoferis vai birojs nofotografē parakstīto CMR pa vienkāršu saiti telefonā (bez lietotnes instalēšanas) vai pārsūta to pa e-pastu. Der arī e-CMR PDF.
2. **Datu nolasīšana ar AI.** Mākslīgais intelekts (Claude) nolasa sūtītāju, saņēmēju, vietas, datumus, kravu un atzīmes par parakstiem un zīmogiem. Cilvēks vienā ekrānā apstiprina vai izlabo.
3. **Rēķins.** Rēķinu sagatavo no CMR datiem un klienta tarifa: PDF un eksports uzņēmuma grāmatvedības programmai (Peppol BIS 3.0 XML vai CSV). E-rēķinu nosūtīšanu un VID atskaiti veic grāmatvedības programma, ko uzņēmums jau lieto.
4. **Maksājumu uzraudzība.** Sistēma rāda apmaksas termiņus un kavēto rēķinu sarakstu, pati sūta atgādinājumus un parāda vienkāršu naudas plūsmas pārskatu.

## Idejas esošās attīstības stadijas un potenciāla apraksts
**Stadija: ideja un sākotnējā izpēte.** Līdz šim esam izdarījuši:
- analizējuši regulējumu (e-rēķini 2028, e-CMR protokols, eFTI);
- izpētījuši konkurentus Latvijā, Baltijā un ES. Tāpēc arī sašaurinājām produktu līdz daļai, ko neviens nedara;
- sagatavojuši MVP apjomu un divus lēmuma punktus: klientu un tehnisko.

Intervijas un programmēšana vēl nav sāktas. Tās ir programmas pirmais darbs. Komandai ir pieredze ātru prototipu izstrādē hakatonā (EUDIS).

**Potenciāls:**
- **Ieņēmumi.** Latvijā ir ~22 000 licencētu kravas auto. Plānotā cena ir €15–25 par auto mēnesī vai maksa par apstrādātu CMR. Jau 1% tirgus (~220 auto) dod ~€40 000–66 000 gadā, un ieņēmumi ir regulāri.
- **Izaugsme.** Lietuvā un Igaunijā ir tāda pati CMR un e-rēķinu problēma.
- **Finanšu tehnoloģiju virziens (MoneyLab).** Uzreiz izrakstīts rēķins ar pievienotu parakstītu CMR ir laba bāze **rēķinu finansēšanai**: pārvadātājs varētu saņemt naudu piegādes dienā. Šādi finansētāji jau pastāv (piem., Aria), tāpēc to plānojam kā partnerību, nevis kā savu produktu.

## Mērķa grupas apraksts
**Primārā mērķa grupa: Latvijas kravu autopārvadātāji ar 5–50 kravas auto, kas strādā ar papīra CMR.** Tie parasti ir īpašnieka vadīti uzņēmumi, un rēķinus kārto viens cilvēks vai ārpakalpojuma grāmatvede.
- **Pircējs: īpašnieks.** Viņam svarīga ir ātrāka nauda un mazāk papīru.
- **Lietotāji:**
  - grāmatvede vai birojs: rēķini un apmaksa;
  - šoferis: tikai nofotografē CMR.

**Sekundārā mērķa grupa: grāmatvedības biroji, kas apkalpo vairākus pārvadātājus.** Tiem ir tā pati sāpe, reizināta ar klientu skaitu. Tie ir arī pārdošanas kanāls.

## Tirgus stāvokļa apraksts, norādot uz sava risinājuma priekšrocībām
**Kas jau eksistē (izpēte 23.09.2026.):**
- **Pilnas transporta vadības (TMS) sistēmas mazajiem pārvadātājiem:**
  - Planlogi (Igaunija, no €79 mēnesī);
  - Dashdoc (Francija);
  - Impargo (Vācija);
  - Trans.eu (Polija).

  Tām ir dispečera panelis, šofera lietotne, e-CMR un rēķini. Taču tās prasa, lai viss uzņēmums pārietu uz jaunu sistēmu un e-CMR.
- **Mapon (Rīga):** GPS, šofera lietotne un digitālās formas. Daudziem Latvijas pārvadātājiem tas jau ir ikdienā.
- **e-CMR platformas:** TransFollow, Pionira un atvērtā koda risinājumi. Tās izmanto <1% pārvadājumu.
- **Dokumentu nolasīšanas (OCR) API:** Klippa, ABBYY. Tie ir rīki izstrādātājiem un lieliem uzņēmumiem, nevis gatavs risinājums mazam pārvadātājam.
- **Grāmatvedības programmas (Horizon, Jumis u.c.):** gatavojas e-rēķiniem, taču neko nezina par CMR.

**Mūsu vieta un priekšrocības:**
1. **Strādā ar papīru, ko lieto 99% pārvadājumu.** Nav jāmaina šofera un dispečera darbs vai jāievieš jauna TMS. Pietiek ar foto.
2. **Papildina, nevis aizstāj.** Rīks strādā kopā ar grāmatvedības programmu, ko uzņēmums jau lieto, un var strādāt blakus Mapon vai TMS.
3. **Pielāgots Latvijai:**
   - latviešu valoda;
   - Latvijas e-rēķinu un VID prasības;
   - eksports Latvijas grāmatvedības programmām;
   - CMR nolasīšana latviešu, krievu un lietuviešu valodā.
4. **Mazs un lēts ieviešanai.** Pirmo rēķinu var sagatavot jau pirmajā dienā.

Neesam pārliecināti, ka problēma ir pietiekami sāpīga, lai par to maksātu. Tāpēc programmas pirmais darbs ir 15 intervijas ar skaidru lēmuma punktu.

## Pielietojamo metožu, tehnoloģiju un pasākumu apraksts
**Metodes:**
- **Klientu izpēte.** 15 daļēji strukturētas intervijas, pārsvarā attālināti ("The Mom Test" pieeja: jautājam par pagātnes faktiem, nevis par hipotētisku vēlmi pirkt).
- **Klientu lēmuma punkts.** Ja mazāk nekā 3 no 15 pārvadātājiem piekrīt bezmaksas pilotam, mainām virzienu.
- **Tehniskais lēmuma punkts.** No interviju dalībniekiem savācam 30 īstu CMR foto. Ja AI nolasa < 90% lauku, rīku veidojam kā "palīgu ievadei", nevis pilnu automātiku.
- **Pilots.** 2–3 pārvadātāji 4–6 nedēļas. Mērām:
  - dienas no piegādes līdz rēķinam;
  - cik laika aizņem viena rēķina sagatavošana;
  - cik lauku bija jālabo ar roku.
- **Biznesa modeļa un cenas validācija.** Sarunas ar pilota klientiem un MoneyLab mentoriem.

**Tehnoloģijas:**
- tīmekļa lietotne (TypeScript, PostgreSQL), mitināta ES datu centrā;
- telefona augšupielāde kā progresīvā tīmekļa lietotne (PWA), bez instalēšanas;
- CMR nolasīšana ar Claude API (attēlu analīze, strukturēti dati);
- rēķini PDF formātā un eksports Peppol BIS 3.0 XML / CSV formātā;
- izstrādē AI programmēšanas rīks (Claude Code), kas ļauj divu cilvēku komandai paveikt MVP četros mēnešos.

**Datu aizsardzība (VDAR):** CMR satur trešo personu vārdus un parakstus. Tāpēc:
- dati glabājas ES;
- piekļuve ir pēc lomām;
- ar pilota uzņēmumiem slēdzam datu apstrādes vienošanos. Tās saturu izvērtēsim ar programmas mentoriem un pēc Datu valsts inspekcijas vadlīnijām.

**Pasākumi:** pilota vienošanās ar pārvadātājiem, MoneyLab mentoru konsultācijas (biznesa modelis, rēķinu finansēšana), dalība Demo dienā.

## Komandas dalībnieks 1
- Vārds, uzvārds: [VĀRDS UZVĀRDS]
- Izglītības iestāde: [AUGSTSKOLA]
- Studējošā apliecības numurs: [NUMURS]
- Mācību programmas līmenis: [bakalaurs / maģistrs / ...]
- Telefona numurs: [TELEFONS]
- Mācību virziens: [PROGRAMMA]
- E-pasts: [E-PASTS]
- Kompetences: Zināšanas finansēs un grāmatvedībā: rēķini, naudas plūsma, nodokļi. [PAPILDINĀT: studiju virziens, darba pieredze, programmēšanas prasmes]. Pieredze tehnoloģiju projektos kopā ar komandas biedru.
- Pienākumi komandā: Produkts un klienti. Organizē intervijas un pilotus, izstrādā rēķinu un grāmatvedības loģiku (rēķins no CMR datiem, eksports grāmatvedībai, maksājumu atgādinājumi), veido biznesa modeli un cenas, atbild par budžetu un LU atskaitēm.
- Motivācija: [PIELĀGOT] Gribu izveidot produktu, kas risina reālu, izmērāmu problēmu: naudas plūsmu mazajiem uzņēmumiem. Man interesē apvienot finanšu zināšanas ar tehnoloģijām. Obligātie e-rēķini 2028. gadā ir konkrēts brīdis, kad tirgum šāds risinājums būs vajadzīgs.
- Ietekme uz profesionālo izaugsmi: [PIELĀGOT] Praktiska pieredze klientu izpētē, produkta vadībā un biznesa modeļa veidošanā. Padziļinātas zināšanas par e-rēķiniem un finanšu tehnoloģijām. Pamats uzņēmuma dibināšanai.

## Komandas dalībnieks 2
- Vārds, uzvārds: Roberts [UZVĀRDS]
- Izglītības iestāde: [AUGSTSKOLA]
- Studējošā apliecības numurs: [NUMURS]
- Mācību programmas līmenis: [bakalaurs / maģistrs / ...]
- Telefona numurs: [TELEFONS]
- Mācību virziens: [PROGRAMMA]
- E-pasts: [E-PASTS]
- Kompetences: Programmatūras izstrāde un sistēmu integrācija. Pieredze EUDIS hakatonā: simulācijas vide ar ArduPilot un MAVLink protokolu. [PAPILDINĀT: valodas, ietvari, citi projekti]
- Pienākumi komandā: Tehnoloģijas. Sistēmas arhitektūra, serveris un datubāze, CMR foto augšupielāde un nolasīšana ar AI, nolasīšanas precizitātes testēšana, drošība un rezerves kopijas, izvietošana.
- Motivācija: [PIELĀGOT] Gribu būvēt programmatūru, ko reāli cilvēki izmanto ikdienas darbā, nevis tikai demonstrācijai. Loģistikā ir daudz papīra darba, un mūsdienu AI to var automatizēt.
- Ietekme uz profesionālo izaugsmi: [PIELĀGOT] Pieredze pilna cikla produkta izstrādē ar reāliem klientiem un praktiska AI (attēlu analīzes) izmantošana ražošanas vidē. Darbs ar ES standartiem (e-rēķini) un datu aizsardzības prasībām.

## Starpdisciplinaritāte
Komandā apvienojas finanses un grāmatvedība ar programmatūras izstrādi un AI. Produkta kodols ir rēķins, kas rodas no loģistikas dokumenta, tāpēc tam vajadzīgas abas kompetences.

## Darba grafiks

### 1. mēnesis
**Rezultāts:** 15 intervijas, 30 CMR foto, abi lēmuma punkti (klientu un tehniskais) izieti.

**Darbs:**
**Dalībnieks 1:**
- 40 pārvadātāju kontaktu saraksts;
- 10 intervijas;
- interviju apkopojums;
- CMR foto vākšana.
**Dalībnieks 2:**
- 5 intervijas (pirmās 3 kopā);
- CMR nolasīšanas tests ar 30 foto;
- arhitektūra, serveris, datubāze.

### 2. mēnesis
**Rezultāts:** MVP darbojas (foto → nolasīti dati → rēķins), ir vienošanās ar 3 pilota pārvadātājiem.

**Darbs:**
**Dalībnieks 1:**
- rēķina ģenerēšana un eksports grāmatvedībai;
- pilota vienošanās.
**Dalībnieks 2:**
- foto augšupielāde (PWA, e-pasts);
- AI nolasīšana un apstiprināšanas ekrāns.

### 3. mēnesis
**Rezultāts:** pilota pārvadātāji izmanto rīku ar reāliem pārvadājumiem, darbojas maksājumu uzraudzība.

**Darbs:**
**Dalībnieks 1:**
- pilota klientu ieviešana;
- maksājumu atgādinājumi;
- rezultātu mērīšana.
**Dalībnieks 2:**
- nolasīšanas precizitātes uzlabošana;
- labojumi pēc atsauksmēm;
- drošība un rezerves kopijas.

### 4. mēnesis
**Rezultāts:** 2–3 piloti ar izmērītiem rezultātiem, vismaz 1 LOI, biznesa modelis, uzstāšanās Demo dienā.

**Darbs:**
**Dalībnieks 1:**
- cenu sarunas;
- biznesa modelis (arī rēķinu finansēšanas partnerība);
- Demo dienas prezentācija;
- LU atskaite.
**Dalībnieks 2:**
- demo video;
- naudas plūsmas pārskats;
- tehniskā dokumentācija.
