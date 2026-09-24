# Kursa — LU pre-incubation application

> Team **Kursa**: **Roberts Linards** (the user; LU, E-Bizness, bachelor) and **Roberts Kaņepons**
> (partner, aka "Matjas", GitHub Matjas01, same partner as DroneSim; LU, Finanšu menedžments,
> bachelor). Applying to the LU pre-incubation programme, track **"Idea to Impact"**, RIS3 area
> ICT (4 months; LU Inovāciju un akselerācijas centrs, ERAF project Nr. 1.1.1.7/1/25/A/005).
> **Application deadline: 2026-09-27 23:59.** Funding up to **€3,506 per team**; every budget
> line needs a 3-supplier price survey or a uniqueness justification and is reported afterwards.
> Also available: €280/month stipend per student, €5,000 Demo Day prize fund.
>
> **Source of truth for what we promise LU: the founders' own form
> [`Kursa_PieteikumaAnketa.docx`](Kursa_PieteikumaAnketa.docx)** (read 2026-09-24). Do not edit it
> unless the user asks. Everything else in this repo must follow it.
>
> (The folder is still called `ops-panel` from an earlier direction.)

## What Kursa is (from the form, 2026-09-24)

An AI platform for road-haulage companies that takes a load from request to invoice in one flow;
the dispatcher checks and approves instead of typing ("cilvēks apstiprina"). Works alongside the
company's existing tools (telematics, freight exchanges, accounting software).

1. **Order intake** — reads load requests from e-mails/PDFs/exchanges in any language → structured order
2. **Pricing** — route, tolls, fuel, margin → draft quote
3. **Planning** — suggests truck/driver (location, remaining hours, trailer type), sends the task
4. **Digital documents** — driver issues an eCMR on the phone or photographs the signed paper CMR
5. **Invoice** — generated on confirmed delivery in the customer country's e-invoice format
   (Latvian Peppol BIS 3.0, Norwegian EHF, via a certified Peppol provider); overdue reminders
6. **Compliance** — driver hours, cabotage, per diem, CO2 reports

- **Target:** Baltic SME hauliers, ~5–100 trucks, international, especially Baltic–Nordic
  corridor; users = owner (buyer), dispatcher (daily user), driver (phone). Secondary: small
  forwarders, Nordic forwarders/shippers working with Baltic carriers.
- **Market / expansion:** Baltics + Nordics first, then Poland and the rest of the EU; long-term a
  data-sharing space for carriers, forwarders and shippers (backhaul, emissions reporting).
- **Stated edges:** underserved SME segment; cross-border e-invoice formats (LV Peppol + NO EHF);
  works with existing tools; automation instead of data entry; local languages (LV/LT/RU/EN) and
  hands-on onboarding.
- **Method:** customer development — problem interviews with owners, dispatchers, accountants;
  **shadowing a dispatcher**; MVP starting with **1–2 functions that save the most** (not the whole
  platform); pilots with 2–3 carriers.

## Goals for the 4 months (identical to the form)

1. At least **15 interviews** with carriers **and forwarders** — confirm the main problems and
   willingness to pay.
2. **First prototype** of the platform's core functions (MVP = the 1–2 highest-saving functions).
3. **Start testing with 2–3 carriers** in real working conditions.
4. **Business model and pricing** based on the test results.

Pilot metrics named in the form: processing time per load, number of document errors, days from
delivery to invoice.

## Before the deadline (2026-09-27)

- [x] Team name — **Kursa**; track Idea to Impact; RIS3 ICT (in the form)
- [x] Personal data for both members (in the form)
- [ ] Form: **Kompetences, Pienākumi komandā, Motivācija, Ietekme uz izaugsmi** — empty for both
- [ ] Form: **Darba grafiks** (months 1–4, individual goals per member) — empty
- [ ] Form: declaration checkboxes (7) — not ticked yet
- [ ] **Budget no longer matches the form** — see below
- [ ] Decide on the factual claims flagged below
- [ ] Ask LU: is a uniqueness justification enough for Claude Max / Claude API credit? Programme dates?
- [ ] Both confirm they are currently matriculated students

### Budget vs the form

The budget in `pieteikums/` (`budzets.py` → the LU .xlsx, now saved by the user as
`pieteikums/Budzeta_veidlapa.xlsx`; €1,020.31: Claude Max 2×4 mo, VPS, .lv domain, Claude API €100)
was built for the narrower "CMR photo → invoice" idea. The form additionally names: map/route and
**toll data services** (e.g. TollGuru ~$80/mo), an **LLM for e-mail/order parsing** (more API use
than CMR-only), and a **certified Peppol provider** for LV Peppol/NO EHF sending. Which of these
the MVP needs depends on which 1–2 functions are chosen — decide with the user before changing
numbers.

### Factual claims in the form (checked 2026-09-24)

- ✅ Norway: mandatory B2B e-invoice **issuance from 2027-01-01** (EHF; receipt + digital
  bookkeeping 2030) — confirmed (vatcalc, Sovos, EY).
- ✅ Latvia B2B e-invoices 2028-01-01 (FM); ✅ eFTI: authorities must accept from 2027-07-09 via
  certified platforms (the form words this correctly — voluntary for hauliers); ✅ ViDA 2030.
- ✅ Nordic freight & logistics market **USD 76.38 bn (2025)** — Mordor Intelligence; note it is the
  whole logistics market, not TMS software spend.
- ⚠️ "~10% of European carriers work only with eCMR in 2026" — **no source found**; trans.info says
  eCMR is used in **<1% of operations**.
- ⚠️ "IRU: eCMR cuts document costs 3–4×" — not found as an IRU figure; trans.info reports ~70%
  lower document costs (€6.23 → €1.69 per document ≈ 3.7×, automotive survey). IRU's own figure:
  75–102 M working hours/year saved in Europe.

## History of the direction

- Option B (live operations map, drones, LoRa, search & rescue) — chosen first, parked 2026-09-23:
  [`ops-panel-option.md`](ops-panel-option.md).
- Option A (freight platform) chosen 2026-09-23: [`freight-platform-option.md`](freight-platform-option.md).
- **Decision #3 (Claude's proposal 2026-09-23: narrow to "CMR photo → invoice → paid") — NOT
  adopted.** The founders' form (2026-09-24) keeps the broad AI platform and narrows only the MVP
  (1–2 functions chosen after interviews). The competitor research behind the proposal stays
  valid and useful for the jury: [`TIRGUS_IZPETE.md`](TIRGUS_IZPETE.md) (Planlogi, Mapon, Dashdoc…).
- eFTI fact (checked 2026-09-23): voluntary for hauliers, mandatory only for authorities to accept.
  Don't let texts slip back to "carriers must digitise".

## Open questions / TODO

- [ ] Which 1–2 functions form the MVP? (decide after the first interviews; candidates in PLAN.md)
- [ ] Team split — the form's "Pienākumi komandā" is empty; proposal in PLAN.md
- [ ] Budget alignment with the form (above)
- [ ] Do we register an SIA now or later? (pilot agreements, invoicing customers)
- [ ] Legal (post-programme): GDPR for CMR photos and driver data; data-processing agreements
- [ ] Do we personally know any hauliers / forwarders? (first interview targets)
- [x] Local git repo exists (3 commits); GitHub remote — waiting for the user to create a private repo
- [ ] Shared checklist https://claude.ai/artifact/8Cufb9nBRmZk6ppiHixwkW still has the CMR-only
      tasks — update to the form's goals if the user wants
