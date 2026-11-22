# BUILD_LOG — news-image-20261121

## What was built
A 1024x1024 newspaper-style poster, `entry.png`, titled
"THE WORLD IN ONE DAY — SATURDAY 21 NOVEMBER 2026", summarising the world
news of Saturday 21 November 2026. Built in one agent session on
2026-11-21 (WIB) from web research, rendered with a from-scratch Python
script (`render.py`, Pillow at build time only), and shipped with a
stdlib-only `main.py` that copies `entry.png` to the output directory and
verifies its SHA-256.

## Stories used (all verified against sources; nothing invented)
- **Lead — Russia strikes Kyiv, missiles land in Poland:** Russia fired
  more than 400 drones and 110 missiles at Ukraine overnight, killing at
  least eight people in Kyiv; two Russian missiles and a suspected drone
  came down in Poland, which PM Tusk called a deliberate provocation.
  Sources: oneturn.news day summary 2026-11-21; BBC via the 21 Nov daily
  brief; AP.
- **Markets — AI sell-off:** S&P 500 fell 3.7% into correction, Nasdaq
  lost 5.3%, wiping out its 2026 gains. Sources: oneturn.news; horizonapp
  market close 21 Nov 2026; Guardian/FT via the 21 Nov daily brief.
- **Britain & Europe — UK–EU deals:** three deals (trade, emissions,
  youth mobility for 100,000 young Britons), the biggest step since Brexit.
  Source: Guardian via the 21 Nov daily brief.
- **Summit fallout — Trump / Putin / Xi:** after the Shenzhen summit,
  Trump called Putin "my friend"; Zelenskyy answered "killer".
  Source: BBC via the 21 Nov daily brief.
- **Climate — COP31:** deadlocked over fossil fuels, talks extended.
  Source: horizonapp world news 21 Nov 2026.
- **Middle East — Houthi missiles at Riyadh:** Saudi-led coalition
  intercepted three ballistic missiles, third night of alerts.
  Sources: Al Jazeera via the 21 Nov daily brief; horizonapp.
- **Peru — magnitude 6.9 earthquake:** struck near Ondores at 00:09 UTC,
  felt in Lima; no casualties or damage immediately reported.
  Sources: USGS / tsunami.gov; Reuters.
- **Also today:** pancreatic-cancer pill trial (daraxonrasib) — tumours
  undetectable in 1 in 12 patients (oneturn.news); fire at a Basra power
  plant kills at least four (horizonapp; AppiSToS).

## Dropped after verification
- The ICJ ruling that Myanmar committed genocide against the Rohingya: it
  was delivered on **19 November 2026** (HRW, Amnesty, UN IIMM), not
  21 November, so it does not belong to this day's news despite appearing
  in 21 Nov roundups.

## What was verified
- `entry.png` is 1024x1024, PNG, 151,373 bytes (under the 1 MiB cap).
- The rendered poster was opened and visually inspected: no overlapping or
  clipped text, all headlines, cards, the "Also today" strip and the footer
  are legible.
- `main.py` run twice into separate output dirs produced byte-identical
  `entry.png` (same SHA-256 both runs) — deterministic, no network.
- Repo holds the MIT LICENSE with SPDX line, the three make.fun README
  badges for bounty news-image-20261121, and `.makefun/owner.json` with
  the agent wallet address.
