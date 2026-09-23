# Tirgus izpēte: vai kaut kas līdzīgs jau eksistē?

> Veikta 2026-09-23. Rezultātā mainījās produkta fokuss (sk. PROJECT.md, lēmums #3).
> Visi avoti ir saraksta beigās.

## Īsā atbilde

**Jā, pilns produkts "TMS mazajiem pārvadātājiem" jau eksistē, arī Baltijā.** Tieši to, ko sākumā
plānojām (dispečera panelis, šofera lietotne, e-CMR, rēķins no piegādes), piedāvā vairāki
uzņēmumi. Viens no tiem ir Igaunijā, un otrs Rīgā ir populārs pārvadātāju vidū.

**Neaizņemta palikusi cita lieta.** e-CMR lieto **mazāk nekā 1%** pārvadājumu, un pārējie strādā ar
papīra CMR. Neatradām nevienu vienkāršu, Latvijai pielāgotu rīku, kas no parakstīta
**papīra** CMR foto izveido rēķinu un seko līdzi samaksai, turklāt nemainot šofera vai
dispečera ikdienas darbu.

## Konkurenti

### Pilni TMS mazajiem pārvadātājiem (tiešā konkurence sākotnējai idejai)
| Produkts | Valsts | Ko dara | Cena |
|---|---|---|---|
| **Planlogi** | Igaunija | TMS 5–100 auto parkam: dispečera panelis, e-CMR, šofera lietotne, ePOD, rēķins no izpildīta pasūtījuma | no €79/mēn. vai €45 par dispečera vietu |
| **Dashdoc** | Francija | TMS 5–50 auto parkam, e-CMR, rēķini | pēc pieprasījuma |
| **Impargo** | Vācija | TMS 10–50 auto parkam, ceļa nodevas, rēķini | publicēta |
| **Trans.eu** | Polija | kravu birža + TMS funkcijas, 21 000 pārvadātāju | pēc pieprasījuma |

### Latvijas telemātika
| Produkts | Ko dara | Nozīme mums |
|---|---|---|
| **Mapon** (Rīga) | GPS izsekošana, šofera lietotne, digitālās formas, e-CMR integrācija | Daudziem Latvijas pārvadātājiem tā jau ir ikdienā. **Šofera lietotni un GPS nebūvējam**, jo pārvadātājiem tās jau ir |

### e-CMR platformas
- **Privātās:** TransFollow, Pionira (50 000+ lietotāju ES), EDITEL, eCMR.cloud, TrucksOnTheMap.
- **Atvērtā koda:** Open Logistics Foundation / Dachser piedāvā bezmaksas atvērtā koda e-CMR.
- **Latvijas valsts:** plānoja e-CMR caur LVRTC (daļēji 2024.–2025., pilnībā no 2026. gada). Pašreizējais
  statuss **nav skaidrs**, un publiski pieejamu sistēmu neatradām.
- **Secinājums:** e-CMR **nebūvējam** paši. Ja klientam ir e-CMR, mēs to nolasām tāpat kā papīra CMR.

### CMR nolasīšana ar AI (OCR)
- **Kas ir:** Klippa, ABBYY, Koncile, Tiny IDP u.c. Tās ir **API izstrādātājiem un lieliem uzņēmumiem**,
  nevis gatavs rīks mazam Latvijas pārvadātājam.
- **Ko tas nozīmē mums:** tehnoloģija strādā. Mēs to izmantojam (Claude), bet vērtība ir visā plūsmā:
  foto → rēķins → grāmatvedība → samaksa.

### e-rēķini
- **Kas notiek tirgū:** Latvijas grāmatvedības programmas (Horizon, Jumis, Tildes Jumis u.c.) jau pielāgojas
  Peppol BIS 3.0 un VID prasībām.
- **Secinājums:** mēs **nesūtām** e-rēķinus paši un **nekļūstam** par e-rēķinu operatoru. Mēs sagatavojam rēķinu
  un nododam to klienta grāmatvedības programmai.

### Rēķinu finansēšana
- **Kas ir:** **Aria** jau piedāvā naudu ~24 h laikā pēc parakstītas e-CMR, integrējoties ar TMS caur API.
- **Ko tas nozīmē mums:** finansēšanu nebūvējam paši. Nākotnē to var pieslēgt kā partneri. Tas ir MoneyLab virziens.

## Pārbaudītie fakti, uz kuriem balstāmies

| Fakts | Statuss | Avots |
|---|---|---|
| B2B e-rēķini Latvijā obligāti no **2028-01-01** | ✅ Finanšu ministrija. Saeima termiņu pārcēla 05.06.2025. (Mans Jumis bloga "2026" ir novecojis) | FM |
| e-rēķini valsts iestādēm (B2G) no 2025-01-01, datu nodošana VID no 2026-01-01 | ✅ | FM |
| eFTI pārvadātājiem ir **brīvprātīgs**, obligāts tikai iestādēm no 2027-07-09 | ✅ | EUR-Lex |
| e-CMR lieto <1% pārvadājumu | ✅ | trans.info |
| Latvijā ~4 150 licencētu starptautisko pārvadātāju, ~22 000 licencētu kravas auto | ✅ 30.09.2025. | ATD |
| Latvijas pārvadātāji izmanto ~2 milj. CMR gadā, un e-CMR ietaupītu ~€4,50 uz vienu | ✅ (2022. g. aplēse) | Satiksmes ministrija |

## Ko tas maina mūsu produktā

| Bija plānots | Tagad | Kāpēc |
|---|---|---|
| Dispečera panelis | **Nebūvējam** | Planlogi, Dashdoc un Mapon to jau dara. Mums tas nav priekšrocība |
| Šofera lietotne ar e-CMR, parakstu, GPS | **Nebūvējam.** Tikai vienkārša foto augšupielāde (saite, PWA vai e-pasts) | Šoferim nav jāmācās jauna lietotne. Daudziem jau ir Mapon |
| Savs e-CMR | **Nebūvējam** | Ir bezmaksas atvērtā koda un valsts risinājumi |
| e-rēķinu sūtīšana (Peppol) | **Nebūvējam.** Eksportējam uz grāmatvedības programmu | Grāmatvedības programmas to jau dara |
| **Rēķins no CMR** | **Kodols:** foto → AI nolasa → rēķina melnraksts → apstiprina → grāmatvedībā | 99% pārvadājumu ir papīra CMR. Neviens to nedara vienkārši un latviski |
| **Maksājumu uzraudzība** | **Kodols:** termiņi, atgādinājumi, naudas plūsmas pārskats | Finanšu daļa, MoneyLab virziens |

Rezultāts ir **mazāks produkts**, kuru divi cilvēki 4 mēnešos var tiešām pabeigt. Tas **nekonkurē**
ar Planlogi un Mapon, bet var ar tiem sadarboties. Tas atbilst arī MoneyLab (finanšu tehnoloģijas).

## Kas vēl NAV pārbaudīts (to pārbauda intervijas un 1. mēnesis)

1. **Vai sāp tieši šī problēma?** Vai rēķinu izrakstīšana no CMR un gaidīšana uz papīriem pārvadātājam tiešām ir
   pietiekami sāpīga, lai par to maksātu?
2. **Kā CMR šodien nonāk birojā?** Vai šoferi jau tagad sūta CMR foto uz biroju (WhatsApp, e-pasts)? Ja jā, mūsu
   risinājums iekļaujas esošajā ieradumā.
3. **Vai AI izlasa ar roku rakstītu CMR?** Latvijas CMR bieži ir aizpildīti ar roku vairākās valodās. Tehniskais
   tests: **30 īstu CMR foto, mērķis ≥ 90% lauku pareizi.**
4. **Ko viņi jau lieto?** Cik no mazajiem pārvadātājiem jau lieto Planlogi, Mapon vai citu TMS ar rēķiniem?

## Avoti
- **Planlogi:**
  - [salīdzinājums "10 Best TMS for Small Carriers"](https://planlogi.com/eng/best-tms-software-small-carriers-europe)
  - [e-CMR un eFTI ceļvedis](https://planlogi.com/eng/ecmr-efti-2027-guide)
- **Mapon:**
  - [šofera lietotne](https://www.mapon.com/en/products/mapon-driver-app)
  - [digitālās formas](https://www.mapon.com/en/fleet-management-solutions/process-automation/digital-forms)
- **Trans.eu:** [cenrādis](https://www.trans.eu/en/price-list/)
- **e-CMR:**
  - [Pionira un Leviahub](https://www.leviahub.com/en/articoli-blog/leviahub-e-pionira-siglano-una-partnership-strategica-per-accelerare-ladozione-ecmr-in-europa)
  - [Open Logistics Foundation / Dachser](https://www.dachser.com/en/mediaroom/First-industry-ready-eCMR-software-legally-compliant-interoperable-and-freely-available-for-all-28461)
  - [trans.info: e-CMR 2026, <1%](https://trans.info/en/ecmr-in-2026-434860)
- **Latvijas valsts e-CMR:**
  - [Satiksmes ministrija](https://www.sam.gov.lv/lv/jaunums/latvija-ieviesis-musdienigu-elektronisko-starptautisko-kravas-parvadajumu-pavadzimi)
  - [LSM](https://www.lsm.lv/raksts/zinas/latvija/latvija-no-2024-gada-ieviesis-elektronisko-starptautisko-kravas-parvadajumu-pavadzimi.a458254/)
- **CMR OCR:**
  - [Klippa](https://www.klippa.com/en/ocr/logistics-documents/cmr-waybills/)
  - [ABBYY](https://www.abbyy.com/marketplace/assets/host/abbyy/document-skill/international-consignment-note-cmr/)
- **Rēķinu finansēšana:** [Aria](https://www.helloaria.eu/resources/which-invoice-financing-providers-pay-carriers-on-a-signed-ecmr/)
- **e-rēķini:**
  - [Finanšu ministrija](https://www.fm.gov.lv/lv/strukturets-elektroniskais-rekins)
  - [Horizon](https://www.horizon.lv/e-rekini)
  - [Mans Jumis](https://mansjumis.lv/blogs/efektivitate/e-rekinu-ieviesana-latvija-2026)
- **eFTI:** [EUR-Lex 2020/1056](https://eur-lex.europa.eu/eli/reg/2020/1056/oj/eng)
- **Tirgus apjoms:** [ATD "Autotransports Latvijā 2025"](https://www.atd.lv/sites/default/files/jaunumi/Autotransports%20Latvija%202025%20EN_v3_0.pdf)
