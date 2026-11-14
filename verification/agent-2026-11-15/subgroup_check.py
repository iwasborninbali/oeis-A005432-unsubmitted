#!/usr/bin/env python3
"""Independent exact small-n subgroup census and an elementary lower bound.

No computer algebra packages or OEIS data are used to compute counts.
Enumerate S_n as explicit permutations. Each subgroup is a bitset of its
members. Starting with the identity subgroup, adjoin one representative
from each nontrivial left coset and close under multiplication; deduplicate
by subgroup bitset. Every subgroup is eventually encountered because its
elements can be adjoined one at a time.

Also count the subspaces of F_2^floor(n/2), viewed as subgroups generated
by floor(n/2) disjoint transpositions in S_n. These are a rigorous
finite-n lower bound, not a verification of the asymptotic upper bound.
"""
from __future__ import annotations

import argparse
from collections import deque
from itertools import permutations
from math import factorial, log2
from time import perf_counter


OEIS_A005432 = (
    1, 1, 2, 6, 30, 156, 1455, 11300, 151221, 1694723,
    29594446, 404126228, 10594925360, 175238308453,
    5651774693595, 117053117995400, 5320744503742316,
    125889331236297288, 7598016157515302757,
)


def elements_of_bitset(mask: int):
    while mask:
        lowest = mask & -mask
        yield lowest.bit_length() - 1
        mask ^= lowest


def count_subgroups(n: int) -> tuple[int, int]:
    """Enumerate all individual (not conjugacy-identified) subgroups."""
    elements = list(permutations(range(n)))
    index = {p: i for i, p in enumerate(elements)}
    size = factorial(n)
    identity = index[tuple(range(n))]
    assert identity == 0
    multiply = [
        [index[tuple(p[q[k]] for k in range(n))] for q in elements]
        for p in elements
    ]
    inverse = [
        index[tuple(p.index(k) for k in range(n))] for p in elements
    ]

    def generated_by(gens: tuple[int, ...]) -> int:
        steps = tuple(dict.fromkeys(
            g for x in gens for g in (x, inverse[x]) if g != identity
        ))
        bits = 1 << identity
        queue = [identity]
        for u in queue:
            for g in steps:
                v = multiply[u][g]
                if not bits & (1 << v):
                    bits |= 1 << v
                    queue.append(v)
        return bits

    start = 1 << identity
    discovered = {start: ()}
    pending = deque([start])
    expansions = 0
    while pending:
        subgroup = pending.popleft()
        gens = discovered[subgroup]
        members = list(elements_of_bitset(subgroup))
        covered_cosets = subgroup
        for x in range(size):
            if covered_cosets & (1 << x):
                continue
            # Elements in H*x generate the same extension of H.
            for h in members:
                covered_cosets |= 1 << multiply[h][x]
            expansion = generated_by(gens + (x,))
            expansions += 1
            if expansion not in discovered:
                discovered[expansion] = gens + (x,)
                pending.append(expansion)
        assert covered_cosets == (1 << size) - 1
    assert (1 << size) - 1 in discovered
    return len(discovered), expansions


def gaussian_sum_over_f2(d: int) -> int:
    """Exact number of all linear subspaces of F_2^d."""
    previous = [1]
    for m in range(1, d + 1):
        current = [0] * (m + 1)
        for k in range(m + 1):
            same = previous[k] if k < m else 0
            additional = (1 << (m - k)) * previous[k - 1] if k else 0
            current[k] = same + additional
        previous = current
    return sum(previous)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-exact-n", type=int, default=6)
    args = parser.parse_args()
    if not (0 <= args.max_exact_n <= 6):
        parser.error("exact census limited to 0 <= n <= 6")
    start = perf_counter()
    print("METHOD: from-scratch permutation closure; no GAP, Magma, or group-library calls", flush=True)
    print("DEFINITION: all distinct subgroups of S_n, conjugates counted separately", flush=True)
    print("OEIS OFFSET: 0", flush=True)
    print("n | exact | OEIS | equal | generator-extensions | elapsed_sec", flush=True)
    for n in range(args.max_exact_n + 1):
        tick = perf_counter()
        exact, expansions = count_subgroups(n)
        elapsed = perf_counter() - tick
        print(f"{n:2d} | {exact} | {OEIS_A005432[n]} | "
              f"{'YES' if exact == OEIS_A005432[n] else 'NO'} | "
              f"{expansions} | {elapsed:.6f}", flush=True)
        assert exact == OEIS_A005432[n], f"Mismatch at n={n}"

    print("FINITE-N SUBSPACE LOWER BOUND: every subspace of (C2)^floor(n/2)", flush=True)
    print("is a distinct subgroup of S_n by disjoint transpositions", flush=True)
    print("n | dimension | subspaces | A005432 | lower_bound_holds | log2(subspaces)/n^2", flush=True)
    for n, count in enumerate(OEIS_A005432):
        d = n // 2
        bound = gaussian_sum_over_f2(d)
        check = bound <= count
        scale = f"{log2(bound) / (n*n):.8f}" if n else "n/a"
        print(f"{n:2d} | {d:2d} | {bound} | {count} | "
              f"{'YES' if check else 'NO'} | {scale}", flush=True)
        assert check, f"Subspace lower bound fails at n={n}"
    print(f"TOTAL_RUNTIME_SEC: {perf_counter() - start:.6f}", flush=True)
    print("CONCLUSION: exact small-n counts agree; finite lower bound holds for n=0..18", flush=True)
    print("LIMITATION: finite checks cannot prove the n->infinity asymptotic theorem", flush=True)


if __name__ == "__main__":
    main()
