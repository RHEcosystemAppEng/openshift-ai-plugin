# Suggested-flow rubric (step 5)

The main advisor agent scores every **suggested flow** from steps 3 and 4 (do not invoke a worker skill).

## Unit

A **suggested flow** is exactly one pair:

- one **observed flow** from step 2, and
- one **component** from step 3 (addition) or step 4 (migration)

One component per suggested flow. If the same observed flow has two candidate components, create two suggested flows. Keep the pairing internal for scoring; user-facing step 5 lists show the **component name** only.

## Dimensions (v1)

### Impact — `high` | `medium` | `low`

Judge how much this suggested flow helps the project **right now**, grounded in the observed flow’s files and handoffs.

| Band | When |
|------|------|
| **high** | The component clearly improves **AI outcome quality** on that flow: correctness, evaluation coverage, safety, or reliability of what the flow produces. Cite concrete gap evidence (missing eval, ungrounded answers, no safety gate, brittle quality loop). Platform packaging alone is not enough. |
| **medium** | Useful on the flow (ops, ergonomics, partial quality) but does not clearly raise outcome quality now. |
| **low** | Weak or speculative tie to the observed flow; nice-to-have catalog coverage. |

### Complexity — `low` | `medium` | `high`

Estimate **touch count**: application/model/config files to change, plus operators/CRDs/packages to introduce. More touches ⇒ higher complexity.

| Band | Touch heuristic |
|------|-----------------|
| **low** | Roughly ≤3 files/manifests to change, and at most one new operator or thin config surface |
| **medium** | Roughly 4–10 files, or changes spanning 2 packages/services, or a moderate operator + wiring set |
| **high** | Roughly >10 files, ≥3 packages/services, severe coupling/rewrite, or a heavy multi-operator / multi-CRD adoption |

Use step 4’s easy/more-complex signal as an input for migrations when present; still assign a Complexity band here.

## Rank

Lexicographic sort across all suggested flows:

1. **Impact** high → medium → low
2. Then **Complexity** low → medium → high

## Cut → lists

| Destination | Rule |
|-------------|------|
| **Migrations worth doing** | Migration suggested flow with Impact=`high`, quality improvement (see Impact high), and Complexity=`low` or `medium` |
| **Additions worth doing** | Addition suggested flow with the same rule |
| **Future improvements** | Everything else — including Impact=`high` when Complexity=`high`, and all medium/low Impact |

Keep worth-doing lists actionable (prefer about 2–4 total direct fits when many pass; park the rest in Future with the rubric reason).
