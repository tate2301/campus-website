## The line (1 Oct 2026)
**A school management platform that puts people first.** Software for every department in your school, with one record at the centre.
- Category: cloud-based school management for K-12. One record per person; a single source of truth.
- "One system for the whole school." heads the department grid.
- Row headlines are verb-led claims (Veracross): "Keep working when the internet goes." "Connect the software your bursar already uses."

# Corelith Campus · voice

Written 1 Oct 2026 from refs/voice-ledger.md; drafted, then put through ux-writing (brief, review checklist) and sepia (professional pass, style pass §2–3, §5).

## The voice in one line
A colleague who has worked in a school office: plain, calm, exact about money, and specific about the school day.

## Five rules
1. **Prove local fit with detail.** Say EcoCash, ZiG, Form 3B, exeat, ZIMSEC and the end-of-term report. Never write "built for Zimbabwe", "local", "homegrown" or "African".
   - No: Built for how Zimbabwean schools run.
   - Yes: Fees in US dollars and ZiG, matched to each pupil.
2. **Start from the school day.** Open with what happens at school, then say what Campus does about it.
   - No: A unified platform for school operations.
   - Yes: Campus works without internet.
3. **One claim, one detail.** Each claim is followed by something a Head can check in a demo: a name, a figure, a screen.
   - No: Save hours every week.
   - Yes: You record a mark once and it appears on the report.
4. **Talk like a colleague.** Plain words and contractions. Speak to the person doing the job as "you", never "your teachers" or "your staff"; "we" is Corelith.
   - No: Empower your educators with seamless workflows.
   - Yes: You enter each mark once.
5. **Be exact about money.** The currency and both decimals, every time, and say what isn't charged.
   - No: Affordable pricing for every school.
   - Yes: US$1 per active pupil per month.

## Tone by reader
| Reader | Tone | Example |
|---|---|---|
| The Head | calm, accountable | Attendance, fees and open jobs are on one screen before assembly. |
| SDC and bursar | exact | 1,140 active pupils × US$1 = US$1,140 a month. The first month is free. |
| Teachers | time and fewer forms | You record a mark once. It shows on the report and on the parent's phone. |
| Parents | warm, about their child | Tanaka was in school all week and scored 71% in Mathematics. |

## Headlines
One claim per headline. Add a grey second line only when it states a fact the first line doesn't.
- One system for the whole school.
- Four portals. / One record behind them.
- Record a mark once. / Everyone sees the same one.

## Words
Use: internet (never "signal" or "the line"), Head, pupil, parent or guardian, term, Form 3B, bursar, bursary, exeat, SDC, register, report, portal, module, active pupil, EcoCash, ZiG.
Don't use: signal, principal, stakeholder, solution (as a noun), seamless, empower, unlock, transform, best-in-class, world-class, cutting-edge, AI-powered, magic, journey, extraordinary, built for Zimbabwe, homegrown, proudly local.

## Changed strings (ux-writing review)
| key | current | proposed | why |
|---|---|---|---|
| hero.h1b | Built for how Zimbabwean schools run. | From the morning register to the term report. | Rule 1: shows the span of the school day instead of claiming local fit |
| hero.body | Registers, marks, fees, boarding and payroll share one record, with a portal each for the office, the staffroom, parents and pupils. It takes US dollars and ZiG, uses ZIMSEC terms, and keeps working when the signal drops. | Teachers mark the register on a tablet. The bursar takes EcoCash and ZiG at the counter. Parents see both on their phone that evening, and Campus keeps working without internet. | Rule 2: starts from people doing their jobs; local fit carried by EcoCash and ZiG; feature list moved to the portals section |
| hero.body_phone | Registers, marks, fees, boarding and payroll share one record, with a portal for the office, the staffroom, parents and pupils. | Registers, fees and reports on one record. It keeps working without internet. | 320px budget; two short sentences |
| hero.pill | Corelith 1.0 is open | Corelith 1.0 is open | unchanged |

## Sepia check (executor Claude, version not in the fingerprint tables: Opus 5 and Fable 5.1 prose layers applied as priors)
- Vocabulary scan: no hits from the ban tables.
- Templates: removed a three-clause list from the old hero body; the new body is three sentences of different lengths, not three parallel clauses.
- Stance: each line commits to one claim.
- Mannered prose: none; no metaphor stands in for a literal phrase.
- Verdict: clean, ship.

## Rules from his edits (1 Oct 2026; read before writing any Campus copy)
| His edit | Rule |
|---|---|
| "the register works without internet. name things correctly" | Call things by the name a Head uses: internet, never "signal" or "the line" |
| "'as they are' doesn't add any value… find all copy like this" | Cut qualifiers and tails that add nothing ("as they are", "does all the work", "carries the words", "the bridge"). Every phrase must state a fact or a rule |
| "You record a mark once and it appears on the report." | A person does the action, in the active voice, with the plain verb (record, not "enter" or "goes in"). Use "you" when speaking to the school |
| "Built for how Zimbabwean schools run" is bad | Show local fit with detail; never claim it |
| "US$1 per active pupil per month." / "lose the stray nothing in the holidays" | The price is always "US$1 per active pupil per month" (US$8.99 for the LMS package). No tag-along clause after it; holiday billing is said once, where pricing details are listed |
| "Not your teachers, You. You enter each mark once." | Address the person who does the job directly as "you". Never "your teachers", "your staff", "your bursar" |
| "the second text isn't necessary. its simply one system for the whole school" | Hero headline is one line: "One system for the whole school." A second line only when it adds a fact ("Four portals. One record behind them." stays) |
| "single source of truth… this is okay to use" | "Single source of truth" is allowed |
| "in fact, the whole system works without internet. write it correctly" | The offline claim is about all of Campus: "Campus works without internet." The register is an example, never the limit of the claim |
