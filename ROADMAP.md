# 🗺️ 12-Month Quantum Roadmap — Learn + Build a Business

**Start: August 2026 · Owner: Fernando Leano**

Two tracks run in parallel, every month:

- **🧠 LEARN** — quantum computing skills, hands-on in this repo
- **💼 BUILD** — audience + income, starting day one

Rules of the game:
1. Ship something public every month, however small.
2. Every LEARN milestone becomes BUILD content ("I just learned X" posts).
3. Don't skip months. Half a milestone beats zero.
4. Revisit this file monthly — check boxes, adjust what's ahead.

---

## Phase 1 — Foundations (Aug–Oct 2026)

### Month 1 · Aug 2026 — One qubit, deeply
- [ ] 🧠 Single-qubit gates (X, Z, H, RY) in a Jupyter notebook with Bloch-sphere visuals
- [ ] 🧠 Understand measurement probabilities = amplitude² — verify by experiment in Aer
- [ ] 🧠 Linear algebra basics: vectors, matrix × vector (Khan Academy / 3Blue1Brown)
- [ ] 💼 Create X/Twitter + TikTok/YouTube handle for the journey (pick one main platform)
- [ ] 💼 Post #1: "I ran code on a real 156-qubit quantum computer" (you already have the material)
- [ ] 💼 Push this repo public on GitHub — it's the portfolio from day one

### Month 2 · Sep 2026 — Two qubits, entanglement for real
- [ ] 🧠 Re-derive the Bell state by hand on paper (H then CNOT, amplitude by amplitude)
- [ ] 🧠 All four Bell states; GHZ state with 3 qubits
- [ ] 🧠 Quantum teleportation circuit — build, run, explain in README
- [ ] 💼 Post weekly (4 posts min): each concept you learn = one post with a visual
- [ ] 💼 Write first long-form piece: "Entanglement explained by a beginner, for beginners"

### Month 3 · Oct 2026 — First real algorithms
- [ ] 🧠 Deutsch–Jozsa algorithm — first proof quantum beats classical
- [ ] 🧠 Grover's search on 3 qubits — understand amplitude amplification
- [ ] 🧠 Run both on real IBM hardware, compare with simulator, write up noise differences
- [ ] 💼 Publish "quantum-playground" as a structured learning path (folders per topic, README per folder)
- [ ] 💼 Milestone check: 100+ followers on main platform. If not, study what's not landing — fix hook, not effort.

**Phase 1 exit bar:** you can explain superposition, entanglement, and one algorithm to a friend without notes. Repo has 5+ working, documented circuits.

---

## Phase 2 — Cryptography Pivot (Nov 2026–Jan 2027)

*This is where the business track gets its teeth. Post-quantum cryptography (PQC) migration is the only quantum-adjacent market paying real money to non-PhDs right now.*

### Month 4 · Nov 2026 — Why quantum breaks encryption
- [ ] 🧠 RSA basics: how public-key crypto works (classical, no quantum needed)
- [ ] 🧠 Shor's algorithm conceptually — period finding, why factoring collapses
- [ ] 🧠 Implement toy Shor (factor 15) in Qiskit — understand every stage
- [ ] 💼 Post series: "Quantum computers will break the internet — here's the actual math"
- [ ] 💼 This series is your PQC credibility seed. Save every well-received explanation.

### Month 5 · Dec 2026 — Post-quantum cryptography
- [ ] 🧠 NIST PQC standards: ML-KEM (Kyber), ML-DSA (Dilithium) — what they are, why lattices resist quantum
- [ ] 🧠 Use them in code: Python `pqcrypto` / liboqs — encrypt, sign, verify
- [ ] 🧠 "Harvest now, decrypt later" threat model — why migration is urgent TODAY
- [ ] 💼 Write the cornerstone piece: "The Post-Quantum Migration, explained for CTOs"
- [ ] 💼 Register a simple domain for yourself (name-brand or PQC-brand — cheap, do it now)

### Month 6 · Jan 2027 — Build the scanner (your first product)
- [ ] 🧠 Learn: how to find crypto usage in codebases (grep patterns for RSA/ECDSA/TLS configs, key sizes)
- [ ] 💼 **Ship: open-source "crypto inventory scanner" CLI** — point at a repo, get a report of quantum-vulnerable crypto
- [ ] 💼 Launch it: post on HN/Reddit/X, README with clear before/after value
- [ ] 💼 Milestone check: 500+ followers, scanner has 25+ GitHub stars. Stars = proof strangers find it useful.

**Phase 2 exit bar:** you can explain to a business owner, in plain English, what quantum does to their encryption and what to do about it. You have a public tool that demonstrates it.

---

## Phase 3 — First Dollars (Feb–Apr 2027)

### Month 7 · Feb 2027 — Package the audit
- [ ] 💼 Define the offer: "PQC Readiness Audit" — fixed scope, fixed price ($1,500–3,000 for small companies): crypto inventory + risk report + migration plan
- [ ] 💼 One-page site on your domain: problem, offer, your scanner + content as proof
- [ ] 💼 Outreach: 20 conversations with dev-agency owners / CTOs in your network's reach. Goal: learn objections, not close.
- [ ] 🧠 Keep hands warm: quantum error correction basics (repetition code, why noise from your ibm_fez run matters)

### Month 8 · Mar 2027 — First paid work
- [ ] 💼 **Close 1 paid audit.** Discount is fine; free-for-testimonial acceptable ONCE. A logo and case study is the asset.
- [ ] 💼 Turn delivery into templates: report template, scanner workflow, migration checklist — repeatability = business
- [ ] 🧠 Variational algorithms intro (VQE) — where near-term quantum research actually is

### Month 9 · Apr 2027 — Systemize
- [ ] 💼 Publish the case study (anonymized fine): "We found X quantum-vulnerable systems in a Y-person company"
- [ ] 💼 Second + third audit in pipeline; raise price after each close
- [ ] 💼 Milestone check: **$1,000+ total revenue.** If zero: diagnosis month — is it offer, audience, or outreach volume? Fix biggest leak, don't add new projects.
- [ ] 🧠 Qiskit certification prep begins (IBM Certified Associate — the resume line)

**Phase 3 exit bar:** money has changed hands at least once for your quantum-adjacent skills. You know why customers said yes and no.

---

## Phase 4 — Compound (May–Jul 2027)

### Month 10 · May 2027 — Credential + authority
- [ ] 🧠 **Take IBM Qiskit Associate certification exam**
- [ ] 💼 Productize content: free email course "PQC in 5 days" — builds the list that sells audits while you sleep
- [ ] 💼 Speak once: local meetup, podcast guest, or conference lightning talk — recorded

### Month 11 · Jun 2027 — Choose your lane
- [ ] 💼 Review the data honestly. Three doors, pick primarily one:
  - **Consulting door**: audits closing → scale to $5k+ engagements, productize further
  - **Content door**: audience growing fast → course/community as main revenue
  - **Employment door**: neither converting but skills strong → apply to quantum companies (Qiskit cert + repo + public work = strong application), build business on the side
- [ ] 🧠 Deep-dive whatever your lane demands (consulting → enterprise crypto; content → teaching craft; employment → interview prep + more algorithms)

### Month 12 · Jul 2027 — Ship the flagship
- [ ] 💼 One flagship deliverable for the chosen lane: signature $5k service / paid course launch / accepted job offer
- [ ] 💼 Write the retrospective post: "12 months into quantum from zero" — this post recruits your next customers, students, or employers
- [ ] 🧠 Set the next 12-month bar

**Phase 4 exit bar:** one of — recurring consulting revenue · paying audience · quantum industry job. Any one = successful year one.

---

## Numbers to watch (monthly)

| Metric | M3 | M6 | M9 | M12 |
|--------|----|----|----|----|
| Followers (main platform) | 100 | 500 | 1,500 | 4,000 |
| GitHub stars (all repos) | 10 | 25 | 75 | 150 |
| Revenue (cumulative) | $0 | $0 | $1,000 | $5,000+ |
| Working circuits in repo | 5 | 10 | 15 | 20+ |

Miss a number = diagnose, don't quit. Numbers are compasses, not judges.

## Anti-goals (things NOT to do this year)

- ❌ Selling raw quantum random numbers as cryptography (market: free competitors, certification wall)
- ❌ Founding a quantum *hardware* anything
- ❌ Buying $2k+ courses — everything needed is free or under $50/month
- ❌ Waiting to post until "expert enough" — the beginner lens IS the content advantage
- ❌ Starting a second business idea before the first dollar arrives
