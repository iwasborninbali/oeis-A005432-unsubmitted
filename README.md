# OEIS A005432: reference for subgroup asymptotics (not yet submitted)

<!-- oeis-status:begin -->
**OEIS status: not submitted.** (replaced by the registry tool)
<!-- oeis-status:end -->

## Definition

a(n) is the number of subgroups of the symmetric group on n labeled points, counting conjugate subgroups separately. The offset is 0; the symmetric group on the empty set has one subgroup.

## Terms / result

No term changes. The live [A005432](https://oeis.org/A005432), read 2026-11-13, has the unattributed line: `L. Pyber shows c^(n^2(1+o(1))) <= a(n) <= d^(n^2(1+o(1))), c=2^(1/16), d=24^(1/6); conjectures lower bound is accurate.` The cited 2025 paper settles the conjectured exponential rate.

## How it was obtained

Colva M. Roney-Dougal and Gareth Tracey, *Subgroups of symmetric groups: enumeration and asymptotic properties*, preprint [arXiv:2503.05416](https://arxiv.org/abs/2503.05416), 2025, [doi:10.48550/arXiv.2503.05416](https://doi.org/10.48550/arXiv.2503.05416). Read 2026-11-13, [full text, Theorem 1](https://arxiv.org/html/2503.05416): “There exist absolute constants α>0 and β” giving upper and lower bounds with leading exponent n²/16. The abstract states that the number of subgroups is 2^(n²/16+o(n²)). This is exactly the labeled subgroup count in A005432, and proves the rate conjectured by Pyber.

## Verification

The theorem and definition were checked against the source and entry. The paper's proof and the tabulated terms were not independently reverified. See [CERTIFICATE.md](CERTIFICATE.md).

## Prior art and credit

Pyber formulated the conjecture in 1993; Roney-Dougal and Tracey prove it. See [PRIOR-ART.md](PRIOR-ART.md).

## Reproduce

Open the linked preprint and compare Theorem 1 with the sequence definition; this takes approximately five minutes. No paper is bundled.

## Provenance

Source: `projects/science/athanor-oeis`, commit `11b7ea9cc6f4c0057731d8e36c023f8b36e7c27f`, `tasks/2026-11-12-A005432-permutation-groups-pyber/answers/2026-11-12-chatgpt.md`.

## Author, licence

Aleksei Kudriashov (ORCID 0009-0006-8885-5338), Athanor lab, with AI assistance (OpenAI Codex cores; Claude Code as the lab's guide). Code: MIT; data and text: CC BY 4.0 (see LICENSE.md).
