# Freight platform — LU incubation application

> Two people (you + partner Roberts, aka "Matjas" — same partner as DroneSim), applying to the
> LU (University of Latvia) **pre-incubation programme** (4 months; organised by LU Inovāciju un
> akselerācijas centrs, ERAF project Nr. 1.1.1.7/1/25/A/005). **Application deadline:
> 2026-09-27 23:59.** Funding up to **€3,506** (expert fees, materials & services, mobility) —
> every euro must be justified with a 3-supplier price survey and reported afterwards.
> Also available: €280/month stipend per student, €5,000 Demo Day prize fund.
> This file is the decision record — update it as choices firm up.
>
> (The folder is still called `ops-panel` from the earlier direction; the project is now the
> freight platform.)

## Before the deadline (2026-09-27)

Submission kit is in [`pieteikums/`](pieteikums/) — checklist in
[`pieteikums/IESNIEGSANA.md`](pieteikums/IESNIEGSANA.md).

- [x] Application form draft — `pieteikums/PIETEIKUMS.md` → `Pieteikuma_Anketa_AIZPILDITA.docx`
      (`python aizpildit.py`); personal fields and `[PIELĀGOT]` texts still to fill
- [x] Budget draft in LU format — `pieteikums/Budzeta_veidlapa_AIZPILDITA.xlsx`
      (`python budzets.py`), €1,020.31 (Claude Max 2×4 months, server, domain, Claude API credit €100 for CMR extraction; lawyer and fuel dropped 2026-09-23); summary in [`BUDZETS.md`](BUDZETS.md)
- [x] Screenshots for the price surveys — `pieteikums/ekranuznemumi.py` (Playwright) → embedded
      by `budzets.py`; still to review, plus Claude billing-page screenshot at purchase
- [ ] Team name; both confirm they are currently matriculated students
- [x] €3,506 is per team (confirmed by user, 2026-09-23). Claude Max stays in the budget.
- [ ] Ask LU: is a uniqueness justification enough for Claude Max and the Claude API credit?
      Exact programme start/end dates?

LU confirmed (via user, 2026-09-23): subscriptions are eligible, VAT is eligible, requesting
less than the maximum is fine.

## The decision (2026-09-23)

**Chosen: Option A — freight platform for small Baltic hauliers.** Full spec in
[`freight-platform-option.md`](freight-platform-option.md). Execution plan in
[`PLAN.md`](PLAN.md).

Originally: a full TMS for a small haulier (dispatch → driver e-CMR → invoice). **Narrowed by
decision #3 below** to "CMR photo → invoice → paid" after competitor research.

Option B (live operations map for search & rescue, drones, LoRa trackers) was the earlier
choice. The team decided on 2026-09-23 to focus on A instead. B is parked, not deleted:
[`ops-panel-option.md`](ops-panel-option.md).

### Why A

- Clear buyers who pay monthly (~€30–80 per truck per month), realistic path to first revenue
  in 3–4 months.
- A hard regulatory deadline: **Latvian B2B structured e-invoicing (Peppol BIS 3.0) becomes
  mandatory on 2028-01-01**, including reporting invoice data to VID.
- Uses the user's finance background (invoicing, payment chasing, per diem).

### Correction to the original pitch (checked 2026-09-23)

The original pitch said carriers "must digitise twice in six months" (eFTI July 2027 + e-invoice
Jan 2028). **That's only half true.** The eFTI Regulation (EU 2020/1056) obliges *authorities*
to accept electronic freight data from 2027-07-09; for hauliers it is **voluntary** — they may
keep using paper. So the pitch must be:
- e-invoicing 2028 = **mandatory** deadline (the "must")
- eFTI / e-CMR = **opportunity** (paperless roadside checks, faster cash) — not an obligation
- Becoming a *certified* eFTI platform requires an accredited conformity assessment body
  (rules in Implementing Regulation (EU) 2025/2243). Out of scope for the incubator; design the
  data model to be "eFTI-ready" and decide later whether to certify or integrate with a certified
  platform.

Also: Latvian accounting software vendors will add e-invoicing themselves, so "we send
e-invoices" alone is not an edge. The edge is **invoice automatically from the signed delivery**,
plus local specifics (Latvian accounting integrations, per diem rules, LV/LT/RU/UA driver app).

## Decision #3 — PROPOSED, awaiting confirmation by both founders (2026-09-23): narrow the product

> Status: Claude's recommendation after competitor research. The user and Roberts have **not**
> confirmed it yet. If they reject it, restore the full-TMS texts from `pieteikums/arhivs/`.

**Read [`TIRGUS_IZPETE.md`](TIRGUS_IZPETE.md) first.** Short version:

- The original v1 (dispatch board + driver app + e-CMR + invoice-from-delivery) **already exists**,
  including next door: Planlogi (Estonia, 5–100 trucks, from €79/mo), Dashdoc, Impargo, Trans.eu;
  Mapon (Riga) already gives many Latvian carriers a driver app, GPS and e-CMR integration.
  "Same thing, but in Latvian" is not a defensible edge.
- But e-CMR is used in **<1%** of operations — paper CMR is the norm. Nobody offers a simple,
  Latvian-localised way to go from a **signed paper CMR** to an invoice and a tracked payment.
- Latvian accounting software (Horizon, Jumis, Tildes) is already doing Peppol/VID e-invoicing,
  so we don't send e-invoices ourselves — we hand the invoice to their accounting program.
- Invoice financing on signed delivery already exists (Aria, API-first) — a future partner, not
  something we build.

**New v1 = "CMR photo → invoice → paid".** The problem (slow cash from delivery to money) and the
target group (Latvian carriers, 5–50 trucks) are unchanged; the solution got smaller and sharper.

Alternatives considered and why not:
- *Keep the full TMS* — head-on with Planlogi/Mapon with no real edge; too big for 2 people × 4 months.
- *Build our own e-CMR* — free open-source (Open Logistics Foundation) and a planned state (LVRTC)
  solution exist; adoption is <1% anyway.
- *Go back to Option B* — not triggered; the freight problem is still real, only the wedge moved.

The v1 full-TMS texts are archived in `pieteikums/arhivs/`.

## Scope for v1 (the 4-month programme)

In:
- Capture: driver or office uploads a photo of the signed CMR (simple web link/PWA, or forward by
  e-mail) — works with paper CMR and with e-CMR PDFs
- Extraction: Claude (vision) reads the CMR fields (sender, consignee, places, dates, goods,
  signatures/stamps present, remarks) → structured data; human confirms/corrects in one screen
- Invoice draft from the CMR + the customer's rate → PDF + export to the carrier's accounting
  program (Peppol BIS 3.0 XML / CSV import) — we do **not** run our own Peppol access point
- Payment tracking: due dates, overdue list, automatic reminders, simple cash-flow view

Out (roadmap only): dispatch board, full driver app, GPS, own e-CMR, own e-invoice delivery,
route optimisation, tolls, backhaul, tachograph, posting declarations, cabotage, per diem, fuel
cards, CO2, customer portal, profitability analytics, hardware, eFTI certification, invoice
financing (partner later, e.g. Aria).

## Validation gates — do these before building much

- [ ] **Customer gate:** 15 interviews with small hauliers (5–50 trucks). If **fewer than 3 agree
      to a free pilot**, stop and rethink before the build weeks. Also learn: how does the CMR
      reach the office today (WhatsApp photos?), which tools they already use (Mapon, Planlogi…).
- [ ] **Technical gate:** collect **30 real signed CMR photos** from interviewees; Claude must read
      **≥ 90% of the invoice-relevant fields correctly**. If not, the product shifts to
      "assisted entry" (AI pre-fills, human types the rest) — still useful, weaker pitch.

## Open questions / TODO

- [x] Partner — Roberts ("Matjas"), same as DroneSim.
- [x] Program + deadline — LU pre-incubation, apply by 2026-09-27 23:59. Track: MoneyLab
      (fintech) recommended — invoicing, payment chasing, future invoice financing.
- [x] Direction — Option A (2026-09-23).
- [ ] Team split (proposal in `PLAN.md`) — decide after the application goes in.
- [x] LU budget rules — 3 categories, 3-supplier price survey per item, VAT and subscriptions
      eligible, €3,506 per team.
- [ ] Do we register an SIA now or later? (Needed to sign pilot agreements / invoice customers.)
- [ ] Legal (post-programme): GDPR for CMR photos (they contain names/signatures of third
      parties), data-processing agreement with carriers. No lawyer in the LU budget — mentors +
      DVI guidance during the pilot.
- [ ] Do we personally know any hauliers? (First interview targets.)
- [ ] GitHub repo — none yet; create a shared one when coding starts.
