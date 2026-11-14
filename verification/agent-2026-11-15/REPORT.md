# Independent verification — 2026-11-15

Repository baseline: `iwasborninbali/oeis-A005432-unsubmitted` commit `b7e10d5c807b34cbe0ccc9657b20b39cd7bbf143` (supplied archive, cross-checked through GitHub). Read `README.md`, `CERTIFICATE.md`, `PRIOR-ART.md`; the archive contains no prior `verification/` files. This review is independent of the certificate's authors. The mathematics in the paper is *not* being independently proved.

## Claim

Exact sentence from `CERTIFICATE.md`: **“Roney-Dougal and Tracey's Theorem 1 proves the exponential rate conjectured in A005432.”** This is a claim about a missing reference, not new mathematical research and not a proposed change to the terms.

## Source check

Primary source: Colva M. Roney-Dougal and Gareth Tracey, *Subgroups of symmetric groups: enumeration and asymptotic properties*, arXiv:2503.05416 (first submitted 7 March 2025), [source abstract](https://arxiv.org/abs/2503.05416), [full HTML text](https://arxiv.org/html/2503.05416), **Section 1 (Introduction), Theorem 1**, immediately after the paragraph describing Pyber's conjecture. The theorem begins, “There exist absolute constants α>0 and β such that for all integers n>1,” and displays

\[
 2^{n^2/16+\alpha n\log_2 n}\ \leq\ |\operatorname{Sub}(S_n)|\ \leq\ 2^{n^2/16+\beta n^{3/2}}.
\]

The abstract independently says the number of subgroups is `2^(n^2/16+o(n^2))` and that this settles Pyber's 1993 conjecture. The source's introduction defines `Sub(S_n)` as the **set of all subgroups** of the symmetric group on `n` points, not subgroup conjugacy classes, isomorphism types, or only transitive groups. Its logarithms are base 2 (stated in the introduction). A005432 counts distinct subgroups of the *same* group `S_n`, with conjugates distinct, and has offset `0,3`: the source's theorem is for `n>1`, which is enough for an asymptotic statement; `a(0)=a(1)=1` are not at issue. The paper explicitly distinguishes conjugacy-class counting as a related but different problem immediately after Theorem 2.

**Support: exact.** Taking base-2 logarithms and dividing Theorem 1 by `n^2` gives `log2(a(n))/n^2 -> 1/16`, since `n log n = o(n^2)` and `n^(3/2) = o(n^2)`. The claimed exponential rate is therefore a stated and immediate consequence. Neither the paper's complete proof nor its computational ingredients have been audited here. The theorem's constants `α` and `β` are existential rather than given as numerical values.

## Independent computation

Program: [`subgroup_check.py`](subgroup_check.py); complete run: [`output.log`](output.log). Only Python 3 standard library; the code directly represents permutations, constructs composition and inverse tables, enumerates all subgroups starting from the identity subgroup by adjoining coset representatives and closing under multiplication, and deduplicates subgroup bitsets. No GAP, Magma, or external subgroup enumeration was used. The `OEIS_A005432` literal is used **only as comparison data**, never to generate subgroup counts.

Exact values computed, `n=0..6`: `1, 1, 2, 6, 30, 156, 1455`. **7/7 agree** with A005432, conjugates counted separately. The `n=6` census made `165281` subgroup-generator extensions (with deduplication). The run also computed the number `L(n)` of subspaces of `F_2^floor(n/2)` by the exact Gaussian-binomial recurrence. Distinct subspaces embed into `S_n` through `floor(n/2)` disjoint transpositions, so `L(n) <= a(n)` unconditionally. This inequality passed against all OEIS terms `n=0..18`; e.g., `L(16)=417199 <= a(16)=5320744503742316`, `L(18)=8283458 <= a(18)=7598016157515302757`. The log of the finite lower-bound count has asymptotic leading exponent `n^2/16`, but finite experiments **do not establish the theorem's sharp upper bound or its error terms**.

Runtime (as recorded in the log): **33.842334 seconds total**, including **33.720887 seconds** for `S_6` enumeration, on the execution host. Reproduce: `python3 subgroup_check.py --max-exact-n 6 > output.log 2>&1` (timings and hence output-log hash will vary on a new run).

SHA-256 of the exact files accompanying this report:

- `subgroup_check.py`: `a8f2484fc71a026d7b194ff92502b7cb5a3335152cc8ef100a527cffcf5ec0cb`
- `output.log`: `5334ba96a7da9382887627542b835b95b8fbbf5e3ed3a3edf87ec82d0bf74d8e`

## Entry check

Read on **2026-11-15**: [A005432 main entry](https://oeis.org/A005432) and [internal format](https://oeis.org/A005432/internal), including the `%C`, `%D`, `%H`, `%N`, `%O`, `%S/%T/%U` fields. Both display the Pyber-era comment, “conjectures lower bound is accurate,” and a citation to **L. Pyber (1993)**. Neither contains Roney-Dougal, Tracey, `2503.05416`, or an equivalent statement that the exponent `1/16` is proven. No terms need correction. The present result complements and supersedes the entry's *asymptotic upper bound*, not its cited finite-n enumerations.

Tried the OEIS **history** link (`https://oeis.org/history?seq=A005432`), both by following the entry's link and opening the URL directly. It returned **403/disabled** in the available web reader; therefore the sequence's edit-by-edit history could not be inspected. This limits claims about what *might once have appeared*, not the directly observed contents of the current public entry. Prior art: Pyber's 1993 conjecture and bounds are credited already. Targeted searches for later publication of this *same exact theorem* did not identify a definitive peer-reviewed journal successor or a stronger replacement source; this is **not proof** that none exists. The arXiv preprint is the primary explicit source and the natural reference to add.

## Verdict

**COMPLETE (as a reference correction to the live entry).** The cited paper explicitly proves the conjectured `1/16` exponential rate for the same subgroup-counting convention, and the checked live OEIS entry does not already cite or state that result. The independent finite enumeration matches `a(0)..a(6)`, and a separate elementary lower-bound sanity check matches inequalities through `n=18`. The paper's proof, exact constants, and inaccessible edit history remain **not independently established** by this audit; those limitations do not negate the narrowly defined *citation* claim. Do not present this as a new proof or a completed OEIS submission.

Suggested OEIS update: cite `C. M. Roney-Dougal and G. Tracey, Subgroups of symmetric groups: enumeration and asymptotic properties, arXiv:2503.05416 (2025), Theorem 1`, and replace the outdated conjectural comment with `a(n)=2^(n^2/16+o(n^2))` (credited to those authors), while retaining appropriate attribution to Pyber's 1993 work.
