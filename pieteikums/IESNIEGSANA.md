# Iesniegšana: kas jāizdara līdz 27.09. plkst. 23:59

Anketa: https://inovacijas.lu.lv/studentiem/programmas/pirmsinkubacijas-programma/pirmsinkubacijas-programmas-pieteikuma-anketa/

## Kas jāiesniedz (3 faili + anketas lauki)

| # | Fails | Statuss |
|---|---|---|
| 1 | Pieteikuma veidlapa (.pdf vai .docx) | Melnraksts ir `Pieteikuma_Anketa_AIZPILDITA.docx`. Jāaizpilda `[KVADRĀTIEKAVAS]`, jāpārlasa un jāsaglabā PDF |
| 2 | Budžeta veidlapa (.pdf vai .xlsx) | Melnraksts ir `Budzeta_veidlapa_AIZPILDITA.xlsx`, lapa "Budžeta lapa" |
| 3 | Excel ar budžeta pielikumiem (cenu aptaujas, ekrānšāviņi) | Tas pats .xlsx, pozīciju lapas 1.1–1.4 Ekrānšāviņi jau ielikti (23.09.2026.) |

Anketas laukos jāieraksta: vārds, uzvārds, e-pasts, tālrunis, komandas nosaukums, programmas virziens (**MoneyLab**) un apliecinājumu rūtiņas.

## Darāmo saraksts

### Jāizlemj abiem
- [ ] **Produkta fokuss:** "CMR foto → rēķins → samaksāts" (sk. ../TIRGUS_IZPETE.md). Ja nepiekrītat, iepriekšējā versija (pilns TMS) ir mapē `arhivs/`
- [ ] **Komandas nosaukums**
- [ ] **Virziens:** MoneyLab (ieteikums) vai Idea to Impact
- [ ] Vai abi pašlaik esat **matrikulēti studenti**? Tas ir obligāti visiem dalībniekiem.

### Pieteikuma veidlapa
- [ ] Katram: augstskola, studenta apliecības nr., līmenis, programma, tālrunis, e-pasts
- [ ] Pārrakstīt savos vārdos laukus "Kompetences", "Motivācija" un "Ietekme uz izaugsmi" (atzīmēti `[PIELĀGOT]`)
- [ ] Labot `PIETEIKUMS.md` → `python aizpildit.py` → pārlasīt .docx → saglabāt PDF

### Budžeta pielikumi

Ekrānšāviņi ir uzņemti automātiski (`python ekranuznemumi.py`, tad `python budzets.py`) un ielikti Excel. Katrā attēlā augšā ir saite un laiks.

- [ ] Atvērt Excel un pārskatīt visas 4 pozīciju lapas
- [ ] **1.1 Claude Max:** pie pirkuma pievienot norēķinu lapas ekrānšāviņu ar EUR cenu (vajag pieteikšanos kontā)
- [ ] **1.2 Serveris:** pārbaudīt, vai OVH VPS-2 cena €7,21 ir mēneša cena bez saistībām
- [ ] **1.3 Domēns:** Hostnet lapā nav norādīts, vai €11,76 ir ar vai bez PVN. Budžetā pieņemts: bez PVN
- [ ] Ja cenas mainās pirms iesniegšanas: palaist abus skriptus vēlreiz

### Iesniegšana
- [ ] Roberts pārlasa visu (26.09.)
- [ ] Iesniegt **27.09. līdz pusdienlaikam**, nevis pēdējā brīdī

## Jautājumi LU (e-pastā vai telefoniski, pirms iesniegšanas)

1. Kad programma sākas un beidzas (precīzi datumi)? Zināms tikai, ka tā ilgst 4 mēnešus.
2. Vai Claude Max un Claude API kredītam pietiek ar **unikalitātes pamatojumu**, vai vajag 3 piedāvājumu salīdzinājumu?
