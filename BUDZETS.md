# Budžets: LU pirmsinkubācija (limits €3 506)

> Atjaunots 2026-09-23 pēc LU budžeta veidlapas un parauga un pēc produkta sašaurināšanas (PROJECT.md, lēmums #3). Iesniedzamā versija ir
> [pieteikums/Budzeta_veidlapa_AIZPILDITA.xlsx](pieteikums/Budzeta_veidlapa_AIZPILDITA.xlsx),
> ko ģenerē `pieteikums/budzets.py`. Summas mainām tur, un šī lapa ir kopsavilkums.

## LU noteikumi (no veidlapas un parauga)

- **Finansējums līdz €3 506 uz komandu** (apstiprināts 2026-09-23).
- **Trīs izmaksu kategorijas:**
  1. materiāli un pakalpojumi;
  2. individuālās konsultācijas (ekspertu atlīdzības). Tās drīkst iekļaut tikai tad, ja programmas mācību saturā tādas nav;
  3. mobilitāte (naktsmītnes pēc MK noteikumiem Nr. 969).
- **Katrai pozīcijai vajag tirgus izpēti:**
  - 3 piegādātāju cenas (ekrānšāviņš ar cenu bez PVN un ar PVN + saite);
  - vai 3 e-pasta piedāvājumi;
  - vai unikalitātes pamatojums.

  Izvēlas **zemāko cenu**.
- **Summas ar PVN.** PVN ir attiecināms (LU apstiprināja).
- Abonementi ir atļauti. Visu summu prasīt nav obligāti (LU apstiprināja).
- Finansējuma avots: "ES Fondi". Programmu finansē ERAF, projekts Nr. 1.1.1.7/1/25/A/005.

## Budžets

| # | Pozīcija | Piegādātājs (zemākā cena) | € ar PVN |
|---|---|---|---|
| **1.** | **Materiāli un pakalpojumi** | | |
| 1.1. | Claude Max 5x, 2 lietotāji × 4 mēn. (€90 + PVN = €108,90/mēn.) | Anthropic (unikalitāte) | 871,20 |
| 1.2. | VPS 4 vCPU / 8 GB, ES, 4 mēn. (€7,21 + PVN = €8,72/mēn.) | OVHcloud VPS-2 (vs Hetzner €41,08 + IPv4 (CX33 šobrīd nav pieejams), DigitalOcean ~€198) | 34,88 |
| 1.3. | .lv domēns, 1 gads (mazāk par gadu nevar) | Hostnet (vs nic.lv €14,52, VPSnet €25,40); jāpārbauda, vai €11,76 ir bez PVN | 14,23 |
| 1.4. | Claude API kredīts CMR foto nolasīšanai (~1 500 CMR × ~$0,064, Opus 5: $5/$25 par 1M tokenu) | Anthropic (unikalitāte) | 100,00 |
| **2.** | **Individuālās konsultācijas** | nav | 0,00 |
| **3.** | **Mobilitāte** | nav | 0,00 |
| | **Kopā** | | **1 020,31** |
| | Neizmantots līdz €3 506 | | 2 485,69 |

## Kas izņemts salīdzinājumā ar pirmo melnrakstu un kāpēc

| Izņemts | Iemesls |
|---|---|
| Testa telefons (€149,99) | Mums pašiem ir telefoni, un pilotā šoferi lieto savus. Vajadzētu 3 veikalu cenu salīdzinājumu, bet vērtība ir maza |
| Grāmatveža konsultācija (~€121) | MoneyLab ir finanšu tehnoloģiju mentori. Ekspertu atlīdzība atļauta tikai tad, ja programma to nenodrošina |
| Drukāti materiāli (~€40) | Maza vērtība, bet tāpat vajag 3 cenas |
| SIA dibināšana (€75) | Valsts nodeva neietilpst nevienā no 3 LU kategorijām |
| Jurists, 4 h (€387,20) | MVP izstrādei nav vajadzīgs: pilotā e-CMR lieto paralēli papīram. Juridiskos jautājumus pilota laikā risina mentori + DVI vadlīnijas; jurists pēc programmas, kad e-CMR aizstās papīru |
| Degviela, ~2 000 km (€264,18) | Intervijas notiek attālināti (telefons/Teams), klātienē tikai 2–3 pilota ieviešanas, ko samaksājam paši. Nav skaidrs, vai LU kompensē personīgā auto degvielu, un tas prasītu maršruta lapas |
| Rezerve (€180) | LU veidlapā rezerves pozīcijas nav. Katrai summai vajag cenu izpēti |

## Ja gribam izmantot vairāk (katrai pozīcijai vajag cenu izpēti)

| Papildinājums | + € | Vērtējums |
|---|---|---|
| Claude Max 20x 5x vietā (2 × 4 mēn.) | +871,20 | Tikai tad, ja 5x limiti traucē |
| Nozares pasākums (loģistikas konference vai izstāde, mobilitāte) | ? | Tur varētu satikt pārvadātājus. Jāatrod pasākums programmas laikā |
| Dokobit kvalificētie e-paraksti | ~€300 + mēn. maksa | Pēc programmas, ja jurists pasaka, ka tie vajadzīgi |

## Avoti (pārbaudīti 2026-09-23; ekrānšāviņi mapē `pieteikums/ekranuznemumi/`, veido `ekranuznemumi.py`)

- **Claude:**
  - [Claude API cenas](https://platform.claude.com/docs/en/about-claude/pricing) (Opus 5: $5 ievade / $25 izvade par 1M tokenu; CMR foto ~5 300 ievades + ~1 500 izvades tokenu ≈ $0,064)
  - [Claude pricing](https://claude.com/pricing)
  - [Claude EUR cenas](https://www.kirstenbiema.com/en/blog/was-kostet-claude/)
- **Serveri:**
  - [OVHcloud VPS (oficiālā lapa)](https://www.ovhcloud.com/en-ie/vps/). Iepriekšējā cena €5,52 no trešās puses bloga bija kļūdaina
  - [Hetzner cenas no 15.06.2026](https://docs.hetzner.com/general/infrastructure-and-availability/price-adjustment/)
  - [DigitalOcean](https://www.digitalocean.com/pricing/droplets)
- **Domēni:**
  - [Hostnet](https://hostnet.lv/en/domains/)
  - [nic.lv](https://www.nic.lv/lv/buj-maksa-un-norekini)
  - [VPSnet](https://www.vpsnet.com/en/services/domains/lv)
- **Jurists (izņemts, atsaucei):** [juristspalidz.lv cenrādis](https://www.juristspalidz.lv/cenas/) (€80/h klātienē, €45/h attālināti, bez PVN)
- **Degviela (izņemta, atsaucei; 23.09.2026.):** [Circle K](https://www.circlek.lv/degvielas-cenas), [Viada](https://www.viada.lv/zemakas-degvielas-cenas/), [Virši](https://www.virsi.lv/lv/privatpersonam/degviela/degvielas-un-elektrouzlades-cenas). Neste cenas tiešsaistē nepublicē. Agrāk: [LSM 09.09.2026](https://www.lsm.lv/raksts/zinas/ekonomika/09.09.2026-degvielas-cenas-tuvojas-rekordiem-ipasi-strauji-sadardzinajusies-dizeldegviela.a662522/)
- **Alternatīvie AI rīki (ja LU prasa salīdzinājumu, nevis unikalitāti):**
  - [ChatGPT Pro $100/$200](https://www.aipricing.guru/chatgpt-subscription-pricing/)
  - [Cursor Pro+ $60, Ultra $200](https://cursor.com/pricing)
