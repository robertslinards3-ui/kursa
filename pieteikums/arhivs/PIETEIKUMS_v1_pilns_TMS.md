# LU pirmsinkubācijas pieteikums: teksta avots

> Šis ir pieteikuma veidlapas ([Pieteikuma_Anketa.docx](Pieteikuma_Anketa_AIZPILDITA.docx))
> teksts pa sadaļām. Labojumus veic šeit, tad pārģenerē .docx (`python aizpildit.py`).
> `[KVADRĀTIEKAVĀS]` ir lauki, kas jāaizpilda jums pašiem.

## Programmas virziens
Tematiskā finanšu tehnoloģiju pirmsinkubācijas programma "MoneyLab"

## Komandas nosaukums
[KOMANDAS NOSAUKUMS]

## RIS3 joma
Informācijas un komunikācijas tehnoloģijas

## Kopsavilkums un mērķi
Veidojam tīmekļa platformu maziem kravu autopārvadātājiem (5–50 kravas automašīnas). Tā vienā plūsmā savieno trīs lietas: kravu dispečerizāciju, elektronisko CMR pavadzīmi (e-CMR) un rēķinu izrakstīšanu. Kad kravas saņēmējs šofera telefonā paraksta e-CMR, sistēma uzreiz sagatavo rēķinu strukturētā e-rēķina formātā (Peppol BIS Billing 3.0) un seko līdzi tā apmaksai. Pārvadātājs naudu saņem par nedēļām ātrāk, nevajag gaidīt, kamēr papīra CMR nonāk birojā. Turklāt uzņēmums jau laikus ir gatavs obligātajiem B2B e-rēķiniem, kas Latvijā stājas spēkā 2028. gada 1. janvārī.

Mērķi četru mēnešu programmā:
1. Validēt problēmu: 15 intervijas ar pārvadātāju īpašniekiem, dispečeriem un grāmatvežiem.
2. Izstrādāt MVP ar četrām daļām:
   - dispečera panelis;
   - šofera lietotne (PWA) ar e-CMR, parakstu un foto;
   - automātisks rēķins no parakstītas piegādes;
   - maksājumu atgādinājumi.
3. Pilots ar 2–3 pārvadātājiem, izmantojot reālas kravas.
4. Izmērīt, cik dienu paiet no piegādes līdz rēķinam. Mērķis ir samazināt šo laiku no 5–15 dienām līdz 0–1 dienai.
5. Iegūt vismaz vienu rakstisku apliecinājumu par gatavību maksāt (LOI) un izstrādāt biznesa modeli.

## Idejas aktualitātes pamatojums
- **Obligāts termiņš.** No 2028. gada 1. janvāra Latvijā B2B darījumos būs obligāti strukturēti e-rēķini (Peppol BIS 3.0), un to dati būs jāziņo VID. Šis termiņš attiecas uz visiem uzņēmumiem. Latvijā ir ~4 150 licencētu starptautisko kravu pārvadātāju un ~22 000 licencētu kravas transportlīdzekļu (ATD dati uz 30.09.2025.).
- **Juridiskais pamats jau ir.** Latvija ir ratificējusi CMR konvencijas papildprotokolu par elektronisko pavadzīmi, tāpēc e-CMR ir tāds pats juridiskais spēks kā papīra CMR. No 2027. gada 9. jūlija ES dalībvalstu iestādēm būs jāpieņem elektroniska kravu informācija (eFTI regula 2020/1056). Uzņēmumiem tas ir brīvprātīgi, taču pāreja uz bezpapīra pārvadājumiem kļūst reāla.
- **Naudas plūsmas spiediens.** Degvielas cenas 2026. gada septembrī tuvojas vēsturiskajiem rekordiem, tāpēc peļņas marža ir zema. Papīra CMR ceļš no šofera līdz grāmatvedei aizkavē rēķinu par dienām vai nedēļām. Tam vēl pieskaitās 30–60 dienu apmaksas termiņš. Mazam uzņēmumam katra nokavēta nedēļa nozīmē apgrozāmos līdzekļus, kuru trūkst degvielai un algām.
- **Mazie pārvadātāji paliek bez rīkiem.** Lielās transporta vadības (TMS) sistēmas ir dārgas un sarežģītas, tāpēc mazie uzņēmumi strādā ar papīru, Excel un WhatsApp.

## Problēmas un risinājuma raksturojums
**Problēma.** Maza pārvadātāja ikdienā kravas ceļš līdz naudai ir sadrumstalots:
- dispečers pa telefonu izlemj, kurš auto brauc;
- šoferis vadā līdzi papīra CMR;
- parakstīto CMR uz biroju atved pēc dienām vai nedēļām, un dažreiz tas pazūd vai ir bojāts;
- grāmatvede datus pārraksta rēķinā ar roku;
- par kavētiem maksājumiem neviens sistemātiski neatgādina.

Sekas ir lēna naudas plūsma, dubults darbs, kļūdas un strīdi ar klientiem par piegādes faktu.

**Risinājums.** Viena platforma, kurā ir viss ceļš no kravas līdz naudai:
1. **Dispečera panelis.** Kravu ievade, auto un šofera piešķiršana, statusi reāllaikā.
2. **Šofera lietotne (PWA).** Atveras pārlūkā un nav jāinstalē no veikala. Tajā ir uzdevums, e-CMR aizpildīšana, saņēmēja paraksts uz ekrāna, foto iekraušanā un izkraušanā ar laika zīmogu un GPS paraksta brīdī. Lietotne strādā arī ar vāju internetu un ir pieejama latviešu un krievu valodā (vēlāk arī lietuviešu un ukraiņu).
3. **Automātisks rēķins.** Tiklīdz piegāde ir parakstīta, sistēma sagatavo rēķinu (PDF un Peppol BIS 3.0 XML) un eksportu grāmatvedības programmai.
4. **Maksājumu atgādinājumi.** Sistēma pati sūta atgādinājumus klientiem, kuri kavē apmaksu.

Parakstīta e-CMR ar foto un GPS ir arī pierādījums strīdos par piegādes faktu vai bojājumiem.

## Idejas esošās attīstības stadijas un potenciāla apraksts
**Stadija: ideja un sākotnējā izpēte.** Līdz šim esam izdarījuši:
- analizējuši regulējumu (e-rēķini 2028, e-CMR protokols, eFTI);
- apzinājuši konkurentus;
- izpētījuši izmaksas;
- sagatavojuši MVP apjomu un validācijas plānu.

Intervijas ar klientiem un programmēšana vēl nav sāktas, un tās ir programmas pirmais darbs. Komandai ir pieredze ātru prototipu izstrādē hakatonā (EUDIS).

**Potenciāls.**
- **Tirgus Latvijā.** Latvijā ir ~22 000 licencētu kravas transportlīdzekļu. Cena €30–80 par auto mēnesī nozīmē, ka jau 1% tirgus (~220 auto) dod €80 000–210 000 gada ieņēmumu. Ieņēmumi ir regulāri (abonements).
- **Izaugsme.** Nākamie soļi ir Lietuva un Igaunija, kur ir līdzīgs regulējums, ES e-rēķinu direktīva (ViDA) un eFTI.
- **Finanšu tehnoloģiju virziens (MoneyLab).** Parakstīta e-CMR un uzreiz izrakstīts rēķins ir uzticams pamats **rēķinu finansēšanai (faktoringam)**. Pārvadātājs varētu saņemt naudu jau piegādes dienā, un finansētājs redz pārbaudītu piegādes faktu. Šo virzienu vēlamies pārbaudīt ar MoneyLab mentoriem.

## Mērķa grupas apraksts
**Primārā mērķa grupa: Latvijas kravu autopārvadātāji ar 5–50 kravas automašīnām.** Tie parasti ir īpašnieka vadīti uzņēmumi. Īpašnieks bieži ir arī dispečers, un grāmatvedību kārto viens cilvēks vai ārpakalpojuma grāmatvede.
- **Pircējs:** īpašnieks vai vadītājs. Viņam svarīga ir naudas plūsma, mazāk papīru un gatavība 2028. gadam.
- **Lietotāji:**
  - dispečers: kravu plānošana;
  - šoferis: e-CMR un foto. Šoferu komandas bieži ir jauktas valodu ziņā (latviešu, krievu, ukraiņu, lietuviešu);
  - grāmatvede: rēķini un apmaksa.

**Sekundārā mērķa grupa:**
- ekspeditori ar apakšuzņēmēju auto parku;
- grāmatvedības biroji, kas apkalpo pārvadātājus. Tie ir arī pārdošanas kanāls, jo katrs apkalpo vairākus pārvadātājus.

## Tirgus stāvokļa apraksts, norādot uz sava risinājuma priekšrocībām
**Esošā situācija.** Lielākā daļa mazo pārvadātāju strādā ar papīra CMR, Excel, WhatsApp un atsevišķu grāmatvedības programmu, kas savā starpā nav saistīti.

**Konkurenti:**
- **Planlogi.** TMS Eiropas pārvadātājiem ar 5–100 auto, ar e-CMR un rēķiniem.
- **Impargo (Vācija).** Risinājums maziem pārvadātājiem, uzsvars uz ceļa nodevu aprēķinu.
- **Lielās TMS un telemātikas sistēmas.** Pārāk dārgas un sarežģītas uzņēmumam ar 10 auto.
- **Latvijas grāmatvedības programmas.** Pievieno e-rēķinu sūtīšanu, taču nav saistītas ar piegādes faktu.

**Mūsu priekšrocības:**
1. **Rēķins rodas no parakstītas piegādes.** Nav jāpārraksta dati un jāgaida papīri. Pārējie risinājumi sūta rēķinu, mēs to radām piegādes brīdī.
2. **Lokāla pielāgošana**, ko lielie spēlētāji nedara:
   - latviešu valoda;
   - Latvijas e-rēķinu un VID prasības;
   - eksports Latvijas grāmatvedības programmām;
   - šofera lietotne četrās valodās.
3. **Vienkārša ieviešana.** Lietotne strādā pārlūkā, nav jāpērk iekārtas, pirmo kravu var noformēt jau pirmajā dienā.
4. **Cena mazam uzņēmumam:** maksa par auto mēnesī, bez ieviešanas maksas.

Mēs neesam vienīgie. Tāpēc programmas pirmais darbs ir 15 intervijas: pārbaudīsim, vai tieši automātiska rēķina izrakstīšana ir pietiekami sāpīga problēma, lai par to maksātu.

## Pielietojamo metožu, tehnoloģiju un pasākumu apraksts
**Metodes:**
- **Klientu izpēte.** 15 daļēji strukturētas intervijas, pārsvarā attālināti pa telefonu vai videozvanā ("The Mom Test" pieeja: jautājam par pagātnes faktiem, nevis par hipotētisku vēlmi pirkt).
- **Lēmuma punkts.** Ja pēc 15 intervijām mazāk nekā 3 pārvadātāji piekrīt pilotam, mainām virzienu.
- **Prototipa pārbaude.** Pirms programmēšanas intervijās rādām klikšķināmu prototipu.
- **Pilots.** 2–3 pārvadātāji 4–6 nedēļas izmanto sistēmu paralēli papīram. Mērām:
  - dienas no piegādes līdz rēķinam;
  - e-CMR kvalitāti;
  - šoferu lietošanas biežumu.
- **Cenu un biznesa modeļa validācija.** Sarunas ar pilota klientiem un MoneyLab mentoriem.

**Tehnoloģijas:**
- tīmekļa platforma (TypeScript, PostgreSQL), mitināta ES datu centrā;
- šofera lietotne kā progresīvā tīmekļa lietotne (PWA) ar bezsaistes režīmu;
- e-CMR datu struktūra pēc UN/CEFACT e-CMR standarta un "eFTI-ready" datu modelis;
- e-rēķini pēc EN 16931 / Peppol BIS Billing 3.0 un PDF;
- OpenStreetMap un OpenRouteService kartēm un maršrutiem;
- izstrādē mākslīgā intelekta programmēšanas rīks (Claude Code). Tas ļauj divu cilvēku komandai uzbūvēt MVP četros mēnešos.

**Datu aizsardzība (VDAR/GDPR):**
- šofera atrašanās vieta tiek fiksēta tikai paraksta brīdī, nevis nepārtraukti;
- piekļuve pēc lomām, šifrēts savienojums, ikdienas rezerves kopijas.

**Pasākumi:**
- juridisko jautājumu (e-CMR paraksts, VDAR, pilota vienošanās) izvērtēšana ar programmas mentoriem un Datu valsts inspekcijas vadlīnijām. Pilotā e-CMR tiek lietots paralēli papīra CMR, tāpēc juridiskais risks pilota laikā ir zems;
- pilota līgumi ar pārvadātājiem;
- MoneyLab mentoru konsultācijas par biznesa modeli un rēķinu finansēšanu;
- dalība programmas Demo dienā.

## Komandas dalībnieks 1
- Vārds, uzvārds: [VĀRDS UZVĀRDS]
- Izglītības iestāde: [AUGSTSKOLA]
- Studējošā apliecības numurs: [NUMURS]
- Mācību programmas līmenis: [bakalaurs / maģistrs / ...]
- Telefona numurs: [TELEFONS]
- Mācību virziens: [PROGRAMMA]
- E-pasts: [E-PASTS]
- Kompetences: Zināšanas finansēs un grāmatvedībā: rēķini, naudas plūsma, nodokļi. [PAPILDINĀT: studiju virziens, darba pieredze, programmēšanas prasmes]. Pieredze tehnoloģiju projektos kopā ar komandas biedru.
- Pienākumi komandā: Produkts un klienti. Organizē klientu intervijas un pilotus, izstrādā rēķinu un grāmatvedības loģiku (automātiskais rēķins, Peppol XML, maksājumu atgādinājumi), veido biznesa modeli un cenas, atbild par budžetu un LU atskaitēm.
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
- Pienākumi komandā: Tehnoloģijas. Sistēmas arhitektūra, serveris un datubāze, dispečera panelis, šofera PWA (e-CMR, paraksts, foto, bezsaistes režīms), drošība un rezerves kopijas, izvietošana.
- Motivācija: [PIELĀGOT] Gribu būvēt programmatūru, ko reāli cilvēki izmanto ikdienas darbā, nevis tikai demonstrācijai. Loģistika ir Latvijas ekonomikai nozīmīga nozare, un tajā vēl ir daudz papīra darba, ko var automatizēt.
- Ietekme uz profesionālo izaugsmi: [PIELĀGOT] Pieredze pilna cikla produkta izstrādē: no arhitektūras līdz ražošanas videi ar reāliem klientiem. Darbs ar ES standartiem (e-rēķini, e-CMR) un datu aizsardzības prasībām.

## Starpdisciplinaritāte
Komandā apvienojas finanses un grāmatvedība ar programmatūras izstrādi. Produkta kodols ir rēķins, kas rodas no loģistikas notikuma, tāpēc tam vajadzīgas abas kompetences.

## Darba grafiks

### 1. mēnesis
**Rezultāts:** problēma validēta (15 intervijas), pieņemts lēmums par turpināšanu, ir klikšķināms prototips, gatavs tehniskais pamats.

**Darbs:**
**Dalībnieks 1:**
- 40 pārvadātāju kontaktu saraksts;
- 10 intervijas;
- interviju apkopojums;
- juridiskie jautājumi (e-CMR, VDAR) ar programmas mentoriem.
**Dalībnieks 2:**
- 5 intervijas (pirmās 3 kopā);
- arhitektūra, repozitorijs, serveris, datubāze;
- klikšķināms prototips intervijām.

### 2. mēnesis
**Rezultāts:** MVP kodols darbojas (kravas ievade → e-CMR ar parakstu → rēķins), ir vienošanās ar 3 pilota pārvadātājiem.

**Darbs:**
**Dalībnieks 1:**
- rēķina ģenerēšana (PDF + Peppol BIS 3.0 XML);
- pilota līgumi.
**Dalībnieks 2:**
- dispečera panelis;
- šofera PWA ar e-CMR, parakstu, foto un bezsaistes režīmu.

### 3. mēnesis
**Rezultāts:** pirmie pilota pārvadātāji izmanto sistēmu ar reālām kravām, darbojas maksājumu atgādinājumi.

**Darbs:**
**Dalībnieks 1:**
- pilota klientu apmācība;
- maksājumu atgādinājumi;
- rezultātu mērīšana.
**Dalībnieks 2:**
- labojumi pēc pilota atsauksmēm;
- latviešu un krievu valoda;
- drošība un rezerves kopijas.

### 4. mēnesis
**Rezultāts:** 2–3 piloti ar izmērītiem rezultātiem, vismaz 1 LOI, biznesa modelis, uzstāšanās Demo dienā.

**Darbs:**
**Dalībnieks 1:**
- cenu sarunas;
- biznesa modelis (arī rēķinu finansēšanas virziens);
- Demo dienas prezentācija;
- LU atskaite.
**Dalībnieks 2:**
- demo video;
- tehniskā dokumentācija;
- stabilitātes uzlabojumi.
