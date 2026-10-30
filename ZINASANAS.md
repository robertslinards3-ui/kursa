# Kursa: zināšanu bāze un sesiju žurnāls

Šeit ir viss, ko Claude ir uzzinājis un pārbaudījis par Kursu. Augšējā daļa ir kopsavilkums, ko atjauno, kad kaut kas mainās. Apakšā ir **sesiju žurnāls**: pēc katras sesijas tam pievieno jaunu ierakstu, un vecos ierakstus nemaina.

Detaļas un avoti ir citos failos: [PROGRAMME.md](PROGRAMME.md) (programmas noteikumi), [PROJECT.md](PROJECT.md) (lēmumi), [PLAN.md](PLAN.md) (darba plāns), [BUDZETS.md](BUDZETS.md) (budžets), [TIRGUS_IZPETE.md](TIRGUS_IZPETE.md) (konkurenti).

Personas datus (personas kodu, IBAN, adresi) šeit neglabājam.

---

## 1. Komanda un produkts

- **Roberts Linards**: LU, E-bizness. Produkts, prototips, integrācijas, pilots.
- **Roberts Kaņepons** ("Matjas", GitHub Matjas01): LU, Finanšu menedžments. Finanses, biznesa modelis, LU atskaites.
- Abiem ir vārds Roberts, tāpēc tekstos lietojam uzvārdus.
- **Kursa** ir AI platforma Baltijas mazajiem un vidējiem pārvadātājiem (5–100 kravas auto, Baltijas un Ziemeļvalstu koridors). Plūsma: pasūtījums no e-pasta vai PDF → cenas aprēķins → plānošana → e-CMR vai CMR foto → rēķins klienta valsts e-rēķina formātā (LV Peppol, NO EHF) → atbilstība. Visu apstiprina cilvēks.
- **MVP ir tikai 1–2 funkcijas**, kas ietaupa visvairāk laika. Tās izvēlas pēc 15+ intervijām un dispečera ēnošanas.
- Avots ir komandas pašu anketa [Kursa_PieteikumaAnketa.docx](Kursa_PieteikumaAnketa.docx). Bez lūguma to nelabo.

## 2. Programma (LU pirmsinkubācija)

- **Uzņemti.** Anketā atzīmējām "Idea to Impact", bet LU ielika **MoneyLab** virzienā (finanšu tehnoloģijas). LU dokumentos rakstām MoneyLab.
- Programmas norise: **27.10.2026.–18.02.2027.** Nodarbības otrdienās un ceturtdienās 18:15–20:45, Zinātņu māja, telpa ALFA. Apmeklējums ir obligāts.
- Reizi nedēļā tikšanās ar darba vadītāju. Viņam jāapstiprina katrs nodevums, pirms to sūta LU.
- **Termiņi:**
  - 01.11. labotā anketa
  - 13.11. stipendijas pieteikums
  - 27.12., 27.01., 27.02. ikmēneša stipendijas atskaites
  - 14.01. starpposma atskaite, 21.01. starpposma prezentācija
  - 18.02. noslēguma atskaite (≥16/24 punkti), pēc tam Demo diena
- **Finansējums:** līdz €3 506 komandai. To administrē LU, naudu neizmaksā mums. Katrai izmaksai vajag 3 piedāvājumus vai unikalitātes pamatojumu. Izvēlas lētāko piedāvājumu, kas atbilst prasībām.
- **Godalgas MoneyLab virzienā:** €2 500, €1 500, €1 000.

### Stipendija (individuāla, nav automātiska)
- €280 mēnesī, ne vairāk kā 3 mēneši (no 27.11.2026.). Visos virzienos kopā ir 60 stipendijas.
- Pieteikums brīvā formā uz inovaciju.granti@lu.lv. Jānorāda vārds, personas kods, IBAN, deklarētā adrese, augstskola, virziens, studenta apliecības nr., e-pasts un tālrunis.
- Katru mēnesi vērtē 0–6 punktos, **jāsavāc vismaz 5**:
  1. Apmeklēti ≥75% tikšanos ar darba vadītāju.
  2. Paveiktais atbilst darba plānam pieteikumā.
  3. Darba vadītāja vērtējums par individuālo ieguldījumu.
- Neizšķirta gadījumā priekšroka ir RIS3 jomai (mums ir IKT), starpdisciplinārai komandai, tad izlozei vai agrākam pieteikumam.
- **Secinājums:** darba grafikā jāraksta tikai izpildāmi mērķi, ko var izmērīt. Tikšanos datumi jāpieraksta. Linards to dara lekciju žurnālā (Google Doc).

### 1. mēneša darba grafiks (27.10.–27.11.)
| Uzdevums | Atbildīgais |
|---|---|
| Intervijas jautājumu izstrāde | Linards |
| Klientu intervijas LV/LT/EE | Kaņepons organizē, intervē abi |
| E-rēķinu prasību analīze | Kaņepons (likumi, termiņi) un Linards (tehniskā puse: Peppol/EHF fails, piekļuves punkts) |
| Biznesa modelis un ieņēmumu avoti | Kaņepons |
| Programmatūras skices un darba plūsmas | Linards |

## 3. Pārbaudītie fakti

- **eFTI** pārvadātājiem ir brīvprātīgs. Iestādēm digitālie dati jāpieņem no 2027-07-09.
- **LV B2B e-rēķini** ir obligāti no 2028-01-01. **Norvēģijā** B2B e-rēķinu izrakstīšana ir obligāta no 2027-01-01.
- **e-CMR** izmanto mazāk nekā 1% pārvadājumu.
- **ATD dati:** Latvijā ir ~4 150 licencētu starptautisko pārvadātāju un ~22 000 kravas auto.
- **Bez avota:** anketas apgalvojumi "~10% tikai eCMR" un "IRU 3–4×". Kamēr nav avota, tos neatkārtojam.

## 4. Konkurenti

- **Pilnas TMS sistēmas jau pārdod** Planlogi, Mapon un Dashdoc. Tāpēc nebūvējam visu platformu.
- **Ybil** (Igaunija) ir tuvākais konkurents. Tas pats segments, digiCMR ar QR parakstu bez konta, TMS, rēķins pēc piegādes. Piedalījās eFTI pilotā EE–LV–LT, saņēma €150k no LatBAN Rīgā.
- **Kursas atšķirība no Ybil** (jāpārbauda viņu demo):
  - AI nolasa pasūtījumus no e-pastiem un PDF
  - cenas aprēķins ar ceļa nodevām
  - papīra CMR foto nolasīšana
  - e-rēķini Peppol un EHF formātā
  - latviešu, krievu un lietuviešu valoda
- **Partnerības iespēja:** pieslēgties Ybil API, nevis būvēt savu e-CMR.
- **Uzmanību:** Ybil mārketingā apgalvo, ka eFTI ir obligāts. Tas ir pārspīlēts, mēs to nekopējam.

## 5. Tehnoloģijas un cenas (pārbaudītas 2026. g. septembrī un oktobrī)

- **Claude API:** Opus 5 maksā $5/$25 par miljonu tokenu. Viens CMR foto izmaksā ~$0,06, viens e-pasts ~$0,02–0,05. Pirmajā mēnesī salīdzināt ar Sonnet 5 ($2/$10).
- **Serveris:** OVH VPS-2 €7,21 + PVN mēnesī. Ieteikts pāriet uz VPS-1 (€3,81). Cenas ņemt tikai no oficiālās lapas, jo bloga cena bija kļūdaina.
- **Ceļa nodevu API:**
  - PTV Developer (bez maksas līdz 100k transakcijām)
  - HERE (bez maksas līdz 5k maršrutiem)
  - TollCalc.eu (€25 mēnesī)
  - RouteCalc (no €14,99)
  - TollGuru ($80 mēnesī)
- **GPS trackeri:** Teltonika FMC130 vai FMC920 ar Traccar serveri. **MVP aparatūru nepērkam**: izmantojam esošo telemātiku (Mapon u. c.) vai šofera telefonu.
- **IoT SIM kartes:**
  - Tele2 M2M €3 par 500 MB
  - iot.cards
  - Onomondo €0,0025 par MB
  - 1NCE €12 par 500 MB uz visu kartes darbības laiku
  - melita.io €10 par 1 GB uz 10 gadiem

## 6. Budžets (iesniegtais)

| Pozīcija | € |
|---|---|
| Claude Max 5x, 2 lietotāji × 4 mēn. | 871,20 |
| OVH VPS-2, 4 mēn. | 34,88 |
| .lv domēns (Hostnet) | 14,23 |
| Claude API kredīts | 100,00 |
| **Kopā** | **1 020,31** |

- Neizmantotā daļa līdz limitam ir €2 485,69.
- Izņemtās pozīcijas un iemesli ir BUDZETS.md.
- Katram izdevumam vajag rēķinu izdevumu žurnālā.

## 7. Lēmumi un noteikumi

- Claude priekšlikums sašaurināt produktu līdz "CMR foto → rēķins" **netika pieņemts**.
- B variants (operāciju karte, droni, LoRa) ir **atlikts, bet nav atmests**: [ops-panel-option.md](ops-panel-option.md).
- **EUDIS hakatons vēl nav noticis.** To nekad neapraksta kā pieredzi.
- Cenu aptaujas ir godīgas. Dārgākus konkurentus nemeklējam, lai pamatotu vēlamo pirkumu.
- Bez lūguma neko neliekam repozitorijā (GitHub remote vēl nav). CV un personas dati git netiek pievienoti.

## 8. Atvērtie jautājumi

- Kas jālabo anketā līdz 01.11.? Vai jāmaina atzīmētais virziens uz MoneyLab?
- Kā sauc darba vadītāju?
- Vai Kaņepons arī piesakās stipendijai?
- Kuras 1–2 funkcijas būs MVP? Izlems pēc intervijām.
- Ybil demo: vai viņi jau nolasa pasūtījumus no e-pastiem?
- Vai budžeta serveri mainām uz VPS-1? Vai budžetā pievienojam ceļa nodevu API?

---

## Sesiju žurnāls

Pēc katras sesijas jāpievieno jauns ieraksts. Formāts: datums, kas izdarīts, kas uzzināts, kas palika atvērts.

### 2026-09-23/24: pieteikuma sagatavošana
- Sastādīts budžets LU formā ar cenu ekrānšāviņiem (budzets.py, ekranuznemumi.py). Izpētīti konkurenti. Uzrakstīts darba plāns.
- Visi faili saskaņoti ar komandas pašu anketu. Aizpildīti Linarda 4 lauki anketā.
- Izpētīti ceļa nodevu API, GPS trackeri un IoT SIM kartes. Sagatavots mentora sarunas dokuments. Atrastas viesnīcas Dohā (Web Summit Qatar, 31.01.–05.02.2027).

### 2026-10-19: Ybil izpēte
- Ybil pievienots TIRGUS_IZPETE.md kā tuvākais konkurents. Noformulēta Kursas atšķirība.

### 2026-10-28: stipendija
- No nolikuma noskaidroti stipendijas kritēriji (8. pielikums) un pieteikuma saturs (53. p.). Sagatavots pieteikuma e-pasta teksts.
- Uzzināts, ka komanda ir MoneyLab virzienā. CLAUDE.md, PROGRAMME.md un PROJECT.md atjaunoti.
- Saglabāta saite uz Linarda lekciju žurnālu (Google Doc, privāts; lai to lasītu, jāpieslēdz Google Drive).

### 2026-10-30: 1. mēneša darba grafiks
- Valodas labojumi 1. mēneša uzdevumiem. Uzdevumi sadalīti pa cilvēkiem (sk. 2. sadaļu). Izveidots šis fails.
- Atvērts: 2.–4. mēneša grafiks.
