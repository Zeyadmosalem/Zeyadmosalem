<p align="center">
  <img src="./8351160.gif" width="100%" alt="Animated pixel-art cockpit banner" />
</p>

<h1 align="center">Zeyad&nbsp;M.&nbsp;Salem</h1>

<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=16&duration=3200&pause=900&color=A855F7&center=true&vCenter=true&width=640&lines=AI+%2F+LLM+Application+Engineer;Text-to-SQL+%C2%B7+RAG+%C2%B7+Retrieval+Systems;Python+%C2%B7+JavaScript+%C2%B7+React+%C2%B7+PostgreSQL;Arabic-BIRD+%E2%80%94+Cross-Lingual+Semantic+Parsing;Open+to+Remote+Work" alt="AI / LLM Application Engineer" />
</p>

<p align="center">
  <a href="https://www.linkedin.com/in/zeyadmosalem/">
    <img src="https://img.shields.io/badge/LinkedIn-A855F7?style=flat-square&logo=linkedin&logoColor=white" alt="LinkedIn" />
  </a>
  &nbsp;
  <a href="mailto:zeyadmosalem@gmail.com">
    <img src="https://img.shields.io/badge/Email-7C3AED?style=flat-square&logo=gmail&logoColor=white" alt="Email" />
  </a>
  &nbsp;
  <a href="https://github.com/Zeyadmosalem?tab=followers">
    <img src="https://img.shields.io/github/followers/Zeyadmosalem?style=flat-square&color=A855F7&labelColor=1a1b27&logo=github&logoColor=white" alt="GitHub followers" />
  </a>
</p>

---

<img align="right" width="330" src="https://user-images.githubusercontent.com/74038190/229223263-cf2e4b07-2615-4f87-9c38-e37600f8381a.gif" alt="" />

### About

I build the layer between language models and real data — text-to-SQL, retrieval,
and the interfaces that make model output usable.

Most of my current work is **cross-lingual semantic parsing**: getting models to
answer questions over relational databases in Arabic as reliably as in English.

I care about systems that hold up under scrutiny — graded server-side, covered by
tests, and measured against a benchmark rather than a demo.

<br clear="right" />

---

### Featured work

#### [NC Spark](https://github.com/Zeyadmosalem/nc-spark)
**A role-based compliance training platform that can prove who did what.**
Four portals and seven authorable activity types. Quizzes are graded server-side —
the answer key lives in a table no browser role has a grant on, reachable only from
an Edge Function. XP, streaks, badges and leaderboards all derive from a single
append-only ledger, so a badge can never disagree with its record.

React 19 · Vite 8 · Supabase / Postgres 17 · Cloudflare Workers
**1,828 tests · 91% statement coverage**

#### [Beyond Seen Mistakes](https://github.com/AbdelrahmanAboegela/beyond-seen-mistakes) — contributor
**A matched test of error-composition generalization in exercise assessment.**
Source of the JAC-ECC 2026 HAR–EAS submission, stress-testing six models
including ST-GCN and FACT against diagnosis combinations withheld from training.

My contribution: the test suite and CI for the published pipeline — data-loader,
split-protocol, training edge-case and reproduction tests — plus a fix making
reproduction checks numerical rather than bit-for-bit.
[My commits →](https://github.com/AbdelrahmanAboegela/beyond-seen-mistakes/commits?author=Zeyadmosalem)

#### Arabic-BIRD & CCER-SQL — cross-lingual Arabic→English text-to-SQL
*Research project. Repositories are private pending publication.*

A bilingual adaptation of the BIRD benchmark, plus a retrieval-centric agentic
pipeline. Multilingual embeddings (`intfloat/multilingual-e5-base`) let Arabic
questions retrieve English schema elements in a shared space with no
task-specific fine-tuning; a LangGraph agent then generates SQL candidates,
executes them against the real database, picks a winner by self-consistency
voting, and escalates to refinement on failure.

**96.43% Recall@5** on table selection · **60% execution accuracy** on the
English pilot · **99.77%** gold-graph column coverage

My contribution: the Arabic dataset — human-reviewed translations of every
question and evidence hint across BIRD — and the retrieval architecture.

---

### Stack

**Core**
`Python` &nbsp;`JavaScript` &nbsp;`React` &nbsp;`PostgreSQL` &nbsp;`Git`

**LLM & retrieval**
`Text-to-SQL` &nbsp;`Retrieval-augmented generation` &nbsp;`Schema linking` &nbsp;`Cross-lingual semantic parsing` &nbsp;`LangGraph` &nbsp;`sentence-transformers / multilingual-e5` &nbsp;`Groq` &nbsp;`BIRD benchmark`

**Testing & CI**
`Vitest` &nbsp;`Playwright` &nbsp;`Testing Library` &nbsp;`pytest` &nbsp;`GitHub Actions`

**Also working with**
`TypeScript (Supabase Edge Functions)` &nbsp;`Supabase` &nbsp;`Cloudflare Workers` &nbsp;`Node.js` &nbsp;`Vite` &nbsp;`pandas` &nbsp;`Linux`

<p>
  <img src="https://skillicons.dev/icons?i=python,js,ts,react,nodejs,vite,postgres,supabase,cloudflare,git,linux&theme=dark&perline=6" alt="Tech stack" />
</p>

---

<div align="center">

<img width="760" src="https://github-profile-summary-cards.vercel.app/api/cards/profile-details?username=Zeyadmosalem&theme=github_dark" alt="Profile summary" />

<img height="190" src="https://github-profile-summary-cards.vercel.app/api/cards/repos-per-language?username=Zeyadmosalem&theme=github_dark" alt="Top languages" />

</div>

---

<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Zeyadmosalem/Zeyadmosalem/output/github-contribution-grid-snake-dark.svg" />
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/Zeyadmosalem/Zeyadmosalem/output/github-contribution-grid-snake.svg" />
  <img src="https://raw.githubusercontent.com/Zeyadmosalem/Zeyadmosalem/output/github-contribution-grid-snake-dark.svg" alt="Contribution graph" />
</picture>

</div>

<p align="center">
  <a href="mailto:zeyadmosalem@gmail.com">
    <img src="https://img.shields.io/badge/Open%20to%20remote%20work-Get%20in%20touch-A855F7?style=for-the-badge&logo=gmail&logoColor=white" alt="Open to remote work — get in touch" />
  </a>
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:A855F7,50:7C3AED,100:4A00E0&height=110&section=footer" alt="" />
</p>
