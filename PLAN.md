# Darba plāns: "CMR foto → rēķins → samaksāts" (LU pirmsinkubācija)

> Kā mums abiem (tev un Robertam) rīkoties 4 mēnešu LU programmā (MoneyLab).
> - **Kāpēc produkts ir tieši tāds:** [TIRGUS_IZPETE.md](TIRGUS_IZPETE.md)
> - **Lēmumi un atvērtie jautājumi:** [PROJECT.md](PROJECT.md)
> - **Nauda:** [BUDZETS.md](BUDZETS.md)
> - **Pieteikuma faili:** [pieteikums/IESNIEGSANA.md](pieteikums/IESNIEGSANA.md)
>
> Iepriekšējais plāns (pilns TMS) ir `pieteikums/arhivs/PLAN_v1_pilns_TMS.md`.

## 1. Ko gribam sasniegt programmas beigās (4. mēnesis, Demo diena)

| Mērķis | Skaitlis |
|---|---|
| Intervijas ar pārvadātājiem (5–50 auto) | **15** |
| Īsti CMR foto, uz kuriem pārbaudīta AI nolasīšana | **30**, ≥ 90% lauku pareizi |
| Pārvadātāji, kas pilotā lieto rīku ar reāliem pārvadājumiem | **2–3** |
| Dienas no piegādes līdz rēķinam pilota klientiem | no **5–15 → 0–1** |
| Laiks viena rēķina sagatavošanai | no **~10 min → < 2 min** (pārbaudīsim intervijās) |
| Rakstisks apliecinājums par gatavību maksāt (LOI vai priekšapmaksa) | **≥ 1** |

## 2. Divi lēmuma punkti (1. mēneša beigās)

Programmēšanā ieguldāmies tikai tad, ja abi ir izieti.

| | Nosacījums | Ja neizdodas |
|---|---|---|
| **Klientu punkts** | ≥ 3 no 15 pārvadātājiem piekrīt bezmaksas pilotam | Apstājamies. Izvērtējam, kura sāpe intervijās bija lielākā, un maināmies uz to |
| **Tehniskais punkts** | Claude pareizi nolasa ≥ 90% rēķinam vajadzīgo lauku 30 īstos CMR foto | Rīks kļūst par "palīgu ievadei": AI aizpilda, ko var, un cilvēks pārbauda. Tas joprojām ir noderīgi, taču vēstījums ir vājāks |

## 3. Lomas

| | Tu: produkts, klienti, finanses | Roberts: tehnoloģija |
|---|---|---|
| Galvenā atbildība | Intervijas, CMR foto vākšana, pilota klienti, rēķinu loģika, biznesa modelis, LU atskaites un izdevumu žurnāls | Arhitektūra, serveris, CMR nolasīšana ar AI un tās precizitātes tests, augšupielāde, drošība |
| Kodē arī | Rēķina ģenerēšana, eksports grāmatvedībai, maksājumu atgādinājumi | Apstiprināšanas ekrāns, datubāze, izvietošana |
| Kopā | Pirmās 3 intervijas ejam abi. Roberts dzird problēmu pats, un tehniskos jautājumus var uzdot uzreiz. |

Princips: **katram ir sava joma, par kuru viņš atskaitās.** Ja Roberts ir stiprāks citur, lomas pielāgojam.

## 4. Darba ritms

- **Pirmdienās 1 h sanāksme:**
  1. Ko izdarījām?
  2. Ko darām šonedēļ?
  3. Kas traucē?
- **Uzdevumu dēlis:** GitHub Projects. Katram uzdevumam ir viens atbildīgais.
- **Lēmumi:** ierakstām PROJECT.md tajā pašā dienā.
- **Izdevumu žurnāls (LU!):**
  - mape `izdevumi/`: tabula (datums, kas, summa, BUDZETS.md pozīcija, kurš maksāja) un rēķinu PDF;
  - rēķinu iegrāmatojam tajā pašā dienā, kad maksājam;
  - mēneša beigās salīdzinām ar BUDZETS.md.
- **Intervijas:**
  - pieraksti uzreiz pēc sarunas pēc veidnes (6. sadaļa), mapē `intervijas/`;
  - CMR foto glabājam mapē `cmr-paraugi/` (privāti, ar atļauju, nekādā gadījumā ne publiskā repo).

## 5. Posmi

### 0. nedēļa: sagatavošanās (uzreiz pēc pieteikuma)
- [ ] Privāts GitHub repo, uzdevumu dēlis, izdevumu žurnāls
- [ ] Claude Max abiem (5x), Claude API konts ar kredītu
- [ ] 40 pārvadātāju saraksts (6. sadaļa)
- [ ] Abi piesakāmies LU stipendijai (€280/mēn.), ja atbilstam

### 1. mēnesis: validācija (klientu un tehniskā)
- **15 intervijas** (~4 nedēļā), pārsvarā pa telefonu vai Teams. Pirmajās 10 produktu nerādām.
- **Katrā intervijā palūdzam 2–3 parakstītu CMR foto** (var aizklāt cenas un vārdus). Mērķis ir 30 foto.
- **Tehniskais tests (Roberts):**
  - neliels skripts: CMR foto → Claude → strukturēti dati;
  - salīdzina ar pareizajām vērtībām, ko ievadām ar roku;
  - mēra precizitāti pa laukiem (sūtītājs, saņēmējs, vietas, datumi, krava, paraksts/zīmogs).
- **Juridiskie jautājumi:** mentori un Datu valsts inspekcijas vadlīnijas. Tēmas: CMR foto satur trešo personu datus, vajag datu apstrādes vienošanos.
- **Mēneša beigās:** abi lēmuma punkti (2. sadaļa).

### 2. mēnesis: MVP
Secība ir svarīga. Katrs solis ir lietojams pats par sevi:
1. **Augšupielāde:** saite telefonā (PWA) → foto; vai e-pasta adrese, uz kuru pārsūta.
2. **Nolasīšana:** Claude nolasa CMR → apstiprināšanas ekrāns (foto blakus laukiem, labošana ar 1 klikšķi).
3. **Rēķins:**
   - klienti un tarifi (fiksēta cena, par km vai par kravu);
   - rēķina numerācija;
   - PDF;
   - eksports grāmatvedībai (Peppol BIS 3.0 XML un CSV). Vispirms tai programmai, ko lieto pirmais pilota klients.
4. **Iekšējais demo mēneša vidū.** Mēneša beigās pirmais pilota klients sāk lietot rīku paralēli savam ierastajam procesam.

### 3. mēnesis: pilots
- 2–3 pārvadātāji ar reāliem pārvadājumiem. Katru nedēļu īsa saruna ar katru.
- **Maksājumu uzraudzība:** termiņi, kavēto saraksts, automātiski atgādinājumi e-pastā.
- **Mērām:**
  - dienas no piegādes līdz rēķinam;
  - minūtes vienam rēķinam;
  - labotie lauki;
  - vai lieto bez atgādināšanas.

### 4. mēnesis: rezultāti un Demo diena
- Naudas plūsmas pārskats (kas cik parādā, kas nāks nākamnedēļ).
- Cenu sarunas → LOI vai priekšapmaksa.
- Saruna ar rēķinu finansēšanas partneri (piem., Aria vai Latvijas faktoringa uzņēmums): vai viņus interesē mūsu dati.
- Demo video: CMR foto → rēķins grāmatvedībā < 2 minūtēs.
- Demo dienas prezentācija, LU atskaite, lēmums par turpinājumu.

## 6. Intervijas

### Kur atrast pārvadātājus
1. **Personīgie kontakti:** radi, draugi, draugu uzņēmumi.
2. **Grāmatveži, kas apkalpo pārvadātājus.** Viņi paši pārraksta CMR rēķinos un pazīst daudzus klientus.
3. **firmas.lv / Lursoft:** NACE **49.41** (kravu autopārvadājumi), filtrs pēc darbinieku skaita.
4. **Nozares asociācijas** (piem., "Latvijas Auto"), Facebook/LinkedIn loģistikas grupas.

Sarakstā 40 kontakti, jo gaidām atsaucību ~40%.

### Jautājumi (neko nepārdodam, jautājam par pagātni)
1. Pastāstiet par pēdējo pārvadājumu no piegādes līdz naudai kontā. Kas notika katrā solī?
2. **Kā parakstītais CMR nonāk birojā?** Oriģināls kopā ar šoferi, foto WhatsApp, e-pastā? Pēc cik dienām?
3. Kas izraksta rēķinus? Kādā programmā? Cik minūšu aizņem viens? Cik rēķinu mēnesī?
4. Cik ilgi parasti paiet no piegādes līdz rēķinam? Un līdz samaksai? Cik bieži klienti kavē?
5. Kā šodien sekojat līdzi, kurš ir samaksājis? Kurš atgādina kavētājiem?
6. **Kādus rīkus jau lietojat** (Mapon, TMS, Excel, WhatsApp, grāmatvedības programma)? Ko esat mēģinājuši un atmetuši? Kāpēc?
7. Vai esat dzirdējuši par obligātajiem e-rēķiniem no 2028. gada? Ko plānojat darīt?
8. Kas jūsu darbā šobrīd sāp visvairāk? (Ja atbilde nav par rēķiniem, tas ir svarīgi zināt!)
9. *(Beigās)* Vai varat iedot 2–3 parakstītu CMR foto testam? (Cenas un vārdus var aizklāt.)
10. *(Beigās)* Ja rēķins būtu gatavs 2 minūtes pēc CMR foto, vai izmēģinātu to 4 nedēļas bez maksas?

### Pieraksta veidne
- **Uzņēmums, auto skaits, kas runāja (loma).** **Rīki:** __
- **CMR ceļš uz biroju:** __. **Dienas līdz rēķinam:** __. **Minūtes vienam rēķinam:** __
- **3 lielākās sāpes (citāti):**
- **CMR foto iedoti:** jā/nē (cik). **Pilotam:** jā / varbūt / nē. **Nākamais solis:**

## 7. Tehniskie principi

- **Izvēlamies to, ko jau protam.** Ieteikums: TypeScript, viens tīmekļa ietvars (piem., Next.js), PostgreSQL, Docker uz viena servera ES.
- **Viens serveris, viena datubāze, viens repo.** Nekādu mikroservisu.
- **AI:**
  - **Modelis:** Claude API ar attēlu analīzi. Pēc noklusējuma lielākais pieejamais modelis (Claude Opus 5).
  - **Izmaksas:** ~$0,06 par CMR (pārbaudīts 23.09.2026.).
  - **Rezultāts:** strukturēti dati pēc shēmas. Cilvēks **vienmēr** apstiprina, pirms rēķins aiziet.
- **Neveidojam paši to, kas jau eksistē:**
  - e-rēķinu nosūtīšana → grāmatvedības programma;
  - e-CMR → esošās platformas;
  - GPS un šofera lietotne → Mapon u.c.;
  - finansēšana → partneris.
- **Dati:**
  - CMR foto satur personas datus, tāpēc glabājam ES;
  - šifrēts savienojums, piekļuve pēc lomām, ikdienas rezerves kopijas;
  - CMR paraugi nekad nenonāk publiskā repo.

## 8. Riski

| Risks | Pazīme | Ko darām |
|---|---|---|
| Sāpe nav pietiekami liela | "Rēķinus izrakstām piektdienās, viss ok" | Klientu lēmuma punkts. Meklējam lielāko sāpi (piem., kavētie maksājumi) |
| AI slikti lasa rokrakstu | < 90% laukos | "Palīgs ievadei" režīms. Uzlabojam foto kvalitātes norādes |
| Pārvadātāji jau lieto Planlogi, Mapon u.c. ar rēķiniem | Intervijās bieži min šos rīkus | Mērķējam uz tiem, kam TMS nav. Izvērtējam integrāciju ar Mapon, nevis konkurenci |
| Grāmatvedības programmu dažādība | Katram klientam cita | Standarta Peppol XML + CSV. Integrācijas tikai pilota klientu programmām |
| Valsts e-CMR (LVRTC) sāk darboties | Ziņas SAM/LVRTC | Mums tas ir vēl viens avots, ko nolasīt. Rēķins un samaksa paliek mūsu daļa |
| Laiks: divi cilvēki, 4 mēneši | Nedēļas mērķi netiek izpildīti 2× pēc kārtas | Griežam funkcijas, nevis kvalitāti |

## 9. Ko programmas laikā NEDARĀM

- **Kodolam nevajadzīgais:**
  - dispečera panelis;
  - šofera lietotne ar GPS;
  - savs e-CMR;
  - sava e-rēķinu nosūtīšana (Peppol piekļuves punkts).
- **Plašākas TMS funkcijas:**
  - maršruti;
  - ceļa nodevas;
  - tahogrāfs;
  - dienas nauda;
  - CO2 atskaites;
  - klientu portāls;
  - rentabilitātes analītika;
  - dzelži (GPS/kameras kaste).
- **Finanšu partnera darbs:** paša rēķinu finansēšana.

Tas viss paliek pieteikumā kā **ceļa karte**. Sākam ar vienu lietu un izdarām to labi.
