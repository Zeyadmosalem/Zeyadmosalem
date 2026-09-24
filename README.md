<div align="center">

<img src="8351160.gif" alt="Animated pixel-art cockpit banner" width="100%" />

# Zeyad M. Salem

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=16&duration=3200&pause=900&color=A855F7&center=true&vCenter=true&width=640&lines=Full-Stack+%26+AI+Application+Developer;Text-to-SQL+%C2%B7+RAG+%C2%B7+Arabic+NLP;React+%C2%B7+TypeScript+%C2%B7+Supabase+%C2%B7+Python;AraBIRD+%E2%80%94+Accepted+at+IEEE+NILES+2026;Open+to+Freelance+%26+Part-Time+Work" alt="Full-Stack & AI Application Developer" />

<a href="https://www.linkedin.com/in/zeyadmosalem/"><img src="https://img.shields.io/badge/LinkedIn-A855F7?style=flat-square&logo=linkedin&logoColor=white" alt="LinkedIn" /></a>
<a href="mailto:zeyadmosalem@gmail.com"><img src="https://img.shields.io/badge/Email-7C3AED?style=flat-square&logo=gmail&logoColor=white" alt="Email" /></a>
<a href="https://github.com/Zeyadmosalem?tab=followers"><img src="https://img.shields.io/github/followers/Zeyadmosalem?style=flat-square&color=A855F7&labelColor=1a1b27&logo=github&logoColor=white" alt="GitHub followers" /></a>

</div>

---

### About

I build bilingual Arabic and English software end to end, from requirements and
database design to security review, testing and production, and I work on the
layer between language models and real data: text-to-SQL, retrieval, and the
interfaces that make model output usable.

My research focus is **cross-lingual semantic parsing**: getting models to answer
questions over relational databases in Arabic as reliably as in English. I'm a
co-author of **AraBIRD**, accepted at **IEEE NILES 2026**.

I care about systems that hold up under scrutiny: authorization enforced in the
database, grading done on the server, everything covered by tests. I use AI coding
tools like Claude Code to move faster, while owning the architecture and the quality.

Computer Science student at **E-JUST**, Alexandria, Egypt (graduating late 2027).
Available for remote freelance, part-time and internship work, up to 20 hours a week.

---

### Featured work

#### [NC Spark](https://github.com/Zeyadmosalem/nc-spark)

**A role-based compliance training platform that can prove who did what.** Four
portals and seven authorable activity types. Quizzes are graded server-side: the
answer key lives in a table no browser role has a grant on, reachable only from an
Edge Function. Privilege escalation is blocked by three independent layers, and the
whole site sits behind a Cloudflare Worker access gate. XP, streaks, badges and
leaderboards all derive from a single append-only ledger, so a badge can never
disagree with its record.

React 19 · Vite 8 · Supabase / Postgres 17 · Cloudflare Workers
**1,828 tests · 91% statement coverage · red-team security suites**

#### [Samboza](https://github.com/Zeyadmosalem/Samboza) — in production

**A bilingual household finance app, used daily since September 2026.** An
installable Arabic/English PWA with a full right-to-left layout, where Postgres
row-level security, not the screen, decides who reads and writes which rows across
four roles. A double-entry ledger with an audit trail, offline writes through an
idempotent outbox, Excel export, and a CI pipeline that refuses to deploy until the
database has every migration the bundle expects.

React 19 · TypeScript · Supabase / Postgres · Cloudflare Workers · GitHub Actions
**532 pgTAP policy tests · 578 front-end tests · 50 migrations**

#### AraBIRD — Arabic Text-to-SQL benchmark · IEEE NILES 2026 (accepted)

**A Modern Standard Arabic adaptation of the BIRD benchmark**, where users ask in
Arabic while schemas, values and SQL stay in English: 8,375 training and 1,469
development examples, built through SQL-aware translation, automatic consistency
checks and native-speaker auditing. Its companion pipeline, CCER-SQL, retrieves
English schema elements for Arabic questions through multilingual embeddings and
drives a LangGraph agent that generates, executes and repairs SQL
(**96.43% Recall@5** on table selection).

My contribution: the Arabic translation of the dataset, research into and
implementation of several translation approaches before the final version, the
novelty assessment, and writing the paper.

#### [Beyond Seen Mistakes](https://github.com/AbdelrahmanAboegela/beyond-seen-mistakes) — contributor

**A matched test of error-composition generalization in exercise assessment.**
Source of the JAC-ECC 2026 HAR–EAS submission, stress-testing six models including
ST-GCN and FACT against diagnosis combinations withheld from training.

My contribution: the test suite and CI for the published pipeline (data-loader,
split-protocol, training edge-case and reproduction tests), plus a fix making
reproduction checks numerical rather than bit-for-bit.
[My commits →](https://github.com/AbdelrahmanAboegela/beyond-seen-mistakes/commits?author=Zeyadmosalem)

---

### Stack

**Core** `TypeScript` `JavaScript` `Python` `React` `PostgreSQL` `SQL` `Git`

**Backend & platform** `Supabase` `Row-level security` `Edge Functions` `Cloudflare Workers` `TanStack Query` `Vite` `Node.js` `PWAs`

**LLM & retrieval** `Text-to-SQL` `Retrieval-augmented generation` `Schema linking` `Cross-lingual semantic parsing` `LangGraph` `sentence-transformers / multilingual-e5` `BIRD benchmark`

**Testing & CI** `Vitest` `pgTAP` `Playwright` `Testing Library` `pytest` `GitHub Actions`

<div align="center">

<img src="https://skillicons.dev/icons?i=python,js,ts,react,nodejs,vite,postgres,supabase,cloudflare,vitest,githubactions,git,linux&theme=dark&perline=7" alt="Tech stack" />

---

<img src="https://github-profile-summary-cards.vercel.app/api/cards/profile-details?username=Zeyadmosalem&theme=github_dark" alt="Profile summary" />
<img src="https://github-profile-summary-cards.vercel.app/api/cards/repos-per-language?username=Zeyadmosalem&theme=github_dark" alt="Top languages" />

---

<img src="https://raw.githubusercontent.com/Zeyadmosalem/Zeyadmosalem/output/github-contribution-grid-snake-dark.svg" alt="Contribution graph" />

<a href="mailto:zeyadmosalem@gmail.com"><img src="https://img.shields.io/badge/Open%20to%20remote%20work-Get%20in%20touch-A855F7?style=for-the-badge&logo=gmail&logoColor=white" alt="Open to remote work — get in touch" /></a>

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:A855F7,50:7C3AED,100:4A00E0&height=110&section=footer" width="100%" />

</div>
