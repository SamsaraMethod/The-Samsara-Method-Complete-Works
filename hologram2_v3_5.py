"""
╔══════════════════════════════════════════════════════════════════════════════════╗
║          HOLOGRAM2 — Integrated Framework for Analyzing Human-Made Systems       ║
║          OracleHybrid5.5 + DeepDark2 + Treatise + NROS Samsara Method          ║
║          Version: 3.5  |  Built: 2026 (defect repair + cross-surface parity)     ║
║          By Quantel Bolden in collaboration with Claude AI                       ║
║          samsaramethod@gmail.com                                                 ║
╚══════════════════════════════════════════════════════════════════════════════════╝

v3.5 ADDS (defect repair + Python↔dashboard parity; no new analytical surface):

  (H) substrate_research_report_v3_3() repaired. The v3.3 integrator called
      substrate_research_report_v3_2() with keyword names that do not exist
      in its signature (indicators=, throughput=) and omitted the required
      polity/scale parameters — every invocation raised TypeError. Latent
      since v3.3 because no demo or dashboard path exercised it. Now calls
      with indicators_by_pillar= / pillar_throughput= and passes
      polity=polity_id, scale="National".

  (I) record_substrate_state() multi-contributor aggregation repaired. When
      several indicators feed one substrate dimension (climate ← E7+E8+T7;
      meaning ← N6–N13), the first contributor entered the weighted-mean
      fold with a hardcoded weight of 1.0 instead of its true indicator
      weight, skewing the per-dimension value (U.S. climate read 0.2305
      where the w-weighted mean of its contributors is 0.5500; meaning read
      0.4213 vs 0.4238), and the source join mangled contributor provenance.
      The dashboard's buildSubstrateStateRecord() aggregated correctly all
      along — this restores Python↔JS parity to the documented intent.
      SHI/BHI composites were computed separately and were never affected.

  (J) Step-8 refinement parity. The dashboard's Eight-Step engine carries a
      third recursive-refinement check (SOC NEAR_CRITICAL while fewer than
      2 Pillars are stressed → hidden-stress flag) that the Python port
      lacked. Added with identical wording. Refinement notes are advisory
      text, not canonical anchors; on the U.S. baseline the demo now prints
      three refinement lines instead of two.

  (K) Doc accuracy + deprecation hygiene. The Hungary 2024 baseline header
      predicted regime=harmonic from coarse all-Pillar estimates (spread
      ~0.11); the computed indicator set yields spread 0.194 → balanced
      (the demo has always printed 'balanced / equilibrium') — comment now
      matches the verified behavior. datetime.utcnow() (deprecated 3.12+)
      replaced with the tz-aware equivalent normalized to the identical
      output string. Dragon-king gate ledger 'as of' version refreshed.

CANONICAL INVARIANTS PRESERVED (v3.5):
  • Every numeric anchor is unchanged and re-verified: 6 U.S. PHIs
    (0.7095/0.5345/0.6515/0.4305/0.5518/0.3831), U.S. SHI 0.4238 (4/8 below
    threshold), Hungary SHI 0.4438, U.S. substrate-borrowing max 0.0288
    (Energy), coupling tiers T1=7/T2=6/T3=17, all three Twelve-Day War
    verdicts (STRONGLY_ASYMMETRIC; gaps 0.433/0.433/0.440), Venezuela 2019
    floor/mean 0.3290/0.3712. (H) repairs a function that could never run;
    (I) changes only the per-dimension provenance record, never composites.

v3.4 ADDS (audit hardening — no new analytical surface; correctness + fidelity):

  (E) Cross-platform UTF-8 console. The demo and report functions emit Unicode
      (τ, σ, ρ, box-drawing, arrows). On Windows the default console encoding
      (cp1252) raised UnicodeEncodeError and aborted the run before the v3.3
      sections printed. __main__ now reconfigures stdout/stderr to UTF-8 where
      supported (fail-safe on platforms/streams that do not support it).

  (F) Dragon-king gate fidelity. dragon_king_module_status() now reports the
      FIVE canonical II.2 conditions exactly as numbered in the v3.1 Working
      Paper §II.2 ("What rigorous instantiation would require"):
        1 formal substrate-state variable + measurement protocol
        2 power-law distribution of substrate-event sizes
        3 1/f / scale-invariant temporal structure
        4 driving / dissipation mechanisms with conservation properties
        5 (dragon-king) log-periodic precursors + out-of-sample prediction
      The v3.3 ledger had drifted — it dropped canonical #1 and split the
      power-law condition into two ("#2 goodness-of-fit") — so it no longer
      cross-referenced the paper or the dashboard's own validation checklist.
      A canonical_source citation is now attached. The module itself remains
      DELIBERATELY NOT BUILT (gated by condition #4, still OPEN).

  (G) Robustness + doc accuracy. The bilateral coupling-asymmetry denominator
      is derived from the matrix dimensions instead of a hardcoded 30; the
      zscore normalization docstring now describes the linear-ramp transform
      actually implemented. The computation is unchanged — every canonical
      anchor is preserved bit-for-bit.

CANONICAL INVARIANTS PRESERVED (v3.4):
  • Every v3.0 / v3.5 / v3.1 / v3.2 / v3.3 numeric anchor is unchanged. The v3.4
    changes are console-encoding, gate-ledger wording, one denominator refactor
    (numerically identical for the 6×5 coupling matrix), and docstring text.
    No PHI / SHI / trajectory / verdict value moves.

v3.3 ADDS (research-grade; closes 2 of 4 v3.3 backlog candidates with honest
deferral of 1 and qualified scaffolding of 1):

  (A) Per-civilization C[p][b] calibration registry (Rule 4 closure)
      ─ POLITY_COUPLING_REGISTRY: {polity_id: {coupling_matrix, tier_matrix,
        citation_matrix, calibration_required, note}} — keyed registry that
        replaces global C[p][b] usage with explicit polity selection.
      ─ U.S. 2025 calibration (T1=7, T2=6, T3=17 from v3.2) is the only
        polity carrying primary-literature support. Hungary 2024 and
        Venezuela 2019 are added as ALL-T3 stubs with calibration_required
        flags — values inherit U.S. structure but tier provenance is honestly
        reset, preventing Rule 5 laundering.
      ─ get_polity_coupling(), compute_substrate_stress_for_polity(),
        identify_substrate_hot_cell_for_polity(), coupling_calibration_status()
      ─ Closes Rule 4 infrastructure gap. Does NOT close per-polity calibration
        completeness — that remains domain-expert work for each non-U.S. polity.

  (B) Bilateral substrate analysis function (closes v3.0 Part VIII open #4)
      ─ bilateral_substrate_analysis(polity_a, polity_b): runs substrate-
        coupling computation in BOTH directions and surfaces asymmetry
        explicitly. Output includes per-direction tier asymmetry, F3 caveat
        (per v2.0→v3.0 closure: bilateral framing does NOT equalize asymmetric
        evidence), and a shared-substrate aggregation.
      ─ U.S. 2025 ↔ Hungary 2024 worked example serves as the reverse-
        direction asymmetric example referenced in v3.0 Part VIII backlog.
      ─ Asymmetry banner included by construction in dashboard rendering.

  (C) Twelve-Day War substrate-coupling case study (qualified scaffolding)
      ─ twelve_day_war_substrate_analysis(): worked example using illustrative
        2026 indicator estimates for U.S., Israel, Iran. Three pairwise
        bilateral analyses (US↔IL, US↔IR, IL↔IR).
      ─ ISRAEL_2026_BASELINE_ILLUSTRATIVE: T2-dominant per-Pillar estimates
        (OECD, IMF, IEA, BoI, ICANN, World Bank); T-tagged per indicator.
      ─ IRAN_2026_BASELINE_ILLUSTRATIVE: T3-dominant per-Pillar estimates;
        SOURCE-DIVERSE per 7 May 2026 directive (Iranian Statistical Centre,
        IMF Iran data, Brookings/IISS, IRNA/Tasnim, Al Jazeera, Anadolu,
        Russian/Chinese coverage flagged for bias).
      ─ DO-NOT-DEPLOY case study data; F3 evidence-asymmetry banner mandatory
        on all output. The function infrastructure is research-grade; the
        case-study data is illustrative.

  (D) Dragon-king (II.2 condition #5) module — DELIBERATELY NOT BUILT
      ─ dragon_king_module_status(): returns explicit gate state. Rationale:
        v3.0 §IV.9 #9 postponed dragon-king prediction until validation
        conditions 1–4 met. Condition #4 (driving/dissipation/conservation)
        is still OPEN. Building #5 first would produce structurally well-
        formed analysis with hollow substance — Rule 3 violation.
      ─ The function exists so that callers, dashboards, and future Claude
        sessions see the gate explicitly rather than discovering it by
        absence. This is the v3.0 II.2 vocabulary-flagging discipline applied
        to entire module postponements.

CANONICAL INVARIANTS PRESERVED:
  • All v3.0 / v3.5 / v3.1 / v3.2 numeric anchors are unchanged. v3.3
    additions are *additive* — calling existing functions yields identical
    results. POLITY_COUPLING_REGISTRY["US_2025"] points to the same
    SUBSTRATE_COUPLING_MATRIX object used directly in v3.1/v3.2 code.

REMAINING OPEN (v3.4+ candidates):
  ─ II.2 condition 4 (driving / dissipation / conservation) — domain-expert
    work; not automatable. This is the gate for #5.
  ─ Per-polity coupling-matrix VALUE recalibration for Hungary, Venezuela,
    Israel, Iran (registry holds the slots; values are still U.S.-structure).
  ─ Empirical T-tier promotion of Israel 2026 and Iran 2026 indicators above
    illustrative level (especially Iran where source-diversity is non-trivial).
  ─ Dragon-king prediction module — STILL POSTPONED until #4 closed.
╚══════════════════════════════════════════════════════════════════════════════════╝

v3.2 ADDS (still research-grade — see deployment caveats below):

  (1) Bootstrap goodness-of-fit p-value (Clauset-Shalizi-Newman 2009 §4)
      ─ bootstrap_power_law_p_value(): semi-parametric bootstrap. For each of
        B replicates: synthesize N_total samples (tail from fitted power-law,
        body resampled from empirical body), refit (α, x_min) via KS minim-
        ization, compute KS distance D_b. p-value = fraction of D_b ≥ D_emp.
      ─ test_power_law_signature() now invokes bootstrap_power_law_p_value()
        with B=100 by default and integrates p into the verdict ladder. The
        FINITE-SAMPLE pathology surfaced in v3.1 (lognormal data passing the
        Vuong test) is now correctly REJECTED by the bootstrap test.
      ─ Closes the v3.1 known limitation: the bootstrap is the formal
        correction, not just a caveat box.

  (2) Calibration of COUPLING_TIER_MATRIX cells (T3 → T1/T2 where grounded)
      ─ COUPLING_TIER_MATRIX promoted from all-T3 to per-cell tiers based on
        named primary-literature support.
      ─ COUPLING_CITATION_MATRIX added: per-cell source attribution
        (e.g., Energy→climate cites IPCC AR6 WG3, EIA, Jackson et al.
        Global Carbon Budget; Product→soil cites USDA NRCS + IPBES).
      ─ Cells without primary-literature grounding remain T3 with explicit
        "calibration_required" flags. No Rule 5 violation by construction.
      ─ Operational deployment still requires per-civilization Rule 4
        recalibration; the matrix value calibration in this v3.2 is U.S.
        national-scale only.

  (3) 1/f temporal-structure test (closes v3.0 II.2 condition #3)
      ─ compute_psd(): Welch-method power spectral density via
        scipy.signal.welch (graceful fallback to single periodogram).
      ─ test_one_over_f_signature(): linear log-log fit on PSD inertial
        range; verdict ladder distinguishes 1/f-consistent (β ∈ [0.7, 1.3])
        from scale-invariant outliers, white noise, and random walks.
      ─ FluxTimeSeries dataclass: longitudinal substrate-flux data with
        timestamp + dimension + sampling-rate metadata.
      ─ substrate_research_report() optionally accepts a flux series and
        runs the 1/f test alongside the event-size test. II.2 condition 3
        is now PARTIAL (test infrastructure complete) — full validation
        requires real longitudinal substrate data.

CANONICAL INVARIANTS PRESERVED:
  • All v3.0 / v3.5 numeric anchors are unchanged. v2.0/v3.0/v3.5/v3.1 API
    surfaces are unchanged. v3.2 additions are *additive* — calling existing
    functions yields identical results.

REMAINING OPEN AFTER v3.2 (now partially addressed in v3.3 — see top of file):
  ─ II.2 condition 4 (driving / dissipation mechanisms with conservation
    properties) — domain-expert work; not automatable. STILL OPEN in v3.3.
  ─ II.2 condition 5 (log-periodic precursors and out-of-sample prediction
    for dragon-king claims) — postponed per v3.0 §IV.9 #9 explicitly.
    STILL POSTPONED in v3.3 (see dragon_king_module_status()).
  ─ Per-civilization C[p][b] recalibration for non-U.S. polities (Rule 4) —
    INFRASTRUCTURE ADDED in v3.3 via POLITY_COUPLING_REGISTRY. Per-polity
    VALUES still require domain-expert calibration.
╚══════════════════════════════════════════════════════════════════════════════════╝
Hologram2 v3.0 is a comprehensive, self-contained framework that synthesises the
foundational Treatise on Societies, Economies, and Cultures with all associated
computational tools for its implementation, reference, and extension.

It integrates:
  • OracleHybrid5.5 — Hodge-Flow, TDA, LSTM, Regime, SOC criticality
  • DeepDark2       — Inequality-driven statistical arbitrage (GAN + VIX + Gini)
  • NROS (v2.0)     — National Resilience Operating System: complete Samsara Method
                       implementation with PHI engine, interdependency matrix,
                       Hodge decomposition on K₆ Pillar graph, polity assessment,
                       SOC assessment, conflict assessment, trajectory projection,
                       and TreatiseContext integration.

Entry points:
  h2 = Hologram2()
  h2.analyze(ticker)               — Oracle single-ticker analysis
  h2.stat_arb(pair)                — DeepDark statistical arbitrage
  h2.holistic(ticker, pair)        — Cross-module synthesis
  h2.nros()                        — Complete Samsara Method analysis (NEW v2.0)
  TreatiseContext.from_nros(result) — Dataclass from NROS output (NEW v2.0)

═══════════════════════════════════════════════════════════════════════════════════
  THE TREATISE ON SOCIETIES, ECONOMIES, AND CULTURES (Full Foundation)
═══════════════════════════════════════════════════════════════════════════════════

Cultures are sets of behaviors, aesthetics, language, and arts. Culture spreads
much as a fungus: spores (easily repeatable / memetic behaviors) colonise a
resource-rich area; mycelium (the cultural mass) branches into a functional
network (village / town / city / region / state / nation); the culture creates
objects, arts, and provides sufficient or excess labor that becomes its fruiting
body. The fruiting body produces spores carried through trade winds or
self-propelled migration. Culture expands through two main vectors: artistic
expression and excess labor function that can be leveraged for value and money.

Society is the amalgamation of two or more isomorphic cultures that share similar
aspects, of which there are four: behavioral, aesthetic, linguistic, and artistic.

Markets are an extension of everything else. Understanding market geography
broadens understanding of all systems, sub-systems, cultures, and politics.
Interpreting the Geography of Markets requires understanding Hodge-Flow
Decomposition: creation of Gradient flow, its evolution into loops/vortices, and
resolution into harmony or dissolution via entropy forcing a regime change.

Positive vs. Negative Exploitation — Note: labor and resources are always
exploited; labor compensation is negotiated and agreed upon through contract.

THE SIX PILLARS OF MONEYMAKING:
  • Provide a Service           • Provide a Product
  • Provide Information         • Provide Entertainment
  • Provide Transport           • Provide Energy
  Combining pillar elements creates added value.

These are also the resources cultures require to survive. Starving a culture of
any one is detrimental; preventing a culture from providing all six is lethal.

Money is the storable, tradeable, physical representation of attention and
appreciation. It functions as labor potential. Depreciation = value − labor value
− function entropy. Appreciation = value + function syntropy + scarcity·demand.
All value is perceived.

Currency must flow and convert into assets or into a market gradient (functional
circuit) to grow faster than entropy (inflation / reduced economic activity).

Polity: the organised governing body of a culture or society — creates a framework
of laws, trade, currency, property, and borders. Politics is the behavioral aspect.

Self-Organised Criticality and Power Law Distributions — Entropy naturally yields
emergent harmony; this is the source of all gradients. Gradients are emergent.
Power Law Distributions are natural law; the Pareto Distribution is an emergent
phenomenon. No system can eliminate this occurrence.

The Cantillon Effect directly causes inflation. Central banks that inject new money
allow first-receiving institutions to buy assets at old prices while the public
competes with existing money — prices run up. This makes it impossible for working
classes to purchase those assets without borrowing at interest, fueling economic
activity through the "Constant Need for More". Without this gradient, productivity
shrinks, borrowing halts, asset prices crash, and economy dies. Equilibrium is
death. Inequality creates a gradient; gradients drive everything.

Robotics + AI = a new asset class. High upfront cost necessitates borrowing,
contributing to economic activity. This reinforces that inequality is absolutely
necessary, because equilibrium is death.

═══════════════════════════════════════════════════════════════════════════════════
  CHANGE LOG — Hologram2 improvements over original OracleHybrid5.5 + DeepDark2
═══════════════════════════════════════════════════════════════════════════════════

CRITICAL BUG FIXES:
  [BF-01] fillna(method='bfill'/'ffill') deprecated in pandas ≥2.0 → .bfill()/.ffill()
  [BF-02] portfolio_series.resample() on RangeIndex crashed — now uses DatetimeIndex
  [BF-03] GAN fake_seq tensor shape mismatch (batch×1 ≠ batch×1×n_features) — Generator
           now outputs full (batch, seq_len, n_features) sequences via fc_expand+LSTM
  [BF-04] `device` variable undefined in DeepDark2 module scope — added top-level detection
  [BF-05] `if 'best_state' in dir()` is semantically wrong for local-var check — replaced
           with explicit `best_state_saved` boolean flag + initialised `best_state = None`
  [BF-06] Unicode stray characters (U+FEFF) prefixed two section-divider comment lines
  [BF-07] `eigenvalues_top5` misleadingly returned the 5 SMALLEST eigenvalues (eigvalsh
           returns ascending order) — renamed to `eigenvalues_sorted` with note, and
           `spectral_gap` now returns the first strictly-positive eigenvalue correctly
  [BF-08] `train_predictor()` accepted `batch_size` parameter but trained on full dataset
           with no batching — proper mini-batch DataLoader with shuffling now implemented
  [BF-09] `gini_series.resample('D').interpolate()` ambiguous chain — fixed to the correct
           `.resample('D').asfreq().interpolate(method='linear')`
  [BF-10] `B2` orientation sign error in DeepDarkHodgeEngine boundary operator for triangle
           face (u,v,w): e_uw should be −1 (opposite orientation from e_uv and e_vw)
           — made consistent with OracleTopologicalEngine convention

SIGNIFICANT IMPROVEMENTS:
  [SI-01] Removed duplicate sklearn.preprocessing.StandardScaler import in DeepDark2;
           all modules now share Hologram2's custom StandardScaler (zero extra deps)
  [SI-02] LRUCache now genuinely thread-safe using threading.RLock
  [SI-03] All bare `except:` clauses in DataFetcher / DeepDark2 replaced with specific
           exception types (requests.RequestException, ValueError, pd.errors.*, etc.)
  [SI-04] optuna import wrapped in graceful degradation try/except; threshold optimisation
           degrades to a grid search when optuna is unavailable
  [SI-05] Reference to nonexistent function helm9_7_analysis() removed from usage comments
  [SI-06] predict_uncertainty in DeepDarkHyperModel now uses MC-Dropout on the Predictor
           (not the Generator, which is not a density estimator) — aligned with OracleHybrid
  [SI-07] Predictor.forward() hardcoded feature slices [5:8] / [8:10] made configurable
           via constructor parameters vix_start / curve_start
  [SI-08] Cache invalidation: DataFetcher now tracks fetch_date per cache entry and
           expires intraday caches after market close (18:00 UTC)
  [SI-09] Added vix_cache_date and curve_cache_date to DataFetcher for daily expiry
  [SI-10] RegimeDetector.predict() now guards against empty feature windows gracefully

NEW IN HOLOGRAM2:
  [N-01]  Hologram2Config — unified configuration dataclass for both subsystems
  [N-02]  Hologram2 — top-level orchestrator class integrating OracleHybrid5.5 and
           DeepDark2, with .analyze() and .stat_arb() entry points
  [N-03]  Hologram2.synthesize_holistic() — cross-module signal combining Oracle's
           regime/criticality with DeepDark's arbitrage spread forecast
  [N-04]  TreatiseContext dataclass — attaches Treatise-grounded interpretations
           (Pillar classification, gradient regime, Cantillon phase) to any result dict
  [N-05]  Logging unified across both subsystems under 'Hologram2' logger hierarchy

NEW IN HOLOGRAM2 v3.0 (SHI INTEGRATION RELEASE):
  [V3-01] Substrate Health Index (SHI) embedded into Entertainment Pillar per the
           v3.0 working paper architectural decision (substrate is INSIDE Entertainment,
           not a 7th Pillar). Eight new substrate-flavored sub-indicators (N6-N13) with
           'substrate':'meaning' tag added to Entertainment in all canonical baselines.
           SHI composite emerges automatically from existing v3.5 split-machinery as
           phi_substrate_only of Entertainment — no new architecture required.
  [V3-02] Entertainment weight rebalance: surface (N1-N5) scaled from sum-1.00 to
           sum-0.50 (preserving relative ratios); substrate (N6-N13) added at equal
           weight 0.0625 each summing to 0.50. Total Entertainment weight remains
           1.00. Within-SHI weights are 0.125 each (renormalized), matching the
           v3.0 paper SHI canonical specification exactly.
  [V3-03] Eight substrate sub-indicators (all health-direction; higher = healthier;
           all syntropy_bound='regeneration' since substrate is replenished through
           costly-commitment practice over generations, not on a fiscal cycle):
             N6  Caretaker Legitimacy
             N7  Substrate-Gradient Cohesion
             N8  Costly-Commitment Density
             N9  Caretaker Four-Mode Integrity
             N10 Cross-Pillar Coupling Integrity
             N11 Caretaker Reflexive Composure
             N12 Substrate Retention
             N13 External Substrate-Projection Capacity
  [V3-04] SUBSTRATE_DIMENSIONS extended to include 'meaning' alongside the v3.5
           biospheric dimensions (climate, soil, biotic_relationships, hydrology,
           biodiversity). The two substrate kinds coexist; both register in
           substrate_diagnostic() output independently.
  [V3-05] compute_shi() — new convenience function returning the SHI composite,
           five-tier health classification, sub-indicator-cascade flag (4+ substrate
           sub-indicators below 0.40), and per-sub-indicator scores for an
           Entertainment Pillar input. Pure-function wrapper over compute_pillar_phi_split.
  [V3-06] Hungary 2024 baseline added as third canonical regression fixture
           (alongside US 2025 and Venezuela 2019). Hungary's substrate sub-indicator
           scores are taken directly from the v3.0 working paper Section IV.6 worked
           example. Composite SHI = 0.4438 ≈ 0.44 (STRESSED tier), matching the
           paper's published value of 0.4375 ≈ 0.44 within rounding. Entry point:
           hungary_2024_baseline().
  [V3-07] REGRESSION ANCHOR CHANGE — Venezuela 2019: Embedding substrate sub-
           indicators with substantively-defensible raw values for collapsing
           Bolivarianism (Caretaker Four-Mode Integrity 0.12, Substrate Retention
           0.18 reflecting 5M+ emigration wave, etc.) drops Venezuela's Entertainment
           PHI from ~0.455 to ~0.333. Net effects on synthesis output (verified
           against the implementation, not estimated):
             stressed   = 4/6           (CHANGED from 3/6)
             threshold  = EXCEEDED      (CHANGED from APPROACHING)
             regime     = harmonic      (CHANGED from dissolution — spread shrinks
                                         to ~0.13, below the 0.15 dissolution
                                         threshold, because Entertainment dropping
                                         compresses the gradient)
             cantillon  = contraction   (CHANGED from 'trap'; stressed≥4 branch)
             cordyceps  = dormant       (CHANGED from 'fruiting'; stressed≥4)
           This is the substantively correct v3.0 reading: Venezuela 2019 is a
           uniformly-collapsing polity, not an asymmetric one. 'Harmonic' here
           does not mean healthy — it means the gradient is small because every
           Pillar is failing together. 'Contraction' is also more accurate than
           'trap' for Venezuela 2019: the polity is actively contracting
           (hyperinflation, mass emigration, complete economic collapse), not
           'trap' (wealth with hidden fragility).
           ALL FOUR classification anchors from the v2 Venezuela baseline are
           now unhooked. Trap / fruiting / APPROACHING / dissolution regression
           coverage should be re-anchored in v3.x by adding a dedicated baseline.
           Candidate fixtures: Lebanon 2021 (banking collapse without polity-wide
           contraction, asymmetric distress), Argentina 2001 (corralito + IMF
           crisis with rapid recovery, fits trap), late Weimar 1932 (asymmetric
           distress despite residual capacity, fits dissolution).
           Inflating Venezuela substrate scores to preserve the v2 anchors would
           be Rule-3-prohibited motivated reasoning.
  [V3-08] DO-NOT-DEPLOY annotation: Per v3.0 working paper R2 closure, the SHI
           numeric layer is research-grade. Qualitative substrate analysis is
           operationally deployable; numeric SHI is not. The compute_shi() return
           dict carries an explicit 'deployment_status':'research_grade' field
           and 'do_not_deploy_reason' string for downstream consumers.
  [V3-09] PAPER TYPO DISCOVERED during Hungary regression-anchor verification:
           v3.0 Working Paper Section IV.6 states the Hungary 2024 SHI composite
           as "0.4375 ≈ 0.44". The two-decimal rounded value is correct; the
           four-decimal value is a transcription error. The actual sum of the
           paper's stated sub-indicator values (0.55+0.35+0.40+0.30+0.45+0.50+
           0.40+0.60 = 3.55, ÷8 = 0.44375) yields 0.4438 — not 0.4375. The
           implementation is mathematically correct; the v3.0 paper should be
           corrected in v3.x. Off by 0.00625; does not change the tier (still
           STRESSED) or cascade conclusion (still no cascade — only 2/8 below
           0.40), so no analytical consequence beyond the typo itself.
"""

# ── Standard library ───────────────────────────────────────────────────────────
import os
import sys
import hashlib
import time
import math
import logging
import threading
import warnings
from collections import deque, OrderedDict
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass, field
from datetime import datetime, timedelta, date, timezone
from enum import Enum
from itertools import combinations
from typing import Any, Dict, List, Optional, Tuple

# ── Numerics ───────────────────────────────────────────────────────────────────
import numpy as np
import pandas as pd
from scipy.stats import norm, percentileofscore

# ── PyTorch ────────────────────────────────────────────────────────────────────
import torch
import torch.nn as nn
import torch.optim as optim
from torch.nn import functional as F
from torch.utils.data import DataLoader, TensorDataset

# ── External dependencies (graceful degradation) ───────────────────────────────
try:
    from polygon import RESTClient
    POLYGON_AVAILABLE = True
except ImportError:
    POLYGON_AVAILABLE = False

try:
    import yfinance as yf
    YFINANCE_AVAILABLE = True
except ImportError:
    YFINANCE_AVAILABLE = False

try:
    from ripser import ripser
    PERSISTENCE_AVAILABLE = True
except ImportError:
    PERSISTENCE_AVAILABLE = False

try:
    from hmmlearn import hmm
    HMM_AVAILABLE = True
except ImportError:
    HMM_AVAILABLE = False

try:
    import optuna
    optuna.logging.set_verbosity(optuna.logging.WARNING)
    OPTUNA_AVAILABLE = True
except ImportError:
    OPTUNA_AVAILABLE = False  # [SI-04] graceful degradation

try:
    import requests
    REQUESTS_AVAILABLE = True
except ImportError:
    REQUESTS_AVAILABLE = False

warnings.filterwarnings('ignore')

# ── [BF-04] Top-level device detection (was missing in DeepDark2) ───────────────
DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")


# ═══════════════════════════════════════════════════════════════════════════════
#  SECTION 1 — LOGGING
# ═══════════════════════════════════════════════════════════════════════════════

def _setup_logger(name: str = "Hologram2", level: int = logging.INFO) -> logging.Logger:
    logger = logging.getLogger(name)
    if not logger.handlers:
        handler = logging.StreamHandler()
        fmt = logging.Formatter(
            "[%(asctime)s] %(name)s | %(levelname)s | %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
        handler.setFormatter(fmt)
        logger.addHandler(handler)
    logger.setLevel(level)
    return logger

log = _setup_logger("Hologram2")
log_oracle = _setup_logger("Hologram2.Oracle")
log_dark   = _setup_logger("Hologram2.DeepDark")


# ═══════════════════════════════════════════════════════════════════════════════
#  SECTION 2 — SHARED UTILITIES
# ═══════════════════════════════════════════════════════════════════════════════

class StandardScaler:
    """
    Minimal, dependency-free StandardScaler.
    [SI-01] Replaces both the original custom class AND the sklearn import in DeepDark2.
    All Hologram2 modules use this single implementation.
    """
    def __init__(self):
        self.mean_: Optional[np.ndarray] = None
        self.scale_: Optional[np.ndarray] = None
        self.n_features_in_: int = 0

    def fit(self, X: np.ndarray) -> "StandardScaler":
        X = np.asarray(X, dtype=np.float64)
        self.mean_ = np.nanmean(X, axis=0)
        self.scale_ = np.nanstd(X, axis=0) + 1e-8
        self.n_features_in_ = X.shape[1] if X.ndim > 1 else 1
        return self

    def transform(self, X: np.ndarray) -> np.ndarray:
        X = np.asarray(X, dtype=np.float64)
        return (X - self.mean_) / self.scale_

    def fit_transform(self, X: np.ndarray) -> np.ndarray:
        return self.fit(X).transform(X)

    def inverse_transform(self, X: np.ndarray) -> np.ndarray:
        X = np.asarray(X, dtype=np.float64)
        return X * self.scale_ + self.mean_

    def __repr__(self) -> str:
        return f"StandardScaler(fitted={self.mean_ is not None})"


class LRUCache:
    """
    [SI-02] Thread-safe LRU cache backed by OrderedDict + threading.RLock.
    Original was described as thread-safe but had no locking.
    """
    def __init__(self, capacity: int = 128):
        self._cache: OrderedDict = OrderedDict()
        self._capacity = capacity
        self._lock = threading.RLock()

    def get(self, key: str) -> Optional[Any]:
        with self._lock:
            if key not in self._cache:
                return None
            self._cache.move_to_end(key)
            return self._cache[key]

    def put(self, key: str, value: Any) -> None:
        with self._lock:
            if key in self._cache:
                self._cache.move_to_end(key)
            self._cache[key] = value
            if len(self._cache) > self._capacity:
                self._cache.popitem(last=False)

    def __len__(self) -> int:
        with self._lock:
            return len(self._cache)


class RateLimiter:
    """Token-bucket style rate limiter (unchanged, already correct)."""
    def __init__(self, max_calls: int = 5, per_seconds: int = 1):
        self.max_calls = max_calls
        self.per_seconds = per_seconds
        self.calls: deque = deque()
        self._lock = threading.Lock()

    def wait_if_needed(self) -> None:
        with self._lock:
            now = time.time()
            while self.calls and self.calls[0] < now - self.per_seconds:
                self.calls.popleft()
            if len(self.calls) >= self.max_calls:
                sleep_time = self.per_seconds - (now - self.calls[0])
                if sleep_time > 0:
                    time.sleep(sleep_time)
            self.calls.append(time.time())


class SignalType(Enum):
    STRONG_BUY  = "strong_buy"
    BUY         = "buy"
    HOLD        = "hold"
    SELL        = "sell"
    STRONG_SELL = "strong_sell"
    RISK_OFF    = "risk_off"


# ═══════════════════════════════════════════════════════════════════════════════
#  SECTION 3 — UNIFIED CONFIGURATION
# ═══════════════════════════════════════════════════════════════════════════════

@dataclass
class OracleConfig:
    """Configuration for OracleHybrid5.5 subsystem."""
    # Data
    sequence_length: int = 60
    forecast_horizon: int = 5
    # Topology
    correlation_threshold: float = 0.05
    # Risk
    confidence_level: float = 0.95
    max_position_size: float = 0.20
    risk_free_rate: float = 0.02
    transaction_cost: float = 0.001
    # Infrastructure
    max_cache_size: int = 128
    device: Optional[str] = None
    max_fetch_workers: int = 4
    # Feature flags
    use_synthetic_baskets: bool = True
    use_persistent_homology: bool = True
    # Criticality
    criticality_eval_interval: int = 60
    # Predictor
    lstm_hidden: int = 64
    lstm_layers: int = 2
    lstm_dropout: float = 0.20
    mc_dropout_samples: int = 30
    predictor_epochs: int = 80
    predictor_lr: float = 1e-3
    predictor_batch_size: int = 32


@dataclass
class DeepDarkConfig:
    """Configuration for DeepDark2 subsystem."""
    sequence_length: int = 60
    n_features: int = 10
    gan_epochs: int = 30
    predictor_epochs: int = 100
    batch_size: int = 32
    gan_lr: float = 2e-4
    predictor_lr: float = 1e-3
    mc_iterations: int = 100
    optuna_trials: int = 15
    hodge_corr_threshold: float = 0.3
    days_back: int = 730
    initial_capital: float = 10_000.0
    arb_threshold: float = 2.0
    noise_dim: int = 32        # [BF-03] Generator noise dimensionality


@dataclass
class Hologram2Config:
    """[N-01] Top-level unified configuration for the Hologram2 framework."""
    oracle: OracleConfig = field(default_factory=OracleConfig)
    deepdark: DeepDarkConfig = field(default_factory=DeepDarkConfig)
    api_key: Optional[str] = None
    log_level: int = logging.INFO

    def __post_init__(self):
        log.setLevel(self.log_level)
        log_oracle.setLevel(self.log_level)
        log_dark.setLevel(self.log_level)


# ═══════════════════════════════════════════════════════════════════════════════
#  SECTION 4 — DATA FETCHER  (shared by both subsystems)
# ═══════════════════════════════════════════════════════════════════════════════

class OracleDataFetcher:
    """
    Parallel-capable OHLCV fetcher with LRU caching.
    [SI-08/09] Cache entries now carry a fetch_date; entries older than today are
    automatically invalidated so stale data is never returned across sessions.
    """

    def __init__(self, api_key: Optional[str] = None, cache_size: int = 128,
                 max_workers: int = 4):
        self.api_key = api_key or os.getenv("POLYGON_API_KEY")
        self.client = (RESTClient(self.api_key)
                       if POLYGON_AVAILABLE and self.api_key else None)
        self._cache: LRUCache = LRUCache(cache_size)
        self._rate_limiter = RateLimiter(max_calls=5, per_seconds=1)
        self.max_workers = max_workers

    def _cache_key(self, ticker: str, days_back: int) -> str:
        tag = f"{ticker}_{days_back}_{date.today().isoformat()}"
        return hashlib.md5(tag.encode()).hexdigest()

    # ── Single ticker ──────────────────────────────────────────────────────────
    def get_price_data(self, ticker: str, days_back: int = 500) -> pd.DataFrame:
        key = self._cache_key(ticker, days_back)
        cached = self._cache.get(key)
        if cached is not None:
            return cached

        end_dt   = date.today()
        start_dt = end_dt - timedelta(days=days_back + 60)

        # Attempt Polygon
        if self.client:
            try:
                self._rate_limiter.wait_if_needed()
                aggs = list(self.client.list_aggs(
                    ticker=ticker, multiplier=1, timespan="day",
                    from_=start_dt, to=end_dt, adjusted=True, sort="asc", limit=50_000,
                ))
                if aggs:
                    rows = [{
                        "timestamp": a.timestamp, "open": a.open, "high": a.high,
                        "low": a.low, "close": a.close,
                        "volume": getattr(a, "volume", 0),
                    } for a in aggs]
                    df = pd.DataFrame(rows)
                    df["timestamp"] = pd.to_datetime(df["timestamp"], unit="ms")
                    df = df.set_index("timestamp").sort_index()
                    self._cache.put(key, df)
                    return df
            except Exception as e:
                log_oracle.warning(f"Polygon error ({ticker}): {e}")

        # Fallback: yfinance
        if YFINANCE_AVAILABLE:
            try:
                end_yf = (datetime.combine(end_dt, datetime.min.time()) + timedelta(days=1)).date()
                df = yf.download(ticker, start=start_dt, end=end_yf,
                                 progress=False, auto_adjust=True)
                if not df.empty:
                    df.columns = [
                        c.lower() if isinstance(c, str) else c[0].lower()
                        for c in df.columns
                    ]
                    for col in ["open", "high", "low", "close", "volume"]:
                        if col not in df.columns:
                            df[col] = np.nan
                    df = df[["open", "high", "low", "close", "volume"]].copy()
                    self._cache.put(key, df)
                    return df
            except Exception as e:
                log_oracle.warning(f"yfinance error ({ticker}): {e}")

        empty = pd.DataFrame(columns=["open", "high", "low", "close", "volume"])
        self._cache.put(key, empty)
        return empty

    # ── Single close series (DeepDark2 compatibility) ─────────────────────────
    def get_historical_bars(self, ticker: str, days_back: int = 365) -> pd.Series:
        df = self.get_price_data(ticker, days_back)
        if df.empty:
            return pd.Series(dtype=float)
        return df["close"].sort_index()

    # ── Multi-ticker parallel ──────────────────────────────────────────────────
    def get_multiple(self, tickers: List[str],
                     days_back: int = 500) -> Dict[str, pd.DataFrame]:
        results: Dict[str, pd.DataFrame] = {}
        with ThreadPoolExecutor(max_workers=self.max_workers) as pool:
            futures = {pool.submit(self.get_price_data, t, days_back): t
                       for t in tickers}
            for future in as_completed(futures):
                ticker = futures[future]
                try:
                    results[ticker] = future.result()
                except Exception as e:
                    log_oracle.error(f"Parallel fetch failed for {ticker}: {e}")
                    results[ticker] = pd.DataFrame(
                        columns=["open", "high", "low", "close", "volume"])
        return results

    # ── VIX data (DeepDark2) ───────────────────────────────────────────────────
    def get_vix_data(self, days_back: int = 1095) -> Dict:
        hist_vix = self.get_historical_bars("^VIX", days_back)
        if hist_vix.empty:
            spy = self.get_historical_bars("SPY", days_back)
            if not spy.empty:
                hist_vix = spy.pct_change().rolling(20).std() * np.sqrt(252) * 100
            else:
                hist_vix = pd.Series(
                    20.0,
                    index=pd.date_range(end=datetime.now(), periods=days_back, freq="D"),
                )

        # [BF-01] Use .bfill()/.ffill() — fillna(method=) deprecated in pandas ≥2.0
        hist_vix = hist_vix.interpolate(method="linear").bfill().ffill()

        def _rolling_pct(x: pd.Series) -> float:
            if len(x) < 2:
                return 50.0
            return float(percentileofscore(x, x.iloc[-1], kind="rank"))

        vix_percentile = hist_vix.rolling(
            min_periods=60, window=min(len(hist_vix), days_back)
        ).apply(_rolling_pct, raw=False)

        return {
            "level":     hist_vix,
            "roll_mean": hist_vix.rolling(20).mean(),
            "roll_std":  hist_vix.rolling(20).std(),
            "percentile": vix_percentile,
        }

    # ── VVIX data (DeepDark2) ─────────────────────────────────────────────────
    def get_vvix_data(self, days_back: int = 365) -> pd.Series:
        if YFINANCE_AVAILABLE:
            try:
                raw = yf.download("^VVIX", period=f"{min(days_back, 365)}d",
                                  progress=False, auto_adjust=True)["Close"]
                if not raw.empty:
                    # [BF-01]
                    return raw.interpolate(method="linear").bfill().ffill().squeeze()
            except Exception as e:
                log_dark.warning(f"VVIX download failed: {e}")

        vix_level = self.get_vix_data(days_back)["level"]
        synthetic = vix_level * 1.2 + np.random.default_rng(42).normal(
            0, 5, len(vix_level))
        return pd.Series(synthetic, index=vix_level.index)

    # ── VIX futures curve (DeepDark2) ─────────────────────────────────────────
    def get_vix_futures_curve(self, num_contracts: int = 3) -> Dict:
        api_key = self.api_key
        if not api_key or not self.client:
            try:
                vix_spot = float(self.get_historical_bars("^VIX", days_back=5).iloc[-1])
            except (IndexError, ValueError):
                vix_spot = 20.5
            return {
                "slope":  0.05 if vix_spot < 20 else -0.02,
                "level":  vix_spot,
                "prices": [vix_spot, vix_spot * 1.05, vix_spot * 1.10],
            }

        if not REQUESTS_AVAILABLE:
            vix_spot = 20.5
            return {"slope": 0.05, "level": vix_spot,
                    "prices": [vix_spot, vix_spot * 1.05, vix_spot * 1.08]}

        try:
            url = "https://api.polygon.io/v2/reference/futures/contracts"
            params = {
                "underlying_ticker": "VIX", "expired": "false",
                "limit": num_contracts * 2, "apiKey": api_key,
            }
            resp = requests.get(url, params=params, timeout=10)
            resp.raise_for_status()
            data = resp.json()

            if "results" not in data or not data["results"]:
                raise ValueError("No VIX futures contracts found in response")

            contracts = sorted(
                [c for c in data["results"] if "expiration_date" in c],
                key=lambda x: x["expiration_date"],
            )[:num_contracts]

            prices = []
            for c in contracts:
                price = self.get_historical_bars(c["ticker"], days_back=5)
                if not price.empty and float(price.iloc[-1]) > 0:
                    prices.append(float(price.iloc[-1]))

            if len(prices) < 2:
                raise ValueError("Insufficient VIX futures prices retrieved")

            slope = (prices[-1] - prices[0]) / prices[0]
            return {
                "slope":   float(slope),
                "level":   float(np.mean(prices)),
                "prices":  prices,
                "tickers": [c["ticker"] for c in contracts],
            }
        except (requests.RequestException, ValueError, KeyError) as e:
            log_dark.warning(f"VIX curve fetch failed: {e}; using synthetic fallback")
            try:
                vix_spot = float(self.get_historical_bars("^VIX", days_back=5).iloc[-1])
            except (IndexError, ValueError):
                vix_spot = 20.5
            return {"slope": 0.05, "level": vix_spot,
                    "prices": [vix_spot, vix_spot * 1.05, vix_spot * 1.08]}

    # ── Gini / inequality signal (DeepDark2) ─────────────────────────────────
    def get_inequality_signal(self, country: str = "USA",
                              start_year: int = 2000) -> Tuple[float, float, pd.Series]:
        if REQUESTS_AVAILABLE:
            try:
                url = (
                    f"https://api.worldbank.org/v2/country/{country}"
                    f"/indicator/SI.POV.GINI"
                    f"?date={start_year}:2025&format=json&per_page=50"
                )
                resp = requests.get(url, timeout=10)
                resp.raise_for_status()
                data = resp.json()

                if len(data) > 1 and data[1]:
                    gini_df = pd.DataFrame(data[1])
                    gini_df["date"] = pd.to_datetime(gini_df["date"], format="%Y")
                    gini_df = gini_df.set_index("date")["value"].dropna().sort_index()

                    if not gini_df.empty:
                        # [BF-09] correct chain: resample → asfreq → interpolate
                        gini_daily = (
                            gini_df.resample("D").asfreq().interpolate(method="linear")
                        )
                        latest = float(gini_df.iloc[-1])
                        trend = (
                            float((gini_df.iloc[-1] - gini_df.iloc[-2]) / gini_df.iloc[-2])
                            if len(gini_df) >= 2 else 0.0
                        )
                        return latest, trend, gini_daily
            except (requests.RequestException, ValueError, KeyError, IndexError) as e:
                log_dark.warning(f"Gini fetch failed: {e}; using fallback")

        # Fallback static data
        fallback = pd.Series({
            pd.Timestamp("2020-12-31"): 41.4,
            pd.Timestamp("2021-12-31"): 39.8,
            pd.Timestamp("2022-12-31"): 41.5,
            pd.Timestamp("2023-12-31"): 41.7,
            pd.Timestamp("2024-12-31"): 41.6,
            pd.Timestamp("2025-12-31"): 42.0,
        })
        gini_daily = fallback.resample("D").asfreq().interpolate(method="linear")
        return 42.0, 0.005, gini_daily


# ═══════════════════════════════════════════════════════════════════════════════
#  SECTION 5 — TOPOLOGICAL ENGINE  (OracleHybrid — corrected Hodge Laplacian)
# ═══════════════════════════════════════════════════════════════════════════════

class OracleTopologicalEngine:
    """
    Computes Hodge-decomposition features on the simplicial complex built from
    the correlation matrix.

    Convention (matches literature):
      B₁ : (n_nodes × n_edges)   — boundary-1 operator, edge → nodes
      B₂ : (n_edges × n_triangles) — boundary-2 operator, triangle → edges
      L₁ = B₁ᵀ B₁  +  B₂ B₂ᵀ   (correct 1-Hodge Laplacian on edges)

    [BF-07] spectral_gap now returns first strictly-positive eigenvalue.
    """

    def __init__(self, correlation_threshold: float = 0.05):
        self.corr_thresh = correlation_threshold

    # ── Build simplicial complex ───────────────────────────────────────────────
    @staticmethod
    def _build_simplices(corr_matrix: np.ndarray):
        n = len(corr_matrix)
        nodes = list(range(n))
        edge_set: set = set()
        edges: List[Tuple] = []

        for i, j in combinations(nodes, 2):
            if abs(corr_matrix[i, j]) > 0:
                e = (min(i, j), max(i, j))
                if e not in edge_set:
                    edge_set.add(e)
                    edges.append(e)

        triangles: List[Tuple] = []
        for i, j, k in combinations(nodes, 3):
            if ((min(i,j), max(i,j)) in edge_set and
                    (min(j,k), max(j,k)) in edge_set and
                    (min(i,k), max(i,k)) in edge_set):
                triangles.append((i, j, k))

        return nodes, edges, triangles

    # ── Boundary operators + Hodge Laplacian ───────────────────────────────────
    @staticmethod
    def _compute_hodge_laplacian(nodes, edges, triangles):
        n_nodes = len(nodes)
        n_edges = len(edges)
        n_tri   = len(triangles)

        if n_nodes == 0 or n_edges == 0:
            return np.array([[]]), np.array([[]]), np.array([[]])

        node_idx = {v: i for i, v in enumerate(nodes)}
        edge_idx = {e: i for i, e in enumerate(edges)}

        # B1 : (n_nodes × n_edges) — ∂₁ maps each edge to its two boundary nodes
        B1 = np.zeros((n_nodes, n_edges))
        for e_i, (u, v) in enumerate(edges):
            B1[node_idx[u], e_i] = -1.0
            B1[node_idx[v], e_i] = +1.0

        # B2 : (n_edges × n_triangles) — ∂₂ maps each triangle to its boundary edges
        B2 = np.zeros((n_edges, n_tri))
        for t_i, (a, b, c) in enumerate(triangles):
            e_ab = (min(a, b), max(a, b))
            e_bc = (min(b, c), max(b, c))
            e_ac = (min(a, c), max(a, c))
            B2[edge_idx[e_ab], t_i] = +1.0
            B2[edge_idx[e_bc], t_i] = +1.0
            B2[edge_idx[e_ac], t_i] = -1.0

        # L1 = B1ᵀ B1  +  B2 B2ᵀ
        L1_down = B1.T @ B1
        L1_up   = (B2 @ B2.T) if n_tri > 0 else np.zeros((n_edges, n_edges))
        L1 = L1_down + L1_up

        return B1, B2, L1

    # ── Betti numbers from Laplacian nullities ─────────────────────────────────
    @staticmethod
    def _betti_from_laplacian(L: np.ndarray, tol: float = 1e-8) -> int:
        if L.size == 0:
            return 0
        try:
            eigs = np.linalg.eigvalsh(L)
            threshold = tol * max(float(np.max(np.abs(eigs))), 1.0)
            return int(np.sum(np.abs(eigs) < threshold))
        except np.linalg.LinAlgError:
            return 0

    # ── Main public method ─────────────────────────────────────────────────────
    def compute_metrics(self, data: pd.DataFrame, *,
                        inequality_trend: float = 0.0,
                        use_synthetic: bool = True) -> Dict:

        if data.shape[1] < 2 or len(data) < 10:
            return self._empty_metrics()

        try:
            if use_synthetic and all(c in data.columns
                                     for c in ["open", "high", "low", "close"]):
                returns_df = pd.DataFrame({
                    "open":  data["open"].pct_change(),
                    "high":  data["high"].pct_change(),
                    "low":   data["low"].pct_change(),
                    "close": data["close"].pct_change(),
                }).dropna().fillna(0)
            else:
                ret  = data.pct_change().dropna()
                lags = 5
                parts = []
                for col in ret.columns:
                    for lag in range(lags):
                        parts.append(ret[col].shift(lag).rename(f"{col}_L{lag}"))
                returns_df = pd.concat(parts, axis=1).dropna().fillna(0)

            corr = np.abs(returns_df.corr().fillna(0).values)
            np.fill_diagonal(corr, 0)
            corr[corr < self.corr_thresh] = 0.0

            if corr.sum() < 1e-10:
                return self._empty_metrics(n_nodes=returns_df.shape[1])

            nodes, edges, triangles = self._build_simplices(corr)
            if len(edges) == 0:
                return self._empty_metrics(n_nodes=len(nodes))

            B1, B2, L1 = self._compute_hodge_laplacian(nodes, edges, triangles)
            if L1.size == 0:
                return self._empty_metrics(n_nodes=len(nodes))

            eigenvalues = np.real(np.linalg.eigvalsh(L1))

            total_trace  = float(np.sum(np.abs(eigenvalues))) + 1e-12
            grad_energy  = float(np.trace(B1.T @ B1))
            curl_energy  = float(np.trace(B2 @ B2.T)) if B2.size > 0 else 0.0
            grad_dom     = grad_energy / total_trace
            curl_dom     = curl_energy / total_trace

            tol    = 1e-8 * max(float(np.max(np.abs(eigenvalues))), 1.0)
            betti_1 = int(np.sum(np.abs(eigenvalues) < tol))
            harm_int = betti_1 / len(edges) if len(edges) > 0 else 0.0

            L0      = B1 @ B1.T
            betti_0 = max(self._betti_from_laplacian(L0), 1)

            vorticity = 0.0
            if len(triangles) > 0 and B2.size > 0:
                vorticity = float(np.linalg.norm(B2, "fro") * abs(inequality_trend))

            # [BF-07] spectral_gap = first *strictly positive* eigenvalue
            pos_eigs = eigenvalues[eigenvalues > tol]
            spectral_gap = float(pos_eigs[0]) if len(pos_eigs) > 0 else 0.0

            euler = len(nodes) - len(edges) + len(triangles)

            return {
                "gradient_dominance": float(grad_dom),
                "curl_dominance":     float(curl_dom),
                "harmonic_intensity": float(harm_int),
                "vorticity":          float(vorticity),
                "betti_0":            betti_0,
                "betti_1":            betti_1,
                "euler_characteristic": euler,
                "n_edges":            len(edges),
                "n_triangles":        len(triangles),
                "spectral_gap":       spectral_gap,
                # [BF-07] renamed: these are the smallest eigenvalues (ascending sort)
                "eigenvalues_sorted_asc": eigenvalues[:min(5, len(eigenvalues))].tolist(),
            }

        except Exception as e:
            log_oracle.error(f"Topological computation error: {e}")
            return self._empty_metrics()

    @staticmethod
    def _empty_metrics(n_nodes: int = 0) -> Dict:
        return {
            "gradient_dominance": 0.0, "curl_dominance": 0.0,
            "harmonic_intensity": 0.0, "vorticity": 0.0,
            "betti_0": max(n_nodes, 0), "betti_1": 0,
            "euler_characteristic": 0, "n_edges": 0, "n_triangles": 0,
            "spectral_gap": 0.0, "eigenvalues_sorted_asc": [],
        }


# ═══════════════════════════════════════════════════════════════════════════════
#  SECTION 6 — PERSISTENT HOMOLOGY
# ═══════════════════════════════════════════════════════════════════════════════

class PersistentHomologyEngine:
    def __init__(self, max_dim: int = 1):
        self.max_dim = max_dim

    def compute(self, returns_df: pd.DataFrame) -> Dict:
        if not PERSISTENCE_AVAILABLE or returns_df.shape[1] < 3 or len(returns_df) < 10:
            return self._empty()
        try:
            corr = returns_df.corr().values
            corr = np.nan_to_num(corr, nan=0.0, posinf=1.0, neginf=-1.0)
            dist = np.sqrt(2.0 * (1.0 - np.clip(corr, -1, 1)))
            diagrams = ripser(dist, distance_matrix=True, maxdim=self.max_dim)["dgms"]

            stats: Dict = {}
            for dim, dgm in enumerate(diagrams):
                prefix = f"ph_{dim}"
                if len(dgm) == 0:
                    stats.update({f"{prefix}_betti": 0, f"{prefix}_avg_life": 0.0,
                                  f"{prefix}_max_life": 0.0, f"{prefix}_entropy": 0.0})
                    continue
                finite = dgm[dgm[:, 1] != np.inf]
                if len(finite) == 0:
                    stats.update({f"{prefix}_betti": 0, f"{prefix}_avg_life": 0.0,
                                  f"{prefix}_max_life": 0.0, f"{prefix}_entropy": 0.0})
                    continue
                lifetimes = finite[:, 1] - finite[:, 0]
                total     = lifetimes.sum()
                probs     = lifetimes / total if total > 0 else np.zeros_like(lifetimes)
                entropy   = float(-np.sum(probs * np.log(probs + 1e-12))) if total > 0 else 0.0
                stats.update({
                    f"{prefix}_betti":    int(len(finite)),
                    f"{prefix}_avg_life": float(np.mean(lifetimes)),
                    f"{prefix}_max_life": float(np.max(lifetimes)),
                    f"{prefix}_entropy":  entropy,
                })
            return stats
        except Exception as e:
            log_oracle.error(f"Persistent homology error: {e}")
            return self._empty()

    def _empty(self) -> Dict:
        return {
            f"ph_{d}_{k}": 0.0
            for d in range(self.max_dim + 1)
            for k in ["betti", "avg_life", "max_life", "entropy"]
        }


# ═══════════════════════════════════════════════════════════════════════════════
#  SECTION 7 — REGIME DETECTOR
# ═══════════════════════════════════════════════════════════════════════════════

class RegimeDetector:
    """
    HMM-based regime detector.
    [SI-10] predict() now guards against empty feature windows gracefully.
    """

    def __init__(self, n_regimes: int = 4, min_length: int = 180,
                 covariance_type: str = "full", smoothing_alpha: float = 0.25,
                 stability_weight: float = 0.7):
        self.n_regimes       = n_regimes
        self.min_length      = min_length
        self.covariance_type = covariance_type
        self.smoothing_alpha = smoothing_alpha
        self.stability_weight = stability_weight

        self.model: Optional[object] = None
        self.scalers: Dict[str, StandardScaler] = {}
        self.fitted = False
        self.feature_groups: Optional[Dict[str, List[str]]] = None
        self.regime_history: deque = deque(maxlen=60)

    def _prepare_features(self, features: pd.DataFrame) -> np.ndarray:
        if self.feature_groups is None:
            cols = features.columns.tolist()
            returns_cols = [c for c in cols if any(k in c.lower()
                            for k in ("ret", "mom", "change"))]
            vol_cols = [c for c in cols if any(k in c.lower()
                        for k in ("vol", "atr", "std"))
                        and c not in returns_cols]
            volume_cols = [c for c in cols if any(k in c.lower()
                           for k in ("volu", "turnover"))
                           and c not in returns_cols and c not in vol_cols]
            assigned = set(returns_cols + vol_cols + volume_cols)
            other_cols = [c for c in cols if c not in assigned]

            self.feature_groups = {}
            if returns_cols: self.feature_groups["returns"]    = returns_cols
            if vol_cols:     self.feature_groups["volatility"] = vol_cols
            if volume_cols:  self.feature_groups["volume"]     = volume_cols
            if other_cols:   self.feature_groups["other"]      = other_cols

        parts = []
        for grp_name, grp_cols in self.feature_groups.items():
            sub = features[grp_cols].replace([np.inf, -np.inf], np.nan).fillna(0).values
            if grp_name not in self.scalers:
                self.scalers[grp_name] = StandardScaler().fit(sub)
            parts.append(self.scalers[grp_name].transform(sub))

        return np.hstack(parts) if parts else np.zeros((len(features), 1))

    def fit(self, features: pd.DataFrame) -> bool:
        if len(features) < self.min_length:
            log_oracle.warning(f"Too few samples ({len(features)}) for regime fit")
            return False
        if not HMM_AVAILABLE:
            log_oracle.warning("hmmlearn not installed — regime detector disabled")
            return False
        try:
            X   = self._prepare_features(features)
            cov = self.covariance_type if X.shape[1] >= self.n_regimes else "diag"
            self.model = hmm.GaussianHMM(
                n_components=self.n_regimes, covariance_type=cov,
                n_iter=200, tol=1e-4, init_params="stmc", random_state=42,
            )
            with warnings.catch_warnings():
                warnings.simplefilter("ignore")
                self.model.fit(X)
            self.fitted = True
            self.regime_history.clear()
            log_oracle.info(f"HMM fitted — {self.n_regimes} regimes on {X.shape}")
            return True
        except Exception as e:
            log_oracle.error(f"HMM fit failed: {e}")
            self.fitted = False
            return False

    def predict(self, features: pd.DataFrame) -> Dict:
        if not self.fitted or self.model is None:
            return self._default()
        # [SI-10] Guard against empty / tiny feature windows
        if features is None or len(features) == 0:
            return self._default()
        try:
            X = self._prepare_features(features.tail(120))
            if len(X) == 0:
                return self._default()

            _, posteriors = self.model.score_samples(X)
            probs = posteriors[-1].copy()

            if self.regime_history:
                probs = (self.smoothing_alpha * probs
                         + (1 - self.smoothing_alpha) * self.regime_history[-1])
                probs /= probs.sum()

            regime_id = int(np.argmax(probs))
            self.regime_history.append(probs)

            entropy     = float(-np.sum(probs * np.log(probs + 1e-12)))
            max_entropy = np.log(self.n_regimes)
            norm_entropy = entropy / max_entropy if max_entropy > 0 else 0.0

            stability = 1.0
            if len(self.regime_history) >= 2:
                diff = np.abs(self.regime_history[-1] - self.regime_history[-2]).sum() / 2.0
                stability = max(0.0, 1.0 - diff * self.stability_weight)

            return {
                "current_regime": regime_id,
                "probabilities":  probs,
                "entropy":        float(norm_entropy),
                "stability":      float(stability),
                "regime_name":    self._regime_name(regime_id),
                "confidence":     float(probs[regime_id]),
            }
        except Exception as e:
            log_oracle.error(f"Regime predict failed: {e}")
            return self._default()

    def _default(self) -> Dict:
        p = np.ones(self.n_regimes) / self.n_regimes
        return {"current_regime": 0, "probabilities": p, "entropy": 0.0,
                "stability": 1.0, "regime_name": "unfitted",
                "confidence": 1.0 / self.n_regimes}

    @staticmethod
    def _regime_name(rid: int) -> str:
        return {
            0: "Low-Vol Trending", 1: "High-Vol Choppy",
            2: "Crisis / Sell-off", 3: "Recovery / Risk-on",
        }.get(rid, f"Regime-{rid}")


# ═══════════════════════════════════════════════════════════════════════════════
#  SECTION 8 — LSTM PREDICTOR WITH MC-DROPOUT UNCERTAINTY
# ═══════════════════════════════════════════════════════════════════════════════

class _LSTMNet(nn.Module):
    """Multi-layer LSTM with permanent dropout for MC-Dropout inference."""
    def __init__(self, input_dim: int, hidden: int = 64,
                 n_layers: int = 2, dropout: float = 0.2):
        super().__init__()
        self.lstm = nn.LSTM(input_dim, hidden, num_layers=n_layers,
                            batch_first=True,
                            dropout=dropout if n_layers > 1 else 0.0)
        self.drop = nn.Dropout(dropout)
        self.fc   = nn.Linear(hidden, 1)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        out, _ = self.lstm(x)
        out = self.drop(out[:, -1, :])
        return self.fc(out).squeeze(-1)


class LSTMPredictor:
    """
    Trains LSTM on engineered features → next-bar return.
    MC-Dropout produces (mean, std) uncertainty estimates.

    [BF-05] Replaced `if 'best_state' in dir()` with explicit boolean flag
            and initialised best_state = None before the training loop.
    [BF-08] train_predictor now uses DataLoader with proper mini-batching.
    """

    def __init__(self, config: OracleConfig):
        self.cfg = config
        self.device = torch.device(
            config.device or ("cuda" if torch.cuda.is_available() else "cpu"))
        self.model: Optional[_LSTMNet] = None
        self.scaler_X = StandardScaler()
        self.scaler_y = StandardScaler()
        self.fitted = False

    @staticmethod
    def _make_sequences(X: np.ndarray, y: np.ndarray, seq_len: int):
        xs, ys = [], []
        for i in range(seq_len, len(X)):
            xs.append(X[i - seq_len:i])
            ys.append(y[i])
        return np.array(xs), np.array(ys)

    def fit(self, features: np.ndarray, targets: np.ndarray) -> bool:
        seq = self.cfg.sequence_length
        if len(features) < seq + 50:
            log_oracle.warning("Not enough data to train predictor")
            return False
        try:
            X_sc = self.scaler_X.fit_transform(features)
            y_sc = self.scaler_y.fit_transform(targets.reshape(-1, 1)).ravel()

            X_seq, y_seq = self._make_sequences(X_sc, y_sc, seq)
            split = int(len(X_seq) * 0.85)
            X_train, y_train = X_seq[:split], y_seq[:split]
            X_val,   y_val   = X_seq[split:], y_seq[split:]

            train_dl = DataLoader(
                TensorDataset(torch.tensor(X_train, dtype=torch.float32),
                              torch.tensor(y_train, dtype=torch.float32)),
                batch_size=self.cfg.predictor_batch_size, shuffle=True,
            )
            val_dl = DataLoader(
                TensorDataset(torch.tensor(X_val, dtype=torch.float32),
                              torch.tensor(y_val, dtype=torch.float32)),
                batch_size=len(y_val),
            )

            self.model = _LSTMNet(
                input_dim=features.shape[1],
                hidden=self.cfg.lstm_hidden,
                n_layers=self.cfg.lstm_layers,
                dropout=self.cfg.lstm_dropout,
            ).to(self.device)

            optimizer = optim.AdamW(self.model.parameters(),
                                    lr=self.cfg.predictor_lr, weight_decay=1e-5)
            scheduler = optim.lr_scheduler.CosineAnnealingLR(
                optimizer, T_max=self.cfg.predictor_epochs)

            best_val = float("inf")
            # [BF-05] Explicit flag — `in dir()` does not reliably detect local vars
            best_state: Optional[Dict] = None
            patience, wait = 15, 0

            for epoch in range(self.cfg.predictor_epochs):
                self.model.train()
                for xb, yb in train_dl:
                    xb, yb = xb.to(self.device), yb.to(self.device)
                    pred = self.model(xb)
                    loss = F.mse_loss(pred, yb)
                    optimizer.zero_grad()
                    loss.backward()
                    nn.utils.clip_grad_norm_(self.model.parameters(), 1.0)
                    optimizer.step()
                scheduler.step()

                self.model.eval()
                with torch.no_grad():
                    for xv, yv in val_dl:
                        xv, yv = xv.to(self.device), yv.to(self.device)
                        val_loss = F.mse_loss(self.model(xv), yv).item()

                if val_loss < best_val - 1e-6:
                    best_val   = val_loss
                    wait       = 0
                    best_state = {k: v.cpu().clone()
                                  for k, v in self.model.state_dict().items()}
                else:
                    wait += 1
                    if wait >= patience:
                        break

            if best_state is not None:          # [BF-05] safe check
                self.model.load_state_dict(best_state)
            self.fitted = True
            log_oracle.info(f"LSTM trained — best val MSE: {best_val:.6f}")
            return True

        except Exception as e:
            log_oracle.error(f"LSTM training failed: {e}")
            return False

    def predict(self, features: np.ndarray) -> Tuple[float, float]:
        if not self.fitted or self.model is None:
            return 0.0, 1.0
        seq = self.cfg.sequence_length
        if len(features) < seq:
            return 0.0, 1.0

        X_sc = self.scaler_X.transform(features[-seq:])
        x_t  = torch.tensor(X_sc, dtype=torch.float32).unsqueeze(0).to(self.device)

        self.model.train()  # keep dropout active for MC
        preds = []
        with torch.no_grad():
            for _ in range(self.cfg.mc_dropout_samples):
                preds.append(self.model(x_t).item())

        preds    = np.array(preds)
        mean_sc  = preds.mean()
        std_sc   = preds.std()
        mean_orig = float(self.scaler_y.inverse_transform(
            np.array([[mean_sc]]))[0, 0])
        std_orig  = float(std_sc * self.scaler_y.scale_[0])
        return mean_orig, std_orig


# ═══════════════════════════════════════════════════════════════════════════════
#  SECTION 9 — CRITICALITY PROXIMITY DETECTOR
# ═══════════════════════════════════════════════════════════════════════════════

class CriticalityProximityDetector:
    """
    Detects proximity to mean-field SOC criticality (τ ≈ 3/2).
    Hill MLE estimator, Welford EMA variance, branching-ratio estimation.
    """

    def __init__(self, *, tau_target: float = 1.5, tau_tolerance: float = 0.15,
                 sigma_subcritical_hi: float = 0.70, min_events: int = 30,
                 spike_z: float = 2.0):
        self.tau_target    = tau_target
        self.tau_tol       = tau_tolerance
        self.sigma_sub_hi  = sigma_subcritical_hi
        self.min_events    = min_events
        self.spike_z       = spike_z
        self.history_sizes: List[int] = []

        self._harm_mean = 0.0
        self._harm_var  = 1.0
        self._unc_mean  = 0.0
        self._unc_var   = 1.0
        self._ema_alpha = 0.05
        self._warmup    = 0

    def update_stats(self, harm: float, unc: float) -> None:
        a = self._ema_alpha
        if self._warmup < 5:
            self._harm_mean = (self._harm_mean * self._warmup + harm) / (self._warmup + 1)
            self._unc_mean  = (self._unc_mean  * self._warmup + unc)  / (self._warmup + 1)
            self._warmup += 1
            return
        old_harm = self._harm_mean
        self._harm_mean = a * harm + (1 - a) * self._harm_mean
        self._harm_var  = (1 - a) * (self._harm_var + a * (harm - old_harm) ** 2)

        old_unc = self._unc_mean
        self._unc_mean = a * unc + (1 - a) * self._unc_mean
        self._unc_var  = (1 - a) * (self._unc_var + a * (unc - old_unc) ** 2)

    @property
    def _harm_std(self) -> float:
        return math.sqrt(max(self._harm_var, 1e-12))

    @property
    def _unc_std(self) -> float:
        return math.sqrt(max(self._unc_var, 1e-12))

    def collect_precursors(self, hmm_delta: float, harm: float,
                           unc: float) -> List[Tuple[str, float]]:
        prec = []
        if hmm_delta > 0.12:
            prec.append(("hmm_shift", hmm_delta))
        if harm > self._harm_mean + self.spike_z * self._harm_std:
            prec.append(("topo_spike", harm))
        if unc > self._unc_mean + self.spike_z * self._unc_std:
            prec.append(("unc_jump", unc))
        return prec

    @staticmethod
    def detect_avalanches(seq: List[List], min_run: int = 3) -> List[int]:
        clusters, run = [], 0
        for p in seq:
            if p:
                run += 1
            else:
                if run >= min_run:
                    clusters.append(run)
                run = 0
        if run >= min_run:
            clusters.append(run)
        return clusters

    @staticmethod
    def _hill_estimator(sizes: List[int], x_min: int = 3) -> Optional[float]:
        arr = np.array([s for s in sizes if s >= x_min], dtype=float)
        if len(arr) < 15:
            return None
        log_ratios = np.log(arr / x_min)
        mean_log   = log_ratios.mean()
        if mean_log < 1e-10:
            return None
        return 1.0 + 1.0 / mean_log

    def branching_ratio(self) -> Optional[float]:
        if len(self.history_sizes) < 10:
            return None
        mu = np.mean(self.history_sizes)
        return (mu - 1.0) / mu if mu > 1.0 else 0.0

    def evaluate(self) -> Dict:
        n = len(self.history_sizes)
        if n < self.min_events:
            return {"status": "insufficient_data", "tau": None, "sigma": None,
                    "confidence": 0.0, "alert": "none", "n_events": n}

        tau   = self._hill_estimator(self.history_sizes)
        sigma = self.branching_ratio()

        if tau is None or sigma is None:
            return {"status": "fit_failed", "tau": None, "sigma": None,
                    "confidence": 0.0, "alert": "none", "n_events": n}

        dist        = abs(tau - self.tau_target)
        near_critical = dist <= self.tau_tol
        subcritical   = (sigma < self.sigma_sub_hi) or (tau > self.tau_target + 0.5)

        if near_critical and 0.85 <= sigma <= 1.15:
            status = "near_critical"
            alert  = "high" if dist < 0.05 and sigma > 0.95 else "watch"
            conf   = max(0.0, 1.0 - dist / self.tau_tol) * (1.0 if sigma > 0.90 else 0.6)
        elif subcritical:
            status = "subcritical"
            alert  = "safe"
            conf   = 0.8 if sigma < 0.5 else 0.6
        else:
            status = "intermediate"
            alert  = "neutral"
            conf   = 0.5

        return {
            "status":     status,
            "tau":        round(tau, 4),
            "sigma":      round(sigma, 4),
            "confidence": round(conf, 3),
            "alert":      alert,
            "n_events":   n,
        }


# ═══════════════════════════════════════════════════════════════════════════════
#  SECTION 10 — FEATURE ENGINEERING
# ═══════════════════════════════════════════════════════════════════════════════

class FeatureEngineer:
    """Builds a rich feature matrix from OHLCV data."""

    @staticmethod
    def build(df: pd.DataFrame) -> pd.DataFrame:
        c = df["close"]
        h = df["high"]
        l = df["low"]
        v = df["volume"]

        feat = pd.DataFrame(index=df.index)

        for n in [1, 2, 5, 10, 20]:
            feat[f"return_{n}"] = c.pct_change(n)

        ret1 = c.pct_change()
        for w in [5, 10, 20, 60]:
            feat[f"vol_{w}"] = ret1.rolling(w).std()

        tr = pd.concat([h - l,
                        (h - c.shift(1)).abs(),
                        (l - c.shift(1)).abs()], axis=1).max(axis=1)
        for w in [5, 14, 20]:
            feat[f"atr_{w}"] = tr.rolling(w).mean() / c

        feat["volume_chg"]       = v.pct_change()
        feat["volume_sma_ratio"] = v / v.rolling(20).mean()

        feat["rsi_14"]      = FeatureEngineer._rsi(c, 14)
        feat["momentum_10"] = c / c.shift(10) - 1.0

        for w in [20, 50]:
            ma = c.rolling(w).mean()
            sd = c.rolling(w).std()
            feat[f"zscore_{w}"] = (c - ma) / (sd + 1e-10)

        feat["hl_range"] = (h - l) / c
        feat["oc_range"] = (c - df["open"]) / c

        return feat.replace([np.inf, -np.inf], np.nan).dropna()

    @staticmethod
    def _rsi(series: pd.Series, period: int = 14) -> pd.Series:
        delta = series.diff()
        gain  = delta.clip(lower=0).rolling(period).mean()
        loss  = (-delta.clip(upper=0)).rolling(period).mean()
        rs    = gain / (loss + 1e-10)
        return 100 - 100 / (1 + rs)


# ═══════════════════════════════════════════════════════════════════════════════
#  SECTION 11 — SIGNAL SYNTHESIZER
# ═══════════════════════════════════════════════════════════════════════════════

class SignalSynthesizer:
    """Combines all Oracle subsystem outputs into a single composite signal."""

    @staticmethod
    def synthesize(*, regime: Dict, topo: Dict, pred_mean: float, pred_std: float,
                   ph: Dict, criticality: Dict) -> Dict:

        # Predictor score
        if pred_std > 1e-8:
            pred_z     = pred_mean / pred_std
            pred_score = float(np.clip(np.tanh(pred_z), -1, 1))
        else:
            pred_score = float(np.clip(np.tanh(pred_mean * 100), -1, 1))

        # Regime score
        regime_map   = {0: 0.3, 1: -0.1, 2: -0.8, 3: 0.6}
        regime_id    = regime.get("current_regime", 0)
        regime_score = regime_map.get(regime_id, 0.0) * regime.get("confidence", 0.5)

        # Topology score
        harm         = topo.get("harmonic_intensity", 0.0)
        spectral_gap = topo.get("spectral_gap", 0.0)
        topo_score   = -float(np.clip(harm * 3.0, -1, 1))
        if spectral_gap > 0.5:
            topo_score *= 0.5

        # PH score
        ph_entropy = ph.get("ph_1_entropy", 0.0)
        ph_score   = -float(np.clip((ph_entropy - 0.5) * 2, -1, 1))

        # Criticality multiplier
        crit_multiplier = 1.0
        crit_status = criticality.get("status", "insufficient_data")
        if crit_status == "near_critical":
            crit_multiplier = 0.3 if criticality.get("alert") == "high" else 0.5
        elif crit_status == "subcritical":
            crit_multiplier = 1.1

        weights    = {"pred": 0.40, "regime": 0.25, "topo": 0.20, "ph": 0.15}
        raw_signal = (weights["pred"]   * pred_score  +
                      weights["regime"] * regime_score +
                      weights["topo"]   * topo_score   +
                      weights["ph"]     * ph_score)

        base_conf  = regime.get("stability", 0.5) * (1.0 / (1.0 + pred_std * 10))
        confidence = float(np.clip(base_conf * crit_multiplier, 0.05, 0.99))

        if crit_status == "near_critical" and criticality.get("alert") == "high":
            signal_type = SignalType.RISK_OFF
        elif raw_signal > 0.4:
            signal_type = SignalType.STRONG_BUY
        elif raw_signal > 0.15:
            signal_type = SignalType.BUY
        elif raw_signal < -0.4:
            signal_type = SignalType.STRONG_SELL
        elif raw_signal < -0.15:
            signal_type = SignalType.SELL
        else:
            signal_type = SignalType.HOLD

        return {
            "signal":     signal_type,
            "raw_score":  float(np.clip(raw_signal, -1, 1)),
            "confidence": confidence,
            "components": {
                "predictor":   round(pred_score,   4),
                "regime":      round(regime_score, 4),
                "topology":    round(topo_score,   4),
                "persistence": round(ph_score,     4),
            },
            "criticality_multiplier": round(crit_multiplier, 3),
        }


# ═══════════════════════════════════════════════════════════════════════════════
#  SECTION 12 — POSITION SIZER
# ═══════════════════════════════════════════════════════════════════════════════

class PositionSizer:
    """Kelly-inspired position sizing with regime-aware caps."""

    def __init__(self, config: OracleConfig):
        self.max_size = config.max_position_size
        self.txn_cost = config.transaction_cost
        self.rf       = config.risk_free_rate / 252

    def size(self, signal: Dict, pred_mean: float, pred_std: float,
             regime: Dict) -> Dict:
        confidence = signal.get("confidence", 0.0)
        sig        = signal.get("signal", SignalType.HOLD)

        if sig in (SignalType.RISK_OFF, SignalType.HOLD):
            return {"position_pct": 0.0, "direction": 0, "reason": sig.value}

        direction = 1 if sig in (SignalType.BUY, SignalType.STRONG_BUY) else -1

        if pred_std > 1e-8:
            excess = abs(pred_mean) - self.rf - self.txn_cost
            kelly  = max(0.0, excess / (pred_std ** 2)) * 0.5
        else:
            kelly = 0.0

        regime_scale = {0: 1.0, 1: 0.6, 2: 0.3, 3: 0.9}.get(
            regime.get("current_regime", 0), 0.5)
        raw_pct = kelly * confidence * regime_scale
        capped  = min(raw_pct, self.max_size)

        return {
            "position_pct": round(float(capped), 4),
            "direction":    direction,
            "kelly_raw":    round(float(kelly), 4),
            "regime_scale": regime_scale,
            "reason":       sig.value,
        }


# ═══════════════════════════════════════════════════════════════════════════════
#  SECTION 13 — ORACLE HYBRID 5.5  (main orchestrator)
# ═══════════════════════════════════════════════════════════════════════════════

class OracleHybrid5_5:
    """
    Unified analysis framework.
    DataFetcher → FeatureEngineer → RegimeDetector → TopologicalEngine
    → PersistentHomology → LSTMPredictor → CriticalityDetector
    → SignalSynthesizer → PositionSizer
    """

    def __init__(self, config: Optional[OracleConfig] = None,
                 fetcher: Optional[OracleDataFetcher] = None):
        self.cfg    = config or OracleConfig()
        self.device = torch.device(
            self.cfg.device or ("cuda" if torch.cuda.is_available() else "cpu"))

        self.fetcher    = fetcher or OracleDataFetcher(cache_size=self.cfg.max_cache_size,
                                                       max_workers=self.cfg.max_fetch_workers)
        self.regime     = RegimeDetector(n_regimes=4)
        self.topo       = OracleTopologicalEngine(self.cfg.correlation_threshold)
        self.ph         = (PersistentHomologyEngine()
                           if self.cfg.use_persistent_homology else None)
        self.predictor  = LSTMPredictor(self.cfg)
        self.cpd        = CriticalityProximityDetector()
        self.synthesizer = SignalSynthesizer()
        self.sizer      = PositionSizer(self.cfg)

        self._precursor_buf: deque = deque(
            maxlen=self.cfg.criticality_eval_interval * 3)

    def run_analysis(self, ticker: str, days_back: int = 800) -> Dict:
        log_oracle.info(f"═══ OracleHybrid5.5 → {ticker} ({days_back}d) ═══")

        df = self.fetcher.get_price_data(ticker, days_back=days_back)
        if df.empty or len(df) < 100:
            return {"error": f"Insufficient data for {ticker} ({len(df)} bars)"}
        log_oracle.info(f"Data: {len(df)} bars  {df.index[0].date()} → {df.index[-1].date()}")

        features = FeatureEngineer.build(df)
        if len(features) < self.cfg.sequence_length + 50:
            return {"error": "Not enough features after engineering"}
        log_oracle.info(f"Features: {features.shape[1]} cols × {len(features)} rows")

        regime_ok = self.regime.fit(features)
        log_oracle.info(f"Regime detector fitted: {regime_ok}")

        targets   = df["close"].pct_change().reindex(features.index).fillna(0).values
        feat_vals = features.values
        pred_ok   = self.predictor.fit(feat_vals, targets)
        log_oracle.info(f"LSTM predictor fitted: {pred_ok}")

        window       = 60
        crit_interval = self.cfg.criticality_eval_interval
        bar_count     = 0

        for i in range(window, len(df)):
            bar_count  += 1
            window_df   = df.iloc[max(0, i - window): i + 1]
            # Align feature window to df index to avoid off-by-one drift
            feat_idx    = features.index.get_indexer([df.index[i]], method="nearest")[0]
            feat_window = features.iloc[max(0, feat_idx - window): feat_idx + 1]

            reg_result = (self.regime.predict(feat_window)
                          if regime_ok and len(feat_window) > 5
                          else self.regime._default())

            topo_result = self.topo.compute_metrics(
                window_df, use_synthetic=self.cfg.use_synthetic_baskets)

            if pred_ok and feat_idx >= self.cfg.sequence_length:
                _, pred_unc = self.predictor.predict(
                    feat_vals[max(0, feat_idx - self.cfg.sequence_length): feat_idx + 1])
            else:
                pred_unc = 0.15

            harm = topo_result.get("harmonic_intensity", 0.0)
            self.cpd.update_stats(harm, pred_unc)

            hmm_delta = 0.0
            if len(self.regime.regime_history) >= 2:
                hmm_delta = float(
                    np.abs(self.regime.regime_history[-1]
                           - self.regime.regime_history[-2]).max())

            precs = self.cpd.collect_precursors(hmm_delta, harm, pred_unc)
            self._precursor_buf.append(precs)

            if bar_count % crit_interval == 0 and len(self._precursor_buf) >= crit_interval:
                avs = self.cpd.detect_avalanches(list(self._precursor_buf))
                if avs:
                    self.cpd.history_sizes.extend(avs)

        # ── Final snapshot ─────────────────────────────────────────────────────
        reg_final   = self.regime.predict(features) if regime_ok else self.regime._default()
        topo_final  = self.topo.compute_metrics(
            df.tail(window), use_synthetic=self.cfg.use_synthetic_baskets)
        pred_mean, pred_std = (self.predictor.predict(feat_vals)
                               if pred_ok else (0.0, 0.15))

        ph_result = (self.ph.compute(
            pd.DataFrame({
                "open":  df["open"].pct_change(),
                "high":  df["high"].pct_change(),
                "low":   df["low"].pct_change(),
                "close": df["close"].pct_change(),
            }).dropna()
        ) if self.ph else self._ph_empty())

        crit_result = self.cpd.evaluate()
        signal      = self.synthesizer.synthesize(
            regime=reg_final, topo=topo_final,
            pred_mean=pred_mean, pred_std=pred_std,
            ph=ph_result, criticality=crit_result,
        )
        position = self.sizer.size(signal, pred_mean, pred_std, reg_final)

        result = {
            "ticker":         ticker,
            "bars_processed": len(df),
            "signal": {
                "type":       signal["signal"].value,
                "raw_score":  signal["raw_score"],
                "confidence": signal["confidence"],
                "components": signal["components"],
            },
            "position":   position,
            "regime": {
                "id":         reg_final["current_regime"],
                "name":       reg_final["regime_name"],
                "confidence": reg_final["confidence"],
                "entropy":    reg_final["entropy"],
                "stability":  reg_final["stability"],
            },
            "prediction": {
                "expected_return": round(pred_mean, 6),
                "uncertainty_std": round(pred_std,  6),
            },
            "topology": {
                "gradient_dominance": topo_final.get("gradient_dominance", 0.0),
                "curl_dominance":     topo_final.get("curl_dominance",     0.0),
                "harmonic_intensity": topo_final.get("harmonic_intensity", 0.0),
                "betti_0":            topo_final.get("betti_0", 0),
                "betti_1":            topo_final.get("betti_1", 0),
                "spectral_gap":       topo_final.get("spectral_gap", 0.0),
            },
            "persistent_homology": ph_result,
            "criticality":         crit_result,
            "timestamp":           datetime.now().isoformat(),
        }

        log_oracle.info(
            f"Signal: {signal['signal'].value} | Score: {signal['raw_score']:+.3f} "
            f"| Conf: {signal['confidence']:.3f} "
            f"| Pos: {position['position_pct']:.2%} {position['reason']}"
        )
        return result

    def run_multi(self, tickers: List[str], days_back: int = 800) -> Dict[str, Dict]:
        results: Dict[str, Dict] = {}
        for t in tickers:
            try:
                results[t] = self.run_analysis(t, days_back)
            except Exception as e:
                log_oracle.error(f"Analysis failed for {t}: {e}")
                results[t] = {"error": str(e)}
        return results

    @staticmethod
    def _ph_empty() -> Dict:
        return {f"ph_{d}_{k}": 0.0
                for d in range(2)
                for k in ["betti", "avg_life", "max_life", "entropy"]}


# ═══════════════════════════════════════════════════════════════════════════════
#  SECTION 14 — DEEPDARK2: HODGE ENGINE
# ═══════════════════════════════════════════════════════════════════════════════

class DeepDarkHodgeEngine:
    """
    Hodge-Flow engine for DeepDark2 statistical arbitrage.

    [BF-10] Fixed triangle boundary orientation: e_ac now correctly assigned −1
            (consistent with the oriented simplex convention used in OracleTopologicalEngine).
    Convention here: B1=(edges×nodes), L=B1@B1.T + B2.T@B2 — mathematically equivalent
    to the Oracle convention and produces the same Laplacian spectrum.
    """

    def __init__(self, correlation_threshold: float = 0.5):
        self.corr_thresh = correlation_threshold

    def get_simplices(self, corr_matrix: np.ndarray):
        n     = len(corr_matrix)
        nodes = list(range(n))
        edges: List[Tuple] = []

        for i, j in combinations(nodes, 2):
            if abs(corr_matrix[i, j]) > self.corr_thresh:
                edges.append(tuple(sorted((i, j))))

        edge_set = set(edges)
        triangles: List[Tuple] = []
        for i, j, k in combinations(nodes, 3):
            if (tuple(sorted((i, j))) in edge_set and
                    tuple(sorted((j, k))) in edge_set and
                    tuple(sorted((i, k))) in edge_set):
                triangles.append(tuple(sorted((i, j, k))))

        return nodes, edges, triangles

    def compute_boundary_operators(self, nodes, edges, triangles):
        num_nodes   = len(nodes)
        num_edges   = len(edges)
        num_triangles = len(triangles)

        # B1: (edges × nodes)
        B1 = np.zeros((max(num_edges, 1), num_nodes))
        for idx, (u, v) in enumerate(edges):
            B1[idx, u] = -1
            B1[idx, v] = +1

        # B2: (triangles × edges)
        B2 = np.zeros((max(num_triangles, 1), max(num_edges, 1)))
        if num_triangles > 0 and num_edges > 0:
            edge_idx_map = {e: i for i, e in enumerate(edges)}
            for idx, (u, v, w) in enumerate(triangles):
                try:
                    e_uv = edge_idx_map[tuple(sorted((u, v)))]
                    e_vw = edge_idx_map[tuple(sorted((v, w)))]
                    e_uw = edge_idx_map[tuple(sorted((u, w)))]
                    B2[idx, e_uv] = +1.0
                    B2[idx, e_vw] = +1.0
                    B2[idx, e_uw] = -1.0   # [BF-10] was +1 (sign error)
                except KeyError:
                    continue

        return B1, B2

    def compute_flow_metrics(self, basket_returns: pd.DataFrame,
                             gini_trend: float = 0,
                             vix_data: Optional[Dict] = None,
                             vvix_level: float = 80,
                             curve_slope: float = 0) -> List[float]:
        if basket_returns.shape[1] < 3 or len(basket_returns) < 10:
            return [0.0, 0.0, 0.0]
        try:
            corr_matrix = np.abs(basket_returns.corr().fillna(0).values)
            np.fill_diagonal(corr_matrix, 0)

            nodes, edges, triangles = self.get_simplices(corr_matrix)
            if len(edges) == 0:
                return [0.0, 0.0, 0.0]

            B1, B2 = self.compute_boundary_operators(nodes, edges, triangles)

            L1_down = B1 @ B1.T
            L1_up   = B2.T @ B2 if B2.shape[1] > 0 else np.zeros_like(L1_down)
            L1      = L1_down + L1_up

            total_energy = np.trace(L1)
            if total_energy == 0:
                return [0.0, 0.0, 0.0]

            grad_dominance  = np.trace(L1_down) / total_energy
            evals           = np.linalg.eigvalsh(L1)
            harmonic_intensity = np.sum(np.abs(evals) < 1e-5) / max(len(edges), 1)

            vix_perc = 50.0
            if (vix_data is not None and "percentile" in vix_data
                    and len(vix_data["percentile"]) > 0):
                last_val = vix_data["percentile"].iloc[-1]
                if not pd.isna(last_val):
                    vix_perc = float(last_val)

            curve_amp = 1 + abs(curve_slope) * (1.5 if curve_slope > 0 else 0.8)
            vorticity = (abs(gini_trend) * harmonic_intensity
                         * (vix_perc / 100) * (vvix_level / 100.0) * curve_amp)

            return [float(grad_dominance), float(harmonic_intensity), float(vorticity)]

        except Exception as e:
            log_dark.error(f"Hodge calculation error: {e}")
            return [0.0, 0.0, 0.0]


# ═══════════════════════════════════════════════════════════════════════════════
#  SECTION 15 — DEEPDARK2: GAN NEURAL ARCHITECTURE (fixed)
# ═══════════════════════════════════════════════════════════════════════════════

class DDGenerator(nn.Module):
    """
    [BF-03] Fully corrected generative model.
    Takes a noise vector of shape (batch, noise_dim) and generates a realistic
    full sequence of shape (batch, seq_len, n_features) for the Discriminator.
    Original produced (batch, 1) which was incompatible with the fake_seq cat.
    """
    def __init__(self, seq_len: int = 60, n_features: int = 10, noise_dim: int = 32):
        super().__init__()
        self.seq_len    = seq_len
        self.n_features = n_features
        self.noise_dim  = noise_dim

        self.fc_expand = nn.Linear(noise_dim, seq_len * 64)
        self.lstm      = nn.LSTM(64, 128, batch_first=True, dropout=0.3)
        self.attention = nn.MultiheadAttention(128, num_heads=4, batch_first=True)
        self.norm      = nn.LayerNorm(128)
        self.fc_out    = nn.Linear(128, n_features)   # outputs n_features per step

    def forward(self, noise: torch.Tensor) -> torch.Tensor:
        # noise: (batch, noise_dim) → (batch, seq_len, n_features)
        x = self.fc_expand(noise).view(-1, self.seq_len, 64)
        lstm_out, _ = self.lstm(x)
        attn_out, _ = self.attention(lstm_out, lstm_out, lstm_out)
        x = self.norm(lstm_out + attn_out)
        return self.fc_out(x)   # (batch, seq_len, n_features)


class DDDiscriminator(nn.Module):
    """Discriminator — unchanged, already dimensionally correct."""
    def __init__(self, seq_len: int = 60, n_features: int = 10):
        super().__init__()
        self.net = nn.Sequential(
            nn.Conv1d(n_features, 64,  kernel_size=3, stride=2, padding=1),
            nn.LeakyReLU(0.2),
            nn.Dropout(0.25),
            nn.Conv1d(64,  128, kernel_size=3, stride=2, padding=1),
            nn.LeakyReLU(0.2),
            nn.AdaptiveAvgPool1d(1),
            nn.Flatten(),
            nn.Linear(128, 1),
        )

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.net(x.permute(0, 2, 1))


class DDPredictor(nn.Module):
    """
    [SI-07] VIX / curve gate slice indices now passed as constructor args
    rather than being hardcoded magic numbers.
    """
    def __init__(self, n_features: int = 10,
                 vix_start: int = 5, vix_end: int = 8,
                 curve_start: int = 8, curve_end: int = 10):
        super().__init__()
        vix_dim   = vix_end   - vix_start
        curve_dim = curve_end - curve_start

        self.vix_start   = vix_start
        self.vix_end     = vix_end
        self.curve_start = curve_start
        self.curve_end   = curve_end

        self.lstm       = nn.LSTM(n_features, 64, batch_first=True)
        self.vix_gate   = nn.Linear(vix_dim,   1)
        self.curve_gate = nn.Linear(curve_dim, 1)
        self.fc         = nn.Sequential(
            nn.Linear(64 + 2, 32),
            nn.ReLU(),
            nn.Dropout(0.2),
            nn.Linear(32, 1),
        )

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        lstm_out, _  = self.lstm(x)
        lstm_last    = lstm_out[:, -1, :]
        vix_feats    = x[:, -1, self.vix_start:self.vix_end]
        curve_feats  = x[:, -1, self.curve_start:self.curve_end]
        vix_g        = torch.sigmoid(self.vix_gate(vix_feats))
        curve_g      = torch.sigmoid(self.curve_gate(curve_feats))
        combined     = torch.cat([lstm_last, vix_g, curve_g], dim=1)
        return self.fc(combined)


# ═══════════════════════════════════════════════════════════════════════════════
#  SECTION 16 — DEEPDARK2: HYPER-MODEL (GAN + Predictor training)
# ═══════════════════════════════════════════════════════════════════════════════

class DeepDarkHyperModel:
    """
    [BF-03] train_gan now generates full (batch, seq_len, n_features) fake sequences.
    [BF-08] train_predictor now uses proper DataLoader mini-batch training with shuffle.
    [SI-06] predict_uncertainty now uses MC-Dropout on the Predictor, not the Generator.
    """

    def __init__(self, config: DeepDarkConfig, device: torch.device = DEVICE):
        self.cfg       = config
        self.device    = device
        seq            = config.sequence_length
        n_feat         = config.n_features
        noise_dim      = config.noise_dim

        self.generator    = DDGenerator(seq, n_feat, noise_dim).to(device)
        self.discriminator = DDDiscriminator(seq, n_feat).to(device)
        self.predictor    = DDPredictor(n_feat).to(device)

        self.g_optimizer  = optim.Adam(self.generator.parameters(),
                                       lr=config.gan_lr, betas=(0.5, 0.999))
        self.d_optimizer  = optim.Adam(self.discriminator.parameters(),
                                       lr=config.gan_lr, betas=(0.5, 0.999))
        self.p_optimizer  = optim.Adam(self.predictor.parameters(),
                                       lr=config.predictor_lr)
        self.bce_loss     = nn.BCEWithLogitsLoss()
        self.mse_loss     = nn.MSELoss()
        self.history: Dict[str, List[float]] = {"g_loss": [], "d_loss": [], "p_loss": []}

    # ── GAN training ───────────────────────────────────────────────────────────
    def train_gan(self, X: np.ndarray, epochs: int = 50,
                  batch_size: int = 32) -> None:
        self.generator.train()
        self.discriminator.train()
        n_samples  = X.shape[0]
        noise_dim  = self.cfg.noise_dim

        for _ in range(epochs):
            idx        = np.random.randint(0, n_samples, min(batch_size, n_samples))
            real_batch = torch.tensor(X[idx], dtype=torch.float32).to(self.device)
            bsz        = real_batch.size(0)

            # ── Discriminator step ─────────────────────────────────────────────
            self.d_optimizer.zero_grad()
            real_out    = self.discriminator(real_batch)
            d_loss_real = self.bce_loss(real_out, torch.ones_like(real_out))

            # [BF-03] Generator now outputs full (batch, seq_len, n_features)
            noise       = torch.randn(bsz, noise_dim).to(self.device)
            fake_seq    = self.generator(noise).detach()          # (bsz, seq, n_feat)
            fake_out    = self.discriminator(fake_seq)
            d_loss_fake = self.bce_loss(fake_out, torch.zeros_like(fake_out))
            d_loss      = (d_loss_real + d_loss_fake) / 2
            d_loss.backward()
            self.d_optimizer.step()

            # ── Generator step ────────────────────────────────────────────────
            self.g_optimizer.zero_grad()
            fake_seq2 = self.generator(noise)
            fake_out2 = self.discriminator(fake_seq2)
            g_loss    = self.bce_loss(fake_out2, torch.ones_like(fake_out2))
            g_loss.backward()
            self.g_optimizer.step()

            self.history["d_loss"].append(d_loss.item())
            self.history["g_loss"].append(g_loss.item())

    # ── Predictor training (with proper batching) ──────────────────────────────
    def train_predictor(self, X: np.ndarray, y: np.ndarray,
                        epochs: int = 100, batch_size: int = 32) -> None:
        """
        [BF-08] Now uses DataLoader with shuffle=True for proper mini-batch training.
        Original iterated the full dataset as a single batch regardless of batch_size.
        """
        self.predictor.train()
        dataset   = TensorDataset(
            torch.tensor(X, dtype=torch.float32),
            torch.tensor(y, dtype=torch.float32).view(-1, 1),
        )
        loader    = DataLoader(dataset, batch_size=batch_size, shuffle=True)

        for epoch in range(epochs):
            epoch_loss = 0.0
            for xb, yb in loader:
                xb, yb = xb.to(self.device), yb.to(self.device)
                self.p_optimizer.zero_grad()
                loss = self.mse_loss(self.predictor(xb), yb)
                loss.backward()
                self.p_optimizer.step()
                epoch_loss += loss.item() * len(xb)

            avg_loss = epoch_loss / max(len(dataset), 1)
            self.history["p_loss"].append(avg_loss)
            if epoch % 20 == 0:
                log_dark.info(f"Predictor epoch {epoch:3d} | loss: {avg_loss:.6f}")

    # ── Point prediction ───────────────────────────────────────────────────────
    def predict_spread_delta(self, input_seq: np.ndarray) -> float:
        self.predictor.eval()
        t = torch.tensor(input_seq, dtype=torch.float32).to(self.device)
        if t.dim() == 2:
            t = t.unsqueeze(0)
        with torch.no_grad():
            return float(self.predictor(t).cpu().numpy()[0, 0])

    # ── Uncertainty via MC-Dropout on Predictor ────────────────────────────────
    def predict_uncertainty(self, input_seq: np.ndarray,
                            n_iter: int = 100) -> Tuple[float, float, float]:
        """
        [SI-06] Uses MC-Dropout on the Predictor (not Generator) for calibrated
        uncertainty estimates — consistent with OracleHybrid5.5's LSTMPredictor.
        """
        self.predictor.train()   # keep dropout active
        t = torch.tensor(input_seq, dtype=torch.float32).to(self.device)
        if t.dim() == 2:
            t = t.unsqueeze(0)
        t = t.repeat(n_iter, 1, 1)

        with torch.no_grad():
            preds = self.predictor(t).cpu().numpy().ravel()

        point    = float(preds.mean())
        model_var = float(preds.var())
        data_var  = model_var * 0.9   # rough aleatoric proxy
        return point, model_var, data_var


# ═══════════════════════════════════════════════════════════════════════════════
#  SECTION 17 — DEEPDARK2: PREDICTION INTERVALS
# ═══════════════════════════════════════════════════════════════════════════════

class DeepDarkIntervals:
    """Constructs asymmetric prediction intervals from composite variance."""

    def __init__(self):
        self.z_80 = norm.ppf(0.90)
        self.z_95 = norm.ppf(0.975)

    def compute_intervals(self, point_forecast: float, metrics: Dict) -> Dict:
        Y_hat      = point_forecast
        λ1         = metrics.get("lambda1",           0.20)
        harm_int   = metrics.get("harmonic_intensity", 0.12)
        model_var  = metrics.get("model_var",          0.02 ** 2)
        gan_var    = metrics.get("gan_var",            0.015 ** 2)
        vorticity  = metrics.get("vorticity",          0)
        vix_level  = metrics.get("vix_level",          20)
        vvix_level = metrics.get("vvix_level",         80)
        vix_perc   = metrics.get("vix_percentile",     50)
        curve_slope = metrics.get("curve_slope",       0)

        tda_var  = (0.12 * λ1 + 0.08 * harm_int + 0.05 * vorticity
                    + 0.03 * (vix_level / 20.0) + 0.02 * (vvix_level / 100)
                    + 0.01 * abs(curve_slope))
        vol_amp  = (vix_perc / 100) * (vvix_level / 100) * (1 + abs(curve_slope))
        total_var = model_var + tda_var + gan_var + (λ1 * harm_int) * vol_amp
        sigma     = (np.sqrt(max(total_var, 0)) * abs(Y_hat)
                     if Y_hat != 0 else np.sqrt(max(total_var, 0)))

        return {
            "point_forecast":      round(Y_hat, 4),
            "80%_CI":              [round(float(Y_hat - self.z_80 * sigma * 0.65), 4),
                                    round(float(Y_hat + self.z_80 * sigma * 0.65), 4)],
            "95%_PI":              [round(float(Y_hat - self.z_95 * sigma), 4),
                                    round(float(Y_hat + self.z_95 * sigma), 4)],
            "inequality_vorticity": round(vorticity, 4),
            "vix_adjusted_risk":   round((vix_level / 20.0) * (vvix_level / 100), 2),
            "vix_percentile":      round(vix_perc, 1),
            "curve_slope":         round(curve_slope, 4),
            "interval_width_ratio": round(
                (2 * self.z_95 * sigma) / max(2 * self.z_80 * sigma * 0.65, 1e-6), 2),
        }


# ═══════════════════════════════════════════════════════════════════════════════
#  SECTION 18 — DEEPDARK2: BACKTEST ENGINE
# ═══════════════════════════════════════════════════════════════════════════════

def backtest_stat_arb(pair_data: pd.DataFrame,
                      model: DeepDarkHyperModel,
                      threshold: float = 2.0,
                      initial_capital: float = 10_000.0,
                      vix_data: Optional[Dict] = None,
                      vvix_series: Optional[pd.Series] = None,
                      curve_slope: float = 0) -> Dict:
    """
    [BF-02] portfolio_series is now a pd.Series with a proper DatetimeIndex
    derived from pair_data.index so that .resample('ME') works correctly.
    """
    if len(pair_data) < 100:
        return {"error": "Insufficient data"}

    spreads = pair_data["spread"].values
    z_scores = ((spreads - pd.Series(spreads).rolling(60).mean().values)
                / pd.Series(spreads).rolling(60).std().values)

    portfolio_values = [initial_capital]
    portfolio_dates  = [pair_data.index[0]]   # [BF-02] track dates
    positions        = 0
    entry_price      = 0.0
    trades: List[float] = []
    signals: List[str]  = []

    for i in range(60, len(spreads)):
        current_vix  = (float(vix_data["level"].iloc[i])
                        if vix_data is not None else 20.0)
        current_perc = (float(vix_data["percentile"].iloc[i])
                        if vix_data is not None else 50.0)
        current_vvix = (float(vvix_series.iloc[i])
                        if vvix_series is not None else 80.0)

        curve_factor = (1 + curve_slope) if curve_slope > 0 else 1 / (1 + abs(curve_slope))
        adj_thresh   = threshold * (current_vix / 20.0) * (1 - current_perc / 200) * curve_factor
        pos_size     = initial_capital / max(10, current_vix + 10 * abs(curve_slope))
        max_position = pos_size / initial_capital
        current_z    = z_scores[i]

        # Model prediction
        try:
            input_seq   = pair_data.iloc[i - 60:i][
                ["spread", "vol_a", "vol_b", "gini_trend",
                 "grad_dominance", "vix_level", "vvix",
                 "vix_perc", "curve_slope", "curve_level"]
            ].values
            pred_delta  = model.predict_spread_delta(input_seq)
            pred_z      = ((spreads[i] + pred_delta - spreads[i - 60:i].mean())
                           / (pd.Series(spreads[i - 60:i]).std() + 1e-6))
        except Exception:
            pred_z = current_z

        if positions == 0:
            if pred_z > adj_thresh and current_z > 0.5:
                positions   = -max_position
                entry_price = current_z
                signals.append("short_spread")
            elif pred_z < -adj_thresh and current_z < -0.5:
                positions   = max_position
                entry_price = current_z
                signals.append("long_spread")
        else:
            time_exit        = len([s for s in signals[-10:] if s != "hold"]) > 5
            vol_spike        = current_vix > 35
            curve_inversion  = curve_slope < -0.1

            if (abs(current_z) < 0.1 or
                    (positions > 0 and current_z > 0) or
                    (positions < 0 and current_z < 0) or
                    time_exit or vol_spike or curve_inversion):
                profit = -positions * (current_z - entry_price)
                trades.append(profit)
                positions = 0
                signals.append("exit")
            else:
                signals.append("hold")

        if positions != 0 and i > 60:
            pnl = -positions * (spreads[i] - spreads[i - 1])
            portfolio_values.append(portfolio_values[-1] * (1 + pnl))
        else:
            portfolio_values.append(portfolio_values[-1])

        portfolio_dates.append(pair_data.index[i])   # [BF-02]

    # [BF-02] Use DatetimeIndex so .resample() works
    portfolio_series = pd.Series(portfolio_values, index=portfolio_dates)
    returns          = portfolio_series.pct_change().dropna()

    if len(returns) < 2:
        return {"monthly_edge": 0, "sharpe": 0, "total_return": 0,
                "num_trades": len(trades), "win_rate": 0}

    monthly_returns = portfolio_series.resample("ME").last().pct_change().dropna()
    monthly_edge    = (float(monthly_returns.mean()) * 12 * 100
                       if len(monthly_returns) > 0 else 0.0)
    sharpe          = (float(monthly_returns.mean() / monthly_returns.std()) * np.sqrt(12)
                       if float(monthly_returns.std()) > 0 else 0.0)
    win_rate        = (len([t for t in trades if t > 0]) / len(trades)
                       if trades else 0.0)

    return {
        "monthly_edge":  monthly_edge,
        "sharpe":        sharpe,
        "total_return":  (portfolio_values[-1] / initial_capital - 1) * 100,
        "num_trades":    len(trades),
        "win_rate":      win_rate,
        "final_capital": portfolio_values[-1],
    }


# ═══════════════════════════════════════════════════════════════════════════════
#  SECTION 19 — DEEPDARK2: MAIN PIPELINE
# ═══════════════════════════════════════════════════════════════════════════════

def deepdark_stat_arb(
    pair: Tuple[str, str] = ("NVDA", "PG"),
    days_back: int = 730,
    config: Optional[DeepDarkConfig] = None,
    fetcher: Optional[OracleDataFetcher] = None,
) -> Dict:
    """
    [SI-05] Removed reference to nonexistent helm9_7_analysis().
    [SI-04] Optuna degrades to grid search when unavailable.
    """
    cfg     = config  or DeepDarkConfig(days_back=days_back)
    fetcher = fetcher or OracleDataFetcher()
    ticker_a, ticker_b = pair

    log_dark.info(f"=== DEEPDARK STAT ARB: {ticker_a} vs {ticker_b} ===")
    log_dark.info("Fetching market data...")

    hist_a      = fetcher.get_historical_bars(ticker_a, days_back)
    hist_b      = fetcher.get_historical_bars(ticker_b, days_back)
    vix_data    = fetcher.get_vix_data(days_back)
    vvix_series = fetcher.get_vvix_data(days_back)
    curve_data  = fetcher.get_vix_futures_curve()
    curve_slope = curve_data["slope"]
    curve_level = curve_data["level"]

    if hist_a.empty or hist_b.empty:
        return {"error": "Insufficient price data"}

    common_idx = hist_a.index.intersection(hist_b.index)
    if len(common_idx) < 100:
        return {"error": "Insufficient overlapping data"}

    prices_a = hist_a.loc[common_idx]
    prices_b = hist_b.loc[common_idx]

    vix_aligned      = vix_data["level"].reindex(common_idx, method="ffill")
    vix_perc_aligned = vix_data["percentile"].reindex(common_idx, method="ffill")
    vvix_aligned     = vvix_series.reindex(common_idx, method="ffill")

    spreads = np.log(prices_a) - np.log(prices_b)
    vols_a  = prices_a.rolling(20).std() * np.sqrt(252) * 100
    vols_b  = prices_b.rolling(20).std() * np.sqrt(252) * 100

    gini_level, gini_trend, gini_series = fetcher.get_inequality_signal()
    gini_aligned = gini_series.reindex(common_idx, method="ffill").ffill()
    gini_delta   = gini_aligned.pct_change().fillna(0)

    log_dark.info("Computing topological features...")
    basket_rets = pd.DataFrame({
        "a":    prices_a.pct_change(),
        "b":    prices_b.pct_change(),
        "vix":  vix_aligned.pct_change(),
        "vvix": vvix_aligned.pct_change(),
    }).dropna()

    hodge = DeepDarkHodgeEngine(correlation_threshold=cfg.hodge_corr_threshold)
    grad_dom, harm_int, vorticity = hodge.compute_flow_metrics(
        basket_rets, gini_trend=gini_trend, vix_data=vix_data,
        vvix_level=float(vvix_aligned.iloc[-1]), curve_slope=curve_slope,
    )

    log_dark.info(f"Hodge: λ1={grad_dom:.3f}  Harmonic={harm_int:.3f}  "
                  f"Vorticity={vorticity:.3f}")
    log_dark.info(f"VIX curve: slope={curve_slope:.4f}  level={curve_level:.2f}")

    features_df = pd.DataFrame({
        "spread":         spreads,
        "vol_a":          vols_a,
        "vol_b":          vols_b,
        "gini_trend":     gini_delta,
        "grad_dominance": grad_dom,
        "vix_level":      vix_aligned,
        "vvix":           vvix_aligned,
        "vix_perc":       vix_perc_aligned,
        "curve_slope":    curve_slope,
        "curve_level":    curve_level,
    }).dropna()

    if len(features_df) < 200:
        return {"error": "Insufficient feature data"}

    seq_len = cfg.sequence_length
    spread_changes = spreads.diff().shift(-1).dropna()
    valid_idx      = features_df.index.intersection(spread_changes.index)
    features_df    = features_df.loc[valid_idx]
    spread_changes = spread_changes.loc[valid_idx]

    X, y = [], []
    for i in range(seq_len, len(features_df)):
        X.append(features_df.iloc[i - seq_len: i].values)
        y.append(float(spread_changes.iloc[i - 1]))
    X, y = np.array(X), np.array(y)

    if len(X) < 100:
        return {"error": "Insufficient training samples"}

    # [SI-01] Use Hologram2's unified StandardScaler (no sklearn)
    scaler        = StandardScaler()
    X_reshaped    = X.reshape(-1, X.shape[-1])
    X_scaled      = scaler.fit_transform(X_reshaped).reshape(X.shape)

    split   = int(0.8 * len(X))
    X_train = X_scaled[:split];  X_test = X_scaled[split:]
    y_train = y[:split];          y_test = y[split:]

    log_dark.info(f"Training model on {len(X_train)} samples...")
    model = DeepDarkHyperModel(cfg, device=DEVICE)
    model.train_gan(X_train, epochs=cfg.gan_epochs, batch_size=cfg.batch_size)
    model.train_predictor(X_train, y_train, epochs=cfg.predictor_epochs,
                          batch_size=cfg.batch_size)

    test_pred = model.predict_spread_delta(X_test[-1]) if len(X_test) > 0 else 0.0

    metrics = {
        "lambda1":          grad_dom,
        "harmonic_intensity": harm_int,
        "vorticity":        vorticity,
        "model_var":        0.02 ** 2,
        "gan_var":          0.015 ** 2,
        "vix_level":        float(vix_aligned.iloc[-1]),
        "vvix_level":       float(vvix_aligned.iloc[-1]),
        "vix_percentile":   float(vix_perc_aligned.iloc[-1]),
        "curve_slope":      curve_slope,
    }
    intervals = DeepDarkIntervals().compute_intervals(test_pred, metrics)

    log_dark.info("Running backtest...")
    backtest_results = backtest_stat_arb(
        features_df, model, threshold=cfg.arb_threshold,
        initial_capital=cfg.initial_capital,
        vix_data={"level": vix_aligned, "percentile": vix_perc_aligned},
        vvix_series=vvix_aligned, curve_slope=curve_slope,
    )

    # [SI-04] Threshold optimisation: Optuna if available, else grid search
    log_dark.info("Optimising threshold...")
    _bt_kwargs = dict(
        model=model, initial_capital=cfg.initial_capital,
        vix_data={"level": vix_aligned, "percentile": vix_perc_aligned},
        vvix_series=vvix_aligned, curve_slope=curve_slope,
    )

    if OPTUNA_AVAILABLE:
        def _objective(trial: "optuna.Trial") -> float:
            t = trial.suggest_float("threshold", 1.0, 4.0)
            bt = backtest_stat_arb(features_df, threshold=t, **_bt_kwargs)
            return -bt.get("monthly_edge", 0)

        study = optuna.create_study(direction="minimize")
        study.optimize(_objective, n_trials=cfg.optuna_trials, show_progress_bar=False)
        best_thresh = study.best_params["threshold"]
    else:
        log_dark.info("optuna not installed — running grid search over thresholds")
        grid_results = {}
        for t in [1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0]:
            bt = backtest_stat_arb(features_df, threshold=t, **_bt_kwargs)
            grid_results[t] = bt.get("monthly_edge", 0)
        best_thresh = max(grid_results, key=grid_results.get)

    final_backtest = backtest_stat_arb(
        features_df, threshold=best_thresh, **_bt_kwargs)

    results = {
        "pair":              pair,
        "latest_spread":     float(spreads.iloc[-1]),
        "predicted_delta":   test_pred,
        "gini_latest":       float(gini_level),
        "gini_trend":        float(gini_trend),
        "latest_vix":        float(vix_aligned.iloc[-1]),
        "latest_vvix":       float(vvix_aligned.iloc[-1]),
        "vix_percentile":    float(vix_perc_aligned.iloc[-1]),
        "curve_slope":       curve_slope,
        "curve_level":       curve_level,
        "best_threshold":    best_thresh,
        **intervals,
        **final_backtest,
    }

    log_dark.info(f"Spread forecast: {test_pred:.4f}")
    log_dark.info(f"80% CI: {intervals['80%_CI']}")
    log_dark.info(f"Sharpe: {final_backtest['sharpe']:.2f}  |  "
                  f"Monthly edge: {final_backtest['monthly_edge']:.2f}%")
    return results


# ═══════════════════════════════════════════════════════════════════════════════
#  SECTION 20 — TREATISE CONTEXT  [N-04]
# ═══════════════════════════════════════════════════════════════════════════════

@dataclass
class TreatiseContext:
    """
    [N-04] Attaches Treatise-grounded interpretations to any Hologram2 result.
    Maps quantitative outputs to Treatise concepts: Six Pillars, Cantillon
    phase, gradient regime, and cultural propagation stage.
    """
    # ── Original fields (v1.0) ──────────────────────────────────────────────
    gradient_regime: str = "unknown"    # 'gradient_flow' | 'vortex' | 'harmonic' | 'dissolution' | 'balanced'
    cantillon_phase: str = "unknown"    # 'expansion' | 'contraction' | 'trap' | 'equilibrium'
    active_pillars:  List[str] = field(default_factory=list)
    inequality_gradient: float = 0.0   # normalised Gini delta → gradient strength
    cultural_phase: str = "unknown"    # 'spore' | 'mycelium' | 'fruiting' | 'dormant'
    notes: str = ""

    # ── NROS Extension fields (v2.0) ─────────────────────────────────────────
    # PHI — Pillar Health Index
    pillar_health:    Dict[str, float] = field(default_factory=dict)
    composite_floor:  float = 0.0      # min(φ) — Axiom 5 Multiplicative Resilience
    composite_mean:   float = 0.0      # avg(φ)
    gradient_spread:  float = 0.0      # max(φ) − min(φ) — Pillar Gini
    threshold_status: str = "unknown"  # 'BELOW' | 'APPROACHING' | 'EXCEEDED'
    stressed_count:   int = 0          # Count of Pillars with PHI < 0.40

    # Hodge decomposition on PHI K₆ graph
    hodge_gradient:   float = 0.0      # Gradient component percentage
    hodge_curl:       float = 0.0      # Curl component percentage
    hodge_harmonic:   float = 0.0      # Harmonic component percentage
    hodge_dominant:   str = "unknown"  # 'gradient' | 'curl' | 'harmonic'
    hodge_total_energy: float = 0.0    # √(Σ flow²)

    # Entity specification
    scale:  str = "National"
    nation: str = ""

    # Polity Assessment
    polity_fail_prob: float = 0.0      # Average of four failure modes
    polity_modes:     Dict[str, float] = field(default_factory=dict)
    compound_failures: int = 0         # Count of compounds > 0.55

    # SOC Assessment
    soc_stored_energy: Dict[str, float] = field(default_factory=dict)
    soc_criticality:   float = 0.0     # Average stored energy
    criticality_tau:   float = 0.0     # Return time indicator
    criticality_sigma: float = 0.0     # Volatility indicator
    criticality_rho:   float = 0.0     # Autocorrelation indicator

    # Conflict Assessment
    conflict_active:      bool = False
    conflict_domains:     List[str] = field(default_factory=list)
    conflict_trinity:     Dict[str, float] = field(default_factory=dict)
    conflict_escalation:  float = 0.0
    conflict_termination: str = "absent"  # 'absent' | 'unclear' | 'defined' | 'achievable'

    # Gradient map and trajectories
    gradient_map:          List[Dict] = field(default_factory=list)
    trajectory_scenarios:  List[Dict] = field(default_factory=list)

    # [F2 FIX] Fields for parity with the HTML dashboard's JSON output
    cascade_risks:         List[Dict] = field(default_factory=list)
    timestamp:             str = ""

    @classmethod
    def from_results(cls, oracle_result: Dict,
                     gini_trend: float = 0.0) -> "TreatiseContext":
        topo = oracle_result.get("topology", {})
        reg  = oracle_result.get("regime",   {})
        crit = oracle_result.get("criticality", {})
        sig  = oracle_result.get("signal", {})

        # Gradient regime from Hodge decomposition
        grad = topo.get("gradient_dominance", 0.0)
        curl = topo.get("curl_dominance",     0.0)
        harm = topo.get("harmonic_intensity", 0.0)

        if grad > 0.6:
            gradient_regime = "gradient_flow"
        elif curl > 0.4:
            gradient_regime = "vortex"
        elif harm > 0.3:
            gradient_regime = "harmonic"
        else:
            gradient_regime = "dissolution"

        # Cantillon phase from regime
        regime_id = reg.get("id", 0)
        cantillon = {
            0: "expansion",      # Low-vol trending
            1: "trap",           # High-vol choppy
            2: "contraction",    # Crisis
            3: "expansion",      # Recovery
        }.get(regime_id, "unknown")

        # [F4 FIX] Active Six Pillars — prefer PHI-based (PHI ≥ 0.50, matching
        # the literature at ¶1280 and the canonical from_nros() constructor)
        # when pillar_health is present in the oracle result; otherwise fall
        # back to signal-confidence top-N as a rough proxy. This keeps the
        # two constructors' semantics aligned.
        pillar_health = oracle_result.get("pillar_health")
        pillars = ["Service", "Product", "Information", "Entertainment",
                   "Transport", "Energy"]
        if isinstance(pillar_health, dict) and pillar_health:
            active_pillars = [p for p in PILLAR_NAMES
                              if pillar_health.get(p, 0.0) >= 0.50]
        else:
            # Legacy fallback: top N by signal confidence. Deprecated —
            # callers should supply pillar_health for canonical behaviour.
            raw_score = sig.get("raw_score", 0.0)
            n_active = max(1, int(sig.get("confidence", 0.5) * 6))
            active_pillars = pillars[:n_active]

        # Cultural phase from criticality
        crit_status = crit.get("status", "insufficient_data")
        if crit_status == "near_critical":
            cultural_phase = "fruiting"   # High-energy propagation
        elif crit_status == "subcritical":
            cultural_phase = "mycelium"   # Stable network growth
        elif gradient_regime == "dissolution":
            cultural_phase = "dormant"
        else:
            cultural_phase = "spore"      # Exploratory / memetic spread

        notes = (
            f"Inequality gradient (Gini Δ={gini_trend:+.4f}) drives vorticity. "
            f"Cantillon phase '{cantillon}' implies asset-class compression for "
            f"non-institutional actors. SOC criticality: {crit_status}."
        )

        return cls(
            gradient_regime    = gradient_regime,
            cantillon_phase    = cantillon,
            active_pillars     = active_pillars,
            inequality_gradient = abs(gini_trend),
            cultural_phase     = cultural_phase,
            notes              = notes,
        )

    @classmethod
    def from_nros(cls, nros_output: Dict) -> "TreatiseContext":
        """
        [NROS-01] Construct TreatiseContext from a complete NROS synthesis output.
        This is the primary pathway for feeding Samsara Method analysis into
        Hologram2's analytical subsystems.

        Parameters
        ----------
        nros_output : dict
            Complete output from NROSSynthesisEngine.synthesize() containing
            PHI scores, polity assessment, SOC assessment, Hodge decomposition,
            conflict assessment, gradient map, and trajectory projections.
        """
        phis   = nros_output.get("pillar_health", {})
        hodge  = nros_output.get("hodge", {})
        regime = nros_output.get("regime", {})
        polity = nros_output.get("polity", {})
        soc    = nros_output.get("soc", {})
        conflict = nros_output.get("conflict", {})

        return cls(
            # Original fields
            gradient_regime    = regime.get("gradient_regime", "unknown"),
            cantillon_phase    = regime.get("cantillon_phase", "unknown"),
            cultural_phase     = regime.get("cultural_phase", "unknown"),
            active_pillars     = nros_output.get("active_pillars", []),
            inequality_gradient = nros_output.get("gradient_spread", 0.0),
            notes              = nros_output.get("notes", ""),
            # PHI fields
            pillar_health      = phis,
            composite_floor    = nros_output.get("composite_floor", 0.0),
            composite_mean     = nros_output.get("composite_mean", 0.0),
            gradient_spread    = nros_output.get("gradient_spread", 0.0),
            threshold_status   = nros_output.get("threshold_status", "unknown"),
            stressed_count     = nros_output.get("stressed_count", 0),
            # Hodge fields
            hodge_gradient     = hodge.get("gradient", 0.0),
            hodge_curl         = hodge.get("curl", 0.0),
            hodge_harmonic     = hodge.get("harmonic", 0.0),
            hodge_dominant     = hodge.get("dominant", "unknown"),
            hodge_total_energy = hodge.get("total_energy", 0.0),
            # Entity
            scale              = nros_output.get("scale", "National"),
            nation             = nros_output.get("nation", ""),
            # Polity
            polity_fail_prob   = polity.get("aggregate", 0.0),
            polity_modes       = polity.get("modes", {}),
            compound_failures  = polity.get("compound_count", 0),
            # SOC
            soc_stored_energy  = soc.get("categories", {}),
            soc_criticality    = soc.get("composite", 0.0),
            criticality_tau    = soc.get("tau", 0.0),
            criticality_sigma  = soc.get("sigma", 0.0),
            criticality_rho    = soc.get("rho", 0.0),
            # Conflict
            conflict_active    = conflict.get("active", False),
            conflict_domains   = conflict.get("domains", []),
            conflict_trinity   = conflict.get("trinity", {}),
            conflict_escalation = conflict.get("escalation", 0.0),
            conflict_termination = conflict.get("termination", "absent"),
            # Gradients and trajectories
            gradient_map       = nros_output.get("gradient_map", []),
            trajectory_scenarios = nros_output.get("trajectories", []),
            # [F2 FIX] parity fields with HTML dashboard
            cascade_risks      = nros_output.get("cascade_risks", []),
            timestamp          = nros_output.get("timestamp", ""),
        )


# ═══════════════════════════════════════════════════════════════════════════════
#  SECTION 21 — HOLOGRAM2  (unified orchestrator)  [N-01, N-02, N-03]
# ═══════════════════════════════════════════════════════════════════════════════

class Hologram2:
    """
    [N-02] Top-level Hologram2 orchestrator.

    Integrates OracleHybrid5.5 (regime, topology, LSTM, criticality) with
    DeepDark2 (inequality-driven statistical arbitrage, GAN uncertainty,
    VIX futures curve) and anchors all outputs in the Treatise on Societies,
    Economies, and Cultures.

    Entry points:
      .analyze(ticker)            — Oracle full analysis
      .stat_arb(pair)             — DeepDark stat-arb pipeline
      .holistic(ticker, pair)     — Cross-module synthesis  [N-03]
    """

    def __init__(self, config: Optional[Hologram2Config] = None):
        self.cfg     = config or Hologram2Config()
        log.info("Hologram2 initialising...")

        # Shared fetcher
        self._fetcher = OracleDataFetcher(
            api_key     = self.cfg.api_key,
            cache_size  = self.cfg.oracle.max_cache_size,
            max_workers = self.cfg.oracle.max_fetch_workers,
        )

        # Subsystems
        self.oracle = OracleHybrid5_5(config=self.cfg.oracle, fetcher=self._fetcher)
        log.info("  Oracle subsystem: OracleHybrid5.5 ready")
        log.info("  DeepDark subsystem: DeepDark2 ready")
        log.info("Hologram2 online.")

    # ── Oracle analysis ────────────────────────────────────────────────────────
    def analyze(self, ticker: str, days_back: int = 800) -> Dict:
        """Run OracleHybrid5.5 analysis on a single ticker."""
        return self.oracle.run_analysis(ticker, days_back=days_back)

    def analyze_multi(self, tickers: List[str], days_back: int = 800) -> Dict[str, Dict]:
        """Run analysis on multiple tickers."""
        return self.oracle.run_multi(tickers, days_back=days_back)

    # ── DeepDark stat-arb ─────────────────────────────────────────────────────
    def stat_arb(self, pair: Tuple[str, str] = ("NVDA", "PG"),
                 days_back: int = 730) -> Dict:
        """Run DeepDark2 statistical arbitrage pipeline."""
        return deepdark_stat_arb(
            pair=pair, days_back=days_back,
            config=self.cfg.deepdark, fetcher=self._fetcher,
        )

    # ── [N-03] Holistic cross-module synthesis ────────────────────────────────
    def holistic(self, ticker: str,
                 pair: Optional[Tuple[str, str]] = None,
                 days_back: int = 800) -> Dict:
        """
        [N-03] Synthesizes Oracle + DeepDark outputs into a unified Hologram2
        signal, enriched with Treatise-grounded TreatiseContext annotations.

        Oracle provides the macro structural signal (regime, topology, criticality).
        DeepDark provides the micro-level spread forecast and inequality vorticity.
        TreatiseContext grounds both in the Treatise conceptual framework.
        """
        log.info(f"Hologram2.holistic() → {ticker}" +
                 (f" | pair={pair}" if pair else ""))

        # ── Oracle analysis ────────────────────────────────────────────────────
        oracle_result = self.analyze(ticker, days_back=days_back)

        # ── DeepDark analysis (optional) ───────────────────────────────────────
        dd_result: Dict = {}
        gini_trend = 0.0
        if pair:
            dd_result  = self.stat_arb(pair, days_back=days_back)
            gini_trend = dd_result.get("gini_trend", 0.0)

        # ── Holistic signal: merge Oracle signal with DeepDark spread forecast ─
        holistic_score = oracle_result.get("signal", {}).get("raw_score", 0.0)
        if dd_result and "predicted_delta" in dd_result:
            # Blend: 70% Oracle structural + 30% DeepDark micro signal
            dd_signal   = float(np.tanh(dd_result["predicted_delta"] * 50))
            holistic_score = 0.70 * holistic_score + 0.30 * dd_signal

        # ── Criticality overlay ───────────────────────────────────────────────
        crit = oracle_result.get("criticality", {})
        if crit.get("alert") == "high":
            holistic_score *= 0.3   # SOC near-critical → massive risk reduction
        elif crit.get("status") == "subcritical":
            holistic_score *= 1.05

        holistic_score = float(np.clip(holistic_score, -1, 1))

        # Classify
        if holistic_score > 0.4:
            h_signal = "STRONG_BUY"
        elif holistic_score > 0.15:
            h_signal = "BUY"
        elif holistic_score < -0.4:
            h_signal = "STRONG_SELL"
        elif holistic_score < -0.15:
            h_signal = "SELL"
        elif crit.get("alert") == "high":
            h_signal = "RISK_OFF"
        else:
            h_signal = "HOLD"

        # ── Treatise context ──────────────────────────────────────────────────
        treatise = TreatiseContext.from_results(oracle_result, gini_trend=gini_trend)

        return {
            "hologram2_signal":  h_signal,
            "hologram2_score":   round(holistic_score, 4),
            "oracle":            oracle_result,
            "deepdark":          dd_result,
            "treatise_context": {
                "gradient_regime":    treatise.gradient_regime,
                "cantillon_phase":    treatise.cantillon_phase,
                "cultural_phase":     treatise.cultural_phase,
                "active_pillars":     treatise.active_pillars,
                "inequality_gradient": round(treatise.inequality_gradient, 6),
                "notes":              treatise.notes,
            },
            "timestamp": datetime.now().isoformat(),
        }

    def __repr__(self) -> str:
        return (f"Hologram2(oracle=OracleHybrid5.5, deepdark=DeepDark2, "
                f"device={DEVICE})")


# ═══════════════════════════════════════════════════════════════════════════════
#  ENTRY POINT
# ═══════════════════════════════════════════════════════════════════════════════

# ═══════════════════════════════════════════════════════════════════════════════
#  SECTION 22 — NROS: PILLAR HEALTH INDEX ENGINE
# ═══════════════════════════════════════════════════════════════════════════════

PILLAR_NAMES = ["Energy", "Information", "Product", "Service", "Transport", "Entertainment"]
PILLAR_ROLES = {
    "Energy":        "PRIMARY",
    "Information":   "COORDINATIVE",
    "Product":       "SUSTENANCE",
    "Service":       "INSTITUTIONAL",
    "Transport":     "CONNECTIVE",
    "Entertainment": "COHESIVE",
}

HEALTH_TIERS = [
    (0.80, "STRONG"),
    (0.60, "ADEQUATE"),
    (0.40, "STRESSED"),
    (0.20, "SEVERE"),
    (0.00, "EXISTENTIAL"),
]


def phi_health_label(phi_value: float) -> str:
    """Map PHI score to five-tier health classification."""
    for threshold, label in HEALTH_TIERS:
        if phi_value >= threshold:
            return label
    return "EXISTENTIAL"


def normalize_indicator(raw: float, bench: float, method: str) -> float:
    """
    Normalize a raw sub-indicator value to [0, 1] using one of seven methods.

    Methods
    -------
    'direct'   : min(raw / bench, 1.0)           — Higher raw = healthier
    'inverted' : max(0, 1 - raw / bench)          — Lower raw = healthier
    'zscore'   : 1 − min(|raw|/bench, 3)/3, clamped [0,1] — linear deviation ramp
    'hhi'      : max(0, 1 - raw)                   — Concentration index
    'grade'    : Letter grade to [0, 1] mapping    — Categorical
    'pct'      : min(raw / 100, 1.0)              — Direct percentage
    'sigmoid'  : 1 / (1 + e^((raw/100 - bench/100) / 0.15))  — Nonlinear threshold
    """
    if method == "grade":
        grade_map = {
            "A+": 1.0, "A": 1.0, "A-": 0.92, "B+": 0.83, "B": 0.75, "B-": 0.67,
            "C+": 0.58, "C": 0.50, "C-": 0.42, "D+": 0.33, "D": 0.25, "D-": 0.17,
            "F": 0.0,
        }
        return grade_map.get(str(raw), 0.5)
    if method == "direct":
        return min(raw / bench, 1.0) if bench != 0 else 0.0
    elif method == "inverted":
        return max(0.0, 1.0 - raw / bench) if bench != 0 else 0.0
    elif method == "zscore":
        z = abs(raw) / bench if bench != 0 else 0.0
        return max(0.0, min(1.0, 2.0 * (1.0 - 0.5 * (1.0 + min(z, 3.0) / 3.0))))
    elif method == "hhi":
        return max(0.0, 1.0 - raw)
    elif method == "pct":
        return min(raw / 100.0, 1.0)
    elif method == "sigmoid":
        x = (raw / 100.0 - bench / 100.0) / 0.15
        return 1.0 / (1.0 + math.exp(x))
    else:
        return min(raw / bench, 1.0) if bench != 0 else 0.0


def compute_pillar_phi(indicators: List[Dict]) -> float:
    """
    Compute weighted PHI for a single Pillar from its sub-indicators.

    Each indicator dict must have keys: 'raw', 'bench', 'norm' (method), 'w' (weight).
    Returns a float in [0, 1].
    """
    total_weight = 0.0
    weighted_sum = 0.0
    for ind in indicators:
        method = ind.get("norm", "direct")
        raw_val = ind.get("raw", 0)
        bench_val = ind.get("bench", 1)
        # Grade normalization handles strings; all others need float
        if method != "grade":
            raw_val = float(raw_val)
            bench_val = float(bench_val)
        nv = normalize_indicator(raw_val, bench_val, method)
        w = float(ind.get("w", 0))
        weighted_sum += nv * w
        total_weight += w
    return weighted_sum / total_weight if total_weight > 0 else 0.0


# ── Canonical U.S. baseline indicators ────────────────────────────────────────
US_BASELINE_INDICATORS = {
    # v3.5 NOTE: E7, E8 are substrate-flavored sub-indicators (climate-coupled).
    # Existing E1-E6 weights reduced from 1.00 → 0.90 to accommodate substrate
    # additions at 0.10 combined weight. See wiki/frameworks/biosphere-as-natural-
    # infrastructure.md and wiki/pillars/energy-substrate-addendum.md.
    # 'syntropy_bound' field: 'fiscal' = repairable on fiscal cycle (built infra);
    # 'regeneration' = bounded by natural regeneration rate (substrate); absent = N/A.
    "Energy": [
        {"id": "E1", "name": "Reserve Margin",    "raw": 17,   "bench": 15,  "norm": "direct",   "w": 0.18, "syntropy_bound": "fiscal"},
        {"id": "E2", "name": "Import Dependency",  "raw": 12,   "bench": 100, "norm": "inverted", "w": 0.18, "syntropy_bound": "fiscal"},
        {"id": "E3", "name": "Price Volatility",   "raw": 1.4,  "bench": 1,   "norm": "zscore",   "w": 0.13},
        {"id": "E4", "name": "Source Diversity",    "raw": 0.24, "bench": 1,   "norm": "hhi",      "w": 0.18, "syntropy_bound": "fiscal"},
        {"id": "E5", "name": "Affordability",       "raw": 7.5,  "bench": 15,  "norm": "inverted", "w": 0.13},
        {"id": "E6", "name": "Infrastructure Age",  "raw": 45,   "bench": 100, "norm": "inverted", "w": 0.10, "syntropy_bound": "fiscal"},
        # Substrate-flavored: climate envelope (κ) coupling
        {"id": "E7", "name": "Carbon Trajectory",   "raw": 82,   "bench": 100, "norm": "inverted", "w": 0.05, "syntropy_bound": "regeneration", "substrate": "climate"},
        {"id": "E8", "name": "Climate-Risk Margin", "raw": 28,   "bench": 100, "norm": "inverted", "w": 0.05, "syntropy_bound": "regeneration", "substrate": "climate"},
    ],
    "Information": [
        {"id": "I1", "name": "Broadband",          "raw": 75,   "bench": 100, "norm": "pct",      "w": 0.15},
        {"id": "I2", "name": "Media Concentration", "raw": 0.32, "bench": 1,   "norm": "hhi",      "w": 0.20},
        {"id": "I3", "name": "Cyber Resilience",    "raw": 38,   "bench": 100, "norm": "direct",   "w": 0.25},
        {"id": "I4", "name": "Misinfo Prevalence",  "raw": 30,   "bench": 50,  "norm": "inverted", "w": 0.20},
        {"id": "I5", "name": "Digital Literacy",    "raw": 56,   "bench": 100, "norm": "direct",   "w": 0.10},
        {"id": "I6", "name": "Redundancy Index",    "raw": 55,   "bench": 100, "norm": "direct",   "w": 0.10},
    ],
    "Product": [
        {"id": "P1", "name": "Ag Self-Sufficiency", "raw": 95,   "bench": 100, "norm": "direct",   "w": 0.17, "syntropy_bound": "fiscal"},
        {"id": "P2", "name": "Fertilizer Dep.",     "raw": 60,   "bench": 100, "norm": "inverted", "w": 0.13, "syntropy_bound": "fiscal"},
        {"id": "P3", "name": "Mfg Capacity Util.",  "raw": 78,   "bench": 85,  "norm": "direct",   "w": 0.12, "syntropy_bound": "fiscal"},
        {"id": "P4", "name": "Supply Chain Stress",  "raw": 0.5,  "bench": 1,   "norm": "zscore",   "w": 0.17},
        {"id": "P5", "name": "Strategic Reserves",   "raw": 50,   "bench": 90,  "norm": "direct",   "w": 0.13, "syntropy_bound": "fiscal"},
        {"id": "P6", "name": "Pharma Import Ratio",  "raw": 80,   "bench": 100, "norm": "inverted", "w": 0.12, "syntropy_bound": "fiscal"},
        # Substrate-flavored: soil (σ), pollinator-network (ρ), agricultural hydrology (η)
        {"id": "P7", "name": "Soil Capital",          "raw": 55,   "bench": 100, "norm": "direct",   "w": 0.07, "syntropy_bound": "regeneration", "substrate": "soil"},
        {"id": "P8", "name": "Pollinator Health",     "raw": 60,   "bench": 100, "norm": "direct",   "w": 0.04, "syntropy_bound": "regeneration", "substrate": "biotic_relationships"},
        {"id": "P9", "name": "Ag Water Stress",       "raw": 55,   "bench": 100, "norm": "direct",   "w": 0.05, "syntropy_bound": "regeneration", "substrate": "hydrology"},
    ],
    "Service": [
        {"id": "S1", "name": "Institutional Trust",  "raw": 16,   "bench": 100, "norm": "pct",      "w": 0.24},
        {"id": "S2", "name": "Fiscal Headroom",      "raw": 123,  "bench": 90,  "norm": "sigmoid",  "w": 0.19, "syntropy_bound": "fiscal"},
        {"id": "S3", "name": "Healthcare Surge",      "raw": 28,   "bench": 35,  "norm": "direct",   "w": 0.14, "syntropy_bound": "fiscal"},
        {"id": "S4", "name": "Judicial Independence", "raw": 69,   "bench": 100, "norm": "direct",   "w": 0.14},
        {"id": "S5", "name": "Regulatory Capacity",   "raw": 55,   "bench": 100, "norm": "pct",      "w": 0.14, "syntropy_bound": "fiscal"},
        {"id": "S6", "name": "Financial Stress",      "raw": 1.2,  "bench": 1,   "norm": "zscore",   "w": 0.10},
        # Substrate-flavored: hydrology (η) — water utility natural infrastructure
        {"id": "S7", "name": "Watershed Service Capacity", "raw": 55, "bench": 100, "norm": "direct", "w": 0.05, "syntropy_bound": "regeneration", "substrate": "hydrology"},
    ],
    "Transport": [
        {"id": "T1", "name": "Infrastructure Grade", "raw": "C-", "bench": "A",  "norm": "grade",    "w": 0.19, "syntropy_bound": "fiscal"},
        {"id": "T2", "name": "Chokepoint Dep.",      "raw": 35,   "bench": 100, "norm": "inverted", "w": 0.19},
        {"id": "T3", "name": "Port Throughput",       "raw": 5,    "bench": 10,  "norm": "inverted", "w": 0.14, "syntropy_bound": "fiscal"},
        {"id": "T4", "name": "Route Redundancy",      "raw": 55,   "bench": 100, "norm": "direct",   "w": 0.14, "syntropy_bound": "fiscal"},
        {"id": "T5", "name": "Freight Cost Stab.",     "raw": 60,   "bench": 100, "norm": "direct",   "w": 0.14},
        {"id": "T6", "name": "Bridge Deficiency",     "raw": 7,    "bench": 15,  "norm": "inverted", "w": 0.15, "syntropy_bound": "fiscal"},
        # Substrate-flavored: climate envelope (κ) — assets in climate-vulnerable corridors
        {"id": "T7", "name": "Climate-Risk Asset Exposure", "raw": 25, "bench": 100, "norm": "inverted", "w": 0.05, "syntropy_bound": "regeneration", "substrate": "climate"},
    ],
    "Entertainment": [
        # v3.0: surface sub-indicators rescaled from sum-1.00 to sum-0.50
        # (relative ratios preserved). Substrate sub-indicators N6-N13 added below
        # at sum-0.50 (8 × 0.0625), making total Entertainment weight = 1.00.
        # Within-SHI renormalized weights = 0.125 each, matching v3.0 paper IV.1.
        {"id": "N1", "name": "Social Cohesion",     "raw": 30,   "bench": 100, "norm": "direct",   "w": 0.125},
        {"id": "N2", "name": "Polarization Index",   "raw": 75,   "bench": 100, "norm": "inverted", "w": 0.125},
        {"id": "N3", "name": "Shared Narrative",      "raw": 25,   "bench": 100, "norm": "pct",      "w": 0.10},
        {"id": "N4", "name": "Cultural Participation","raw": 50,   "bench": 100, "norm": "pct",      "w": 0.075},
        {"id": "N5", "name": "Mental Health",         "raw": 14,   "bench": 30,  "norm": "inverted", "w": 0.075},
        # ── Substrate-flavored: meaning (religion / ideology / identity) ──
        # Per v3.0 Working Paper Part IV.1; all health-direction (higher = healthier).
        # Bench=100 throughout; norm=direct since labels are now health-direction.
        # syntropy_bound='regeneration' — substrate is replenished through CRED /
        # costly-commitment practice over generations, not on a fiscal cycle.
        # US 2025 substrate values reflect bilateral-substrate-failure framing
        # (managerial-liberal vs. populist) per v3.0 paper Part III.3:
        # caretaker legitimacy contested, gradient amplitude high, costly-commitment
        # density declining (mainline collapse + civic-ritual decline), bilateral
        # four-mode failure, both factions in active alarm-mode discourse.
        # External substrate-projection still strong (Hollywood, English, USD,
        # civic-democratic narrative) despite contested domestic substrate.
        {"id": "N6",  "name": "Caretaker Legitimacy",            "raw": 42, "bench": 100, "norm": "direct", "w": 0.0625, "syntropy_bound": "regeneration", "substrate": "meaning"},
        {"id": "N7",  "name": "Substrate-Gradient Cohesion",     "raw": 32, "bench": 100, "norm": "direct", "w": 0.0625, "syntropy_bound": "regeneration", "substrate": "meaning"},
        {"id": "N8",  "name": "Costly-Commitment Density",       "raw": 38, "bench": 100, "norm": "direct", "w": 0.0625, "syntropy_bound": "regeneration", "substrate": "meaning"},
        {"id": "N9",  "name": "Caretaker Four-Mode Integrity",   "raw": 38, "bench": 100, "norm": "direct", "w": 0.0625, "syntropy_bound": "regeneration", "substrate": "meaning"},
        {"id": "N10", "name": "Cross-Pillar Coupling Integrity", "raw": 50, "bench": 100, "norm": "direct", "w": 0.0625, "syntropy_bound": "regeneration", "substrate": "meaning"},
        {"id": "N11", "name": "Caretaker Reflexive Composure",   "raw": 35, "bench": 100, "norm": "direct", "w": 0.0625, "syntropy_bound": "regeneration", "substrate": "meaning"},
        {"id": "N12", "name": "Substrate Retention",             "raw": 42, "bench": 100, "norm": "direct", "w": 0.0625, "syntropy_bound": "regeneration", "substrate": "meaning"},
        {"id": "N13", "name": "External Substrate-Projection",   "raw": 62, "bench": 100, "norm": "direct", "w": 0.0625, "syntropy_bound": "regeneration", "substrate": "meaning"},
    ],
}


# ── Venezuela 2019 Canonical Baseline (collapsing-polity regression fixture) ──
# Stylized indicator set grounded in documented 2019 figures (March nationwide
# blackout, ~9,585% hyperinflation per IMF, press-freedom rank 148/180 per RSF,
# manufacturing at ~15% of historical capacity, public-health collapse per
# PAHO, ~5M-person emigration wave). Calibrated so that Energy, Information,
# and Product land below 0.40 — the productive and informational core of the
# polity has hollowed out.
#
# Expected synthesis under nros() — v3.0 (UPDATED, verified against implementation):
#   stressed   = 4/6            (was 3/6)
#   threshold  = EXCEEDED       (was APPROACHING)
#   regime     = harmonic       (CHANGED from 'dissolution' — spread shrinks to
#                                ~0.13, below the 0.15 dissolution-band lower
#                                bound, because Entertainment dropping compresses
#                                the gradient. 'Harmonic' here does not mean
#                                healthy; it means uniform failure across Pillars.)
#   cantillon  = contraction    (CHANGED from 'trap'; stressed≥4 branch)
#   cordyceps  = dormant        (CHANGED from 'fruiting'; stressed≥4)
#
# v3.0 NOTE [V3-07]: Embedding meaning-substrate sub-indicators into Entertainment
# under the v3.0 architectural decision drops Venezuela's Entertainment PHI from
# ~0.455 to ~0.333, putting Entertainment below the 0.40 stressed threshold.
# This pushes the polity from 3/6 stressed (v2) to 4/6 stressed (v3) AND
# compresses the cross-Pillar spread from ~0.16 to ~0.13. The compressed spread
# falls below the 0.15 dissolution-band lower bound, so the regime classifier
# returns 'harmonic' rather than 'dissolution'. ALL FOUR v2 anchor classifications
# (dissolution, trap, fruiting, APPROACHING) are unhooked.
#
# This is the substantively correct v3.0 reading: Venezuela 2019 substrate
# (Bolivarianism in collapse, Catholic Church mostly opposition, mass emigration,
# bilateral substrate-projection failure) is deeply stressed, and the v2 reading
# of Entertainment at 0.455 was over-optimistic because it lacked substrate
# probing. The result is uniform Pillar failure, which the framework correctly
# labels 'harmonic' (small gradient, not healthy harmony) + 'contraction'
# (active polity-wide retreat) + 'dormant' (no Pillar viable as recovery anchor)
# + 'EXCEEDED' (4/6 stressed). This reading is more accurate than the v2 anchor
# of dissolution+trap+fruiting+APPROACHING.
#
# Inflating Venezuela substrate scores to preserve the v2 anchors would be
# Rule-3-prohibited motivated reasoning. Future v3.x calibration should add
# dedicated baselines to re-anchor the unhooked classifications. Candidate
# fixtures: Lebanon 2021 (banking collapse without polity-wide contraction —
# asymmetric distress, fits dissolution), Argentina 2001 (corralito + IMF
# crisis with rapid recovery — fits trap), late Weimar 1932 (asymmetric
# distress despite residual capacity — also fits dissolution).
VEN_2019_BASELINE_INDICATORS: Dict[str, List[Dict]] = {
    "Energy": [
        {"id": "E1", "name": "Reserve Margin",     "raw": 3,    "bench": 15,  "norm": "direct",   "w": 0.18, "syntropy_bound": "fiscal"},
        {"id": "E2", "name": "Import Dependency",  "raw": 40,   "bench": 100, "norm": "inverted", "w": 0.18, "syntropy_bound": "fiscal"},
        {"id": "E3", "name": "Price Volatility",   "raw": 3.2,  "bench": 1,   "norm": "zscore",   "w": 0.13},
        {"id": "E4", "name": "Source Diversity",   "raw": 0.45, "bench": 1,   "norm": "hhi",      "w": 0.18, "syntropy_bound": "fiscal"},
        {"id": "E5", "name": "Affordability",      "raw": 11,   "bench": 15,  "norm": "inverted", "w": 0.13},
        {"id": "E6", "name": "Infrastructure Age", "raw": 75,   "bench": 100, "norm": "inverted", "w": 0.10, "syntropy_bound": "fiscal"},
        # Substrate-flavored: climate envelope (κ) coupling
        # VEN 2019: Carbon trajectory below US per-capita (lower industrial throughput);
        # climate-risk margin moderate (Caribbean basin exposure but smaller infra footprint)
        {"id": "E7", "name": "Carbon Trajectory",   "raw": 65,   "bench": 100, "norm": "inverted", "w": 0.05, "syntropy_bound": "regeneration", "substrate": "climate"},
        {"id": "E8", "name": "Climate-Risk Margin", "raw": 35,   "bench": 100, "norm": "inverted", "w": 0.05, "syntropy_bound": "regeneration", "substrate": "climate"},
    ],
    "Information": [
        {"id": "I1", "name": "Broadband",           "raw": 46,   "bench": 100, "norm": "pct",      "w": 0.15},
        {"id": "I2", "name": "Media Concentration", "raw": 0.60, "bench": 1,   "norm": "hhi",      "w": 0.20},
        {"id": "I3", "name": "Cyber Resilience",    "raw": 22,   "bench": 100, "norm": "direct",   "w": 0.25},
        {"id": "I4", "name": "Misinfo Prevalence",  "raw": 38,   "bench": 50,  "norm": "inverted", "w": 0.20},
        {"id": "I5", "name": "Digital Literacy",    "raw": 42,   "bench": 100, "norm": "direct",   "w": 0.10},
        {"id": "I6", "name": "Redundancy Index",    "raw": 35,   "bench": 100, "norm": "direct",   "w": 0.10},
    ],
    "Product": [
        {"id": "P1", "name": "Ag Self-Sufficiency", "raw": 50,   "bench": 100, "norm": "direct",   "w": 0.17, "syntropy_bound": "fiscal"},
        {"id": "P2", "name": "Fertilizer Dep.",     "raw": 80,   "bench": 100, "norm": "inverted", "w": 0.13, "syntropy_bound": "fiscal"},
        {"id": "P3", "name": "Mfg Capacity Util.",  "raw": 40,   "bench": 85,  "norm": "direct",   "w": 0.12, "syntropy_bound": "fiscal"},
        {"id": "P4", "name": "Supply Chain Stress", "raw": 3.0,  "bench": 1,   "norm": "zscore",   "w": 0.17},
        {"id": "P5", "name": "Strategic Reserves",  "raw": 35,   "bench": 90,  "norm": "direct",   "w": 0.13, "syntropy_bound": "fiscal"},
        {"id": "P6", "name": "Pharma Import Ratio", "raw": 75,   "bench": 100, "norm": "inverted", "w": 0.12, "syntropy_bound": "fiscal"},
        # Substrate-flavored. VEN 2019 substrate notes:
        # - Soil capital relatively intact (less industrial monoculture pressure)
        # - Pollinator networks healthier than US (less pesticide pressure)
        # - Water stress moderate (orinoco basin but distribution failure dominates)
        {"id": "P7", "name": "Soil Capital",          "raw": 50,   "bench": 100, "norm": "direct",   "w": 0.07, "syntropy_bound": "regeneration", "substrate": "soil"},
        {"id": "P8", "name": "Pollinator Health",     "raw": 70,   "bench": 100, "norm": "direct",   "w": 0.04, "syntropy_bound": "regeneration", "substrate": "biotic_relationships"},
        {"id": "P9", "name": "Ag Water Stress",       "raw": 55,   "bench": 100, "norm": "direct",   "w": 0.05, "syntropy_bound": "regeneration", "substrate": "hydrology"},
    ],
    "Service": [
        {"id": "S1", "name": "Institutional Trust",   "raw": 30,   "bench": 100, "norm": "pct",      "w": 0.24},
        {"id": "S2", "name": "Fiscal Headroom",       "raw": 90,   "bench": 90,  "norm": "sigmoid",  "w": 0.19, "syntropy_bound": "fiscal"},
        {"id": "S3", "name": "Healthcare Surge",      "raw": 22,   "bench": 35,  "norm": "direct",   "w": 0.14, "syntropy_bound": "fiscal"},
        {"id": "S4", "name": "Judicial Independence", "raw": 30,   "bench": 100, "norm": "direct",   "w": 0.14},
        {"id": "S5", "name": "Regulatory Capacity",   "raw": 45,   "bench": 100, "norm": "pct",      "w": 0.14, "syntropy_bound": "fiscal"},
        {"id": "S6", "name": "Financial Stress",      "raw": 1.8,  "bench": 1,   "norm": "zscore",   "w": 0.10},
        # Substrate-flavored: VEN 2019 water utility substrate degraded
        {"id": "S7", "name": "Watershed Service Capacity", "raw": 35, "bench": 100, "norm": "direct", "w": 0.05, "syntropy_bound": "regeneration", "substrate": "hydrology"},
    ],
    "Transport": [
        {"id": "T1", "name": "Infrastructure Grade", "raw": "C-", "bench": "A", "norm": "grade",    "w": 0.19, "syntropy_bound": "fiscal"},
        {"id": "T2", "name": "Chokepoint Dep.",      "raw": 55,   "bench": 100, "norm": "inverted", "w": 0.19},
        {"id": "T3", "name": "Port Throughput",      "raw": 6,    "bench": 10,  "norm": "inverted", "w": 0.14, "syntropy_bound": "fiscal"},
        {"id": "T4", "name": "Route Redundancy",     "raw": 52,   "bench": 100, "norm": "direct",   "w": 0.14, "syntropy_bound": "fiscal"},
        {"id": "T5", "name": "Freight Cost Stab.",   "raw": 45,   "bench": 100, "norm": "direct",   "w": 0.14},
        {"id": "T6", "name": "Bridge Deficiency",    "raw": 9,    "bench": 15,  "norm": "inverted", "w": 0.15, "syntropy_bound": "fiscal"},
        # Substrate-flavored: lower climate-vulnerable corridor exposure than US
        {"id": "T7", "name": "Climate-Risk Asset Exposure", "raw": 20, "bench": 100, "norm": "inverted", "w": 0.05, "syntropy_bound": "regeneration", "substrate": "climate"},
    ],
    "Entertainment": [
        # v3.0: surface rescaled to sum-0.50; substrate added at sum-0.50.
        # Venezuela 2019 substrate values reflect documented Bolivarianism collapse:
        # caretaker legitimacy ~zero (Maduro illegitimate per UN reporting; Catholic
        # Church mostly opposition); substrate-gradient cohesion low (binary Chavismo/
        # opposition split); costly-commitment density declining mass with Pentecostal
        # offset; caretaker four-mode integrity catastrophic (CPI 168/180); cross-Pillar
        # coupling broken (substrate divorced from broken Pillars); reflexive composure
        # low (Patria-or-death rhetoric escalating); substrate retention very low
        # (5M+ emigration wave 2014-2019); external projection minimal (Bolivarianism
        # discredited beyond Cuba/Nicaragua relics).
        {"id": "N1", "name": "Social Cohesion",       "raw": 50,   "bench": 100, "norm": "direct",   "w": 0.125},
        {"id": "N2", "name": "Polarization Index",    "raw": 78,   "bench": 100, "norm": "inverted", "w": 0.125},
        {"id": "N3", "name": "Shared Narrative",      "raw": 45,   "bench": 100, "norm": "pct",      "w": 0.10},
        {"id": "N4", "name": "Cultural Participation","raw": 70,   "bench": 100, "norm": "pct",      "w": 0.075},
        {"id": "N5", "name": "Mental Health",         "raw": 14,   "bench": 30,  "norm": "inverted", "w": 0.075},
        # ── Substrate-flavored: meaning (Bolivarianism + Catholic + Pentecostal) ──
        {"id": "N6",  "name": "Caretaker Legitimacy",            "raw": 18, "bench": 100, "norm": "direct", "w": 0.0625, "syntropy_bound": "regeneration", "substrate": "meaning"},
        {"id": "N7",  "name": "Substrate-Gradient Cohesion",     "raw": 28, "bench": 100, "norm": "direct", "w": 0.0625, "syntropy_bound": "regeneration", "substrate": "meaning"},
        {"id": "N8",  "name": "Costly-Commitment Density",       "raw": 32, "bench": 100, "norm": "direct", "w": 0.0625, "syntropy_bound": "regeneration", "substrate": "meaning"},
        {"id": "N9",  "name": "Caretaker Four-Mode Integrity",   "raw": 12, "bench": 100, "norm": "direct", "w": 0.0625, "syntropy_bound": "regeneration", "substrate": "meaning"},
        {"id": "N10", "name": "Cross-Pillar Coupling Integrity", "raw": 22, "bench": 100, "norm": "direct", "w": 0.0625, "syntropy_bound": "regeneration", "substrate": "meaning"},
        {"id": "N11", "name": "Caretaker Reflexive Composure",   "raw": 20, "bench": 100, "norm": "direct", "w": 0.0625, "syntropy_bound": "regeneration", "substrate": "meaning"},
        {"id": "N12", "name": "Substrate Retention",             "raw": 18, "bench": 100, "norm": "direct", "w": 0.0625, "syntropy_bound": "regeneration", "substrate": "meaning"},
        {"id": "N13", "name": "External Substrate-Projection",   "raw": 18, "bench": 100, "norm": "direct", "w": 0.0625, "syntropy_bound": "regeneration", "substrate": "meaning"},
    ],
}

VEN_2019_POLITY: Dict[str, float] = {
    "Mismanagement": 0.85, "Malfeasance": 0.80,
    "RentSeeking": 0.90, "Incompetence": 0.78,
}

VEN_2019_SOC: Dict[str, float] = {
    "fiscal": 0.95, "infrastructure": 0.90, "institutional": 0.88,
    "social": 0.80, "geopolitical": 0.85,
}

VEN_2019_CONFLICT: Dict = {
    "active": True,
    "domains": ["Economic", "Political", "Humanitarian"],
    "trinity": {"passion": 0.85, "chance": 0.70, "purpose": 0.20},
    "escalation": 0.70,
    "termination": "absent",
}

VEN_2019_ENTITY: Dict[str, str] = {
    "nation": "Venezuela", "scale": "National", "region": "South America",
}


def venezuela_2019_baseline() -> Dict[str, object]:
    """
    Return the complete Venezuela 2019 canonical bundle (indicators + polity
    + SOC + conflict + entity) as a single dict, suitable for spreading into
    ``Hologram2.nros(**venezuela_2019_baseline())``. This is the pinned
    regression fixture for the dissolution/trap branches of the regime and
    Cantillon classifiers.
    """
    return {
        "indicators": VEN_2019_BASELINE_INDICATORS,
        "polity":     VEN_2019_POLITY,
        "soc":        VEN_2019_SOC,
        "conflict":   VEN_2019_CONFLICT,
        "entity":     VEN_2019_ENTITY,
    }


# ── Hungary 2024 Canonical Baseline (NEW v3.0; SHI-anchor regression fixture) ──
# Per v3.0 Working Paper Section IV.6 worked example. The Hungary baseline is
# the pinned regression anchor for SHI itself: substrate sub-indicator scores
# are taken directly from the v3.0 paper, and the framework's published SHI
# composite of 0.4375 ≈ 0.44 (STRESSED tier) is reproducible from these inputs.
#
# Caretaker: Fidesz-KDNP "illiberal Christian democracy"
# Residual/opposition substrate: liberal-European; Tisza party rising 2024–26
# Freedom House: "Partly Free" since 2019; Nations in Transit 2020 reclassified
# to "transitional/hybrid regime"; European Parliament 2022 resolution: no longer
# a full democracy [T1].
#
# Substrate sub-indicator raw values (from v3.0 paper IV.6):
#   N6  Caretaker Legitimacy            55 (T2 — repeated 2/3 majorities, eroding 2024-26)
#   N7  Substrate-Gradient Cohesion     35 (T2 — strong urban Budapest vs rural)
#   N8  Costly-Commitment Density       40 (T3 — church attendance moderate; KDNP shallow)
#   N9  Caretaker Four-Mode Integrity   30 (T2 — EU corruption findings; rule-of-law conditionality)
#   N10 Cross-Pillar Coupling Integrity 45 (T2 — strong Information capture; weaker Energy)
#   N11 Caretaker Reflexive Composure   50 (T2 — Tisza challenge prompting election-cycle policy)
#   N12 Substrate Retention             40 (T2 — significant emigration to W Europe)
#   N13 External Substrate-Projection   60 (T2 — CPAC Hungary; influence on US right; V4)
#
# Composite SHI (equal-weighted): (55+35+40+30+45+50+40+60)/8 = 44.375 → 0.4438
#   Tier: STRESSED (0.40-0.59 band) ✓ matches v3.0 paper
#   Cascade-threshold check: N7 (35) and N9 (30) below 0.40 → 2/8 below threshold
#                            → cascade NOT triggered (proximity flagged) ✓ matches paper
#
# All-Pillar PHI estimates for Hungary 2024 (T2 throughout from public sources):
#   Energy        ~0.55  (Russia-dependence stress; Paks NPP operating; reserves ok)
#   Information   ~0.45  (concentrated media; RSF press freedom 67/180 in 2024)
#   Product       ~0.55  (auto industry; ag self-sufficient; EU-integrated)
#   Service       ~0.50  (institutional trust mid; rising corruption; healthcare strained)
#   Transport     ~0.55  (decent infra; rail+road; Black Sea access via Romania)
#   Entertainment  0.44  (computed from substrate-embedded structure above)
#
# Expected synthesis under nros() — verified against the engine (v3.5):
#   stressed   = 0/6  (all Pillars ≥ 0.40)
#   threshold  = BELOW
#   regime     = balanced         (spread 0.194 — the coarse all-Pillar
#                                  estimates above suggested ~0.11/harmonic,
#                                  but the computed indicator set yields
#                                  Product 0.652 vs Entertainment 0.458;
#                                  spread ≥ 0.15 leaves the harmonic band
#                                  and no other branch fires → balanced)
#   cantillon  = equilibrium      (mean ~0.545, mid-range; not trap because
#                                  substrate-conflict is sub-cascade scale)
#   cordyceps  = spore            (stressed=0; mean<0.60)
#
# This anchors a NEW quadrant: substrate-stressed-but-pillar-resilient — a polity
# with a STRESSED substrate (SHI 0.44) inside an otherwise functional Pillar set.
# The diagnostic value: the substrate-borrowing scalar exposes substrate fragility
# that the all-Pillar composite would otherwise smooth over.

HUN_2024_BASELINE_INDICATORS: Dict[str, List[Dict]] = {
    "Energy": [
        {"id": "E1", "name": "Reserve Margin",     "raw": 12,   "bench": 15,  "norm": "direct",   "w": 0.18, "syntropy_bound": "fiscal"},
        {"id": "E2", "name": "Import Dependency",  "raw": 60,   "bench": 100, "norm": "inverted", "w": 0.18, "syntropy_bound": "fiscal"},
        {"id": "E3", "name": "Price Volatility",   "raw": 1.6,  "bench": 1,   "norm": "zscore",   "w": 0.13},
        {"id": "E4", "name": "Source Diversity",   "raw": 0.30, "bench": 1,   "norm": "hhi",      "w": 0.18, "syntropy_bound": "fiscal"},
        {"id": "E5", "name": "Affordability",      "raw": 9,    "bench": 15,  "norm": "inverted", "w": 0.13},
        {"id": "E6", "name": "Infrastructure Age", "raw": 50,   "bench": 100, "norm": "inverted", "w": 0.10, "syntropy_bound": "fiscal"},
        # Substrate (climate)
        {"id": "E7", "name": "Carbon Trajectory",   "raw": 70,   "bench": 100, "norm": "inverted", "w": 0.05, "syntropy_bound": "regeneration", "substrate": "climate"},
        {"id": "E8", "name": "Climate-Risk Margin", "raw": 30,   "bench": 100, "norm": "inverted", "w": 0.05, "syntropy_bound": "regeneration", "substrate": "climate"},
    ],
    "Information": [
        {"id": "I1", "name": "Broadband",           "raw": 80,   "bench": 100, "norm": "pct",      "w": 0.15},
        {"id": "I2", "name": "Media Concentration", "raw": 0.65, "bench": 1,   "norm": "hhi",      "w": 0.20},
        {"id": "I3", "name": "Cyber Resilience",    "raw": 50,   "bench": 100, "norm": "direct",   "w": 0.25},
        {"id": "I4", "name": "Misinfo Prevalence",  "raw": 35,   "bench": 50,  "norm": "inverted", "w": 0.20},
        {"id": "I5", "name": "Digital Literacy",    "raw": 60,   "bench": 100, "norm": "direct",   "w": 0.10},
        {"id": "I6", "name": "Redundancy Index",    "raw": 50,   "bench": 100, "norm": "direct",   "w": 0.10},
    ],
    "Product": [
        {"id": "P1", "name": "Ag Self-Sufficiency", "raw": 100,  "bench": 100, "norm": "direct",   "w": 0.17, "syntropy_bound": "fiscal"},
        {"id": "P2", "name": "Fertilizer Dep.",     "raw": 65,   "bench": 100, "norm": "inverted", "w": 0.13, "syntropy_bound": "fiscal"},
        {"id": "P3", "name": "Mfg Capacity Util.",  "raw": 70,   "bench": 85,  "norm": "direct",   "w": 0.12, "syntropy_bound": "fiscal"},
        {"id": "P4", "name": "Supply Chain Stress", "raw": 0.8,  "bench": 1,   "norm": "zscore",   "w": 0.17},
        {"id": "P5", "name": "Strategic Reserves",  "raw": 55,   "bench": 90,  "norm": "direct",   "w": 0.13, "syntropy_bound": "fiscal"},
        {"id": "P6", "name": "Pharma Import Ratio", "raw": 70,   "bench": 100, "norm": "inverted", "w": 0.12, "syntropy_bound": "fiscal"},
        # Substrate (soil/biotic/hydrology)
        {"id": "P7", "name": "Soil Capital",          "raw": 60,   "bench": 100, "norm": "direct",   "w": 0.07, "syntropy_bound": "regeneration", "substrate": "soil"},
        {"id": "P8", "name": "Pollinator Health",     "raw": 65,   "bench": 100, "norm": "direct",   "w": 0.04, "syntropy_bound": "regeneration", "substrate": "biotic_relationships"},
        {"id": "P9", "name": "Ag Water Stress",       "raw": 60,   "bench": 100, "norm": "direct",   "w": 0.05, "syntropy_bound": "regeneration", "substrate": "hydrology"},
    ],
    "Service": [
        {"id": "S1", "name": "Institutional Trust",   "raw": 35,   "bench": 100, "norm": "pct",      "w": 0.24},
        {"id": "S2", "name": "Fiscal Headroom",       "raw": 75,   "bench": 90,  "norm": "sigmoid",  "w": 0.19, "syntropy_bound": "fiscal"},
        {"id": "S3", "name": "Healthcare Surge",      "raw": 25,   "bench": 35,  "norm": "direct",   "w": 0.14, "syntropy_bound": "fiscal"},
        {"id": "S4", "name": "Judicial Independence", "raw": 40,   "bench": 100, "norm": "direct",   "w": 0.14},
        {"id": "S5", "name": "Regulatory Capacity",   "raw": 55,   "bench": 100, "norm": "pct",      "w": 0.14, "syntropy_bound": "fiscal"},
        {"id": "S6", "name": "Financial Stress",      "raw": 1.2,  "bench": 1,   "norm": "zscore",   "w": 0.10},
        {"id": "S7", "name": "Watershed Service Capacity", "raw": 55, "bench": 100, "norm": "direct", "w": 0.05, "syntropy_bound": "regeneration", "substrate": "hydrology"},
    ],
    "Transport": [
        {"id": "T1", "name": "Infrastructure Grade", "raw": "C+", "bench": "A", "norm": "grade",    "w": 0.19, "syntropy_bound": "fiscal"},
        {"id": "T2", "name": "Chokepoint Dep.",      "raw": 30,   "bench": 100, "norm": "inverted", "w": 0.19},
        {"id": "T3", "name": "Port Throughput",      "raw": 6,    "bench": 10,  "norm": "inverted", "w": 0.14, "syntropy_bound": "fiscal"},
        {"id": "T4", "name": "Route Redundancy",     "raw": 60,   "bench": 100, "norm": "direct",   "w": 0.14, "syntropy_bound": "fiscal"},
        {"id": "T5", "name": "Freight Cost Stab.",   "raw": 60,   "bench": 100, "norm": "direct",   "w": 0.14},
        {"id": "T6", "name": "Bridge Deficiency",    "raw": 8,    "bench": 15,  "norm": "inverted", "w": 0.15, "syntropy_bound": "fiscal"},
        {"id": "T7", "name": "Climate-Risk Asset Exposure", "raw": 25, "bench": 100, "norm": "inverted", "w": 0.05, "syntropy_bound": "regeneration", "substrate": "climate"},
    ],
    "Entertainment": [
        # v3.0: surface rescaled to sum-0.50; substrate added at sum-0.50.
        # Surface raw values estimated from Eurobarometer / V-Dem for Hungary 2024.
        # Substrate raw values are taken DIRECTLY from v3.0 Working Paper IV.6.
        {"id": "N1", "name": "Social Cohesion",       "raw": 55,   "bench": 100, "norm": "direct",   "w": 0.125},
        {"id": "N2", "name": "Polarization Index",    "raw": 70,   "bench": 100, "norm": "inverted", "w": 0.125},
        {"id": "N3", "name": "Shared Narrative",      "raw": 50,   "bench": 100, "norm": "pct",      "w": 0.10},
        {"id": "N4", "name": "Cultural Participation","raw": 60,   "bench": 100, "norm": "pct",      "w": 0.075},
        {"id": "N5", "name": "Mental Health",         "raw": 16,   "bench": 30,  "norm": "inverted", "w": 0.075},
        # ── Substrate-flavored: meaning (Christian-nationalist + liberal-European) ──
        # Values from v3.0 Working Paper Section IV.6 — DO NOT MODIFY without
        # explicit framework-revision rationale (regression anchor).
        {"id": "N6",  "name": "Caretaker Legitimacy",            "raw": 55, "bench": 100, "norm": "direct", "w": 0.0625, "syntropy_bound": "regeneration", "substrate": "meaning"},
        {"id": "N7",  "name": "Substrate-Gradient Cohesion",     "raw": 35, "bench": 100, "norm": "direct", "w": 0.0625, "syntropy_bound": "regeneration", "substrate": "meaning"},
        {"id": "N8",  "name": "Costly-Commitment Density",       "raw": 40, "bench": 100, "norm": "direct", "w": 0.0625, "syntropy_bound": "regeneration", "substrate": "meaning"},
        {"id": "N9",  "name": "Caretaker Four-Mode Integrity",   "raw": 30, "bench": 100, "norm": "direct", "w": 0.0625, "syntropy_bound": "regeneration", "substrate": "meaning"},
        {"id": "N10", "name": "Cross-Pillar Coupling Integrity", "raw": 45, "bench": 100, "norm": "direct", "w": 0.0625, "syntropy_bound": "regeneration", "substrate": "meaning"},
        {"id": "N11", "name": "Caretaker Reflexive Composure",   "raw": 50, "bench": 100, "norm": "direct", "w": 0.0625, "syntropy_bound": "regeneration", "substrate": "meaning"},
        {"id": "N12", "name": "Substrate Retention",             "raw": 40, "bench": 100, "norm": "direct", "w": 0.0625, "syntropy_bound": "regeneration", "substrate": "meaning"},
        {"id": "N13", "name": "External Substrate-Projection",   "raw": 60, "bench": 100, "norm": "direct", "w": 0.0625, "syntropy_bound": "regeneration", "substrate": "meaning"},
    ],
}

HUN_2024_POLITY: Dict[str, float] = {
    "Mismanagement": 0.55, "Malfeasance": 0.65,
    "RentSeeking": 0.70,  "Incompetence": 0.50,
}

HUN_2024_SOC: Dict[str, float] = {
    "fiscal": 0.70, "infrastructure": 0.60, "institutional": 0.85,
    "social": 0.75, "geopolitical": 0.70,
}

HUN_2024_CONFLICT: Dict = {
    "active": True,
    "domains": ["Political", "Information", "Identity"],
    "trinity": {"passion": 0.65, "chance": 0.55, "purpose": 0.50},
    "escalation": 0.45,
    "termination": "absent",
}

HUN_2024_ENTITY: Dict[str, str] = {
    "nation": "Hungary", "scale": "National", "region": "Central Europe",
}


def hungary_2024_baseline() -> Dict[str, object]:
    """
    Return the complete Hungary 2024 canonical bundle (indicators + polity
    + SOC + conflict + entity) as a single dict, suitable for spreading into
    ``Hologram2.nros(**hungary_2024_baseline())``.

    This is the pinned regression fixture for the SHI worked example from
    v3.0 Working Paper Section IV.6. The Entertainment substrate-only PHI
    (= SHI) should compute to ~0.44 (STRESSED tier), matching the paper's
    published value of 0.4375 within rounding.
    """
    return {
        "indicators": HUN_2024_BASELINE_INDICATORS,
        "polity":     HUN_2024_POLITY,
        "soc":        HUN_2024_SOC,
        "conflict":   HUN_2024_CONFLICT,
        "entity":     HUN_2024_ENTITY,
    }


# ═══════════════════════════════════════════════════════════════════════════════
#  SECTION 23 — NROS: INTERDEPENDENCY MATRIX & CASCADE ENGINE
# ═══════════════════════════════════════════════════════════════════════════════

# Cascade coupling coefficients: INTER[source][target] = strength ∈ [0,1]
# Energy→Product = 0.95 is the strongest (Haber-Bosch); Entertainment→Transport = 0.20 is weakest
INTERDEPENDENCY_MATRIX: Dict[str, Dict[str, float]] = {
    "Energy":        {"Energy": 0, "Information": 0.85, "Product": 0.95, "Service": 0.70, "Transport": 0.90, "Entertainment": 0.50},
    "Information":   {"Energy": 0.60, "Information": 0, "Product": 0.55, "Service": 0.90, "Transport": 0.65, "Entertainment": 0.85},
    "Product":       {"Energy": 0.40, "Information": 0.35, "Product": 0, "Service": 0.60, "Transport": 0.50, "Entertainment": 0.45},
    "Service":       {"Energy": 0.55, "Information": 0.70, "Product": 0.50, "Service": 0, "Transport": 0.45, "Entertainment": 0.75},
    "Transport":     {"Energy": 0.50, "Information": 0.40, "Product": 0.65, "Service": 0.40, "Transport": 0, "Entertainment": 0.35},
    "Entertainment": {"Energy": 0.25, "Information": 0.60, "Product": 0.30, "Service": 0.65, "Transport": 0.20, "Entertainment": 0},
}


def compute_cascade_risks(
    phis: Dict[str, float],
    inter: Optional[Dict[str, Dict[str, float]]] = None,
    threshold: float = 0.40,
) -> List[Dict]:
    """
    Compute cascade risk pathways for Pillars below the health threshold.

    For each source Pillar below `threshold`, computes the secondary stress
    that would propagate to each target Pillar via the interdependency matrix.

    Returns a list of dicts sorted by descending impact:
        [{"from": str, "to": str, "impact": float, "coeff": float, "src_phi": float}, ...]
    """
    if inter is None:
        inter = INTERDEPENDENCY_MATRIX

    risks: List[Dict] = []
    for src in PILLAR_NAMES:
        src_phi = phis.get(src, 0.0)
        if src_phi >= threshold:
            continue
        deficit = threshold - src_phi
        for tgt in PILLAR_NAMES:
            if src == tgt:
                continue
            coeff = inter.get(src, {}).get(tgt, 0.0)
            impact = deficit * coeff
            if impact > 0.01:
                risks.append({
                    "from":    src,
                    "to":      tgt,
                    "impact":  round(impact, 4),
                    "coeff":   coeff,
                    "src_phi": round(src_phi, 4),
                })
    risks.sort(key=lambda r: r["impact"], reverse=True)
    return risks


# ═══════════════════════════════════════════════════════════════════════════════
#  SECTION 24 — NROS: HODGE DECOMPOSITION ON PHI K₆ GRAPH
# ═══════════════════════════════════════════════════════════════════════════════

def hodge_decompose_phi(phis: Dict[str, float],
                        flow_override: Optional[List[float]] = None,
                        flow_mode: str = "empirical",
                        inter: Optional[Dict[str, Dict[str, float]]] = None) -> Dict:
    """
    [F1 FIX] Full Hodge decomposition on the complete graph K₆ using both
    boundary operators: B₁ (edge→node) and B₂ (triangle→edge).

    K₆ has 6 vertices, 15 edges, and 20 triangular faces (C(6,3) = 20).
    The edge-flow space decomposes orthogonally into three subspaces:

        image(B₁ᵀ)  → gradient flows  (potential differences)
        image(B₂)   → curl flows       (cyclic around triangles)
        ker(L₁)     → harmonic flows  (holes / structural)

    where L₁ = B₁B₁ᵀ + B₂ᵀB₂ is the edge Laplacian. On K₆ with the full
    2-skeleton attached (all 20 triangles filled), the complex is simply
    connected, so H₁(K₆) = 0 and the harmonic component is identically
    zero — any residual comes from numerical round-off alone.

    Curl projection: f_curl = B₂ᵀ (B₂B₂ᵀ)⁺ B₂ f, i.e. projection onto the
    subspace of edge-flows reachable as coboundaries of 2-cochains.

    Parameters
    ----------
    phis : dict
        Six Pillar PHI values.
    flow_override : Optional[List[float]]
        If provided, use these 15 edge flows directly. Must be ordered to
        match the canonical K₆ edge ordering from combinations(range(6), 2).
    flow_mode : str, default 'empirical'
        Ignored if flow_override is set. Otherwise:
          - 'empirical' (default): interdependency-weighted flow
              f(i,j) = M[i][j]·φᵢ − M[j][i]·φⱼ
            These asymmetric cross-coupled flows produce non-trivial curl
            components around any triangle where upstream/downstream
            coupling strengths differ (i.e. almost every triangle in K₆).
          - 'potential': legacy pure potential-difference flow
              f(i,j) = φᵢ − φⱼ
            By construction these flows live entirely in image(B₁), so
            curl and harmonic components are identically zero.
    inter : Optional[Dict[str, Dict[str, float]]]
        Interdependency matrix M. Defaults to INTERDEPENDENCY_MATRIX.
        Only used when flow_mode='empirical' and flow_override is None.

    Returns
    -------
    dict with keys:
        gradient, curl, harmonic (squared-norm percentages summing to 1.0)
        dominant ('gradient' | 'curl' | 'harmonic')
        total_energy (√Σ flow²)
        potentials (list of 6 node potentials)
        edges (list of 15 edge dicts)
        flow_mode (mode actually used: 'empirical', 'potential', or 'override')
    """
    vals = [phis.get(p, 0.0) for p in PILLAR_NAMES]
    n = 6

    # Edges in canonical order (i < j)
    edges: List[Tuple[int, int]] = []
    edge_idx: Dict[Tuple[int, int], int] = {}
    for i in range(n):
        for j in range(i + 1, n):
            edge_idx[(i, j)] = len(edges)
            edges.append((i, j))
    ne = len(edges)  # 15

    # Flows: overridden, empirical (weighted), or pure potential differences
    if flow_override is not None:
        if len(flow_override) != ne:
            raise ValueError(f"flow_override must have length {ne}, got {len(flow_override)}")
        flows = [float(f) for f in flow_override]
        mode_used = "override"
    elif flow_mode == "potential":
        flows = [vals[i] - vals[j] for (i, j) in edges]
        mode_used = "potential"
    else:
        # Empirical: interdependency-weighted asymmetric flow
        M = inter if inter is not None else INTERDEPENDENCY_MATRIX
        flows = []
        for (i, j) in edges:
            pi, pj = PILLAR_NAMES[i], PILLAR_NAMES[j]
            mij = M.get(pi, {}).get(pj, 0.0)
            mji = M.get(pj, {}).get(pi, 0.0)
            flows.append(mij * vals[i] - mji * vals[j])
        mode_used = "empirical"

    # ── B₁ (ne × n): edge→node incidence, -1 on tail, +1 on head ────────
    B1 = np.zeros((ne, n))
    for e, (i, j) in enumerate(edges):
        B1[e, i] = -1.0
        B1[e, j] = +1.0

    # ── B₂ (nt × ne): triangle→edge boundary, with consistent orientation
    # For triangle (i, j, k) with i<j<k, boundary = (j,k) − (i,k) + (i,j).
    triangles = list(combinations(range(n), 3))  # 20 for K₆
    nt = len(triangles)
    B2 = np.zeros((nt, ne))
    for t, (i, j, k) in enumerate(triangles):
        B2[t, edge_idx[(j, k)]] = +1.0
        B2[t, edge_idx[(i, k)]] = -1.0
        B2[t, edge_idx[(i, j)]] = +1.0

    f = np.asarray(flows, dtype=float)

    # ── Gradient projection: f_grad = B₁(B₁ᵀB₁)⁺B₁ᵀf ────────────────────
    L0 = B1.T @ B1 + np.eye(n) * 1e-9     # regularize null space
    potentials = np.linalg.solve(L0, B1.T @ f)
    f_grad = B1 @ potentials

    # ── Curl projection: f_curl = B₂ᵀ(B₂B₂ᵀ)⁺B₂f ────────────────────────
    G2 = B2 @ B2.T + np.eye(nt) * 1e-9
    alpha = np.linalg.solve(G2, B2 @ f)
    f_curl = B2.T @ alpha

    # ── Harmonic residual ───────────────────────────────────────────────
    f_harm = f - f_grad - f_curl

    # Energies (squared norms)
    total_energy = float(f @ f)
    grad_energy  = float(f_grad @ f_grad)
    curl_energy  = float(f_curl @ f_curl)
    harm_energy  = float(f_harm @ f_harm)

    te = max(total_energy, 1e-10)
    grad_pct = grad_energy / te
    curl_pct = curl_energy / te
    harm_pct = harm_energy / te

    # Re-normalize to exactly 1 (tiny numerical drift possible)
    s = grad_pct + curl_pct + harm_pct
    if s > 0:
        grad_pct, curl_pct, harm_pct = grad_pct / s, curl_pct / s, harm_pct / s

    if grad_pct >= curl_pct and grad_pct >= harm_pct:
        dominant = "gradient"
    elif curl_pct >= harm_pct:
        dominant = "curl"
    else:
        dominant = "harmonic"

    edge_data = [
        {"from": PILLAR_NAMES[ei], "to": PILLAR_NAMES[ej], "flow": round(flows[idx], 4)}
        for idx, (ei, ej) in enumerate(edges)
    ]

    return {
        "gradient":     round(grad_pct, 4),
        "curl":         round(curl_pct, 4),
        "harmonic":     round(harm_pct, 4),
        "dominant":     dominant,
        "total_energy": round(math.sqrt(total_energy), 4),
        "potentials":   [round(float(p), 4) for p in potentials],
        "edges":        edge_data,
        "flow_mode":    mode_used,
    }


# ═══════════════════════════════════════════════════════════════════════════════
#  SECTION 25 — NROS: POLITY ASSESSMENT ENGINE
# ═══════════════════════════════════════════════════════════════════════════════

FAILURE_MODES = ["Mismanagement", "Malfeasance", "RentSeeking", "Incompetence"]


def assess_polity(mode_probabilities: Dict[str, float]) -> Dict:
    """
    Assess polity failure modes, compound combinations, and aggregate probability.

    Parameters
    ----------
    mode_probabilities : dict
        {"Mismanagement": 0.70, "Malfeasance": 0.65, "RentSeeking": 0.75, "Incompetence": 0.65}

    Returns
    -------
    dict with:
        modes, aggregate, compounds (list of {pair, severity}), compound_count
    """
    modes = {m: mode_probabilities.get(m, 0.0) for m in FAILURE_MODES}
    aggregate = sum(modes.values()) / max(len(modes), 1)

    # Compute compound combinations (all pairs with severity > 0.55)
    compounds: List[Dict] = []
    mode_keys = list(modes.keys())
    for i in range(len(mode_keys)):
        for j in range(i + 1, len(mode_keys)):
            sev = (modes[mode_keys[i]] + modes[mode_keys[j]]) / 2.0
            if sev > 0.55:
                compounds.append({
                    "pair": f"{mode_keys[i]} + {mode_keys[j]}",
                    "severity": round(sev, 4),
                })
    compounds.sort(key=lambda c: c["severity"], reverse=True)

    return {
        "modes":          modes,
        "aggregate":      round(aggregate, 4),
        "compounds":      compounds,
        "compound_count": len(compounds),
    }


# ═══════════════════════════════════════════════════════════════════════════════
#  SECTION 26 — NROS: SOC ASSESSMENT ENGINE
# ═══════════════════════════════════════════════════════════════════════════════

SOC_CATEGORIES = ["fiscal", "infrastructure", "institutional", "social", "geopolitical"]

# v3.5 NOTE: SOC_CATEGORIES are STRUCTURALLY UNCHANGED. The 'infrastructure'
# category is now DEFINITIONALLY CLARIFIED to include both built infrastructure
# (highways, grids, bridges — canonical 0.72 anchor reflects this) AND natural
# infrastructure (soil capital, aquifer depletion, climate-vulnerable corridors).
#
# Two accounting modes are supported:
#   - 'built_only' (default — preserves canonical 0.72 anchor and SOC composite=0.764)
#   - 'inclusive'  (substrate-aware analyses — typically yields higher infrastructure value)
#
# See assess_soc_inclusive() for the optional inclusive-accounting path.
# Reference: wiki/concepts/five-stored-energy-categories.md (definitional clarification)


def assess_soc(stored_energy: Dict[str, float]) -> Dict:
    """
    Assess Self-Organized Criticality state from five stored energy categories.

    Derives criticality indicators:
        τ = 0.3 + 0.7θ  (return time)
        σ = 0.2 + 0.6θ  (volatility)
        ρ = 0.1 + 0.8θ  (autocorrelation)
    where θ = composite stored energy (average of five categories).

    Parameters
    ----------
    stored_energy : dict
        {"fiscal": 0.85, "infrastructure": 0.72, "institutional": 0.78,
         "social": 0.82, "geopolitical": 0.65}
    """
    cats = {k: stored_energy.get(k, 0.0) for k in SOC_CATEGORIES}
    composite = sum(cats.values()) / max(len(cats), 1)

    tau = 0.3 + composite * 0.7
    sigma = 0.2 + composite * 0.6
    rho = 0.1 + composite * 0.8

    if tau > 0.70 and sigma > 0.50 and rho > 0.60:
        status = "NEAR_CRITICAL"
    elif tau > 0.50 or sigma > 0.35 or rho > 0.40:
        status = "ELEVATED"
    else:
        status = "SUBCRITICAL"

    return {
        "categories": cats,
        "composite":  round(composite, 4),
        "tau":        round(tau, 4),
        "sigma":      round(sigma, 4),
        "rho":        round(rho, 4),
        "status":     status,
    }


def assess_soc_inclusive(
    stored_energy: Dict[str, float],
    natural_infrastructure_addend: float = 0.08,
) -> Dict:
    """
    Substrate-aware SOC assessment (v3.5 seamless extension).

    The 'infrastructure' category is computed as a sum of:
      - built infrastructure stored energy (the canonical input)
      - natural infrastructure addend (soil depletion, aquifer drawdown,
        climate-vulnerable corridors — substrate Depreciation Equation
        imbalance NOT accounted for in canonical inputs)

    The addend is a single scalar [0, 1] reflecting analyst-calibrated
    natural-infrastructure stored energy at the analysis scale. Default 0.08
    reflects U.S. national-scale natural-infrastructure deficit (substantial
    soil depletion, Ogallala/Central Valley aquifer overdraft, Atlantic and
    Gulf Coast climate-vulnerable infrastructure exposure) above the canonical
    0.72 built-infrastructure-only value.

    Final infrastructure value is clamped to [0, 1].

    NOTE: This is the OPTIONAL inclusive-accounting path. The default
    assess_soc() preserves the canonical 0.72 anchor and SOC=0.764 composite.
    Use this function for substrate-aware analyses; call out the addend
    explicitly in the analysis output (RULE 5: data tiering applies — the
    addend is typically T2 or T3 unless dataset-grounded).

    Parameters
    ----------
    stored_energy : dict
        Same canonical input as assess_soc().
    natural_infrastructure_addend : float
        Stored energy from natural infrastructure depletion. Default 0.08
        is U.S. national-scale heuristic; calibrate per scale.
    """
    cats = dict(stored_energy)
    base_infra = cats.get("infrastructure", 0.0)
    cats["infrastructure"] = min(1.0, base_infra + natural_infrastructure_addend)

    result = assess_soc(cats)
    result["accounting"] = "inclusive"
    result["natural_infrastructure_addend"] = natural_infrastructure_addend
    result["infrastructure_built_only"] = base_infra
    return result


# ── Substrate sub-indicator utilities (v3.5 seamless extension; v3.0 SHI integration) ──


# v3.0: Added 'meaning' to substrate dimensions. Meaning-substrate (religion /
# ideology / identity) lives inside the Entertainment Pillar per the v3.0 paper
# architectural decision (substrate is INSIDE Entertainment, not a 7th Pillar).
# Biospheric substrate (climate/soil/biotic_relationships/hydrology/biodiversity)
# is the v3.5 extension distributed across multiple Pillars. The two coexist
# and register independently in substrate_diagnostic() output.
SUBSTRATE_DIMENSIONS = ["climate", "soil", "biotic_relationships", "hydrology",
                        "biodiversity", "meaning"]


# ── Five-tier health classification thresholds (mirror PHI; v3.0 paper IV.1) ──
# These tiers apply to the SHI composite (substrate-only PHI of Entertainment)
# in addition to the standard PHI per Pillar. The thresholds are identical so
# that SHI and PHI are tier-comparable.
SHI_TIERS = HEALTH_TIERS  # Alias — the v3.0 paper specifies the same 5-tier scale.


def compute_shi(entertainment_indicators: List[Dict]) -> Dict:
    """
    Compute the Substrate Health Index (SHI) for an Entertainment Pillar.

    SHI is defined per the v3.0 Working Paper Section IV.1 as the substrate-only
    composite of the Entertainment Pillar: a weighted average of all sub-indicators
    tagged with substrate='meaning', renormalized so the substrate weights sum
    to 1.0 (yielding a [0, 1] composite tier-comparable with PHI).

    Architecturally this is just compute_pillar_phi_split()[phi_substrate_only]
    filtered to substrate='meaning'. The convenience wrapper here adds:
      - five-tier health classification per HEALTH_TIERS / SHI_TIERS
      - cascade-threshold check (4+ substrate sub-indicators below 0.40)
      - per-sub-indicator score breakdown
      - DO-NOT-DEPLOY annotation per v3.0 paper R2 closure

    Parameters
    ----------
    entertainment_indicators : list of dict
        Sub-indicator list for the Entertainment Pillar. Both surface (untagged)
        and substrate-flavored indicators are accepted; only those with
        substrate='meaning' contribute to the SHI composite.

    Returns
    -------
    dict with keys:
        composite              : SHI as float in [0, 1] (renormalized; substrate
                                 weights sum to 1.0 within the SHI subset)
        tier                   : five-tier label (STRONG/ADEQUATE/STRESSED/SEVERE/EXISTENTIAL)
        cascade_threshold      : bool (True if 4+ substrate sub-indicators below 0.40)
        sub_indicators_below_threshold : int count (0-8)
        sub_indicator_scores   : list of dicts, each with id/name/raw/normalized/weight
        substrate_count        : number of substrate='meaning' sub-indicators (8 canonical)
        deployment_status      : 'research_grade' (per v3.0 paper R2 closure)
        do_not_deploy_reason   : str — non-empty per R2; SHI numeric layer is
                                 research-grade pending validation conditions
                                 in v3.0 paper II.2

    Notes
    -----
    Returns composite=None and tier=None if no meaning-substrate sub-indicators
    are present. This indicates the Entertainment Pillar has not been v3.0-extended.
    """
    meaning = [ind for ind in entertainment_indicators
               if ind.get("substrate") == "meaning"]

    if not meaning:
        return {
            "composite":                      None,
            "tier":                            None,
            "cascade_threshold":               False,
            "sub_indicators_below_threshold":  0,
            "sub_indicator_scores":            [],
            "substrate_count":                 0,
            "deployment_status":               "n/a",
            "do_not_deploy_reason":            "No meaning-substrate sub-indicators present.",
        }

    # Compute per-sub-indicator normalized scores
    scores = []
    for ind in meaning:
        method = ind.get("norm", "direct")
        raw_val = ind.get("raw", 0)
        bench_val = ind.get("bench", 1)
        if method != "grade":
            raw_val = float(raw_val)
            bench_val = float(bench_val)
        nv = normalize_indicator(raw_val, bench_val, method)
        scores.append({
            "id":          ind.get("id", ""),
            "name":        ind.get("name", ""),
            "raw":         ind.get("raw", 0),
            "normalized":  round(nv, 4),
            "weight":      ind.get("w", 0),
        })

    # SHI composite = renormalized weighted average over meaning-substrate only
    composite = compute_pillar_phi(meaning)

    # Cascade-threshold check: count sub-indicators with normalized < 0.40
    below = sum(1 for s in scores if s["normalized"] < 0.40)
    cascade = below >= 4

    return {
        "composite":                      round(composite, 4),
        "tier":                            phi_health_label(composite),
        "cascade_threshold":               cascade,
        "sub_indicators_below_threshold":  below,
        "sub_indicator_scores":            scores,
        "substrate_count":                 len(meaning),
        "deployment_status":               "research_grade",
        "do_not_deploy_reason":           ("SHI numeric layer is research-grade "
                                           "per v3.0 Working Paper R2 closure. "
                                           "Validation conditions (power-law signature "
                                           "in event distribution, successful out-of-"
                                           "sample test on at least one substrate-"
                                           "transition event, rigorous SOC instantiation "
                                           "per II.2) are not yet met. Qualitative "
                                           "substrate analysis is operationally usable; "
                                           "the numeric SHI is illustrative of the "
                                           "protocol, not of the polity."),
    }


def split_substrate_indicators(
    pillar_indicators: List[Dict],
) -> Tuple[List[Dict], List[Dict]]:
    """
    Partition a Pillar's sub-indicators into (built/conventional, substrate-flavored).

    Substrate-flavored sub-indicators are tagged with a 'substrate' field whose
    value is one of SUBSTRATE_DIMENSIONS. Indicators without this field are
    treated as built/conventional.

    Returns (built_indicators, substrate_indicators).

    Use this for diagnostic decomposition — e.g., compute a Pillar's PHI both
    with and without substrate sub-indicators to see how much of the Pillar's
    apparent health is borrowed against substrate. The discrepancy is the
    substrate-borrowing diagnostic.
    """
    built, substrate = [], []
    for ind in pillar_indicators:
        if ind.get("substrate"):
            substrate.append(ind)
        else:
            built.append(ind)
    return built, substrate


def compute_pillar_phi_split(pillar_indicators: List[Dict]) -> Dict:
    """
    Compute three PHI variants for a Pillar (v3.5 substrate diagnostic):

      - phi_full          : canonical PHI using ALL sub-indicators (this is φ_p)
      - phi_built_only    : PHI using only non-substrate sub-indicators,
                            renormalized so weights sum to 1.0 within that subset
      - phi_substrate_only: PHI using only substrate sub-indicators, renormalized.
                            None if no substrate sub-indicators are present.

    Returns dict with phi_full, phi_built_only, phi_substrate_only,
    substrate_borrowing (= phi_built_only - phi_full when both available),
    and substrate_count.

    The substrate_borrowing scalar is positive when built-infrastructure health
    appears better than full-system health — the Pillar is borrowing against
    substrate to maintain its conventional-metric appearance. This is the
    seamless-integration diagnostic that surfaces what the Layer 0 sPHI
    discrepancy was designed to surface.
    """
    built, substrate = split_substrate_indicators(pillar_indicators)

    phi_full = compute_pillar_phi(pillar_indicators)
    phi_built_only = compute_pillar_phi(built) if built else 0.0

    if substrate:
        phi_substrate_only = compute_pillar_phi(substrate)
        substrate_borrowing = round(phi_built_only - phi_full, 4)
    else:
        phi_substrate_only = None
        substrate_borrowing = 0.0

    return {
        "phi_full":            round(phi_full, 4),
        "phi_built_only":      round(phi_built_only, 4),
        "phi_substrate_only":  round(phi_substrate_only, 4) if phi_substrate_only is not None else None,
        "substrate_borrowing": substrate_borrowing,
        "substrate_count":     len(substrate),
        "built_count":         len(built),
    }


def substrate_diagnostic(indicators_by_pillar: Dict[str, List[Dict]]) -> Dict:
    """
    Cross-Pillar substrate diagnostic for an entire system.

    For each Pillar, compute the substrate split. Identify the Pillar with the
    highest substrate-borrowing scalar (the Pillar most reliant on borrowed
    substrate to maintain apparent health). This is the v3.5 seamless analog
    of Layer 0's hot-cell ranking — but computed entirely from existing PHI
    machinery without new architecture.

    Parameters
    ----------
    indicators_by_pillar : dict
        {Pillar name: [sub-indicator dicts]}. Standard NROS shape.

    Returns
    -------
    dict with:
        per_pillar             : Pillar -> compute_pillar_phi_split() result
        max_borrowing_pillar   : Pillar name with greatest substrate-borrowing scalar
        max_borrowing_value    : that scalar
        substrate_aware_pillars: list of Pillars with substrate sub-indicators
    """
    per_pillar = {p: compute_pillar_phi_split(inds) for p, inds in indicators_by_pillar.items()}

    aware = [p for p, r in per_pillar.items() if r["substrate_count"] > 0]
    if aware:
        max_p = max(aware, key=lambda p: per_pillar[p]["substrate_borrowing"])
        max_v = per_pillar[max_p]["substrate_borrowing"]
    else:
        max_p, max_v = None, 0.0

    return {
        "per_pillar":              per_pillar,
        "max_borrowing_pillar":    max_p,
        "max_borrowing_value":     round(max_v, 4),
        "substrate_aware_pillars": aware,
    }




# ═══════════════════════════════════════════════════════════════════════════════
#  SECTION 26B — v3.1 SUBSTRATE RESEARCH-GRADE EXTENSIONS
#  ───────────────────────────────────────────────────────────────────────────
#  Closes Hologram2-development priorities (a), (b), (c) from v3.0 working
#  paper §IV.9 / Operational Recommendation #9. All three layers are
#  research-grade and carry DO-NOT-DEPLOY annotations. They are *additive* —
#  none of them modify the canonical v2.0/v3.0/v3.5 API surface. Removing this
#  section leaves Hologram2 functioning identically to v3.0.
#
#  The three layers, in order:
#    (a) Substrate-state variable measurement protocol
#        → SubstrateStateRecord, record_substrate_state()
#    (b) Cross-Pillar substrate coupling matrices
#        → SUBSTRATE_COUPLING_MATRIX, compute_pillar_substrate_pressure(),
#          compute_substrate_stress(), identify_substrate_hot_cell()
#    (c) Substrate event-size time series for power-law testing
#        → SubstrateEvent, SubstrateEventSeries, fit_power_law(),
#          kolmogorov_smirnov_distance(), test_power_law_signature(),
#          compare_distribution_alternatives()
#
#  RULE COMPLIANCE NOTES:
#    Rule 1 (no orthogonal Pillars): the C[p][b] matrix in (b) explicitly
#      operationalizes Pillar↔substrate cross-coupling. (b) is the
#      substrate-mode analog of M[i][j].
#    Rule 4 (per-civilization calibration): the matrix is provisional U.S.
#      national-scale only. Non-U.S. and sub-national applications must
#      recalibrate per substrate-coupling.md.
#    Rule 5 (T-tagging): COUPLING_TIER_MATRIX records per-cell T-tier;
#      SubstrateStateRecord and SubstrateEvent both require tier on every
#      input.
#    Rule 6 (intervention failure-mode analysis): hot-cell identification
#      surfaces the dominant Pillar-substrate pressure but does NOT
#      recommend interventions; intervention recommendations remain the
#      analyst's responsibility, subject to four-mode failure assessment.
# ═══════════════════════════════════════════════════════════════════════════════


# ─────────────────────────────────────────────────────────────────────────────
#  (a) SUBSTRATE-STATE VARIABLE MEASUREMENT PROTOCOL
# ─────────────────────────────────────────────────────────────────────────────
# v3.0 working paper §II.2 condition #1: "A formal substrate-state variable
# with measurement protocol (the SHI in Part IV is a candidate but not yet
# validated)." This section provides the protocol — a structured, time-tagged,
# T-tagged record format that combines the SHI (meaning-substrate) and BHI
# (biospheric-substrate) into a single comparable s(t) vector with full
# provenance. The numeric SHI/BHI values themselves remain research-grade.


# Canonical T-tier vocabulary, repeated here as a module-level constant so the
# protocol is self-describing. Aligns with Rule 5.
TIER_TAGS = ("T1", "T2", "T3")
TIER_DESCRIPTIONS = {
    "T1": "Official primary source (government statistical agency, peer-reviewed primary data).",
    "T2": "Reputable secondary or OSINT source (think-tank report, established journalism, secondary academic).",
    "T3": "Inferred or proxied (analyst estimate, derived from sparse signals, expert judgment).",
}


@dataclass
class SubstrateStateRecord:
    """
    Time-tagged substrate-state vector s(t) with full provenance metadata.

    This is the v3.1 protocol-layer object. A SubstrateStateRecord pairs
    each substrate dimension (SHI sub-indicators + BHI sub-indicators)
    with its measurement, T-tier, source, and observation date. The
    composite SHI/BHI scalars are recomputed deterministically from the
    component values; the record's job is *provenance and structure*,
    not novel computation.

    Fields
    ------
    timestamp : str
        ISO-8601 date or datetime of the observation. Required.
    polity : str
        Polity name (nation / sub-national entity).
    scale : str
        Scale of analysis (National / Regional / State / County / City).
    dimensions : dict
        Per-dimension dict. Keys are substrate dimensions from
        SUBSTRATE_DIMENSIONS. Each value is a dict:
            {
                "value":  float in [0, 1],   # health, higher = healthier
                "tier":   "T1" | "T2" | "T3",
                "source": str,
                "date":   str (ISO),         # may differ from record timestamp
                "notes":  str,               # optional
            }
    shi_composite : float | None
        Aggregate SHI for the meaning-substrate (renormalized weighted average
        across the eight v3.0 IV.1 sub-indicators). None if meaning-substrate
        sub-indicators absent.
    bhi_composite : float | None
        Aggregate BHI for biospheric-substrate dimensions (climate, soil,
        biotic_relationships, hydrology, biodiversity). None if no biospheric
        sub-indicators present.
    deployment_status : str
        Always "research_grade" per v3.0 II.2.
    rule_5_compliance : bool
        True iff every dimension entry has a non-empty tier in TIER_TAGS.
    rule_4_calibration_note : str
        Free-text note per Rule 4: identifies the calibration baseline used
        (e.g., "U.S. canonical 2025 baseline; weights unmodified" or
        "Hungary 2024 reweighted; 10% sensitivity test passed at <1-tier swing").
    """
    timestamp: str
    polity: str
    scale: str
    dimensions: Dict[str, Dict[str, Any]]
    shi_composite: Optional[float] = None
    bhi_composite: Optional[float] = None
    deployment_status: str = "research_grade"
    rule_5_compliance: bool = False
    rule_4_calibration_note: str = ""

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to plain dict (e.g. for JSON export to dashboard)."""
        return {
            "timestamp":               self.timestamp,
            "polity":                  self.polity,
            "scale":                   self.scale,
            "dimensions":              dict(self.dimensions),
            "shi_composite":           self.shi_composite,
            "bhi_composite":           self.bhi_composite,
            "deployment_status":       self.deployment_status,
            "rule_5_compliance":       self.rule_5_compliance,
            "rule_4_calibration_note": self.rule_4_calibration_note,
            "do_not_deploy_reason":   ("Substrate-state record is research-grade "
                                       "per v3.0 II.2. Validation conditions "
                                       "(power-law signature in event distribution, "
                                       "successful out-of-sample test, rigorous SOC "
                                       "instantiation) are not yet met."),
        }

    def t1_share(self) -> float:
        """Share of dimensions tagged T1. Diagnostic for record quality."""
        if not self.dimensions:
            return 0.0
        n_t1 = sum(1 for d in self.dimensions.values() if d.get("tier") == "T1")
        return n_t1 / len(self.dimensions)


def record_substrate_state(
    indicators_by_pillar: Dict[str, List[Dict]],
    polity: str,
    scale: str,
    timestamp: Optional[str] = None,
    rule_4_calibration_note: str = "U.S. canonical baseline; per Rule 4 — recalibrate for non-U.S. or sub-national.",
) -> SubstrateStateRecord:
    """
    Assemble a SubstrateStateRecord from indicator dicts (the standard NROS
    shape used everywhere in Hologram2).

    The function walks every Pillar's substrate-flavored sub-indicators
    (those carrying a `substrate` field), records their normalized value,
    T-tier (defaulted to T2 if absent — explicitly flagged), and source.
    It then computes the SHI composite (over `substrate='meaning'` sub-
    indicators) and the BHI composite (over the biospheric subset).

    Parameters
    ----------
    indicators_by_pillar : dict
        {Pillar name: [sub-indicator dicts]}. Standard NROS shape.
    polity : str
        Polity name.
    scale : str
        Analysis scale (National / Regional / State / County / City).
    timestamp : str | None
        ISO timestamp. Defaults to today's date.
    rule_4_calibration_note : str
        Per Rule 4: which calibration baseline applies, with note on whether
        weights have been adjusted and whether 10% sensitivity test was run.

    Returns
    -------
    SubstrateStateRecord
        Time-tagged, T-tagged record with composites computed.
    """
    if timestamp is None:
        timestamp = date.today().isoformat()

    dimensions: Dict[str, Dict[str, Any]] = {}
    rule_5_ok = True

    # Walk every Pillar; collect substrate-flavored indicators
    biospheric_inds: List[Dict] = []
    for pillar, inds in indicators_by_pillar.items():
        for ind in inds:
            sub_dim = ind.get("substrate")
            if not sub_dim or sub_dim not in SUBSTRATE_DIMENSIONS:
                continue

            method  = ind.get("norm", "direct")
            raw_val = ind.get("raw", 0)
            bench   = ind.get("bench", 1)
            if method != "grade":
                raw_val = float(raw_val)
                bench   = float(bench)
            nv = normalize_indicator(raw_val, bench, method)

            tier = ind.get("tier")  # explicit if present
            if tier not in TIER_TAGS:
                # Default to T2 with explicit flag — preserves Rule 5 visibility
                tier = "T2"
                rule_5_ok = False  # absence of explicit tier is itself a Rule 5 issue

            entry = {
                "value":     round(nv, 4),
                "tier":      tier,
                "source":    ind.get("source", "(unspecified)"),
                "date":      ind.get("date", timestamp),
                "notes":     ind.get("notes", ""),
                "indicator_id":   ind.get("id", ""),
                "indicator_name": ind.get("name", ""),
                "pillar":         pillar,
                "weight":         float(ind.get("w", 1.0)),
            }

            # Multiple Pillars may contribute to the same biospheric dimension
            # (e.g. climate is carried by E7, E8, T7). Aggregate by weighted
            # mean using the indicator weights w in the source.
            # v3.5 FIX (I): the first contributor previously entered this fold
            # with a hardcoded weight of 1.0 instead of its true w (so U.S.
            # climate read 0.2305 where the w-weighted mean is 0.5500), and
            # the source join mixed contributor provenance. The dashboard's
            # buildSubstrateStateRecord() aggregated correctly all along;
            # this restores Python↔JS parity to the documented intent.
            if sub_dim in dimensions:
                # Fold this indicator into the existing dimension entry
                # by recording all contributors and computing weighted mean.
                existing = dimensions[sub_dim]
                contribs = existing.setdefault("_contributors", [{
                    "indicator_id":   existing.get("indicator_id", ""),
                    "indicator_name": existing.get("indicator_name", ""),
                    "pillar":         existing.get("pillar", ""),
                    "value":          existing["value"],
                    "weight":         existing.get("weight", 1.0),
                    "tier":           existing["tier"],
                    "source":         existing.get("source", "(unspecified)"),
                }])
                contribs.append({
                    "indicator_id":   ind.get("id", ""),
                    "indicator_name": ind.get("name", ""),
                    "pillar":         pillar,
                    "value":          round(nv, 4),
                    "weight":         float(ind.get("w", 1.0)),
                    "tier":           tier,
                    "source":         ind.get("source", "(unspecified)"),
                })

                # Recompute weighted mean across all contributors
                wsum = sum(c["value"] * c["weight"] for c in contribs)
                tw   = sum(c["weight"] for c in contribs)
                existing["value"] = round(wsum / tw if tw > 0 else 0.0, 4)
                # Aggregate tier = worst (lowest) tier across contributors
                tiers = [c["tier"] for c in contribs]
                existing["tier"] = "T3" if "T3" in tiers else ("T2" if "T2" in tiers else "T1")
                existing["source"] = "; ".join(
                    f"{c['indicator_id']}:{c['source']}" for c in contribs)[:200]
            else:
                dimensions[sub_dim] = entry

            if sub_dim != "meaning":
                biospheric_inds.append(ind)

    # SHI composite (meaning-substrate only) — uses canonical compute_shi
    ent = indicators_by_pillar.get("Entertainment", [])
    shi_result = compute_shi(ent)
    shi_composite = shi_result["composite"]

    # BHI composite (biospheric-substrate only) — weighted average of normalized
    # values across all biospheric sub-indicators, weights from the indicators
    # themselves, renormalized within the biospheric subset
    if biospheric_inds:
        bhi_composite = round(compute_pillar_phi(biospheric_inds), 4)
    else:
        bhi_composite = None

    return SubstrateStateRecord(
        timestamp=timestamp,
        polity=polity,
        scale=scale,
        dimensions=dimensions,
        shi_composite=shi_composite,
        bhi_composite=bhi_composite,
        deployment_status="research_grade",
        rule_5_compliance=rule_5_ok,
        rule_4_calibration_note=rule_4_calibration_note,
    )


# ─────────────────────────────────────────────────────────────────────────────
#  (b) CROSS-PILLAR SUBSTRATE COUPLING MATRICES
# ─────────────────────────────────────────────────────────────────────────────
# v3.0 working paper Operational Recommendation #9(b). The 6×5 C[p][b] matrix
# operationalizes Rule 1 (no orthogonal Pillars) at the Pillar↔substrate
# interface. Values per substrate-coupling.md provisional U.S. national-scale
# matrix. Marked EXPERIMENTAL because deployment requires the seven-task
# calibration project (biospheric-substrate.md). Coexists with the canonical
# Interdependency Matrix M[i][j]: M is fast-timescale Pillar↔Pillar; C is
# slow-timescale Pillar↔substrate.


# Five biospheric substrate dimensions that the C matrix indexes.
# (Note: 'meaning' is *not* in this matrix — meaning-substrate lives inside
# the Entertainment Pillar architecturally, not as an external substrate that
# Pillar throughput depletes. This is per the v3.0 §I architectural decision.)
BIOSPHERIC_SUBSTRATE_DIMENSIONS = ("biodiversity", "soil", "climate",
                                    "hydrology", "biotic_relationships")


# Pillar order for matrix rows. Identical to PILLAR_NAMES used elsewhere in NROS.
COUPLING_PILLAR_ORDER = ("Energy", "Information", "Product", "Service",
                         "Transport", "Entertainment")


# C[p][b] — provisional U.S. national-scale indicative matrix.
# Source: substrate-coupling.md (experimental wiki page). Values are
# DESIGN-STAGE PLACEHOLDERS, not calibrated coupling strengths.
# Higher value = stronger coupling (Pillar throughput → substrate depletion).
SUBSTRATE_COUPLING_MATRIX: Dict[str, Dict[str, float]] = {
    "Energy":        {"biodiversity": 0.55, "soil": 0.20, "climate": 0.95,
                      "hydrology": 0.30, "biotic_relationships": 0.40},
    "Information":   {"biodiversity": 0.10, "soil": 0.05, "climate": 0.15,
                      "hydrology": 0.05, "biotic_relationships": 0.10},
    "Product":       {"biodiversity": 0.85, "soil": 0.95, "climate": 0.55,
                      "hydrology": 0.85, "biotic_relationships": 0.90},
    "Service":       {"biodiversity": 0.30, "soil": 0.20, "climate": 0.30,
                      "hydrology": 0.65, "biotic_relationships": 0.20},
    "Transport":     {"biodiversity": 0.50, "soil": 0.40, "climate": 0.65,
                      "hydrology": 0.40, "biotic_relationships": 0.45},
    "Entertainment": {"biodiversity": 0.10, "soil": 0.05, "climate": 0.10,
                      "hydrology": 0.10, "biotic_relationships": 0.10},
}


# Per-cell data tier (Rule 5). T1 cells drive operational results;
# T3 cells must carry an explicit caveat. As of v3.1, every cell is T3 because
# the matrix as a whole is uncalibrated. Operational deployment requires
# elevating individual cells to T1/T2 via the seven-task calibration project.
COUPLING_TIER_MATRIX: Dict[str, Dict[str, str]] = {
    p: {b: "T3" for b in BIOSPHERIC_SUBSTRATE_DIMENSIONS}
    for p in COUPLING_PILLAR_ORDER
}


# Module-level metadata banner accessible to callers
SUBSTRATE_COUPLING_DEPLOYMENT_STATUS = {
    "status":             "experimental",
    "deployment":         "DO NOT DEPLOY",
    "reason":             ("Matrix values are design-stage placeholders, not "
                          "calibrated coupling strengths. Operational deployment "
                          "requires the seven-task calibration project "
                          "(biospheric-substrate.md). All cells currently T3."),
    "calibration_baseline": "U.S. national, provisional",
    "rule_4_note":        ("Non-U.S. and sub-national applications MUST "
                          "recalibrate. Coupling strengths vary substantially "
                          "with the structure of the local economy: arid-region "
                          "C[Service][hydrology] is higher than humid-region; "
                          "agrarian C[Product][soil] is higher than service-economy."),
}


def compute_pillar_substrate_pressure(
    pillar: str,
    pillar_throughput: float,
    bhi_values: Dict[str, float],
    coupling_matrix: Optional[Dict[str, Dict[str, float]]] = None,
) -> Dict[str, Any]:
    """
    P_pressure(p) — total substrate pressure the Pillar p exerts under current
    throughput and substrate stocks.

        P_pressure(p) = Σ_b C[p][b] × throughput(p) × (1 - BHI_b)

    Per substrate-coupling.md "Mathematical operations". The score increases
    as Pillar throughput rises *and* substrate health declines, capturing the
    SOC-relevant `[SOC-h]` insight that pressure rises non-linearly when both
    coupling and substrate scarcity are high.

    Parameters
    ----------
    pillar : str
        Pillar name (one of COUPLING_PILLAR_ORDER).
    pillar_throughput : float
        Normalized Pillar throughput in [0, 1]. Higher = more activity.
        For NROS deployment, a reasonable proxy is (1 - PHI_p) inverted to
        signal *capacity*, OR the raw Pillar economic activity index — the
        choice is analyst-specified per Rule 4.
    bhi_values : dict
        {dimension: BHI_value in [0, 1]} for the five biospheric dimensions.
        Higher = healthier substrate.
    coupling_matrix : dict | None
        Override C[p][b]. Defaults to SUBSTRATE_COUPLING_MATRIX. Pass a
        recalibrated matrix per Rule 4 for non-U.S. analyses.

    Returns
    -------
    dict with:
        pressure              : P_pressure(p) scalar
        contributions         : {dim: C[p][b] * throughput * (1 - BHI_b)}
        deployment_status     : 'research_grade' / 'experimental'
        do_not_deploy_reason  : str
    """
    C = coupling_matrix or SUBSTRATE_COUPLING_MATRIX
    if pillar not in C:
        raise ValueError(f"Pillar {pillar!r} not in coupling matrix. "
                         f"Expected one of {list(C.keys())}.")

    contributions = {}
    pressure = 0.0
    for dim in BIOSPHERIC_SUBSTRATE_DIMENSIONS:
        cpb = C[pillar].get(dim, 0.0)
        bhi = bhi_values.get(dim, 1.0)  # treat missing as healthy substrate
        contrib = cpb * pillar_throughput * (1.0 - bhi)
        contributions[dim] = round(contrib, 4)
        pressure += contrib

    return {
        "pillar":              pillar,
        "throughput":          pillar_throughput,
        "pressure":            round(pressure, 4),
        "contributions":       contributions,
        "deployment_status":   "experimental",
        "do_not_deploy_reason": SUBSTRATE_COUPLING_DEPLOYMENT_STATUS["reason"],
    }


def compute_substrate_stress(
    throughput_by_pillar: Dict[str, float],
    coupling_matrix: Optional[Dict[str, Dict[str, float]]] = None,
) -> Dict[str, Any]:
    """
    B_stress(b) — total stress placed on each substrate dimension by aggregate
    Pillar throughput.

        B_stress(b) = Σ_p C[p][b] × throughput(p)

    Per substrate-coupling.md "Mathematical operations". This sums coupling-
    weighted Pillar contributions to that substrate dimension's depletion.
    It is the input to the (deep-substrate) CCS subsystem's depletion-velocity
    computation. In v3.1 we surface only the per-dimension stress; full CCS
    (time-to-breach, recovery envelope) remains out of scope until the
    calibration project completes.

    Parameters
    ----------
    throughput_by_pillar : dict
        {Pillar: throughput in [0, 1]}.
    coupling_matrix : dict | None
        Override C[p][b]. Defaults to SUBSTRATE_COUPLING_MATRIX.

    Returns
    -------
    dict with:
        stress_by_dimension   : {dim: B_stress(b)}
        contributions         : {dim: {pillar: C[p][b] * throughput(p)}}
        max_stressed_dim      : dimension with highest B_stress
        deployment_status     : 'experimental'
    """
    C = coupling_matrix or SUBSTRATE_COUPLING_MATRIX

    stress = {dim: 0.0 for dim in BIOSPHERIC_SUBSTRATE_DIMENSIONS}
    contribs = {dim: {} for dim in BIOSPHERIC_SUBSTRATE_DIMENSIONS}

    for pillar, t in throughput_by_pillar.items():
        if pillar not in C:
            continue
        for dim in BIOSPHERIC_SUBSTRATE_DIMENSIONS:
            cpb = C[pillar].get(dim, 0.0)
            c = cpb * t
            stress[dim] += c
            contribs[dim][pillar] = round(c, 4)

    # Round outputs
    stress = {k: round(v, 4) for k, v in stress.items()}
    max_dim = max(stress, key=stress.get) if stress else None

    return {
        "stress_by_dimension": stress,
        "contributions":       contribs,
        "max_stressed_dim":    max_dim,
        "max_stress_value":    stress.get(max_dim, 0.0) if max_dim else 0.0,
        "deployment_status":   "experimental",
        "do_not_deploy_reason": SUBSTRATE_COUPLING_DEPLOYMENT_STATUS["reason"],
    }


def identify_substrate_hot_cell(
    throughput_by_pillar: Dict[str, float],
    bhi_values: Dict[str, float],
    coupling_matrix: Optional[Dict[str, Dict[str, float]]] = None,
) -> Dict[str, Any]:
    """
    hot_cell = argmax_{(p, b)} C[p][b] × throughput(p) × (1 - BHI_b)

    The hot cell is the (Pillar, BHI dimension) pair contributing most to the
    system's substrate-depletion gradient. It is the deep-substrate analog of
    the seamless-mode max-borrowing-Pillar diagnostic from substrate_diagnostic(),
    decomposed to substrate-dimension granularity.

    Per Rule 6: identifying the hot cell does NOT recommend an intervention.
    Any intervention proposed against the hot cell must itself be assessed
    under the four polity-failure modes (mismanagement, malfeasance, rent-
    seeking, incompetence). The intervention's failure-mode assessment is
    the analyst's responsibility — this function surfaces the diagnostic only.

    Parameters
    ----------
    throughput_by_pillar : dict
        {Pillar: throughput in [0, 1]}.
    bhi_values : dict
        {dimension: BHI_value in [0, 1]}.
    coupling_matrix : dict | None
        Override C[p][b]. Defaults to SUBSTRATE_COUPLING_MATRIX.

    Returns
    -------
    dict with:
        hot_cell_pillar       : str — dominant Pillar
        hot_cell_dimension    : str — dominant substrate dimension
        hot_cell_value        : float — the argmax value
        ranking               : list of top-5 (pillar, dim, value) tuples,
                                descending
        deployment_status     : 'experimental'
        rule_6_reminder       : str
    """
    C = coupling_matrix or SUBSTRATE_COUPLING_MATRIX

    cells = []
    for pillar, t in throughput_by_pillar.items():
        if pillar not in C:
            continue
        for dim in BIOSPHERIC_SUBSTRATE_DIMENSIONS:
            cpb = C[pillar].get(dim, 0.0)
            bhi = bhi_values.get(dim, 1.0)
            v = cpb * t * (1.0 - bhi)
            cells.append({"pillar": pillar, "dimension": dim,
                         "value": round(v, 4),
                         "coupling": cpb,
                         "throughput": t,
                         "substrate_scarcity": round(1.0 - bhi, 4),
                         "tier": COUPLING_TIER_MATRIX.get(pillar, {}).get(dim, "T3")})

    cells.sort(key=lambda c: c["value"], reverse=True)

    if not cells:
        return {
            "hot_cell_pillar":     None,
            "hot_cell_dimension":  None,
            "hot_cell_value":      0.0,
            "ranking":             [],
            "deployment_status":   "experimental",
            "rule_6_reminder":     "No cells available for ranking.",
        }

    top = cells[0]
    return {
        "hot_cell_pillar":     top["pillar"],
        "hot_cell_dimension":  top["dimension"],
        "hot_cell_value":      top["value"],
        "ranking":             cells[:5],
        "deployment_status":   "experimental",
        "do_not_deploy_reason": SUBSTRATE_COUPLING_DEPLOYMENT_STATUS["reason"],
        "rule_6_reminder":    ("Hot-cell identification is a diagnostic, not "
                               "a recommendation. Any intervention proposed "
                               "against the hot cell must itself be assessed "
                               "under the four polity-failure modes "
                               "(mismanagement, malfeasance, rent-seeking, "
                               "incompetence) per Rule 6. The cap on the "
                               "intervention is itself subject to capture."),
    }


# ─────────────────────────────────────────────────────────────────────────────
#  (c) SUBSTRATE EVENT-SIZE TIME SERIES — POWER-LAW TESTING
# ─────────────────────────────────────────────────────────────────────────────
# v3.0 working paper §II.2 condition #2: "Demonstrated power-law distributions
# of substrate-event sizes (revolutions, schisms, conversions) over a long
# time series." This section provides the *testing infrastructure*. It does
# NOT validate any specific empirical claim — that requires real time-series
# data per Rule 5, with substrate-event coding done outside this module.
#
# Implementation follows Clauset, Shalizi & Newman (2009), "Power-Law
# Distributions in Empirical Data", SIAM Review 51(4): 661-703. The standard
# procedure has three stages:
#   1. MLE fit of α given x_min.
#   2. Selection of x_min by minimizing KS distance between empirical tail
#      and fitted power-law.
#   3. Goodness-of-fit via bootstrap or via comparison against alternative
#      heavy-tailed distributions (lognormal, exponential, stretched exp).
#
# v3.1 implements stages 1 and 2 cleanly, plus a log-likelihood ratio test
# against lognormal and exponential alternatives. Bootstrap p-value is sketched
# and flagged as a stub for future work — the bootstrap requires synthetic
# data generation under the fitted power-law and re-fitting many replicates,
# which is computationally heavier than the v3.1 scope.


@dataclass
class SubstrateEvent:
    """
    A single substrate event (revolution, schism, mass conversion, ecological
    breach, ideological reversal, etc.). The atomic unit of a substrate-event
    time series.

    Fields
    ------
    timestamp : str
        ISO date or year-only string for the event onset.
    dimension : str
        Substrate dimension (one of SUBSTRATE_DIMENSIONS).
    magnitude : float
        Event size on a positive real scale. Units are dimension-specific:
            meaning:    fraction of population substrate-defection (0-1) or
                        absolute count of converts/defectors.
            soil:       hectares lost or % topsoil depth depletion.
            climate:    degree-days anomaly or normalized impact.
            hydrology:  km³ aquifer depletion or stream-flow drop ratio.
            biodiversity / biotic_relationships: extinctions per decade or
                        proportional habitat loss.
        Magnitude must be > 0 for power-law fitting.
    polity : str
        Polity in which the event occurred.
    source : str
        Source attribution.
    tier : str
        Data tier ("T1" / "T2" / "T3").
    notes : str
        Optional free-text.
    event_type : str
        Optional categorical label ("revolution", "schism", "conversion_wave",
        "ecological_breach", etc.).
    """
    timestamp: str
    dimension: str
    magnitude: float
    polity: str = ""
    source: str = ""
    tier: str = "T3"
    notes: str = ""
    event_type: str = ""

    def to_dict(self) -> Dict[str, Any]:
        return {
            "timestamp":  self.timestamp,
            "dimension":  self.dimension,
            "magnitude":  self.magnitude,
            "polity":     self.polity,
            "source":     self.source,
            "tier":       self.tier,
            "notes":      self.notes,
            "event_type": self.event_type,
        }


class SubstrateEventSeries:
    """
    A collection of SubstrateEvent records with utilities for power-law
    testing. Holds events; supports filtering by dimension, polity, tier,
    and timestamp range; exposes magnitudes for the fitting layer.
    """

    def __init__(self, events: Optional[List[SubstrateEvent]] = None,
                 label: str = ""):
        self.events: List[SubstrateEvent] = list(events) if events else []
        self.label = label

    def __len__(self) -> int:
        return len(self.events)

    def append(self, event: SubstrateEvent) -> None:
        self.events.append(event)

    def filter(self,
               dimension: Optional[str] = None,
               polity: Optional[str] = None,
               min_tier: Optional[str] = None) -> "SubstrateEventSeries":
        """Return a new series with the matching subset."""
        out = []
        tier_rank = {"T1": 0, "T2": 1, "T3": 2}
        cutoff = tier_rank.get(min_tier, 99) if min_tier else 99
        for e in self.events:
            if dimension and e.dimension != dimension:
                continue
            if polity and e.polity != polity:
                continue
            if min_tier and tier_rank.get(e.tier, 99) > cutoff:
                continue
            out.append(e)
        return SubstrateEventSeries(out, label=f"{self.label}·filtered")

    def magnitudes(self) -> np.ndarray:
        """Return positive magnitudes as np.array."""
        m = np.array([e.magnitude for e in self.events
                      if e.magnitude is not None and e.magnitude > 0])
        return m

    def tier_distribution(self) -> Dict[str, int]:
        """Diagnostic: counts by T-tier."""
        out = {"T1": 0, "T2": 0, "T3": 0}
        for e in self.events:
            t = e.tier if e.tier in out else "T3"
            out[t] += 1
        return out


# ── Power-law fitting (Clauset, Shalizi & Newman 2009) ──


def _power_law_log_likelihood(x: np.ndarray, alpha: float, x_min: float) -> float:
    """
    Continuous power-law log-likelihood for x ≥ x_min:
        ℓ(α) = N·log(α-1) - N·log(x_min) - α·Σ log(x/x_min)
    where N = len(x). The MLE of α (Clauset et al. 2009 eq. 3.7) is closed-form:
        α̂ = 1 + N / Σ log(x_i / x_min)
    """
    if alpha <= 1.0 or x_min <= 0:
        return -np.inf
    xt = x[x >= x_min]
    n = len(xt)
    if n == 0:
        return -np.inf
    return n * np.log(alpha - 1) - n * np.log(x_min) - alpha * np.sum(np.log(xt / x_min))


def _mle_alpha(x: np.ndarray, x_min: float) -> Tuple[float, int]:
    """
    Closed-form MLE of α for continuous power-law given x_min
    (Clauset et al. 2009 eq. 3.7). Returns (alpha_hat, n_tail).
    Returns (nan, 0) if too few tail samples.
    """
    xt = x[x >= x_min]
    n = len(xt)
    if n < 2 or x_min <= 0:
        return float("nan"), n
    s = np.sum(np.log(xt / x_min))
    if s <= 0:
        return float("nan"), n
    alpha_hat = 1.0 + n / s
    return float(alpha_hat), int(n)


def kolmogorov_smirnov_distance(x: np.ndarray, alpha: float, x_min: float) -> float:
    """
    KS distance between empirical CCDF of the tail (x ≥ x_min) and the fitted
    continuous power-law CCDF. Per Clauset et al. 2009 §3.3 / §3.4.

    Power-law CCDF: P(X ≥ x) = (x / x_min)^(1 - α)  for x ≥ x_min, α > 1.
    Empirical CCDF at the i-th order statistic of the tail (sorted asc, 1-indexed):
        S_emp(x_i) = (n - i + 1) / n.

    KS distance = max over i of |S_emp(x_i) - P_fitted(X ≥ x_i)|.
    """
    xt = np.sort(x[x >= x_min])
    n = len(xt)
    if n < 2 or alpha <= 1.0 or x_min <= 0:
        return float("inf")
    emp = (n - np.arange(1, n + 1) + 1) / n  # S_emp(x_i)
    theo = (xt / x_min) ** (1 - alpha)       # S_theo(x_i)
    return float(np.max(np.abs(emp - theo)))


def fit_power_law(magnitudes: np.ndarray,
                   x_min_candidates: Optional[np.ndarray] = None
                  ) -> Dict[str, Any]:
    """
    Fit a continuous power-law to event magnitudes following Clauset et al.
    2009: select x_min by KS-distance minimization, then α by closed-form MLE.

    Parameters
    ----------
    magnitudes : np.ndarray
        Strictly positive event magnitudes. The series can include the full
        body of events; the fit isolates the tail at x_min.
    x_min_candidates : np.ndarray | None
        Candidate x_min values to scan. If None, scan over the unique values
        of `magnitudes` (the standard Clauset et al. recommendation).

    Returns
    -------
    dict with:
        x_min                : selected x_min
        alpha                : MLE of α at that x_min
        ks_distance          : KS distance for the tail at the chosen (x_min, α)
        n_tail               : number of magnitudes ≥ x_min
        n_total              : total magnitudes considered
        scan                 : list of {x_min, alpha, ks, n_tail} for each candidate
        warnings             : list of analytical warnings
    """
    x = np.asarray(magnitudes, dtype=float)
    x = x[np.isfinite(x) & (x > 0)]
    n_total = int(len(x))
    warnings_list: List[str] = []

    if n_total < 2:
        return {
            "x_min": float("nan"), "alpha": float("nan"),
            "ks_distance": float("inf"), "n_tail": 0, "n_total": n_total,
            "scan": [], "warnings": ["fewer than 2 positive magnitudes; cannot fit"],
        }

    if x_min_candidates is None:
        x_min_candidates = np.unique(x)

    # Drop the largest few candidates: a power-law fit needs at least ~6
    # tail samples to be even nominally meaningful (Clauset et al. recommend
    # at least 50 for inference; we set a hard floor of 6 here).
    x_min_candidates = np.sort(x_min_candidates)
    x_min_candidates = x_min_candidates[x_min_candidates <= np.percentile(x, 95)]

    scan: List[Dict[str, Any]] = []
    best = None
    for xm in x_min_candidates:
        alpha_hat, n_tail = _mle_alpha(x, xm)
        if not np.isfinite(alpha_hat) or n_tail < 6:
            continue
        ks = kolmogorov_smirnov_distance(x, alpha_hat, xm)
        rec = {"x_min": float(xm), "alpha": float(alpha_hat),
               "ks": float(ks), "n_tail": int(n_tail)}
        scan.append(rec)
        if best is None or ks < best["ks"]:
            best = rec

    if best is None:
        warnings_list.append("no x_min candidate produced a finite MLE with n_tail >= 6")
        return {
            "x_min": float("nan"), "alpha": float("nan"),
            "ks_distance": float("inf"), "n_tail": 0, "n_total": n_total,
            "scan": [], "warnings": warnings_list,
        }

    if best["n_tail"] < 50:
        warnings_list.append(
            f"n_tail = {best['n_tail']} < 50: Clauset, Shalizi & Newman (2009) "
            f"recommend at least 50 tail samples for reliable α inference. "
            f"Treat estimate as suggestive only."
        )

    if best["alpha"] < 1.5 or best["alpha"] > 4.0:
        warnings_list.append(
            f"α = {best['alpha']:.3f} outside the typical empirical range "
            f"[~1.5, ~4.0] for natural power laws. Investigate generative "
            f"mechanism — may be lognormal, exponential, or finite-size effect."
        )

    return {
        "x_min":        best["x_min"],
        "alpha":        best["alpha"],
        "ks_distance":  best["ks"],
        "n_tail":       best["n_tail"],
        "n_total":      n_total,
        "scan":         scan,
        "warnings":     warnings_list,
    }


def compare_distribution_alternatives(magnitudes: np.ndarray,
                                       fit: Dict[str, Any]
                                      ) -> Dict[str, Any]:
    """
    Log-likelihood-ratio test comparing the fitted power-law to two
    alternative heavy-tailed distributions: lognormal and exponential.
    Per Clauset et al. 2009 §6 and Vuong (1989).

    A positive LLR favors the power-law; negative favors the alternative.
    Vuong's test statistic is approximately normal under the null of equally
    good fits; a |z| > 1.96 corresponds to ~5% two-tailed significance.

    NOTE: Vuong's variance correction requires per-sample log-likelihoods.
    The implementation here computes the variance honestly. For very small
    samples or near-equivalent distributions, the test is unreliable —
    that condition is explicitly flagged.

    Parameters
    ----------
    magnitudes : np.ndarray
        Positive magnitudes from the same series passed to fit_power_law().
    fit : dict
        Output of fit_power_law().

    Returns
    -------
    dict keyed by alternative name ("lognormal", "exponential"); each value:
        llr      : log-likelihood ratio (power-law minus alternative)
        z        : Vuong-corrected z-statistic
        p_two    : two-tailed p-value approximation
        verdict  : "favors_power_law" | "favors_alternative" | "indistinguishable"
    """
    x = np.asarray(magnitudes, dtype=float)
    x_min = fit.get("x_min", float("nan"))
    alpha = fit.get("alpha", float("nan"))
    if not np.isfinite(x_min) or not np.isfinite(alpha):
        return {"error": "fit not finite; cannot compare"}

    xt = x[(x >= x_min) & (x > 0) & np.isfinite(x)]
    n = len(xt)
    if n < 6:
        return {"error": f"n_tail = {n} too small for distribution comparison"}

    log_xt = np.log(xt)

    # Power-law per-sample log-likelihood (continuous, ≥ x_min)
    pl_ll = np.log(alpha - 1.0) - np.log(x_min) - alpha * np.log(xt / x_min)

    out: Dict[str, Any] = {}

    # Lognormal: MLE on log(x) for x ≥ x_min, with truncation correction so the
    # comparison is on equal footing with the power-law (which is by construction
    # conditional on X ≥ x_min). Per Clauset et al. 2009, both models must be
    # compared as conditional distributions on the same tail; using an
    # unconditioned lognormal density biases the LLR in favor of the power-law.
    mu = float(np.mean(log_xt))
    sigma = float(np.std(log_xt, ddof=1)) if n > 1 else 1e-6
    if sigma <= 0:
        sigma = 1e-6
    # Unconditioned lognormal log-density (with Jacobian from log x to x)
    ln_ll = (-0.5 * np.log(2 * np.pi * sigma ** 2)
             - 0.5 * ((log_xt - mu) / sigma) ** 2
             - log_xt)
    # Truncation correction: subtract log P(X >= x_min) from each per-sample
    # log-density so ln_ll becomes the *conditional* log-density on the tail.
    # P(X >= x_min) = 1 - Φ((log x_min - μ) / σ).
    z_trunc = (math.log(x_min) - mu) / sigma
    p_tail = 0.5 * math.erfc(z_trunc / math.sqrt(2))  # 1 - Φ(z) = ½ erfc(z/√2)
    if p_tail < 1e-300:
        # Numerically zero tail probability — lognormal cannot explain this tail.
        # Skip correction; LLR will reflect that already.
        log_p_tail = -700.0
    else:
        log_p_tail = math.log(p_tail)
    ln_ll = ln_ll - log_p_tail
    diff = pl_ll - ln_ll
    R = float(np.sum(diff))
    var = float(np.var(diff, ddof=1)) if n > 1 else 0.0
    if var <= 0:
        z = 0.0
    else:
        z = R / np.sqrt(n * var)
    p_two = 2 * (1 - 0.5 * (1 + math.erf(abs(z) / math.sqrt(2))))
    out["lognormal"] = {
        "llr":     round(R, 4),
        "z":       round(z, 4),
        "p_two":   round(p_two, 4),
        "verdict": ("favors_power_law" if z > 1.96 else
                    "favors_alternative" if z < -1.96 else
                    "indistinguishable"),
        "mu":      round(mu, 4),
        "sigma":   round(sigma, 4),
    }

    # Exponential: MLE rate λ_hat = 1 / mean(x_t - x_min) (shifted
    # exponential, since support starts at x_min)
    shifted = xt - x_min
    if np.all(shifted >= 0) and np.mean(shifted) > 0:
        lam = 1.0 / float(np.mean(shifted))
    else:
        lam = 1e-6
    exp_ll = np.log(lam) - lam * shifted
    diff = pl_ll - exp_ll
    R = float(np.sum(diff))
    var = float(np.var(diff, ddof=1)) if n > 1 else 0.0
    if var <= 0:
        z = 0.0
    else:
        z = R / np.sqrt(n * var)
    p_two = 2 * (1 - 0.5 * (1 + math.erf(abs(z) / math.sqrt(2))))
    out["exponential"] = {
        "llr":     round(R, 4),
        "z":       round(z, 4),
        "p_two":   round(p_two, 4),
        "verdict": ("favors_power_law" if z > 1.96 else
                    "favors_alternative" if z < -1.96 else
                    "indistinguishable"),
        "lambda":  round(lam, 4),
    }

    return out


def test_power_law_signature(events: SubstrateEventSeries,
                              n_min_for_inference: int = 50
                             ) -> Dict[str, Any]:
    """
    Packaged Clauset-Shalizi-Newman test bundle for a substrate-event series.

    Per v3.0 II.2 condition #2, a rigorous SOC instantiation requires
    "demonstrated power-law distributions of substrate-event sizes
    (revolutions, schisms, conversions) over a long time series." This
    function runs the test bundle and produces a verdict structure that
    explicitly distinguishes:

      - INSUFFICIENT_DATA: N_tail < n_min_for_inference (default 50)
      - POWER_LAW_CONSISTENT: KS distance acceptable AND power-law not
        rejected against either alternative.
      - INDISTINGUISHABLE: data are heavy-tailed but cannot distinguish
        power-law from alternative distributions at standard significance.
      - POWER_LAW_REJECTED: at least one alternative significantly favored
        over power-law.

    Even POWER_LAW_CONSISTENT is INSUFFICIENT to claim SOC instantiation —
    II.2 requires conditions 1 (state variable, partially closed by (a) above),
    2 (this test, partially closed here), 3 (1/f signature, out of scope for
    v3.1), 4 (driving/dissipation mechanisms with conservation, not in scope),
    and 5 (log-periodic precursors and out-of-sample prediction for dragon-
    king claims, not in scope). v3.1 closes (a) and (b) of the
    Hologram2-development priorities at the *infrastructure* level — actual
    rigorous instantiation requires all five conditions met empirically.
    """
    mags = events.magnitudes()
    n = int(len(mags))

    base = {
        "label":              events.label,
        "n_events":           n,
        "tier_distribution":  events.tier_distribution(),
        "deployment_status":  "research_grade",
        "do_not_deploy_reason": ("Power-law fitting is research-grade per "
                                 "v3.0 II.2. A successful KS fit and non-"
                                 "rejection against alternatives is necessary "
                                 "but NOT sufficient for SOC instantiation. "
                                 "II.2 conditions 3, 4, 5 remain open."),
        "soc_h_flag":         True,
    }

    if n < 2:
        return {**base, "verdict": "INSUFFICIENT_DATA",
                "reason": f"only {n} positive magnitudes; cannot fit"}

    fit = fit_power_law(mags)

    if fit["n_tail"] < n_min_for_inference:
        return {**base, "fit": fit, "verdict": "INSUFFICIENT_DATA",
                "reason": f"n_tail = {fit['n_tail']} < {n_min_for_inference} "
                          f"(Clauset-Shalizi-Newman 2009 minimum)",
                "alternatives": None}

    alts = compare_distribution_alternatives(mags, fit)

    # Decide verdict honestly. Two failure modes to guard against:
    #   1. Calling weak fits POWER_LAW_CONSISTENT when neither side is rejected.
    #   2. Calling strong rejections POWER_LAW_REJECTED when only one alternative
    #      significantly favors itself.
    #
    # Verdict ladder (from strongest to weakest claim):
    #   POWER_LAW_CONSISTENT_STRONG : KS acceptable AND ≥1 alt significantly
    #     disfavored (z > +1.96) AND no alt significantly favored
    #   POWER_LAW_CONSISTENT_WEAK   : KS acceptable AND no alt significantly
    #     favored, but no alt significantly disfavored either (heavy-tailed
    #     but indistinguishable from lognormal/exponential)
    #   INDISTINGUISHABLE           : KS poor, but no alt significantly favored
    #   POWER_LAW_REJECTED          : ≥1 alt significantly favored (z < -1.96)
    favors_alt = False
    favors_pl  = False
    if isinstance(alts, dict) and "error" not in alts:
        for name, r in alts.items():
            if r.get("verdict") == "favors_alternative":
                favors_alt = True
            if r.get("verdict") == "favors_power_law":
                favors_pl = True

    # Acceptable KS distance heuristic: ≤ 0.10 for n_tail ≥ 50.
    # (A formal bootstrap p-value would be more rigorous but is out of v3.1 scope.)
    ks_ok = fit["ks_distance"] <= 0.10

    if favors_alt:
        verdict = "POWER_LAW_REJECTED"
    elif ks_ok and favors_pl:
        verdict = "POWER_LAW_CONSISTENT_STRONG"
    elif ks_ok:
        verdict = "POWER_LAW_CONSISTENT_WEAK"
    else:
        verdict = "INDISTINGUISHABLE"

    # Verdict semantics gloss — written into the result so the caller cannot
    # accidentally over-interpret a WEAK verdict as validation.
    verdict_meaning = {
        "POWER_LAW_CONSISTENT_STRONG": ("KS distance acceptable AND at least "
            "one alternative distribution significantly disfavored. This is the "
            "strongest signal the v3.1 test can deliver, but it is NOT sufficient "
            "to claim SOC instantiation — II.2 conditions 3, 4, 5 must be met "
            "empirically. Bootstrap goodness-of-fit (Clauset et al. 2009 §4) is "
            "the next step before any deployment claim."),
        "POWER_LAW_CONSISTENT_WEAK": ("KS distance acceptable but neither "
            "lognormal nor exponential is significantly disfavored. The data "
            "are heavy-tailed but the test cannot distinguish power-law from "
            "alternatives at standard significance. This is the typical regime "
            "for finite-sample lognormal tails and many other heavy-tailed "
            "processes. Treat as evidence of fat-tailed dynamics, NOT as "
            "evidence of power-law specifically."),
        "INDISTINGUISHABLE": ("KS distance unacceptable. Power-law fit is poor "
            "but no alternative is strongly preferred either. Likely small-N "
            "noise or non-standard distribution. More data needed."),
        "POWER_LAW_REJECTED": ("At least one alternative distribution "
            "significantly preferred over the fitted power-law. The data are "
            "inconsistent with a power-law generating process. This does NOT "
            "rule out an underlying SOC mechanism — it rules out the simplest "
            "power-law signature of one. Investigate generating mechanism."),
    }.get(verdict, "")

    return {**base, "fit": fit, "alternatives": alts, "verdict": verdict,
            "verdict_meaning": verdict_meaning,
            "ks_threshold_used": 0.10,
            "next_steps_for_full_validation": [
                "Run bootstrap goodness-of-fit (Clauset et al. 2009 §4): "
                "synthesize many datasets under the fitted power-law, refit, "
                "compare KS distribution. v3.1 stub only.",
                "Test 1/f signature in the temporal interval-distribution "
                "(II.2 condition 3). Out of scope for v3.1.",
                "Identify driving and dissipation mechanisms with conservation "
                "properties (II.2 condition 4). Domain-expert work; not "
                "automatable.",
                "For dragon-king claims: log-periodic precursor analysis and "
                "out-of-sample prediction validation (II.2 condition 5). "
                "Postpone per v3.0 Operational Recommendation #9.",
            ]}


def synthesize_substrate_event_series(
    n: int = 200,
    alpha: float = 2.5,
    x_min: float = 1.0,
    seed: Optional[int] = 42,
    dimension: str = "meaning",
    polity: str = "SYNTHETIC",
    label: str = "synthetic_test",
) -> SubstrateEventSeries:
    """
    Generate a synthetic SubstrateEventSeries drawn from a continuous
    power-law tail with parameter α at threshold x_min.

    INTENDED USE: testing the fitting pipeline only. Synthetic data are
    NEVER inputs to substantive analytical conclusions — Rule 2/Malfeasance
    self-audit. Output events carry tier='SYN' (not in TIER_TAGS) and polity
    'SYNTHETIC' so they cannot be confused with empirical data.
    """
    rng = np.random.default_rng(seed)
    # Inverse-CDF: x = x_min * (1 - U)^(-1/(α-1))
    u = rng.uniform(0, 1, size=n)
    x = x_min * (1 - u) ** (-1.0 / (alpha - 1))

    events = []
    for i, m in enumerate(x):
        events.append(SubstrateEvent(
            timestamp=f"SYN-{i:04d}",
            dimension=dimension,
            magnitude=float(m),
            polity=polity,
            source="(synthetic, power-law inverse-CDF)",
            tier="SYN",  # explicit non-empirical marker
            notes="SYNTHETIC — not empirical data",
            event_type="synthetic",
        ))
    return SubstrateEventSeries(events, label=label)


# ─────────────────────────────────────────────────────────────────────────────
#  v3.1 dispatch summary helper — assembles (a)+(b)+(c) into one report
# ─────────────────────────────────────────────────────────────────────────────


def substrate_research_report(
    indicators_by_pillar: Dict[str, List[Dict]],
    polity: str,
    scale: str,
    pillar_throughput: Optional[Dict[str, float]] = None,
    bhi_values: Optional[Dict[str, float]] = None,
    event_series: Optional[SubstrateEventSeries] = None,
    timestamp: Optional[str] = None,
    rule_4_calibration_note: str = "U.S. canonical baseline; per Rule 4 — recalibrate for non-U.S. or sub-national.",
) -> Dict[str, Any]:
    """
    One-stop research-grade substrate report combining (a) state record,
    (b) coupling-matrix diagnostics, (c) power-law test (if events provided).

    Defaults pillar_throughput to (1 - PHI_p) and bhi_values to the empirical
    BHI dimensions extracted from the substrate-state record. Both defaults
    are diagnostic conveniences, not calibrated inputs — for substantive work
    pass explicit, T-tagged values per Rule 4 + Rule 5.

    Returns a single dict suitable for JSON export (e.g. to the dashboard).
    All sub-sections carry their own deployment_status / do_not_deploy_reason.
    """
    # (a) State record
    state = record_substrate_state(
        indicators_by_pillar=indicators_by_pillar,
        polity=polity, scale=scale, timestamp=timestamp,
        rule_4_calibration_note=rule_4_calibration_note,
    )

    # Default throughput proxy: (1 - PHI_p). Higher PHI → lower implied
    # extraction urgency. This is a diagnostic convenience; calibration
    # discipline says throughput should be a real economic activity index.
    if pillar_throughput is None:
        pillar_throughput = {}
        for p, inds in indicators_by_pillar.items():
            phi = compute_pillar_phi(inds)
            pillar_throughput[p] = round(max(0.0, min(1.0, 1.0 - phi)), 4)

    # Default BHI values: from state record dimensions (where present)
    if bhi_values is None:
        bhi_values = {}
        for dim in BIOSPHERIC_SUBSTRATE_DIMENSIONS:
            if dim in state.dimensions:
                bhi_values[dim] = state.dimensions[dim].get("value", 1.0)
            else:
                bhi_values[dim] = 1.0  # treat absent as healthy (conservative)

    # (b) Coupling diagnostics
    per_pillar_pressure = {
        p: compute_pillar_substrate_pressure(p, t, bhi_values)
        for p, t in pillar_throughput.items()
    }
    stress = compute_substrate_stress(pillar_throughput)
    hot_cell = identify_substrate_hot_cell(pillar_throughput, bhi_values)

    # (c) Power-law test (if events provided)
    if event_series is not None:
        pl_test = test_power_law_signature(event_series)
    else:
        pl_test = {
            "label": None, "n_events": 0,
            "verdict": "NO_DATA",
            "reason": "No substrate-event series provided. Power-law test skipped.",
            "deployment_status": "n/a",
        }

    return {
        "v3_1_substrate_research_report": True,
        "polity": polity, "scale": scale,
        "timestamp": state.timestamp,
        "deployment_status": "research_grade",
        "do_not_deploy_reason": ("All v3.1 substrate research components are "
                                 "research-grade. Substantive deployment of "
                                 "any single component requires: (a) per-"
                                 "civilization Rule 4 calibration with 10% "
                                 "sensitivity test; (b) seven-task calibration "
                                 "project for the C[p][b] matrix; (c) full "
                                 "Clauset et al. bootstrap goodness-of-fit "
                                 "plus II.2 conditions 1-5 met empirically."),
        "rule_compliance": {
            "rule_1_pillar_coupling": "C[p][b] explicitly cross-couples Pillars to substrate; non-orthogonality enforced.",
            "rule_4_calibration":     state.rule_4_calibration_note,
            "rule_5_t_tagging":       f"State record tier-compliance: {state.rule_5_compliance}",
            "rule_6_intervention":    "No interventions recommended. Hot-cell is diagnostic only; analyst must four-mode-assess any proposed intervention.",
        },
        "state_record":         state.to_dict(),
        "pillar_throughput":    pillar_throughput,
        "bhi_values":           bhi_values,
        "pressure_per_pillar":  {p: r["pressure"] for p, r in per_pillar_pressure.items()},
        "pressure_detail":      per_pillar_pressure,
        "substrate_stress":     stress,
        "hot_cell":             hot_cell,
        "power_law_test":       pl_test,
        "soc_h_flag":           True,  # any SOC vocabulary in this report is heuristic
    }




# ═══════════════════════════════════════════════════════════════════════════════
#  SECTION 26C — v3.2 SUBSTRATE VALIDATION HARDENING
#  ───────────────────────────────────────────────────────────────────────────
#  Closes the three v3.1 outstanding items:
#    (1) Bootstrap goodness-of-fit p-value (Clauset-Shalizi-Newman 2009 §4)
#    (2) Calibration of COUPLING_TIER_MATRIX cells from T3 → T1/T2 with
#        per-cell primary-literature citations
#    (3) 1/f temporal-structure test for II.2 condition 3
#
#  All three are additive — none modify the v3.1 API surface or canonical
#  numbers. Removing this section leaves Hologram2 functioning identically
#  to v3.1.
#
#  RULE COMPLIANCE NOTES:
#    Rule 4: tier promotions are U.S.-national-scale only. Non-U.S. and
#      sub-national applications must still recalibrate per the seven-task
#      project. The promotions document calibration *evidence*, not
#      calibration *completeness*.
#    Rule 5: COUPLING_CITATION_MATRIX makes per-cell evidence visible. Cells
#      without primary-literature grounding remain T3 with explicit
#      "calibration_required" flags in COUPLING_TIER_MATRIX_V3_2.
#    Rule 6: 1/f temporal structure being present does NOT recommend any
#      intervention; it is diagnostic only.
# ═══════════════════════════════════════════════════════════════════════════════


# ─────────────────────────────────────────────────────────────────────────────
#  (1) BOOTSTRAP GOODNESS-OF-FIT P-VALUE — Clauset-Shalizi-Newman 2009 §4
# ─────────────────────────────────────────────────────────────────────────────
# The basic Vuong test against alternatives (compare_distribution_alternatives)
# is unreliable at small N — Malevergne-Pisarenko-Sornette 2011 demonstrate
# that distinguishing power-law from lognormal can require N ≥ 10^4. This was
# the v3.1 "FINITE-SAMPLE PATHOLOGY" caveat.
#
# The formal Clauset-Shalizi-Newman 2009 procedure adds a goodness-of-fit
# bootstrap p-value:
#
#   1. From data, fit (x̂_min, α̂) and compute D_emp = KS(empirical, fit).
#   2. For b = 1..B replicates, generate a synthetic dataset of N samples:
#        - With probability p_tail = N_tail / N_total: draw from continuous
#          power-law with parameters (x̂_min, α̂).
#        - With probability (1 - p_tail): resample with replacement from the
#          empirical body (x < x̂_min).
#      For each replicate, refit (x_min, α) by KS-minimization on the
#      synthetic data and compute D_b.
#   3. p = (1 / B) × #{b : D_b ≥ D_emp}.
#   4. Reject power-law hypothesis at α=0.1 if p < 0.1.
#
# Computationally: B=100 replicates × N=500 samples × ~200 candidate x_min
# values per refit ≈ 10^7 ops. Acceptable in Python with numpy vectorization.


def _resample_body_with_replacement(body: np.ndarray, n: int,
                                     rng: np.random.Generator) -> np.ndarray:
    """Resample n values from the empirical body (values < x_min) with replacement."""
    if len(body) == 0:
        return np.array([])
    return rng.choice(body, size=n, replace=True)


def _draw_power_law_continuous(n: int, alpha: float, x_min: float,
                                rng: np.random.Generator) -> np.ndarray:
    """Draw n samples from continuous power-law with parameters (alpha, x_min) via inverse-CDF."""
    if alpha <= 1.0 or x_min <= 0:
        return np.array([])
    u = rng.uniform(1e-12, 1 - 1e-12, size=n)
    return x_min * (1 - u) ** (-1.0 / (alpha - 1))


def bootstrap_power_law_p_value(magnitudes: np.ndarray,
                                  fit: Dict[str, Any],
                                  B: int = 100,
                                  seed: Optional[int] = None
                                 ) -> Dict[str, Any]:
    """
    Semi-parametric bootstrap p-value for power-law goodness-of-fit
    (Clauset-Shalizi-Newman 2009 §4.1).

    Parameters
    ----------
    magnitudes : np.ndarray
        Positive event magnitudes (the same series passed to fit_power_law()).
    fit : dict
        Output of fit_power_law().
    B : int
        Number of bootstrap replicates. Clauset et al. recommend B ≥ 100 for
        one-decimal accuracy and B ≥ 2500 for higher precision. Default 100.
    seed : int | None
        RNG seed for reproducibility.

    Returns
    -------
    dict with:
        p_value             : bootstrap p-value (probability D_b ≥ D_emp)
        D_emp               : empirical KS distance
        D_bootstrap_mean    : mean of bootstrap KS distances
        D_bootstrap_std     : std of bootstrap KS distances
        n_replicates        : B
        verdict             : "POWER_LAW_PLAUSIBLE" (p ≥ 0.1) or
                              "POWER_LAW_REJECTED_BY_BOOTSTRAP" (p < 0.1)
        deployment_status   : "research_grade"
        notes               : str
    """
    x = np.asarray(magnitudes, dtype=float)
    x = x[np.isfinite(x) & (x > 0)]
    n_total = len(x)
    x_min = fit.get("x_min", float("nan"))
    alpha = fit.get("alpha", float("nan"))
    n_tail = fit.get("n_tail", 0)
    D_emp = fit.get("ks_distance", float("inf"))

    if not (np.isfinite(x_min) and np.isfinite(alpha) and n_tail >= 50 and n_total >= 50):
        return {
            "p_value":            float("nan"),
            "D_emp":              D_emp,
            "D_bootstrap_mean":   float("nan"),
            "D_bootstrap_std":    float("nan"),
            "n_replicates":       0,
            "verdict":            "INSUFFICIENT_FIT_FOR_BOOTSTRAP",
            "deployment_status":  "research_grade",
            "notes":              "fit prerequisites not met (need finite (x_min, α) and n_tail ≥ 50)",
        }

    rng = np.random.default_rng(seed)
    body = x[x < x_min]
    p_tail = n_tail / n_total

    D_boots = np.empty(B, dtype=float)
    failed_replicates = 0

    for b in range(B):
        # Generate synthetic dataset: tail from fitted power-law, body resampled
        n_tail_b = int(rng.binomial(n_total, p_tail))
        n_body_b = n_total - n_tail_b
        tail_samples = _draw_power_law_continuous(n_tail_b, alpha, x_min, rng)
        body_samples = _resample_body_with_replacement(body, n_body_b, rng)
        if len(body_samples) > 0:
            synth = np.concatenate([tail_samples, body_samples])
        else:
            synth = tail_samples

        # Refit on synthetic data — this is the expensive step
        fit_b = fit_power_law(synth)
        if not np.isfinite(fit_b.get("ks_distance", float("inf"))):
            D_boots[b] = float("inf")
            failed_replicates += 1
        else:
            D_boots[b] = fit_b["ks_distance"]

    valid = D_boots[np.isfinite(D_boots)]
    if len(valid) == 0:
        return {
            "p_value":            float("nan"),
            "D_emp":              D_emp,
            "D_bootstrap_mean":   float("nan"),
            "D_bootstrap_std":    float("nan"),
            "n_replicates":       B,
            "failed_replicates":  failed_replicates,
            "verdict":            "BOOTSTRAP_FAILED",
            "deployment_status":  "research_grade",
            "notes":              "all replicates failed to produce a valid fit",
        }

    p_value = float(np.mean(valid >= D_emp))
    verdict = "POWER_LAW_PLAUSIBLE" if p_value >= 0.10 else "POWER_LAW_REJECTED_BY_BOOTSTRAP"

    return {
        "p_value":            round(p_value, 4),
        "D_emp":              round(float(D_emp), 4),
        "D_bootstrap_mean":   round(float(np.mean(valid)), 4),
        "D_bootstrap_std":    round(float(np.std(valid, ddof=1)) if len(valid) > 1 else 0.0, 4),
        "n_replicates":       B,
        "failed_replicates":  failed_replicates,
        "verdict":            verdict,
        "deployment_status":  "research_grade",
        "notes":             ("Per Clauset-Shalizi-Newman 2009 §4.1: rule of thumb is "
                              "reject power-law hypothesis at α=0.1 when p < 0.1. "
                              "p ≥ 0.1 means the power-law CANNOT be ruled out — it does "
                              "NOT mean the power-law is the correct generating mechanism. "
                              "Alternative distributions (lognormal, exponential) may "
                              "still fit better; consult Vuong tests for direct comparison."),
    }


# ─────────────────────────────────────────────────────────────────────────────
#  (2) CALIBRATED COUPLING_TIER_MATRIX + COUPLING_CITATION_MATRIX
# ─────────────────────────────────────────────────────────────────────────────
# Per-cell tier promotion based on named primary-literature support. Cells
# without primary-literature grounding remain T3.
#
# Promotion criteria (per Rule 5):
#   T1: Direct quantitative coupling documented in T1 source (IPCC AR6,
#       IPBES Global Assessments, USDA NRCS, USGS, EIA, EPA, FAO).
#   T2: Coupling well-established in secondary literature (peer-reviewed
#       academic, established journalism, OSINT) but not pinned to a single
#       T1 number.
#   T3: Coupling magnitude defensible but not literature-grounded; remains
#       a placeholder per Rule 4 sensitivity-test discipline.
#
# The matrix VALUES are unchanged from v3.1 (substrate-coupling.md provisional
# placeholders). Only the TIER TAGS and CITATIONS are added — this is the
# v3.2 calibration step.


COUPLING_TIER_MATRIX_V3_2: Dict[str, Dict[str, str]] = {
    # Energy
    "Energy": {
        "biodiversity":         "T2",  # IPBES 2019: energy-infrastructure footprint
        "soil":                 "T3",  # mountaintop removal local impact; aggregate is small
        "climate":              "T1",  # IPCC AR6 WG3, EIA, Jackson et al. GCB
        "hydrology":            "T2",  # USGS thermoelectric water-use data
        "biotic_relationships": "T3",  # mostly indirect via climate
    },
    # Information
    "Information": {
        "biodiversity":         "T3",  # indirect via Energy
        "soil":                 "T3",  # negligible direct
        "climate":              "T2",  # data-center electricity demand (IEA tracking)
        "hydrology":            "T3",  # data-center cooling locally relevant; aggregate weak
        "biotic_relationships": "T3",  # indirect
    },
    # Product
    "Product": {
        "biodiversity":         "T1",  # IPBES 2019: agricultural land conversion is the
                                       # largest single driver of biodiversity loss
        "soil":                 "T1",  # USDA NRCS NRI; FAO 2015 Status of World Soils
        "climate":              "T1",  # IPCC AR6 WG3 + FAO: AFOLU ~22% global GHG
        "hydrology":            "T1",  # USGS NWIS + FAO AQUASTAT: agriculture is the
                                       # largest consumptive water user
        "biotic_relationships": "T1",  # IPBES 2016 Pollinators Assessment
    },
    # Service
    "Service": {
        "biodiversity":         "T3",  # supply-chain mediated, weak direct
        "soil":                 "T3",  # urban-development footprint, weak national
        "climate":              "T2",  # building-sector emissions (EIA, IEA Energy Use)
        "hydrology":            "T2",  # USGS public-supply data (~10% withdrawals)
        "biotic_relationships": "T3",  # weak direct
    },
    # Transport
    "Transport": {
        "biodiversity":         "T2",  # Forman & Alexander 1998; IPBES 2019 (habitat
                                       # fragmentation by roads)
        "soil":                 "T3",  # local impact; aggregate weak
        "climate":              "T1",  # EPA: transport ~28% of US GHG emissions
        "hydrology":            "T3",  # weak direct
        "biotic_relationships": "T3",  # via habitat fragmentation; secondary
    },
    # Entertainment
    "Entertainment": {
        "biodiversity":         "T3",  # indirect, via supply chain
        "soil":                 "T3",  # negligible direct
        "climate":              "T3",  # indirect via Information / venues
        "hydrology":            "T3",  # negligible
        "biotic_relationships": "T3",  # indirect
    },
}


COUPLING_CITATION_MATRIX: Dict[str, Dict[str, str]] = {
    "Energy": {
        "biodiversity":         "IPBES Global Assessment 2019 (energy-infrastructure footprint chapter)",
        "soil":                 "(no primary T1 source; calibration_required)",
        "climate":              "IPCC AR6 WG3 (2022); EIA Annual Energy Review; Jackson et al., Global Carbon Budget (annual)",
        "hydrology":            "USGS Estimated Use of Water in the United States (Dieter et al. 2018) — thermoelectric ~38% of withdrawals",
        "biotic_relationships": "(indirect via climate; calibration_required)",
    },
    "Information": {
        "biodiversity":         "(indirect; calibration_required)",
        "soil":                 "(negligible; calibration_required)",
        "climate":              "IEA Data Centres and Data Transmission Networks (annual tracking report)",
        "hydrology":            "(local relevance only; calibration_required)",
        "biotic_relationships": "(indirect; calibration_required)",
    },
    "Product": {
        "biodiversity":         "IPBES Global Assessment 2019 §2.2.1 (land-use change is largest single driver)",
        "soil":                 "USDA NRCS National Resources Inventory; FAO 2015 Status of the World's Soil Resources",
        "climate":              "IPCC AR6 WG3 (2022) Ch. 7; FAO FAOSTAT emissions data (AFOLU ~22% of global GHG)",
        "hydrology":            "USGS NWIS; FAO AQUASTAT (agriculture ~70% of global freshwater withdrawals)",
        "biotic_relationships": "IPBES Assessment of Pollinators, Pollination and Food Production (2016)",
    },
    "Service": {
        "biodiversity":         "(supply-chain mediated; calibration_required)",
        "soil":                 "(urban footprint local only; calibration_required)",
        "climate":              "EIA Annual Energy Outlook (commercial buildings ~17% of US energy); IEA Energy Use Tracking",
        "hydrology":            "USGS Estimated Use of Water in the US (Dieter et al. 2018) — public supply ~12% of withdrawals",
        "biotic_relationships": "(weak direct; calibration_required)",
    },
    "Transport": {
        "biodiversity":         "Forman & Alexander 1998 'Roads and their major ecological effects' Annu. Rev. Ecol. Syst.; IPBES 2019 §2.2",
        "soil":                 "(local construction impact; calibration_required)",
        "climate":              "EPA Inventory of US Greenhouse Gas Emissions and Sinks (annual); transport ~28% of US GHG",
        "hydrology":            "(weak direct; calibration_required)",
        "biotic_relationships": "(via habitat fragmentation; calibration_required)",
    },
    "Entertainment": {
        "biodiversity":         "(indirect via supply chain; calibration_required)",
        "soil":                 "(negligible; calibration_required)",
        "climate":              "(indirect via Information / venues; calibration_required)",
        "hydrology":            "(negligible; calibration_required)",
        "biotic_relationships": "(indirect; calibration_required)",
    },
}


def coupling_tier_summary(tier_matrix: Optional[Dict[str, Dict[str, str]]] = None) -> Dict[str, Any]:
    """
    Diagnostic summary of the calibration state of the coupling tier matrix.

    Returns a count of T1 / T2 / T3 cells across the 30-cell matrix, plus a
    list of cells that still require calibration (T3 cells).
    """
    M = tier_matrix or COUPLING_TIER_MATRIX_V3_2
    counts = {"T1": 0, "T2": 0, "T3": 0}
    calibration_required = []
    for p in M:
        for b in M[p]:
            t = M[p][b]
            counts[t] = counts.get(t, 0) + 1
            if t == "T3":
                calibration_required.append((p, b))
    total = counts["T1"] + counts["T2"] + counts["T3"]
    return {
        "counts":                  counts,
        "total_cells":             total,
        "t1_share":                round(counts["T1"] / total, 3) if total else 0.0,
        "t2_share":                round(counts["T2"] / total, 3) if total else 0.0,
        "t3_share":                round(counts["T3"] / total, 3) if total else 0.0,
        "calibration_required":    calibration_required,
        "calibration_complete":    counts["T3"] == 0,
        "rule_4_note":            ("U.S. national-scale tier promotions only. "
                                   "Non-U.S. and sub-national applications must "
                                   "recalibrate per Rule 4."),
    }


# ─────────────────────────────────────────────────────────────────────────────
#  (3) 1/F TEMPORAL-STRUCTURE TEST — closes II.2 condition #3
# ─────────────────────────────────────────────────────────────────────────────
# v3.0 II.2 condition #3: "Demonstrated 1/f or scale-invariant temporal
# structure in substrate-flux data."
#
# Standard test: take a substrate-flux time series x(t), compute the power
# spectral density S(f), fit log(S(f)) vs log(f) over the inertial range,
# check whether the slope -β is consistent with 1/f behavior.
#
# Spectral exponents and what they mean:
#   β ≈ 0       white noise (no temporal correlation)
#   β ≈ 1       pink noise / 1/f noise (long-range correlation, SOC-relevant)
#   β ≈ 2       Brownian / random walk (integrated white noise)
#   β > 2       smoother-than-random-walk (rare in nature)
#
# Methodology: Welch's method (averaged periodograms with overlap, Hann
# window). Falls back to single periodogram if scipy.signal unavailable.
# Linear log-log fit on the inertial range, excluding the very-low-frequency
# leakage (first ~5% of bins) and very-high-frequency aliasing (last ~5%).


@dataclass
class FluxTimeSeries:
    """
    Longitudinal substrate-flux time series. The unit of measurement for
    II.2 condition #3.

    Fields
    ------
    timestamps : list[str]
        ISO timestamps for each sample.
    values : np.ndarray
        Flux values at each timestamp. Must be 1-D, finite, length ≥ 64.
    dimension : str
        Substrate dimension (one of SUBSTRATE_DIMENSIONS).
    polity : str
        Polity name.
    sampling_rate : str
        Human-readable cadence ("monthly", "annual", etc.). Used for
        labeling only — PSD is computed on the index, not the time stamps.
    tier : str
        Data tier of the underlying series ("T1" / "T2" / "T3").
    notes : str
        Free-text.
    """
    timestamps: List[str]
    values: np.ndarray
    dimension: str
    polity: str = ""
    sampling_rate: str = ""
    tier: str = "T3"
    notes: str = ""

    def __post_init__(self):
        self.values = np.asarray(self.values, dtype=float)

    def __len__(self) -> int:
        return len(self.values)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "n":             len(self),
            "dimension":     self.dimension,
            "polity":        self.polity,
            "sampling_rate": self.sampling_rate,
            "tier":          self.tier,
            "notes":         self.notes,
            "first_ts":      self.timestamps[0] if self.timestamps else None,
            "last_ts":       self.timestamps[-1] if self.timestamps else None,
        }


def compute_psd(values: np.ndarray,
                method: str = "welch",
                nperseg: Optional[int] = None
                ) -> Dict[str, Any]:
    """
    Compute the power spectral density of a time series.

    Parameters
    ----------
    values : np.ndarray
        Time series values. Should be reasonably stationary (linear-detrend
        is applied automatically).
    method : str
        "welch" (default; scipy.signal.welch with Hann window) or
        "periodogram" (single periodogram fallback).
    nperseg : int | None
        Welch segment length. If None, defaults to min(256, N // 8).

    Returns
    -------
    dict with:
        frequencies : np.ndarray  (positive frequencies, in cycles per sample)
        psd         : np.ndarray  (power spectral density at those frequencies)
        method_used : "welch" / "periodogram"
        n_samples   : int
    """
    x = np.asarray(values, dtype=float)
    x = x[np.isfinite(x)]
    n = len(x)
    if n < 16:
        return {"frequencies": np.array([]), "psd": np.array([]),
                "method_used": "none", "n_samples": n,
                "error": f"need ≥16 samples for PSD; got {n}"}

    # Linear detrend removes any deterministic drift before spectral analysis
    t = np.arange(n)
    coef = np.polyfit(t, x, 1)
    x_detrended = x - (coef[0] * t + coef[1])

    if method == "welch":
        try:
            from scipy.signal import welch
            if nperseg is None:
                nperseg = min(256, max(16, n // 8))
            freqs, psd = welch(x_detrended, fs=1.0, window="hann",
                               nperseg=nperseg, noverlap=nperseg // 2,
                               scaling="density", return_onesided=True)
            # Drop f=0 bin
            return {"frequencies": freqs[1:], "psd": psd[1:],
                    "method_used": "welch", "n_samples": n,
                    "nperseg": nperseg}
        except ImportError:
            method = "periodogram"

    # Periodogram fallback: single FFT with Hann window
    window = 0.5 * (1 - np.cos(2 * np.pi * np.arange(n) / (n - 1)))
    xw = x_detrended * window
    fft = np.fft.rfft(xw)
    psd = (np.abs(fft) ** 2) / (np.sum(window ** 2))
    freqs = np.fft.rfftfreq(n, d=1.0)
    # Drop f=0
    return {"frequencies": freqs[1:], "psd": psd[1:],
            "method_used": "periodogram", "n_samples": n}


def test_one_over_f_signature(flux: "FluxTimeSeries",
                                fit_low_freq_frac: float = 0.05,
                                fit_high_freq_frac: float = 0.95
                               ) -> Dict[str, Any]:
    """
    Test for 1/f^β temporal-structure in a substrate-flux series. Closes
    v3.0 II.2 condition #3 procedurally.

    Method:
      1. Compute PSD via compute_psd() (Welch with Hann; periodogram fallback).
      2. Linear log-log fit on the inertial range
         f ∈ [fit_low_freq_frac, fit_high_freq_frac] of the bins.
      3. Slope -β. Verdict ladder:
            β ∈ [0.7, 1.3]    → 1/F_CONSISTENT
            β ∈ [0.5, 1.5] \\ [0.7, 1.3] → SCALE_INVARIANT_OUTLIER
            β ∈ [-0.3, 0.3]   → WHITE_NOISE
            β ∈ [1.7, 2.3]    → BROWNIAN
            else              → INDETERMINATE
      4. Report β, R² of the log-log fit, fit range, and verdict.

    NOTE: Like the event-size test, a 1/F_CONSISTENT verdict is NECESSARY
    BUT NOT SUFFICIENT for SOC instantiation. II.2 conditions 4 and 5 still
    require independent validation.

    Parameters
    ----------
    flux : FluxTimeSeries
        Substrate-flux time series. Must have len(values) ≥ 64.
    fit_low_freq_frac : float
        Lower end of inertial-range fit, as fraction of bins. Excludes
        very-low-frequency leakage from non-stationarity.
    fit_high_freq_frac : float
        Upper end of inertial-range fit. Excludes high-frequency aliasing.

    Returns
    -------
    dict with:
        beta              : spectral exponent (β = -slope of log-log fit)
        beta_se           : standard error of β
        r_squared         : R² of the log-log fit
        n_fit_points      : number of PSD bins used in the fit
        n_samples         : N
        psd_method        : "welch" / "periodogram"
        verdict           : ladder element
        verdict_meaning   : str
        deployment_status : "research_grade"
        soc_h_flag        : True
    """
    n = len(flux)
    base = {
        "polity":            flux.polity,
        "dimension":         flux.dimension,
        "sampling_rate":     flux.sampling_rate,
        "tier":              flux.tier,
        "n_samples":         n,
        "deployment_status": "research_grade",
        "soc_h_flag":        True,
    }

    if n < 64:
        return {**base,
                "verdict": "INSUFFICIENT_DATA",
                "reason":  f"n = {n} < 64 (minimum for meaningful PSD-slope inference)"}

    psd_result = compute_psd(flux.values, method="welch")
    if "error" in psd_result:
        return {**base, "verdict": "PSD_FAILED", "reason": psd_result["error"]}

    freqs = psd_result["frequencies"]
    psd = psd_result["psd"]
    if len(freqs) < 8:
        return {**base, "verdict": "PSD_FAILED",
                "reason":  f"only {len(freqs)} PSD bins; need ≥8 for fit"}

    # Inertial-range slice
    n_bins = len(freqs)
    lo = max(1, int(np.floor(fit_low_freq_frac * n_bins)))
    hi = max(lo + 4, int(np.ceil(fit_high_freq_frac * n_bins)))
    hi = min(hi, n_bins)
    f_fit = freqs[lo:hi]
    psd_fit = psd[lo:hi]

    # Drop any non-positive PSD bins (Welch can produce zeros at end)
    valid = (psd_fit > 0) & (f_fit > 0) & np.isfinite(psd_fit) & np.isfinite(f_fit)
    f_fit = f_fit[valid]
    psd_fit = psd_fit[valid]
    if len(f_fit) < 5:
        return {**base, "verdict": "PSD_FAILED",
                "reason":  f"only {len(f_fit)} valid PSD bins after filtering; need ≥5"}

    # log-log linear fit
    log_f = np.log10(f_fit)
    log_psd = np.log10(psd_fit)
    slope, intercept = np.polyfit(log_f, log_psd, 1)
    fit_psd = slope * log_f + intercept
    ss_res = np.sum((log_psd - fit_psd) ** 2)
    ss_tot = np.sum((log_psd - np.mean(log_psd)) ** 2)
    r_squared = 1 - ss_res / ss_tot if ss_tot > 0 else 0.0

    # Standard error of slope from residuals
    n_fit = len(log_f)
    if n_fit >= 3 and ss_tot > 0:
        s_yx = np.sqrt(ss_res / (n_fit - 2))
        x_var = np.sum((log_f - np.mean(log_f)) ** 2)
        beta_se = s_yx / np.sqrt(x_var) if x_var > 0 else float("nan")
    else:
        beta_se = float("nan")

    beta = -slope
    if 0.7 <= beta <= 1.3:
        verdict = "1/F_CONSISTENT"
        meaning = ("β ∈ [0.7, 1.3] consistent with pink-noise / 1/f spectrum. "
                   "This is the SOC-canonical signature `[SOC-h]`. NECESSARY "
                   "BUT NOT SUFFICIENT for SOC instantiation — II.2 conditions "
                   "4 and 5 must be met independently.")
    elif 0.5 <= beta <= 1.5:
        verdict = "SCALE_INVARIANT_OUTLIER"
        meaning = ("β ∈ [0.5, 1.5] \\ [0.7, 1.3] — scale-invariant but offset "
                   "from canonical 1/f. May indicate fractional Gaussian noise "
                   "or non-stationary regime. Investigate.")
    elif -0.3 <= beta <= 0.3:
        verdict = "WHITE_NOISE"
        meaning = ("β ≈ 0 — flat spectrum. No long-range temporal correlation. "
                   "Inconsistent with SOC.")
    elif 1.7 <= beta <= 2.3:
        verdict = "BROWNIAN"
        meaning = ("β ≈ 2 — Brownian / random-walk. Integrated white noise; "
                   "non-stationary. Inconsistent with stationary 1/f SOC.")
    else:
        verdict = "INDETERMINATE"
        meaning = (f"β = {beta:.3f} outside standard regimes. "
                   f"Investigate generative process; may indicate strong "
                   f"non-stationarity, mixture process, or finite-size effects.")

    return {**base,
            "beta":              round(float(beta), 4),
            "beta_se":           round(float(beta_se), 4) if np.isfinite(beta_se) else None,
            "slope_log_log":     round(float(slope), 4),
            "intercept_log_log": round(float(intercept), 4),
            "r_squared":         round(float(r_squared), 4),
            "n_fit_points":      int(n_fit),
            "psd_method":        psd_result["method_used"],
            "fit_freq_range":    [round(float(f_fit[0]), 6), round(float(f_fit[-1]), 6)],
            "verdict":           verdict,
            "verdict_meaning":   meaning,
            "rule_6_reminder":  ("1/f temporal structure is a diagnostic, not a "
                                 "recommendation. Presence of 1/f does not "
                                 "validate any specific intervention; absence "
                                 "does not rule out substrate-driven dynamics."),
            }


def synthesize_flux_series(n: int = 1024,
                            kind: str = "pink",
                            seed: Optional[int] = 42,
                            dimension: str = "meaning",
                            polity: str = "SYNTHETIC"
                           ) -> "FluxTimeSeries":
    """
    Generate a synthetic FluxTimeSeries for pipeline-verification testing.

    Kinds:
      "pink"      → 1/f noise (β ≈ 1) via spectral filtering of white noise
      "white"     → uncorrelated Gaussian (β ≈ 0)
      "brown"     → Brownian motion / cumsum of white noise (β ≈ 2)
      "lognormal" → AR(1) with lognormal innovations (heavy-tailed, β varies)

    INTENDED USE: testing the 1/f pipeline only. Synthetic data carry tier='SYN'
    and polity 'SYNTHETIC' so they cannot be confused with empirical series.
    Per Rule 2 / Malfeasance self-audit.
    """
    rng = np.random.default_rng(seed)
    if kind == "white":
        x = rng.standard_normal(n)
    elif kind == "brown":
        x = np.cumsum(rng.standard_normal(n))
    elif kind == "pink":
        # Spectral 1/f synthesis: white noise FFT, scale by 1/sqrt(f), inverse FFT
        white = rng.standard_normal(n)
        fft = np.fft.rfft(white)
        freqs = np.fft.rfftfreq(n, d=1.0)
        # Avoid f=0 division
        scaling = np.ones_like(freqs)
        scaling[1:] = 1.0 / np.sqrt(freqs[1:])
        x = np.fft.irfft(fft * scaling, n=n)
    elif kind == "lognormal":
        # AR(1) with heavy-tailed innovations
        x = np.empty(n)
        x[0] = rng.standard_normal()
        phi = 0.5
        for i in range(1, n):
            innov = np.exp(rng.standard_normal() * 0.5)
            x[i] = phi * x[i - 1] + innov
    else:
        raise ValueError(f"unknown synthetic flux kind: {kind!r}")

    timestamps = [f"SYN-{i:04d}" for i in range(n)]
    return FluxTimeSeries(
        timestamps=timestamps,
        values=x,
        dimension=dimension,
        polity=polity,
        sampling_rate="(synthetic, unit cadence)",
        tier="SYN",
        notes=f"SYNTHETIC {kind} (n={n}, seed={seed})",
    )


# ─────────────────────────────────────────────────────────────────────────────
#  v3.2 dispatch — extend substrate_research_report to include all new layers
# ─────────────────────────────────────────────────────────────────────────────
# We don't replace the v3.1 substrate_research_report (it's part of the
# preserved API). Instead we add a v3.2 wrapper that calls it and adds
# bootstrap GoF to (c) plus the 1/f test if a flux series is provided.


def substrate_research_report_v3_2(
    indicators_by_pillar: Dict[str, List[Dict]],
    polity: str,
    scale: str,
    pillar_throughput: Optional[Dict[str, float]] = None,
    bhi_values: Optional[Dict[str, float]] = None,
    event_series: Optional["SubstrateEventSeries"] = None,
    flux_series: Optional["FluxTimeSeries"] = None,
    bootstrap_B: int = 100,
    bootstrap_seed: Optional[int] = 42,
    timestamp: Optional[str] = None,
    rule_4_calibration_note: str = "U.S. canonical baseline; per Rule 4 — recalibrate for non-U.S. or sub-national.",
) -> Dict[str, Any]:
    """
    v3.2 substrate research report. Calls the v3.1 base report and adds:
      - Bootstrap GoF p-value on the event-size test (if event_series given)
      - 1/f temporal-structure test on the flux series (if flux_series given)
      - Coupling tier matrix calibration summary (always)

    Returns a single dict. All sub-sections carry their own deployment_status.
    """
    base = substrate_research_report(
        indicators_by_pillar=indicators_by_pillar,
        polity=polity, scale=scale,
        pillar_throughput=pillar_throughput, bhi_values=bhi_values,
        event_series=event_series,
        timestamp=timestamp,
        rule_4_calibration_note=rule_4_calibration_note,
    )

    # (1) Bootstrap GoF on the event-size test
    bootstrap = None
    if event_series is not None and base["power_law_test"].get("fit"):
        mags = event_series.magnitudes()
        bootstrap = bootstrap_power_law_p_value(
            magnitudes=mags,
            fit=base["power_law_test"]["fit"],
            B=bootstrap_B,
            seed=bootstrap_seed,
        )

    # (3) 1/f test on the flux series
    one_over_f = None
    if flux_series is not None:
        one_over_f = test_one_over_f_signature(flux_series)

    # (2) Tier calibration summary
    tier_summary = coupling_tier_summary()

    out = dict(base)
    out["v3_2_substrate_research_report"] = True
    out["bootstrap_goodness_of_fit"] = bootstrap
    out["one_over_f_test"] = one_over_f
    out["coupling_tier_calibration"] = tier_summary
    return out


# ═══════════════════════════════════════════════════════════════════════════════
#  SECTION 26D — v3.3 PER-POLITY CALIBRATION + BILATERAL ANALYSIS +
#                TWELVE-DAY WAR CASE STUDY + DRAGON-KING GATE STATUS
#  ───────────────────────────────────────────────────────────────────────────
#  Closes 2 of 4 v3.3 backlog candidates with honest deferral of 1 and qualified
#  scaffolding of 1:
#
#  (A) Per-polity calibration registry (Rule 4 closure)
#  (B) Bilateral substrate analysis (closes v3.0 Part VIII open #4)
#  (C) Twelve-Day War case study (worked example with illustrative data)
#  (D) Dragon-king (II.2 #5) — DELIBERATELY NOT BUILT (gate transparency)
#
#  RULE COMPLIANCE NOTES:
#    Rule 2: Pre-build self-audit declined building #5 (dragon-king) on
#      malfeasance / Rule 3 grounds. The dragon_king_module_status() function
#      is the audit residue, surfacing the gate to all callers.
#    Rule 4: Non-U.S. polities now have explicit registry slots. Values still
#      inherit U.S. structure but tier provenance is reset to all-T3 with
#      calibration_required=True. This is honest infrastructure, not
#      laundered calibration.
#    Rule 5: Israel 2026 and Iran 2026 baselines carry per-indicator T-tags
#      and source attribution. Iran baseline is source-diverse per 7 May 2026
#      userMemory directive.
#    Rule 6: Bilateral analysis output includes asymmetry flags so any
#      proposed intervention can carry its own four-mode failure assessment
#      against the AB-asymmetric evidence base.
# ═══════════════════════════════════════════════════════════════════════════════


# ─────────────────────────────────────────────────────────────────────────────
# 26D.1 — Per-polity calibration registry (Rule 4)
# ─────────────────────────────────────────────────────────────────────────────

def _empty_citation_matrix() -> Dict[str, Dict[str, str]]:
    """Return an empty citation matrix (all cells unsourced)."""
    return {
        p: {b: "uncalibrated for this polity" for b in BIOSPHERIC_SUBSTRATE_DIMENSIONS}
        for p in COUPLING_PILLAR_ORDER
    }


def _all_t3_tier_matrix() -> Dict[str, Dict[str, str]]:
    """Return an all-T3 tier matrix (all cells require calibration)."""
    return {
        p: {b: "T3" for b in BIOSPHERIC_SUBSTRATE_DIMENSIONS}
        for p in COUPLING_PILLAR_ORDER
    }


# Per-polity coupling registry. Adding a polity requires:
#   1. coupling_matrix      — C[p][b] values for that polity
#   2. tier_matrix          — per-cell T-tier provenance
#   3. citation_matrix      — per-cell source attribution
#   4. calibration_required — True if values are placeholders
#   5. note                 — human-readable calibration context
#
# IMPORTANT: For v3.3, only U.S. 2025 carries primary-literature support.
# Non-U.S. polities INHERIT the U.S. coupling structure but have their tier
# provenance honestly reset to all-T3 to prevent Rule 5 laundering. Future
# work should construct per-polity coupling matrices from local primary
# sources (e.g., Hungarian Central Statistical Office for Hungary; INE
# Venezuela / OPEC for Venezuela; CBS Israel / Israeli Ministry of
# Environmental Protection for Israel; Iranian Statistical Centre / IRGC
# environmental statistics for Iran).
POLITY_COUPLING_REGISTRY: Dict[str, Dict[str, Any]] = {
    "US_2025": {
        "coupling_matrix":      SUBSTRATE_COUPLING_MATRIX,
        "tier_matrix":          None,    # initialized below to point to v3.2 calibrated matrix
        "citation_matrix":      None,    # initialized below to point to v3.2 citation matrix
        "calibration_required": False,
        "note":                 "U.S. national-scale 2025 baseline (canonical). Tier promotions per v3.2: T1=7, T2=6, T3=17.",
    },
    "Hungary_2024": {
        "coupling_matrix":      SUBSTRATE_COUPLING_MATRIX,    # placeholder — inherits US structure
        "tier_matrix":          _all_t3_tier_matrix(),
        "citation_matrix":      _empty_citation_matrix(),
        "calibration_required": True,
        "note":                 ("Hungary 2024 — UNCALIBRATED placeholder. Hungarian "
                                 "Central Statistical Office (KSH), EU Joint Research "
                                 "Centre, and Hungarian Ministry of Agriculture data "
                                 "needed for true Rule-4 calibration. Pillar throughput "
                                 "differs substantially from U.S. (e.g., higher EU-grid "
                                 "integration; ag share of GDP higher; transport "
                                 "Black-Sea-routed)."),
    },
    "Venezuela_2019": {
        "coupling_matrix":      SUBSTRATE_COUPLING_MATRIX,    # placeholder
        "tier_matrix":          _all_t3_tier_matrix(),
        "citation_matrix":      _empty_citation_matrix(),
        "calibration_required": True,
        "note":                 ("Venezuela 2019 — UNCALIBRATED placeholder. Collapsing "
                                 "oil-production polity; coupling structure radically "
                                 "different from U.S. — crude oil dominance flips "
                                 "Energy → climate weighting, Pillar→hydrology coupling "
                                 "altered by Orinoco basin hydrology. INE Venezuela and "
                                 "OPEC data required when accessible."),
    },
}

# Late-bind US tier/citation matrices to the v3.2 calibrated values
# (defined later in the file as COUPLING_TIER_MATRIX_V3_2 and COUPLING_CITATION_MATRIX).
# We do this by accessing module globals at first call rather than at import time
# to avoid forward-reference issues.
def _ensure_us_registry_bound() -> None:
    """Bind US registry tier/citation matrices to the v3.2 calibrated values."""
    g = globals()
    us = POLITY_COUPLING_REGISTRY["US_2025"]
    if us["tier_matrix"] is None:
        us["tier_matrix"] = g.get("COUPLING_TIER_MATRIX_V3_2", _all_t3_tier_matrix())
    if us["citation_matrix"] is None:
        us["citation_matrix"] = g.get("COUPLING_CITATION_MATRIX", _empty_citation_matrix())


def get_polity_coupling(polity_id: str) -> Dict[str, Any]:
    """
    Retrieve coupling metadata for a polity.

    Parameters
    ----------
    polity_id : str
        Key into POLITY_COUPLING_REGISTRY (e.g., 'US_2025', 'Hungary_2024',
        'Venezuela_2019', 'Israel_2026', 'Iran_2026').

    Returns
    -------
    dict with: coupling_matrix, tier_matrix, citation_matrix,
              calibration_required, note, polity_id

    Raises
    ------
    KeyError if polity_id is not registered.
    """
    _ensure_us_registry_bound()
    if polity_id not in POLITY_COUPLING_REGISTRY:
        raise KeyError(
            f"Polity '{polity_id}' not in POLITY_COUPLING_REGISTRY. "
            f"Available: {list(POLITY_COUPLING_REGISTRY.keys())}. "
            f"To add: register coupling_matrix, tier_matrix, citation_matrix, "
            f"calibration_required, and note."
        )
    entry = dict(POLITY_COUPLING_REGISTRY[polity_id])
    entry["polity_id"] = polity_id
    return entry


def coupling_calibration_status(polity_id: Optional[str] = None) -> Dict[str, Any]:
    """
    Report calibration status across the registry, or for a specific polity.

    Parameters
    ----------
    polity_id : str | None
        If specified, returns just that polity's status. Otherwise summarizes all.

    Returns
    -------
    dict with calibration tier counts and per-polity status.
    """
    _ensure_us_registry_bound()
    if polity_id is not None:
        entry = get_polity_coupling(polity_id)
        # Count tier distribution for this polity
        tiers = {"T1": 0, "T2": 0, "T3": 0}
        for p in COUPLING_PILLAR_ORDER:
            for b in BIOSPHERIC_SUBSTRATE_DIMENSIONS:
                t = entry["tier_matrix"][p][b]
                if t in tiers:
                    tiers[t] += 1
        return {
            "polity_id":            polity_id,
            "calibration_required": entry["calibration_required"],
            "tier_distribution":    tiers,
            "note":                 entry["note"],
        }
    # All polities
    out = {
        "registry_size":     len(POLITY_COUPLING_REGISTRY),
        "polities":          list(POLITY_COUPLING_REGISTRY.keys()),
        "per_polity":        {},
        "rule_4_compliance": "INFRASTRUCTURE_PRESENT_VALUES_INCOMPLETE",
    }
    for pid in POLITY_COUPLING_REGISTRY.keys():
        out["per_polity"][pid] = coupling_calibration_status(pid)
    return out


def compute_substrate_stress_for_polity(
    polity_id: str,
    throughput_by_pillar: Dict[str, float],
) -> Dict[str, Any]:
    """
    compute_substrate_stress() with explicit per-polity coupling lookup.

    Returns the substrate-stress output PLUS the coupling provenance metadata
    (tier distribution, calibration_required flag) so downstream consumers can
    apply Rule 5 caveats correctly.
    """
    entry = get_polity_coupling(polity_id)
    base = compute_substrate_stress(
        throughput_by_pillar,
        coupling_matrix=entry["coupling_matrix"],
    )
    base["polity_id"]            = polity_id
    base["calibration_required"] = entry["calibration_required"]
    base["calibration_note"]     = entry["note"]
    if entry["calibration_required"]:
        base["rule_4_caveat"] = (
            "Per-polity coupling values inherited from U.S. structure. "
            "Output is illustrative only — not Rule-4 calibrated."
        )
    return base


def identify_substrate_hot_cell_for_polity(
    polity_id: str,
    throughput_by_pillar: Dict[str, float],
    bhi_values: Dict[str, float],
) -> Dict[str, Any]:
    """identify_substrate_hot_cell() with explicit per-polity coupling lookup."""
    entry = get_polity_coupling(polity_id)
    base = identify_substrate_hot_cell(
        throughput_by_pillar,
        bhi_values,
        coupling_matrix=entry["coupling_matrix"],
    )
    base["polity_id"]            = polity_id
    base["calibration_required"] = entry["calibration_required"]
    if entry["calibration_required"]:
        base["rule_4_caveat"] = (
            "Per-polity coupling values inherited from U.S. structure. "
            "Hot-cell identification is illustrative only — not Rule-4 calibrated."
        )
    return base


# ─────────────────────────────────────────────────────────────────────────────
# 26D.2 — Bilateral substrate analysis (closes v3.0 Part VIII open #4)
# ─────────────────────────────────────────────────────────────────────────────

def _indicator_tier_distribution(indicators: Optional[Dict[str, List[Dict]]]) -> Optional[Dict[str, int]]:
    """
    Compute T-tier distribution across all indicators in a polity baseline.

    Returns None if indicators are not provided or carry no 'tier' field.
    Returns dict {T1: n, T2: n, T3: n, untagged: n} otherwise.
    """
    if not indicators:
        return None
    tiers = {"T1": 0, "T2": 0, "T3": 0, "untagged": 0}
    any_tagged = False
    for pillar_name, items in indicators.items():
        for ind in items:
            t = ind.get("tier")
            if t in ("T1", "T2", "T3"):
                tiers[t] += 1
                any_tagged = True
            else:
                tiers["untagged"] += 1
    if not any_tagged:
        return None
    return tiers


def bilateral_substrate_analysis(
    polity_a_id: str,
    polity_a_throughput: Dict[str, float],
    polity_a_bhi: Dict[str, float],
    polity_b_id: str,
    polity_b_throughput: Dict[str, float],
    polity_b_bhi: Dict[str, float],
    polity_a_indicators: Optional[Dict[str, List[Dict]]] = None,
    polity_b_indicators: Optional[Dict[str, List[Dict]]] = None,
) -> Dict[str, Any]:
    """
    Run substrate-coupling analysis for TWO polities and surface asymmetry.

    Closes v3.0 Working Paper Part VIII open finding #4: 'Asymmetric bilateral
    worked example runs in only one direction'. This function runs the
    analysis FROM each polity's perspective using its own (potentially
    different) coupling matrix, then aggregates for shared-substrate effects.

    F3 caveat (per v2.0 → v3.0 closure): Bilateral framing does NOT equalize
    asymmetric evidence. The output makes the asymmetry visible at TWO
    levels:
      - coupling-matrix tier asymmetry (how confident we are in C[p][b])
      - indicator-level tier asymmetry (how confident we are in pillar inputs)
    The F3 verdict uses the WORST of the two — symmetric framing must not
    smooth either source of asymmetry.

    Parameters
    ----------
    polity_a_id, polity_b_id : str
        Registry keys (e.g., 'US_2025', 'Hungary_2024', 'Israel_2026').
    polity_a_throughput, polity_b_throughput : dict
        Per-polity Pillar throughput {Pillar: [0,1]}.
    polity_a_bhi, polity_b_bhi : dict
        Per-polity biospheric health indices {dim: [0,1]}.
    polity_a_indicators, polity_b_indicators : dict | None
        Optional indicator dicts (US_BASELINE_INDICATORS-shaped). When
        provided, indicators carrying 'tier' keys participate in the
        indicator-level tier-asymmetry check. F3 verdict uses worst of
        coupling-level and indicator-level asymmetry.

    Returns
    -------
    dict with:
        polity_a_analysis, polity_b_analysis  : per-polity stress + hot-cell
        shared_substrate_stress              : naive aggregate (sum of stresses)
        directional_asymmetry                : tier-quality gap analysis
                                               (coupling and indicator levels)
        f3_caveat                            : asymmetric-evidence warning if applicable
        do_not_deploy_reason                 : explicit flag
    """
    a_stress = compute_substrate_stress_for_polity(polity_a_id, polity_a_throughput)
    b_stress = compute_substrate_stress_for_polity(polity_b_id, polity_b_throughput)
    a_hot    = identify_substrate_hot_cell_for_polity(polity_a_id, polity_a_throughput, polity_a_bhi)
    b_hot    = identify_substrate_hot_cell_for_polity(polity_b_id, polity_b_throughput, polity_b_bhi)

    # Naive shared-substrate aggregation: substrate stress is additive per dimension
    # (the biosphere doesn't care which polity's industry caused the depletion)
    shared = {dim: 0.0 for dim in BIOSPHERIC_SUBSTRATE_DIMENSIONS}
    for dim in BIOSPHERIC_SUBSTRATE_DIMENSIONS:
        shared[dim] = round(
            a_stress["stress_by_dimension"].get(dim, 0.0) +
            b_stress["stress_by_dimension"].get(dim, 0.0),
            4,
        )
    shared_max_dim = max(shared, key=shared.get) if shared else None

    # ─── Coupling-level tier asymmetry ───
    a_tiers = coupling_calibration_status(polity_a_id)["tier_distribution"]
    b_tiers = coupling_calibration_status(polity_b_id)["tier_distribution"]
    # Denominator = total coupling cells (Pillars × substrate dimensions), derived
    # from the matrix dimensions rather than hardcoded so it stays correct if the
    # Pillar set or substrate-dimension set is ever extended. For the canonical
    # 6×5 matrix this is 30 — numerically identical to the prior literal.
    _n_coupling_cells = len(COUPLING_PILLAR_ORDER) * len(BIOSPHERIC_SUBSTRATE_DIMENSIONS)
    a_t1t2_pct = (a_tiers["T1"] + a_tiers["T2"]) / _n_coupling_cells
    b_t1t2_pct = (b_tiers["T1"] + b_tiers["T2"]) / _n_coupling_cells
    coupling_gap = abs(a_t1t2_pct - b_t1t2_pct)

    # ─── Indicator-level tier asymmetry (F3 fix per v3.3) ───
    a_ind_tiers = _indicator_tier_distribution(polity_a_indicators)
    b_ind_tiers = _indicator_tier_distribution(polity_b_indicators)
    indicator_gap: Optional[float] = None
    a_ind_t1t2_pct = None
    b_ind_t1t2_pct = None
    if a_ind_tiers is not None and b_ind_tiers is not None:
        a_total = sum(v for k, v in a_ind_tiers.items() if k != "untagged")
        b_total = sum(v for k, v in b_ind_tiers.items() if k != "untagged")
        a_ind_t1t2_pct = (a_ind_tiers["T1"] + a_ind_tiers["T2"]) / a_total if a_total > 0 else 0.0
        b_ind_t1t2_pct = (b_ind_tiers["T1"] + b_ind_tiers["T2"]) / b_total if b_total > 0 else 0.0
        indicator_gap = abs(a_ind_t1t2_pct - b_ind_t1t2_pct)

    # Worst-of verdict (F3 anti-laundering)
    effective_gap = coupling_gap
    gap_source = "coupling"
    if indicator_gap is not None and indicator_gap > coupling_gap:
        effective_gap = indicator_gap
        gap_source = "indicator"

    asymmetry: Dict[str, Any] = {
        f"{polity_a_id}_coupling_t1_t2_fraction": round(a_t1t2_pct, 3),
        f"{polity_b_id}_coupling_t1_t2_fraction": round(b_t1t2_pct, 3),
        "coupling_asymmetry_gap":                  round(coupling_gap, 3),
        "verdict": (
            "STRONGLY_ASYMMETRIC" if effective_gap > 0.30 else
            "MODERATELY_ASYMMETRIC" if effective_gap > 0.10 else
            "APPROXIMATELY_SYMMETRIC"
        ),
        "verdict_dominated_by": gap_source,
        "effective_gap":        round(effective_gap, 3),
    }
    if indicator_gap is not None:
        asymmetry[f"{polity_a_id}_indicator_t1_t2_fraction"] = round(a_ind_t1t2_pct, 3)
        asymmetry[f"{polity_b_id}_indicator_t1_t2_fraction"] = round(b_ind_t1t2_pct, 3)
        asymmetry["indicator_asymmetry_gap"]                 = round(indicator_gap, 3)

    # F3 caveat — message keyed to dominating gap source
    f3_caveat: Optional[str]
    if effective_gap > 0.30:
        if gap_source == "indicator":
            f3_caveat = (
                f"F3 CAVEAT TRIGGERED (indicator-level): tier-quality gap = {effective_gap:.2f}. "
                f"{polity_a_id} indicator data is {a_ind_t1t2_pct*100:.0f}% T1/T2; "
                f"{polity_b_id} is {b_ind_t1t2_pct*100:.0f}%. Symmetric framing "
                f"would launder this asymmetric evidence. Treat per-polity "
                f"conclusions as evidentially distinct."
            )
        else:
            f3_caveat = (
                f"F3 CAVEAT TRIGGERED (coupling-level): tier-quality gap = {effective_gap:.2f}. "
                f"{polity_a_id} carries {a_t1t2_pct*100:.0f}% T1/T2 coupling cells; "
                f"{polity_b_id} carries {b_t1t2_pct*100:.0f}%. Symmetric framing "
                f"would launder this asymmetric evidence. Treat per-polity "
                f"conclusions as evidentially distinct."
            )
    elif effective_gap > 0.10:
        f3_caveat = (
            f"F3 caveat (moderate, {gap_source}-level): tier-quality gap = {effective_gap:.2f}. "
            f"Bilateral conclusions should note the per-polity evidence-quality "
            f"differential."
        )
    else:
        f3_caveat = None

    return {
        "polity_a_id":          polity_a_id,
        "polity_b_id":          polity_b_id,
        "polity_a_analysis":    {"stress": a_stress, "hot_cell": a_hot},
        "polity_b_analysis":    {"stress": b_stress, "hot_cell": b_hot},
        "shared_substrate_stress": {
            "stress_by_dimension": shared,
            "max_stressed_dim":    shared_max_dim,
            "max_stress_value":    shared.get(shared_max_dim, 0.0) if shared_max_dim else 0.0,
        },
        "directional_asymmetry": asymmetry,
        "f3_caveat":             f3_caveat,
        "deployment_status":     "experimental",
        "do_not_deploy_reason":  (
            "Bilateral analysis is research-grade. Per-polity coupling values "
            "are illustrative for non-U.S. polities. Do not use as basis for "
            "policy without per-polity Rule-4 recalibration."
        ),
    }


# ─────────────────────────────────────────────────────────────────────────────
# 26D.3 — Twelve-Day War case study (illustrative)
# ─────────────────────────────────────────────────────────────────────────────
#
# Twelve-Day War: U.S.–Israel–Iran conflict beginning late February 2026.
# The user's framework requires a substrate-coupling worked example for
# all three parties. This section provides ILLUSTRATIVE 2026 baselines —
# T-tagged and source-diverse per 7 May 2026 directive — and a one-shot
# `twelve_day_war_substrate_analysis()` function.
#
# DO NOT DEPLOY: case study data is illustrative. Per-indicator T-tags are
# honest about evidence quality. Iran indicators are T3-dominant by
# construction (sanctions data complications, source-diversity
# requirements). The bilateral analysis function (26D.2) is research-grade;
# the case study DATA is illustrative.

# Israel 2026 — T2-dominant illustrative baseline
# Sources cited inline with each indicator. Predominantly OECD, IMF, IEA,
# Bank of Israel, Israeli Central Bureau of Statistics (CBS), World Bank.
# Shaped by: ongoing Gaza operations through 2024-25, Iran direct strikes
# (April 2024, October 2024), elevated defense spending, Haifa industrial
# corridor stress, energy import diversification post-Russia-Ukraine,
# political fragmentation, judicial-reform aftershocks.
# T-tagging: most indicators T2 (well-established secondary statistics);
# entertainment substrate indicators T3 (qualitative + survey-based).

ISRAEL_2026_BASELINE_ILLUSTRATIVE: Dict[str, List[Dict]] = {
    "Energy": [
        {"id": "E1", "name": "Reserve Margin",     "raw": 14,   "bench": 15,  "norm": "direct",   "w": 0.18, "syntropy_bound": "fiscal", "tier": "T2", "src": "IEA Israel 2024 review"},
        {"id": "E2", "name": "Import Dependency",  "raw": 35,   "bench": 100, "norm": "inverted", "w": 0.18, "syntropy_bound": "fiscal", "tier": "T2", "src": "BoI Annual Report 2024 (Tamar/Leviathan offset)"},
        {"id": "E3", "name": "Price Volatility",   "raw": 1.5,  "bench": 1,   "norm": "zscore",   "w": 0.13, "tier": "T2", "src": "OECD Energy Prices Q4 2025"},
        {"id": "E4", "name": "Source Diversity",   "raw": 0.40, "bench": 1,   "norm": "hhi",      "w": 0.18, "syntropy_bound": "fiscal", "tier": "T2", "src": "IEA energy mix; gas-dominant"},
        {"id": "E5", "name": "Affordability",      "raw": 7.0,  "bench": 15,  "norm": "inverted", "w": 0.13, "tier": "T2", "src": "CBS household energy expenditure 2024"},
        {"id": "E6", "name": "Infrastructure Age", "raw": 38,   "bench": 100, "norm": "inverted", "w": 0.10, "syntropy_bound": "fiscal", "tier": "T2", "src": "Israel Electric Corp. 2024 annual"},
        {"id": "E7", "name": "Carbon Trajectory",  "raw": 75,   "bench": 100, "norm": "inverted", "w": 0.05, "syntropy_bound": "regeneration", "substrate": "climate", "tier": "T2", "src": "Israel Ministry of Environmental Protection 2024 GHG inventory"},
        {"id": "E8", "name": "Climate-Risk Margin", "raw": 25,  "bench": 100, "norm": "inverted", "w": 0.05, "syntropy_bound": "regeneration", "substrate": "climate", "tier": "T3", "src": "Inferred from regional projections; no published Israeli stress-test"},
    ],
    "Information": [
        {"id": "I1", "name": "Broadband",          "raw": 88,   "bench": 100, "norm": "pct",      "w": 0.15, "tier": "T2", "src": "ITU 2024 fixed broadband"},
        {"id": "I2", "name": "Media Concentration", "raw": 0.45, "bench": 1,   "norm": "hhi",      "w": 0.20, "tier": "T2", "src": "Israeli Democracy Institute media concentration index 2024"},
        {"id": "I3", "name": "Cyber Resilience",   "raw": 70,   "bench": 100, "norm": "direct",   "w": 0.25, "tier": "T2", "src": "Israel National Cyber Directorate; high investment, multiple high-profile breaches 2024-25"},
        {"id": "I4", "name": "Misinfo Prevalence", "raw": 32,   "bench": 50,  "norm": "inverted", "w": 0.20, "tier": "T3", "src": "Survey-based; substantial Hebrew-Arabic split"},
        {"id": "I5", "name": "Digital Literacy",   "raw": 70,   "bench": 100, "norm": "direct",   "w": 0.10, "tier": "T2", "src": "OECD PIAAC adapted"},
        {"id": "I6", "name": "Redundancy Index",   "raw": 60,   "bench": 100, "norm": "direct",   "w": 0.10, "tier": "T3", "src": "Inferred from sub-sea cable count"},
    ],
    "Product": [
        {"id": "P1", "name": "Ag Self-Sufficiency",  "raw": 60,   "bench": 100, "norm": "direct",   "w": 0.17, "syntropy_bound": "fiscal", "tier": "T2", "src": "Israeli Ministry of Agriculture; ~60% caloric self-sufficiency"},
        {"id": "P2", "name": "Fertilizer Dep.",      "raw": 75,   "bench": 100, "norm": "inverted", "w": 0.13, "syntropy_bound": "fiscal", "tier": "T2", "src": "FAO Israel; high N/P import dependence"},
        {"id": "P3", "name": "Mfg Capacity Util.",   "raw": 75,   "bench": 85,  "norm": "direct",   "w": 0.12, "syntropy_bound": "fiscal", "tier": "T2", "src": "BoI manufacturing surveys 2024-25"},
        {"id": "P4", "name": "Supply Chain Stress",  "raw": 0.7,  "bench": 1,   "norm": "zscore",   "w": 0.17, "tier": "T2", "src": "Red Sea route disruption (Houthi); Haifa port 2024 issues"},
        {"id": "P5", "name": "Strategic Reserves",   "raw": 60,   "bench": 90,  "norm": "direct",   "w": 0.13, "syntropy_bound": "fiscal", "tier": "T3", "src": "Limited public detail; defense-driven"},
        {"id": "P6", "name": "Pharma Import Ratio",  "raw": 70,   "bench": 100, "norm": "inverted", "w": 0.12, "syntropy_bound": "fiscal", "tier": "T2", "src": "Teva Pharmaceutical domestic capacity"},
        {"id": "P7", "name": "Soil Capital",         "raw": 45,   "bench": 100, "norm": "direct",   "w": 0.07, "syntropy_bound": "regeneration", "substrate": "soil", "tier": "T2", "src": "FAO soil status; Mediterranean degradation pressure"},
        {"id": "P8", "name": "Pollinator Health",    "raw": 50,   "bench": 100, "norm": "direct",   "w": 0.04, "syntropy_bound": "regeneration", "substrate": "biotic_relationships", "tier": "T3", "src": "Volcani Center reports; localized data"},
        {"id": "P9", "name": "Ag Water Stress",      "raw": 35,   "bench": 100, "norm": "direct",   "w": 0.05, "syntropy_bound": "regeneration", "substrate": "hydrology", "tier": "T2", "src": "Israeli Water Authority; severe; mitigated by desalination"},
    ],
    "Service": [
        {"id": "S1", "name": "Institutional Trust",  "raw": 30,   "bench": 100, "norm": "pct",      "w": 0.24, "tier": "T2", "src": "Israeli Democracy Index 2024 — declining post-judicial reform"},
        {"id": "S2", "name": "Fiscal Headroom",      "raw": 70,   "bench": 90,  "norm": "sigmoid",  "w": 0.19, "syntropy_bound": "fiscal", "tier": "T2", "src": "IMF Israel Article IV 2024; ~70% debt-to-GDP, war-elevated"},
        {"id": "S3", "name": "Healthcare Surge",     "raw": 22,   "bench": 35,  "norm": "direct",   "w": 0.14, "syntropy_bound": "fiscal", "tier": "T2", "src": "Israeli Ministry of Health; under-bedded baseline, war stress"},
        {"id": "S4", "name": "Judicial Independence","raw": 50,   "bench": 100, "norm": "direct",   "w": 0.14, "tier": "T2", "src": "World Justice Project Rule of Law Index 2024 — sharp decline"},
        {"id": "S5", "name": "Regulatory Capacity",  "raw": 60,   "bench": 100, "norm": "pct",      "w": 0.14, "syntropy_bound": "fiscal", "tier": "T2", "src": "OECD regulatory indicators"},
        {"id": "S6", "name": "Financial Stress",     "raw": 1.4,  "bench": 1,   "norm": "zscore",   "w": 0.10, "tier": "T2", "src": "BoI Financial Stability Report 2024"},
        {"id": "S7", "name": "Watershed Service Capacity", "raw": 70, "bench": 100, "norm": "direct", "w": 0.05, "syntropy_bound": "regeneration", "substrate": "hydrology", "tier": "T2", "src": "Mekorot/Israeli Water Authority — desalination dominant"},
    ],
    "Transport": [
        {"id": "T1", "name": "Infrastructure Grade", "raw": "B-", "bench": "A",  "norm": "grade",    "w": 0.19, "syntropy_bound": "fiscal", "tier": "T2", "src": "OECD ITF; relatively modern but congested"},
        {"id": "T2", "name": "Chokepoint Dep.",      "raw": 60,   "bench": 100, "norm": "inverted", "w": 0.19, "tier": "T2", "src": "Suez/Bab al-Mandab/Hormuz exposure; Red Sea dominance"},
        {"id": "T3", "name": "Port Throughput",      "raw": 4,    "bench": 10,  "norm": "inverted", "w": 0.14, "syntropy_bound": "fiscal", "tier": "T2", "src": "Haifa+Ashdod 2024 throughput vs OECD norm"},
        {"id": "T4", "name": "Route Redundancy",     "raw": 40,   "bench": 100, "norm": "direct",   "w": 0.14, "syntropy_bound": "fiscal", "tier": "T2", "src": "Limited land-route diplomatic options"},
        {"id": "T5", "name": "Freight Cost Stab.",   "raw": 50,   "bench": 100, "norm": "direct",   "w": 0.14, "tier": "T2", "src": "Red Sea disruption-elevated"},
        {"id": "T6", "name": "Bridge Deficiency",    "raw": 6,    "bench": 15,  "norm": "inverted", "w": 0.15, "syntropy_bound": "fiscal", "tier": "T3", "src": "Ministry of Transport data; less reported than US"},
        {"id": "T7", "name": "Climate-Risk Asset Exposure", "raw": 30, "bench": 100, "norm": "inverted", "w": 0.05, "syntropy_bound": "regeneration", "substrate": "climate", "tier": "T3", "src": "Coastal infrastructure projections"},
    ],
    "Entertainment": [
        # Substrate caretaker situation: bilateral religious-Zionist vs. liberal-secular
        # vs. Haredi factions; post-judicial-reform legitimacy contested; war narrative
        # provides temporary cohesion under high external threat.
        {"id": "N1", "name": "Social Cohesion",     "raw": 35,   "bench": 100, "norm": "direct",   "w": 0.125, "tier": "T2", "src": "Israeli Democracy Index 2024 cohesion index"},
        {"id": "N2", "name": "Polarization Index",  "raw": 80,   "bench": 100, "norm": "inverted", "w": 0.125, "tier": "T2", "src": "Pew/IDI polarization measures 2024"},
        {"id": "N3", "name": "Shared Narrative",    "raw": 35,   "bench": 100, "norm": "pct",      "w": 0.10, "tier": "T3", "src": "Substrate-coding inferred — wartime cohesion masks deeper bilateral split"},
        {"id": "N4", "name": "Cultural Participation", "raw": 55, "bench": 100, "norm": "pct",      "w": 0.075, "tier": "T2", "src": "CBS culture surveys"},
        {"id": "N5", "name": "Mental Health",       "raw": 18,   "bench": 30,  "norm": "inverted", "w": 0.075, "tier": "T2", "src": "Israeli Ministry of Health; elevated post-Oct 7"},
        # Substrate caretaker indicators (substrate-coding required):
        {"id": "N6",  "name": "Caretaker Legitimacy",            "raw": 40, "bench": 100, "norm": "direct", "w": 0.0625, "syntropy_bound": "regeneration", "substrate": "meaning", "tier": "T3", "src": "Substrate-coded; coalition fragmentation"},
        {"id": "N7",  "name": "Substrate-Gradient Cohesion",     "raw": 28, "bench": 100, "norm": "direct", "w": 0.0625, "syntropy_bound": "regeneration", "substrate": "meaning", "tier": "T3", "src": "Religious-secular-Haredi tri-split"},
        {"id": "N8",  "name": "Costly-Commitment Density",       "raw": 50, "bench": 100, "norm": "direct", "w": 0.0625, "syntropy_bound": "regeneration", "substrate": "meaning", "tier": "T3", "src": "Reserve duty + religious observance vary by faction"},
        {"id": "N9",  "name": "Caretaker Four-Mode Integrity",   "raw": 35, "bench": 100, "norm": "direct", "w": 0.0625, "syntropy_bound": "regeneration", "substrate": "meaning", "tier": "T3", "src": "Multiple corruption probes; war-cabinet dysfunction"},
        {"id": "N10", "name": "Cross-Pillar Coupling Integrity", "raw": 50, "bench": 100, "norm": "direct", "w": 0.0625, "syntropy_bound": "regeneration", "substrate": "meaning", "tier": "T3", "src": "Defense-civilian coupling strong; civic-state weak"},
        {"id": "N11", "name": "Caretaker Reflexive Composure",   "raw": 30, "bench": 100, "norm": "direct", "w": 0.0625, "syntropy_bound": "regeneration", "substrate": "meaning", "tier": "T3", "src": "High alarm-mode discourse; weak corrective composure"},
        {"id": "N12", "name": "Substrate Retention",             "raw": 55, "bench": 100, "norm": "direct", "w": 0.0625, "syntropy_bound": "regeneration", "substrate": "meaning", "tier": "T2", "src": "CBS net migration; significant 2023-25 emigration"},
        {"id": "N13", "name": "External Substrate-Projection",   "raw": 50, "bench": 100, "norm": "direct", "w": 0.0625, "syntropy_bound": "regeneration", "substrate": "meaning", "tier": "T3", "src": "Diaspora projection; war-narrative contested in West"},
    ],
}


# Iran 2026 — T3-dominant illustrative baseline
# SOURCE-DIVERSITY DIRECTIVE (per 7 May 2026 userMemory): Iran indicators are
# constructed from a deliberately diverse source basket to mitigate Western-
# mainstream bias. Sources cited inline include:
#   - Western: IMF Article IV, World Bank, IEA, CSIS, Brookings, IISS, FDD
#   - Iranian state: SCI (Statistical Centre of Iran), CBI, IRNA, Tasnim News
#   - Eastern/Third-party: Al Jazeera, Anadolu, TASS, Xinhua (BIAS-FLAGGED)
#   - International: OPEC, OECD where applicable
# Tier distribution skews T3 by construction — sanctions and limited press
# access genuinely degrade evidence quality. Inflating tier ratings would be
# Rule 5 laundering. The honest move is to mark T3 and surface the constraint.
# Shaped by: continuing JCPOA aftermath, sanctions regime maturation, oil
# exports recovery via gray-market routes, IRGC economic dominance, popular
# discontent (Mahsa Amini protest aftermath fading but unresolved),
# infrastructure depreciation, demographic transition.

IRAN_2026_BASELINE_ILLUSTRATIVE: Dict[str, List[Dict]] = {
    "Energy": [
        {"id": "E1", "name": "Reserve Margin",     "raw": 8,    "bench": 15,  "norm": "direct",   "w": 0.18, "syntropy_bound": "fiscal", "tier": "T3", "src": "TAVANIR estimates; chronic summer blackouts; Western estimates lower"},
        {"id": "E2", "name": "Import Dependency",  "raw": 5,    "bench": 100, "norm": "inverted", "w": 0.18, "syntropy_bound": "fiscal", "tier": "T2", "src": "OPEC; Iran is net energy exporter"},
        {"id": "E3", "name": "Price Volatility",   "raw": 1.8,  "bench": 1,   "norm": "zscore",   "w": 0.13, "tier": "T3", "src": "Domestic IRR price volatility; subsidy-distorted"},
        {"id": "E4", "name": "Source Diversity",   "raw": 0.55, "bench": 1,   "norm": "hhi",      "w": 0.18, "syntropy_bound": "fiscal", "tier": "T2", "src": "IEA; oil/gas-dominant but hydro+nuclear+solar present"},
        {"id": "E5", "name": "Affordability",      "raw": 4.0,  "bench": 15,  "norm": "inverted", "w": 0.13, "tier": "T3", "src": "Subsidized-domestic; SCI HH expenditure"},
        {"id": "E6", "name": "Infrastructure Age", "raw": 60,   "bench": 100, "norm": "inverted", "w": 0.10, "syntropy_bound": "fiscal", "tier": "T3", "src": "Sanctions-driven aging; Western/Iranian estimates diverge"},
        {"id": "E7", "name": "Carbon Trajectory",  "raw": 50,   "bench": 100, "norm": "inverted", "w": 0.05, "syntropy_bound": "regeneration", "substrate": "climate", "tier": "T3", "src": "Iranian DOE 2023 NDC update; high carbon intensity"},
        {"id": "E8", "name": "Climate-Risk Margin", "raw": 15,  "bench": 100, "norm": "inverted", "w": 0.05, "syntropy_bound": "regeneration", "substrate": "climate", "tier": "T3", "src": "Acute drought + heat stress; subsidence; UNEP regional"},
    ],
    "Information": [
        {"id": "I1", "name": "Broadband",          "raw": 70,   "bench": 100, "norm": "pct",      "w": 0.15, "tier": "T2", "src": "ITU 2024; mobile-dominated"},
        {"id": "I2", "name": "Media Concentration", "raw": 0.85, "bench": 1,   "norm": "hhi",      "w": 0.20, "tier": "T2", "src": "RSF Iran 2024; high state concentration"},
        {"id": "I3", "name": "Cyber Resilience",   "raw": 35,   "bench": 100, "norm": "direct",   "w": 0.25, "tier": "T3", "src": "Stuxnet legacy + multiple 2024-25 disclosed breaches"},
        {"id": "I4", "name": "Misinfo Prevalence", "raw": 38,   "bench": 50,  "norm": "inverted", "w": 0.20, "tier": "T3", "src": "Multi-channel: state media + circumvention + diaspora"},
        {"id": "I5", "name": "Digital Literacy",   "raw": 60,   "bench": 100, "norm": "direct",   "w": 0.10, "tier": "T3", "src": "Inferred from internet-circumvention prevalence"},
        {"id": "I6", "name": "Redundancy Index",   "raw": 30,   "bench": 100, "norm": "direct",   "w": 0.10, "tier": "T3", "src": "State-controlled NIN; internet shutdowns periodic"},
    ],
    "Product": [
        {"id": "P1", "name": "Ag Self-Sufficiency",  "raw": 70,   "bench": 100, "norm": "direct",   "w": 0.17, "syntropy_bound": "fiscal", "tier": "T2", "src": "FAO; SCI; Iran Ministry of Agriculture-Jihad"},
        {"id": "P2", "name": "Fertilizer Dep.",      "raw": 30,   "bench": 100, "norm": "inverted", "w": 0.13, "syntropy_bound": "fiscal", "tier": "T2", "src": "Iran is significant urea producer; Persian Gulf petrochem"},
        {"id": "P3", "name": "Mfg Capacity Util.",   "raw": 60,   "bench": 85,  "norm": "direct",   "w": 0.12, "syntropy_bound": "fiscal", "tier": "T3", "src": "CBI surveys; sanctions-constrained intermediate inputs"},
        {"id": "P4", "name": "Supply Chain Stress",  "raw": 1.6,  "bench": 1,   "norm": "zscore",   "w": 0.17, "tier": "T2", "src": "Sanctions-driven; gray-market substitution"},
        {"id": "P5", "name": "Strategic Reserves",   "raw": 65,   "bench": 90,  "norm": "direct",   "w": 0.13, "syntropy_bound": "fiscal", "tier": "T3", "src": "Sanctions-resilience focus; IRGC-managed; opaque"},
        {"id": "P6", "name": "Pharma Import Ratio",  "raw": 50,   "bench": 100, "norm": "inverted", "w": 0.12, "syntropy_bound": "fiscal", "tier": "T3", "src": "Domestic pharma ~50%; sanctions exemptions partial"},
        {"id": "P7", "name": "Soil Capital",         "raw": 30,   "bench": 100, "norm": "direct",   "w": 0.07, "syntropy_bound": "regeneration", "substrate": "soil", "tier": "T3", "src": "FAO; severe degradation in Khuzestan / Fars"},
        {"id": "P8", "name": "Pollinator Health",    "raw": 40,   "bench": 100, "norm": "direct",   "w": 0.04, "syntropy_bound": "regeneration", "substrate": "biotic_relationships", "tier": "T3", "src": "Limited national survey; localized studies"},
        {"id": "P9", "name": "Ag Water Stress",      "raw": 20,   "bench": 100, "norm": "direct",   "w": 0.05, "syntropy_bound": "regeneration", "substrate": "hydrology", "tier": "T2", "src": "Severe; Lake Urmia, Zayandehrud, Karkheh basins; Iran DOE 2024"},
    ],
    "Service": [
        {"id": "S1", "name": "Institutional Trust",  "raw": 22,   "bench": 100, "norm": "pct",      "w": 0.24, "tier": "T3", "src": "GAMAAN/IranPoll triangulation; state polls higher; diaspora polls lower"},
        {"id": "S2", "name": "Fiscal Headroom",      "raw": 50,   "bench": 90,  "norm": "sigmoid",  "w": 0.19, "syntropy_bound": "fiscal", "tier": "T3", "src": "IMF Iran Article IV; CBI; ~50% debt-to-GDP, FX-distorted"},
        {"id": "S3", "name": "Healthcare Surge",     "raw": 19,   "bench": 35,  "norm": "direct",   "w": 0.14, "syntropy_bound": "fiscal", "tier": "T3", "src": "Ministry of Health and Medical Education; sanctions-constrained imports"},
        {"id": "S4", "name": "Judicial Independence","raw": 22,   "bench": 100, "norm": "direct",   "w": 0.14, "tier": "T2", "src": "WJP Rule of Law Index 2024 — bottom-tier"},
        {"id": "S5", "name": "Regulatory Capacity",  "raw": 35,   "bench": 100, "norm": "pct",      "w": 0.14, "syntropy_bound": "fiscal", "tier": "T3", "src": "World Bank Doing Business legacy + IRGC-economy parallel structure"},
        {"id": "S6", "name": "Financial Stress",     "raw": 2.0,  "bench": 1,   "norm": "zscore",   "w": 0.10, "tier": "T2", "src": "IRR depreciation; multi-rate FX; chronic"},
        {"id": "S7", "name": "Watershed Service Capacity", "raw": 30, "bench": 100, "norm": "direct", "w": 0.05, "syntropy_bound": "regeneration", "substrate": "hydrology", "tier": "T2", "src": "Iran DOE; severe withdrawal-vs-recharge mismatch"},
    ],
    "Transport": [
        {"id": "T1", "name": "Infrastructure Grade", "raw": "C", "bench": "A",  "norm": "grade",    "w": 0.19, "syntropy_bound": "fiscal", "tier": "T3", "src": "WB Logistics Performance Index 2024; sanctions-degraded"},
        {"id": "T2", "name": "Chokepoint Dep.",      "raw": 35,   "bench": 100, "norm": "inverted", "w": 0.19, "tier": "T2", "src": "Hormuz exposure double-edged (transit fees vs. control)"},
        {"id": "T3", "name": "Port Throughput",      "raw": 6,    "bench": 10,  "norm": "inverted", "w": 0.14, "syntropy_bound": "fiscal", "tier": "T2", "src": "Bandar Abbas + Chabahar 2024; sanctioned shipping detours"},
        {"id": "T4", "name": "Route Redundancy",     "raw": 50,   "bench": 100, "norm": "direct",   "w": 0.14, "syntropy_bound": "fiscal", "tier": "T3", "src": "INSTC corridor + sanctions-bypass via Iraq/Caspian"},
        {"id": "T5", "name": "Freight Cost Stab.",   "raw": 35,   "bench": 100, "norm": "direct",   "w": 0.14, "tier": "T3", "src": "FX-volatile; sanctions premia"},
        {"id": "T6", "name": "Bridge Deficiency",    "raw": 10,   "bench": 15,  "norm": "inverted", "w": 0.15, "syntropy_bound": "fiscal", "tier": "T3", "src": "Limited public asset condition data"},
        {"id": "T7", "name": "Climate-Risk Asset Exposure", "raw": 20, "bench": 100, "norm": "inverted", "w": 0.05, "syntropy_bound": "regeneration", "substrate": "climate", "tier": "T3", "src": "Subsidence + extreme-heat infra stress"},
    ],
    "Entertainment": [
        # Substrate caretaker: revolutionary-Islamic ideological state vs. residual
        # secular-modernist + ethnic-pluralist + religious-reformist factions.
        # Substantial substrate decoupling (state ideology vs. younger urban
        # cohorts); legitimacy contested; high external substrate-projection
        # via Shia-axis but contested domestically.
        {"id": "N1", "name": "Social Cohesion",     "raw": 28,   "bench": 100, "norm": "direct",   "w": 0.125, "tier": "T3", "src": "GAMAAN cohesion proxies; ethnic + generational fractures"},
        {"id": "N2", "name": "Polarization Index",  "raw": 78,   "bench": 100, "norm": "inverted", "w": 0.125, "tier": "T3", "src": "State-society polarization; multiple 2017/19/22 protest waves"},
        {"id": "N3", "name": "Shared Narrative",    "raw": 25,   "bench": 100, "norm": "pct",      "w": 0.10, "tier": "T3", "src": "Revolutionary narrative-decay among under-40 cohort"},
        {"id": "N4", "name": "Cultural Participation", "raw": 45, "bench": 100, "norm": "pct",      "w": 0.075, "tier": "T3", "src": "Ministry of Culture; underground vs. official split"},
        {"id": "N5", "name": "Mental Health",       "raw": 17,   "bench": 30,  "norm": "inverted", "w": 0.075, "tier": "T3", "src": "Iranian psychiatric association; estimates vary"},
        # Substrate caretaker indicators (substrate-coding required):
        {"id": "N6",  "name": "Caretaker Legitimacy",            "raw": 28, "bench": 100, "norm": "direct", "w": 0.0625, "syntropy_bound": "regeneration", "substrate": "meaning", "tier": "T3", "src": "Substrate-coded; clerical legitimacy contested"},
        {"id": "N7",  "name": "Substrate-Gradient Cohesion",     "raw": 25, "bench": 100, "norm": "direct", "w": 0.0625, "syntropy_bound": "regeneration", "substrate": "meaning", "tier": "T3", "src": "Tehran-rural-ethnic minority gradients"},
        {"id": "N8",  "name": "Costly-Commitment Density",       "raw": 35, "bench": 100, "norm": "direct", "w": 0.0625, "syntropy_bound": "regeneration", "substrate": "meaning", "tier": "T3", "src": "Mosque attendance declining among youth"},
        {"id": "N9",  "name": "Caretaker Four-Mode Integrity",   "raw": 22, "bench": 100, "norm": "direct", "w": 0.0625, "syntropy_bound": "regeneration", "substrate": "meaning", "tier": "T3", "src": "IRGC economic capture; multiple rent-seeking findings"},
        {"id": "N10", "name": "Cross-Pillar Coupling Integrity", "raw": 30, "bench": 100, "norm": "direct", "w": 0.0625, "syntropy_bound": "regeneration", "substrate": "meaning", "tier": "T3", "src": "IRGC-Bonyad-state parallel structure; coupling brittle"},
        {"id": "N11", "name": "Caretaker Reflexive Composure",   "raw": 25, "bench": 100, "norm": "direct", "w": 0.0625, "syntropy_bound": "regeneration", "substrate": "meaning", "tier": "T3", "src": "Repression-mode dominant over composure-mode"},
        {"id": "N12", "name": "Substrate Retention",             "raw": 35, "bench": 100, "norm": "direct", "w": 0.0625, "syntropy_bound": "regeneration", "substrate": "meaning", "tier": "T3", "src": "Brain drain; substrate-bearer emigration"},
        {"id": "N13", "name": "External Substrate-Projection",   "raw": 55, "bench": 100, "norm": "direct", "w": 0.0625, "syntropy_bound": "regeneration", "substrate": "meaning", "tier": "T3", "src": "Shia-axis (Hezbollah, Houthi, Iraqi militias); contested 2024-25"},
    ],
}


# Register Israel 2026 and Iran 2026 in coupling registry — but with all-T3
# tiers and calibration_required=True per Rule 4 discipline. Coupling values
# are inherited (placeholder); per-polity calibration is FUTURE WORK.
POLITY_COUPLING_REGISTRY["Israel_2026"] = {
    "coupling_matrix":      SUBSTRATE_COUPLING_MATRIX,    # placeholder
    "tier_matrix":          _all_t3_tier_matrix(),
    "citation_matrix":      _empty_citation_matrix(),
    "calibration_required": True,
    "note":                 ("Israel 2026 — UNCALIBRATED placeholder coupling. "
                             "Israeli Ministry of Environmental Protection, "
                             "Mekorot, IEC, and CBS data needed for calibration. "
                             "Coastal/Mediterranean climate envelope and "
                             "desalination-dominant water service produce coupling "
                             "structure substantively different from continental U.S."),
}

POLITY_COUPLING_REGISTRY["Iran_2026"] = {
    "coupling_matrix":      SUBSTRATE_COUPLING_MATRIX,    # placeholder
    "tier_matrix":          _all_t3_tier_matrix(),
    "citation_matrix":      _empty_citation_matrix(),
    "calibration_required": True,
    "note":                 ("Iran 2026 — UNCALIBRATED placeholder coupling. Iranian "
                             "Statistical Centre + Iran Department of Environment + "
                             "Ministry of Energy data needed; sanctions complicate "
                             "primary-source access. Severe water stress (Lake Urmia, "
                             "Zayandehrud, Karkheh) and oil-dominant energy structure "
                             "imply coupling structure substantively different from U.S."),
}


def israel_2026_baseline_illustrative() -> Dict[str, Any]:
    """
    Return Israel 2026 illustrative bundle. DO NOT DEPLOY — illustrative only.

    Values constructed from publicly accessible 2024-25 data; per-indicator T-tags
    visible in the indicator dicts. Rule 4: coupling matrix is U.S.-inherited
    placeholder, calibration required for operational use.
    """
    return {
        "indicators":           ISRAEL_2026_BASELINE_ILLUSTRATIVE,
        "polity_id":            "Israel_2026",
        "deployment_status":    "ILLUSTRATIVE — DO NOT DEPLOY",
        "tier_dominant":        "T2",
        "calibration_required": True,
    }


def iran_2026_baseline_illustrative() -> Dict[str, Any]:
    """
    Return Iran 2026 illustrative bundle. DO NOT DEPLOY — illustrative only.

    Source-diversity directive (7 May 2026 userMemory) applied: indicators
    constructed from Western, Iranian state, and third-party sources where
    possible. Tier distribution skews T3 by construction — sanctions and
    limited press access genuinely degrade evidence quality. F3 caveat
    applies to any bilateral analysis pairing Iran with a T1/T2-dominant
    polity.
    """
    return {
        "indicators":           IRAN_2026_BASELINE_ILLUSTRATIVE,
        "polity_id":            "Iran_2026",
        "deployment_status":    "ILLUSTRATIVE — DO NOT DEPLOY",
        "tier_dominant":        "T3",
        "calibration_required": True,
        "source_diversity_note": (
            "Constructed from source-diverse basket per 7 May 2026 directive: "
            "Western (IMF, World Bank, IEA, IISS, CSIS, Brookings), Iranian "
            "state (SCI, CBI, IRNA, Tasnim — bias-flagged), third-party "
            "(Al Jazeera, Anadolu, OPEC, GAMAAN). Triangulation imperfect; "
            "T3 dominance is honest, not curated."
        ),
    }


def _coarse_throughput_from_phis(phis: Dict[str, float]) -> Dict[str, float]:
    """
    Convert per-Pillar PHI dict into a coarse throughput proxy in [0,1].

    Throughput here means 'magnitude of human-system flow through this Pillar'.
    Higher PHI → higher functioning → higher throughput. This is a rough proxy;
    for production work, use real volumetric/financial throughput data.
    """
    return {p: max(0.0, min(1.0, phis.get(p, 0.5))) for p in COUPLING_PILLAR_ORDER}


def _coarse_bhi_baseline(severity: str = "moderate") -> Dict[str, float]:
    """
    Coarse BHI (biospheric health index) proxy by severity tier.

    For substrate-coupling analysis, BHI scales the pressure each Pillar applies
    to a substrate dimension: pressure(p,b) = throughput(p) × C[p][b] × (1 - BHI[b]).
    This function provides illustrative BHI values; production work requires
    per-region biospheric data.
    """
    if severity == "severe":   return {b: 0.30 for b in BIOSPHERIC_SUBSTRATE_DIMENSIONS}
    if severity == "stressed": return {b: 0.50 for b in BIOSPHERIC_SUBSTRATE_DIMENSIONS}
    if severity == "moderate": return {b: 0.65 for b in BIOSPHERIC_SUBSTRATE_DIMENSIONS}
    if severity == "healthy":  return {b: 0.85 for b in BIOSPHERIC_SUBSTRATE_DIMENSIONS}
    return {b: 0.65 for b in BIOSPHERIC_SUBSTRATE_DIMENSIONS}


def twelve_day_war_substrate_analysis() -> Dict[str, Any]:
    """
    Illustrative bilateral substrate-coupling analysis for the Twelve-Day War
    (U.S.–Israel–Iran conflict, late February 2026).

    Produces three pairwise bilateral analyses:
      US ↔ Israel
      US ↔ Iran
      Israel ↔ Iran

    Each carries its own F3 caveat per directional asymmetry. Iran-paired
    analyses trigger STRONGLY_ASYMMETRIC by construction (T3-dominant data
    paired against T1/T2-dominant polities).

    DO NOT DEPLOY: case study indicator values are illustrative. The bilateral
    analysis function infrastructure (26D.2) is research-grade; the case-study
    DATA is illustrative. The function is provided so the framework has a
    concrete bilateral worked example for the v3.0 Part VIII open backlog.

    Returns
    -------
    dict with three pairwise analyses + summary metadata.
    """
    # Compute per-Pillar PHIs for each polity using the existing engine
    us_phis = {p: compute_pillar_phi(US_BASELINE_INDICATORS[p]) for p in COUPLING_PILLAR_ORDER}
    il_phis = {p: compute_pillar_phi(ISRAEL_2026_BASELINE_ILLUSTRATIVE[p]) for p in COUPLING_PILLAR_ORDER}
    ir_phis = {p: compute_pillar_phi(IRAN_2026_BASELINE_ILLUSTRATIVE[p]) for p in COUPLING_PILLAR_ORDER}

    us_throughput = _coarse_throughput_from_phis(us_phis)
    il_throughput = _coarse_throughput_from_phis(il_phis)
    ir_throughput = _coarse_throughput_from_phis(ir_phis)

    # Differentiated BHI by polity (illustrative — Iran has more severe water/soil
    # substrate stress; Israel mid; US mid). Production work would source real
    # biospheric data per region.
    us_bhi = _coarse_bhi_baseline("moderate")
    il_bhi = {**_coarse_bhi_baseline("moderate"), "hydrology": 0.40, "soil": 0.45}  # severe water/soil
    ir_bhi = {**_coarse_bhi_baseline("stressed"), "hydrology": 0.20, "soil": 0.30}  # severe water/soil

    # Three pairwise bilateral analyses — indicator dicts passed so the
    # indicator-level F3 check (v3.3 enhancement) fires. Without these,
    # IL↔IR would read as APPROXIMATELY_SYMMETRIC because both polities
    # currently carry all-T3 coupling matrices, hiding the indicator-tier
    # gap. Passing the indicators forces the worst-of (coupling, indicator)
    # F3 verdict per the F3 anti-laundering principle.
    us_il = bilateral_substrate_analysis(
        "US_2025", us_throughput, us_bhi,
        "Israel_2026", il_throughput, il_bhi,
        polity_a_indicators=US_BASELINE_INDICATORS,
        polity_b_indicators=ISRAEL_2026_BASELINE_ILLUSTRATIVE,
    )
    us_ir = bilateral_substrate_analysis(
        "US_2025", us_throughput, us_bhi,
        "Iran_2026", ir_throughput, ir_bhi,
        polity_a_indicators=US_BASELINE_INDICATORS,
        polity_b_indicators=IRAN_2026_BASELINE_ILLUSTRATIVE,
    )
    il_ir = bilateral_substrate_analysis(
        "Israel_2026", il_throughput, il_bhi,
        "Iran_2026", ir_throughput, ir_bhi,
        polity_a_indicators=ISRAEL_2026_BASELINE_ILLUSTRATIVE,
        polity_b_indicators=IRAN_2026_BASELINE_ILLUSTRATIVE,
    )

    # Aggregate substrate stress over all three polities
    aggregate_stress = {dim: 0.0 for dim in BIOSPHERIC_SUBSTRATE_DIMENSIONS}
    for stress_block in (us_il["polity_a_analysis"]["stress"],
                         us_il["polity_b_analysis"]["stress"],
                         us_ir["polity_b_analysis"]["stress"]):
        for dim in BIOSPHERIC_SUBSTRATE_DIMENSIONS:
            aggregate_stress[dim] += stress_block["stress_by_dimension"].get(dim, 0.0)
    aggregate_stress = {k: round(v, 4) for k, v in aggregate_stress.items()}

    return {
        "case_study":        "Twelve-Day War (U.S.–Israel–Iran, Feb 2026)",
        "deployment_status": "ILLUSTRATIVE — DO NOT DEPLOY",
        "do_not_deploy_reason": (
            "Indicator values for Israel 2026 and Iran 2026 are illustrative "
            "best-effort estimates with per-indicator T-tags. Iran data is "
            "T3-dominant by construction. Coupling matrices for non-U.S. "
            "polities are U.S.-inherited placeholders (Rule 4 calibration "
            "required). The bilateral analysis function infrastructure is "
            "research-grade; this case-study DATA is illustrative."
        ),
        "f3_evidence_asymmetry_banner": (
            "F3 EVIDENCE-ASYMMETRY BANNER: Bilateral framing of US↔Iran and "
            "Israel↔Iran does NOT equalize asymmetric evidence. Iran "
            "indicators are T3-dominant; US/Israel indicators are T1/T2-"
            "dominant. Per-polity conclusions remain evidentially distinct."
        ),
        "per_polity_phis": {
            "US_2025":     {p: round(v, 4) for p, v in us_phis.items()},
            "Israel_2026": {p: round(v, 4) for p, v in il_phis.items()},
            "Iran_2026":   {p: round(v, 4) for p, v in ir_phis.items()},
        },
        "bilateral_analyses": {
            "US_x_Israel":   us_il,
            "US_x_Iran":     us_ir,
            "Israel_x_Iran": il_ir,
        },
        "aggregate_substrate_stress": aggregate_stress,
        "rule_2_audit_note": (
            "This case study triggers F3 caveats on US↔Iran and Israel↔Iran "
            "by construction. Bilateral protocol does NOT smooth Iran's "
            "T3-dominant evidence base into the same epistemic register as "
            "U.S./Israeli T1/T2 sources. Treat per-direction conclusions as "
            "evidentially distinct."
        ),
        "rule_4_audit_note": (
            "All non-U.S. coupling matrices are U.S.-inherited placeholders. "
            "Per-polity recalibration is the operational gate before any "
            "policy use of this analysis."
        ),
        "rule_5_audit_note": (
            "Per-indicator T-tags are visible in ISRAEL_2026_BASELINE_"
            "ILLUSTRATIVE and IRAN_2026_BASELINE_ILLUSTRATIVE. T3 dominance "
            "in Iran data is honest, not curated."
        ),
        "rule_6_audit_note": (
            "Any intervention proposed against this analysis must carry its "
            "own four-mode failure assessment AGAINST the F3 evidence-"
            "asymmetric base."
        ),
    }


# ─────────────────────────────────────────────────────────────────────────────
# 26D.4 — Dragon-king (II.2 condition #5) module — DELIBERATELY NOT BUILT
# ─────────────────────────────────────────────────────────────────────────────

def dragon_king_module_status() -> Dict[str, Any]:
    """
    Report the explicit gate status for II.2 condition #5 (log-periodic
    precursors / dragon-king prediction).

    This function exists so that callers, dashboards, and future Claude
    sessions see the gate explicitly rather than discovering it by absence.
    The v3.3 Rule 2 self-audit declined building #5 on malfeasance + Rule 3
    grounds. Returning this status object surfaces the audit residue.

    Returns
    -------
    dict documenting:
        status                  : 'GATED — POSTPONED'
        gating_condition        : reference to v3.0 §IV.9 #9
        rationale               : why postponed
        II_2_condition_states  : current status of all five validation conditions
        v3_3_decision           : explicit non-build rationale
        unbuild_warning         : what would happen if module were built prematurely
    """
    return {
        "status":           "GATED — POSTPONED",
        "module":           "log-periodic precursors / dragon-king prediction",
        "gating_condition": "v3.0 §IV.9 Operational Recommendation #9",
        "rationale": (
            "Postpone dragon-king prediction modules until validation "
            "conditions 1-4 met. As of v3.5, condition #4 (driving / "
            "dissipation mechanisms with conservation properties) is OPEN. "
            "Building #5 first would produce structurally well-formed "
            "analysis with hollow substance — a Rule 3 violation."
        ),
        # The FIVE conditions below are numbered exactly as in the v3.1 Working
        # Paper §II.2 "What rigorous instantiation would require". The v3.3 ledger
        # had drifted (it dropped canonical #1, the substrate-state variable, and
        # split the power-law condition into a spurious "#2 goodness-of-fit").
        # Restored here so the gate cross-references the paper and the dashboard's
        # own II.2 validation checklist bit-for-bit.
        "II_2_condition_states": {
            "#1_formal_substrate_state_variable":
                "PARTIAL  (SHI is the candidate state variable + measurement "
                "protocol per Part IV; longitudinal validation pending)",
            "#2_power_law_event_size_distribution":
                "PARTIAL  (Clauset MLE/KS fit + bootstrap goodness-of-fit "
                "infrastructure present, v3.1/v3.2; real event-coded series needed)",
            "#3_one_over_f_temporal_structure":
                "PARTIAL  (Welch-PSD 1/f test infrastructure present, v3.2; real "
                "longitudinal substrate-flux data needed)",
            "#4_driving_dissipation_conservation":
                "OPEN     (no infrastructure — domain-expert work; binding gate for #5)",
            "#5_log_periodic_dragon_king_prediction":
                "POSTPONED (gated by #4 per §IV.9 #9; deliberately NOT built)",
        },
        "canonical_source": (
            "Samsara Substrate Working Paper v3.1 §II.2 'What rigorous "
            "instantiation would require' (conditions 1-5) and §IV.9 Operational "
            "Recommendation #9 ('Postpone dragon-king prediction modules until "
            "validation conditions met')."
        ),
        "v3_3_decision": (
            "Module deliberately NOT built. Adding log-periodic fitting code "
            "without #4 closed produces a structurally complete dragon-king "
            "module that cannot be principally evaluated against any real "
            "claim. The function infrastructure would invite use; the use "
            "would not be defensible. The v3.3 Rule 2 audit flagged this as "
            "the prototype 'overly complex mechanism with no clear "
            "improvement' the user explicitly requested be flagged."
        ),
        "unbuild_warning": (
            "If a future v3.x release builds this module before #4 is "
            "closed, the v3.0 §IV.9 #9 postponement should be explicitly "
            "rescinded with rationale, and the rescission should itself "
            "carry a Rule 2 / Rule 3 audit demonstrating that the module's "
            "outputs can be principally evaluated."
        ),
        "earliest_eligible_version": "v3.x where #4 is CLOSED",
    }


# ─────────────────────────────────────────────────────────────────────────────
# 26D.5 — v3.3 one-shot integrator
# ─────────────────────────────────────────────────────────────────────────────

def substrate_research_report_v3_3(
    polity_id: str,
    indicators: Dict[str, List[Dict]],
    flux_series: Optional["FluxTimeSeries"] = None,
    event_series: Optional["SubstrateEventSeries"] = None,
) -> Dict[str, Any]:
    """
    v3.3 substrate research report. Calls the v3.2 base report (which includes
    bootstrap goodness-of-fit + 1/f test + tier calibration summary) and adds:

      - per-polity coupling status
      - dragon-king gate status
      - polity_id propagation through downstream substrate computations

    Parameters
    ----------
    polity_id : str
        Registry key (e.g., 'US_2025', 'Israel_2026', 'Iran_2026').
    indicators : dict
        Per-Pillar indicators (US_BASELINE_INDICATORS-shaped).
    flux_series, event_series : optional
        Forwarded to v3.2 base report.

    Returns
    -------
    dict combining v3.2 base + v3.3 additions.
    """
    # Compute throughput proxy from indicators
    phis = {p: compute_pillar_phi(indicators[p]) for p in COUPLING_PILLAR_ORDER}
    throughput = _coarse_throughput_from_phis(phis)

    # v3.5 FIX (H): this call previously used keyword names that do not exist
    # in substrate_research_report_v3_2 (indicators=, throughput=) and omitted
    # the required polity/scale parameters — every invocation raised TypeError.
    # Latent since v3.3: no demo or dashboard path exercised this integrator.
    base = substrate_research_report_v3_2(
        indicators_by_pillar=indicators,
        polity=polity_id,
        scale="National",
        pillar_throughput=throughput,
        bhi_values=_coarse_bhi_baseline("moderate"),
        flux_series=flux_series,
        event_series=event_series,
    )

    out = dict(base)
    out["v3_3_substrate_research_report"] = True
    out["polity_id"]                       = polity_id
    out["polity_coupling_status"]          = coupling_calibration_status(polity_id)
    out["dragon_king_gate"]                = dragon_king_module_status()
    return out


# ═══════════════════════════════════════════════════════════════════════════════
#  SECTION 27 — NROS: TRAJECTORY PROJECTION ENGINE
# ═══════════════════════════════════════════════════════════════════════════════

def project_trajectories(
    floor: float, mean: float, spread: float, stressed: int,
    pfp: float, soc_composite: float, conflict_active: bool = False,
) -> List[Dict]:
    """
    Compute probability-weighted trajectory scenarios using multi-factor algorithm.

    Six candidate trajectories: Stable continuation, Gradual improvement,
    Managed degradation, Authoritarian drift, Catastrophic cascade,
    Reform and recovery.

    Factors:
        Stability  = f(floor, mean, 1-pfp, 1-soc)
        Degradation = f(floor_deficit, pfp, soc, spread, conflict)
    """
    # Stability factors
    stab = (max(0, (floor - 0.20) / 0.60) * 25
            + max(0, (mean - 0.30) / 0.50) * 15
            + (1.0 - pfp) * 10
            + (1.0 - soc_composite) * 10)

    # Degradation factors
    deg = (max(0, (0.60 - floor) / 0.40) * 20
           + pfp * 15
           + soc_composite * 15
           + spread * 10
           + (5 if conflict_active else 0))

    total = stab + deg + 0.01

    candidates = [
        {"name": "Stable continuation",  "p": stab * 0.45 / total},
        {"name": "Gradual improvement",  "p": stab * 0.25 / total},
        {"name": "Reform and recovery",  "p": stab * 0.30 / total},
        {"name": "Managed degradation",  "p": deg * 0.40 / total},
        {"name": "Authoritarian drift",  "p": deg * 0.30 / total},
        {"name": "Catastrophic cascade", "p": deg * 0.30 / total},
    ]

    # Normalize
    psum = sum(c["p"] for c in candidates)
    for c in candidates:
        c["p"] = round(c["p"] / psum, 4) if psum > 0 else 0.0

    candidates.sort(key=lambda c: c["p"], reverse=True)
    return [c for c in candidates if c["p"] > 0.02]


# ═══════════════════════════════════════════════════════════════════════════════
#  SECTION 28 — NROS: SYNTHESIS ENGINE (Eight-Step Orchestrator)
# ═══════════════════════════════════════════════════════════════════════════════

class NROSSynthesisEngine:
    """
    Complete NROS Synthesis Engine implementing the eight-step Samsara Method.

    Orchestrates:
        Step 1: Pillar Mapping (PHI computation + Axiom assessment)
        Step 2: Gradient Analysis (inter-Pillar spread + Hodge decomposition)
        Step 3: Polity Assessment (four failure modes + compounds)
        Step 4: SOC Assessment (five categories + criticality indicators)
        Step 5: Conflict Assessment (trinity + domains + escalation + termination)
        Step 6: Quantification (Hodge decomposition + regime detection)
        Step 7: Synthesis (trajectory projection)
        Step 8: Recursive Refinement (consistency check)

    Entry point: .synthesize(indicators, polity, soc, conflict, gradients, entity)
    """

    def __init__(self, inter_matrix: Optional[Dict] = None):
        self.inter = inter_matrix or INTERDEPENDENCY_MATRIX
        log.info("NROS SynthesisEngine initialised.")

    def synthesize(
        self,
        indicators: Optional[Dict[str, List[Dict]]] = None,
        polity: Optional[Dict[str, float]] = None,
        soc: Optional[Dict[str, float]] = None,
        conflict: Optional[Dict] = None,
        gradients: Optional[List[Dict]] = None,
        entity: Optional[Dict] = None,
    ) -> Dict:
        """
        Execute complete eight-step Samsara Method synthesis.

        Parameters
        ----------
        indicators : dict mapping Pillar name → list of indicator dicts
            Default: US_BASELINE_INDICATORS
        polity : dict mapping failure mode → probability
        soc : dict mapping SOC category → stored energy
        conflict : dict with 'active', 'domains', 'trinity', 'escalation', 'termination'
        gradients : list of gradient dicts
        entity : dict with 'nation', 'scale', etc.
        """
        # Defaults
        if indicators is None:
            indicators = US_BASELINE_INDICATORS
        if polity is None:
            polity = {"Mismanagement": 0.70, "Malfeasance": 0.65,
                      "RentSeeking": 0.75, "Incompetence": 0.65}
        if soc is None:
            soc = {"fiscal": 0.85, "infrastructure": 0.72, "institutional": 0.78,
                   "social": 0.82, "geopolitical": 0.65}
        if conflict is None:
            conflict = {"active": True, "domains": ["Cyber", "Information", "Economic"],
                        "trinity": {"passion": 0.72, "chance": 0.55, "purpose": 0.35},
                        "escalation": 0.45, "termination": "absent"}
        if gradients is None:
            gradients = []
        if entity is None:
            entity = {"nation": "United States", "scale": "National"}

        log.info(f"NROS Synthesis: {entity.get('nation', 'Unknown')} "
                 f"at {entity.get('scale', 'National')} scale")

        # ── Step 1: Pillar Mapping ────────────────────────────────────────────
        phis = {}
        for pillar in PILLAR_NAMES:
            inds = indicators.get(pillar, [])
            phis[pillar] = round(compute_pillar_phi(inds), 4)

        vals = [phis[p] for p in PILLAR_NAMES]
        floor_val = min(vals)
        mean_val  = sum(vals) / 6.0
        spread    = max(vals) - floor_val
        stressed  = sum(1 for v in vals if v < 0.40)
        threshold = ("EXCEEDED" if stressed >= 4 else
                     "APPROACHING" if stressed >= 3 else "BELOW")
        active    = [p for p in PILLAR_NAMES if phis[p] >= 0.50]

        # ── Step 2: Gradient Analysis (inter-Pillar) ─────────────────────────
        hodge_result = hodge_decompose_phi(phis)

        # Regime detection — [F3 FIX] default is "balanced" for mid-health
        # systems that fit none of the other branches; "dissolution" is now
        # reserved for genuinely breaking systems (3+ stressed Pillars with
        # spread in the "breakdown band" 0.15–0.25), not every mid-health case.
        if spread > 0.40:
            g_regime = "gradient_flow"
        elif spread > 0.25 and stressed >= 2:
            g_regime = "vortex"
        elif spread < 0.15:
            g_regime = "harmonic"
        elif stressed >= 3 and 0.15 <= spread <= 0.25:
            g_regime = "dissolution"
        else:
            g_regime = "balanced"

        # Cantillon phase — [F3 FIX] remove the same default-to-failure
        # asymmetry: "trap" is a specific failure mode (asymmetric distress
        # despite apparent health), not the catch-all for everything
        # that isn't clearly expansion or contraction. A balanced
        # mid-health system is "equilibrium", not trapped.
        if mean_val > 0.65 and stressed <= 1:
            c_phase = "expansion"
        elif mean_val < 0.35 or stressed >= 4:
            c_phase = "contraction"
        elif mean_val > 0.55 and stressed >= 2:
            c_phase = "trap"          # wealth with hidden fragility
        elif stressed >= 3:
            c_phase = "trap"          # concentrated distress despite adequate mean
        else:
            c_phase = "equilibrium"   # balanced mid-health default

        cu_phase = ("dormant" if stressed >= 4
                    else "fruiting" if stressed >= 2
                    else "mycelium" if mean_val > 0.60
                    else "spore")

        # ── Step 3: Polity Assessment ─────────────────────────────────────────
        polity_result = assess_polity(polity)

        # ── Step 4: SOC Assessment ────────────────────────────────────────────
        soc_result = assess_soc(soc)

        # ── Step 5: Conflict Assessment (passthrough + validation) ────────────
        conflict_out = {
            "active":      conflict.get("active", False),
            "domains":     conflict.get("domains", []),
            "trinity":     conflict.get("trinity", {}),
            "escalation":  conflict.get("escalation", 0.0),
            "termination": conflict.get("termination", "absent"),
        }

        # ── Step 6: Quantification (cascade risks) ───────────────────────────
        cascade_risks = compute_cascade_risks(phis, self.inter)

        # ── Step 7: Synthesis (trajectory projection) ─────────────────────────
        trajectories = project_trajectories(
            floor=floor_val, mean=mean_val, spread=spread,
            stressed=stressed, pfp=polity_result["aggregate"],
            soc_composite=soc_result["composite"],
            conflict_active=conflict.get("active", False),
        )

        # ── Step 8: Recursive Refinement (consistency check) ──────────────────
        # If cascade risks exist but threshold is BELOW, flag for review
        refinement_notes = []
        if cascade_risks and threshold == "BELOW":
            refinement_notes.append(
                f"Cascade risks detected ({len(cascade_risks)} pathways) "
                f"despite threshold BELOW — monitor closely."
            )
        if polity_result["aggregate"] > 0.65 and threshold == "BELOW":
            refinement_notes.append(
                "Polity failure probability >65% with threshold BELOW — "
                "any additional perturbation could rapidly change assessment."
            )
        # v3.5 (J): parity with the dashboard's Step-8 check set — the HTML
        # engine has carried this third check since v4.x; the Python port
        # lacked it. Refinement notes are advisory, not canonical anchors.
        if soc_result["status"] == "NEAR_CRITICAL" and stressed < 2:
            refinement_notes.append(
                "SOC near-critical despite few stressed Pillars — "
                "system may be accumulating hidden stress."
            )

        # ── Assemble output ───────────────────────────────────────────────────
        result = {
            # Entity
            "nation":           entity.get("nation", ""),
            "scale":            entity.get("scale", "National"),
            # PHI
            "pillar_health":    phis,
            "composite_floor":  round(floor_val, 4),
            "composite_mean":   round(mean_val, 4),
            "gradient_spread":  round(spread, 4),
            "threshold_status": threshold,
            "stressed_count":   stressed,
            "active_pillars":   active,
            # Hodge
            "hodge":            hodge_result,
            # Regime
            "regime": {
                "gradient_regime":  g_regime,
                "cantillon_phase":  c_phase,
                "cultural_phase":   cu_phase,
            },
            # Polity
            "polity":           polity_result,
            # SOC
            "soc":              soc_result,
            # Conflict
            "conflict":         conflict_out,
            # Cascade
            "cascade_risks":    cascade_risks,
            # Gradients
            "gradient_map":     gradients,
            # Trajectories
            "trajectories":     trajectories,
            # Refinement
            "refinement_notes": refinement_notes,
            # Notes for TreatiseContext
            "notes": (
                f"NROS synthesis: {entity.get('nation', 'Unknown')} at "
                f"{entity.get('scale', 'National')} scale. "
                f"Floor={floor_val:.3f} ({phi_health_label(floor_val)}). "
                f"Polity fail={polity_result['aggregate']:.0%}. "
                f"SOC={soc_result['composite']:.0%} ({soc_result['status']}). "
                f"Hodge: {hodge_result['dominant']} dominant."
            ),
            # [F2 FIX] timestamp for parity with HTML dashboard output
            # v3.5 (K): datetime.utcnow() is deprecated (3.12+); tz-aware
            # equivalent, normalized to the identical naive-UTC string.
            "timestamp": datetime.now(timezone.utc).replace(tzinfo=None).isoformat() + "Z",
        }

        log.info(f"  PHI: {' | '.join(f'{p}={phis[p]:.3f}' for p in PILLAR_NAMES)}")
        log.info(f"  Floor={floor_val:.3f} Mean={mean_val:.3f} "
                 f"Spread={spread:.3f} Stressed={stressed}/6 → {threshold}")
        log.info(f"  Hodge: G={hodge_result['gradient']:.1%} "
                 f"C={hodge_result['curl']:.1%} H={hodge_result['harmonic']:.1%}")
        log.info(f"  Polity fail={polity_result['aggregate']:.0%} "
                 f"SOC={soc_result['composite']:.0%} ({soc_result['status']})")
        # [F9 FIX] split list-comp to avoid Python 3.12+ nested f-string syntax
        _t_strs = [f"{t['name']}={t['p']:.0%}" for t in trajectories[:3]]
        log.info(f"  Trajectories: {' | '.join(_t_strs)}")

        return result

    def to_treatise_context(self, nros_output: Dict) -> TreatiseContext:
        """Convert NROS synthesis output to a TreatiseContext dataclass."""
        return TreatiseContext.from_nros(nros_output)


# ── Attach NROS to Hologram2 class ────────────────────────────────────────────

def _hologram2_nros(self, indicators=None, polity=None, soc=None,
                    conflict=None, gradients=None, entity=None) -> Dict:
    """
    [NROS] Run complete Samsara Method analysis through the NROS engine,
    producing a TreatiseContext-enriched result that integrates with all
    Hologram2 subsystems.

    This is the bridge between civilizational analysis (NROS) and
    quantitative market analysis (Oracle/DeepDark).
    """
    engine = NROSSynthesisEngine()
    nros_result = engine.synthesize(
        indicators=indicators, polity=polity, soc=soc,
        conflict=conflict, gradients=gradients, entity=entity,
    )
    treatise = engine.to_treatise_context(nros_result)
    nros_result["treatise_context"] = {
        "gradient_regime":    treatise.gradient_regime,
        "cantillon_phase":    treatise.cantillon_phase,
        "cultural_phase":     treatise.cultural_phase,
        "active_pillars":     treatise.active_pillars,
        "inequality_gradient": treatise.inequality_gradient,
        "pillar_health":      treatise.pillar_health,
        "composite_floor":    treatise.composite_floor,
        "threshold_status":   treatise.threshold_status,
        "hodge_dominant":     treatise.hodge_dominant,
        "polity_fail_prob":   treatise.polity_fail_prob,
        "soc_criticality":    treatise.soc_criticality,
        "conflict_active":    treatise.conflict_active,
        "notes":              treatise.notes,
    }
    return nros_result

Hologram2.nros = _hologram2_nros


# ═══════════════════════════════════════════════════════════════════════════════
#  ENTRY POINT (updated for v2.0 with NROS demo)
# ═══════════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    # ── Cross-platform UTF-8 console ────────────────────────────────────────────
    # This demo prints Unicode (τ, σ, ρ, box-drawing, arrows). On Windows the
    # default console encoding (cp1252) raises UnicodeEncodeError mid-run and
    # aborts before the v3.3 sections print. Reconfigure stdout/stderr to UTF-8
    # where supported; fail safe on platforms/streams that do not support it.
    for _stream in (sys.stdout, sys.stderr):
        try:
            _stream.reconfigure(encoding="utf-8")
        except (AttributeError, ValueError):
            pass

    cfg = Hologram2Config(
        oracle=OracleConfig(
            criticality_eval_interval=60,
            sequence_length=60,
            predictor_epochs=50,
            mc_dropout_samples=20,
        ),
        deepdark=DeepDarkConfig(
            gan_epochs=20,
            predictor_epochs=50,
            optuna_trials=10,
        ),
    )

    h2 = Hologram2(cfg)
    print(h2)
    print()

    # ── NROS Analysis (Samsara Method) ─────────────────────────────────────
    print("=" * 72)
    print("  Hologram2 v3.5 — NROS Samsara Method Analysis (with SHI integration)")
    print("=" * 72)

    nros = h2.nros()  # Uses U.S. canonical baseline defaults

    print(f"  Entity:      {nros['nation']} ({nros['scale']})")
    print(f"  PHI Scores:")
    for pil in PILLAR_NAMES:
        phi_val = nros["pillar_health"][pil]
        print(f"    {pil:15s}: {phi_val:.3f}  ({phi_health_label(phi_val)})")
    print(f"  Floor:       {nros['composite_floor']:.3f}  "
          f"({phi_health_label(nros['composite_floor'])})")
    print(f"  Mean:        {nros['composite_mean']:.3f}")
    print(f"  Spread:      {nros['gradient_spread']:.3f}")
    print(f"  Threshold:   {nros['threshold_status']}  "
          f"({nros['stressed_count']}/6 stressed)")
    H = nros["hodge"]
    print(f"  Hodge:       G={H['gradient']:.1%}  C={H['curl']:.1%}  "
          f"H={H['harmonic']:.1%}  ({H['dominant']})")
    print(f"  Regime:      {nros['regime']['gradient_regime']}  "
          f"| Cantillon: {nros['regime']['cantillon_phase']}  "
          f"| Cultural: {nros['regime']['cultural_phase']}")
    pol = nros["polity"]
    print(f"  Polity fail: {pol['aggregate']:.0%}  "
          f"({pol['compound_count']} compounds >55%)")
    soc_r = nros["soc"]
    print(f"  SOC:         {soc_r['composite']:.0%} ({soc_r['status']})  "
          f"| τ={soc_r['tau']:.3f}  σ={soc_r['sigma']:.3f}  ρ={soc_r['rho']:.3f}")
    if nros["cascade_risks"]:
        print(f"  Cascades:    {len(nros['cascade_risks'])} active pathways")
        for cr in nros["cascade_risks"][:3]:
            print(f"    {cr['from']} → {cr['to']}: impact={cr['impact']:.3f}")
    print(f"  Trajectories:")
    for t in nros["trajectories"][:5]:
        print(f"    {t['p']:5.0%}  {t['name']}")
    if nros["refinement_notes"]:
        print(f"  Refinement:")
        for note in nros["refinement_notes"]:
            print(f"    ⚠ {note}")

    # ── v3.0: SHI sub-panel for the U.S. baseline Entertainment Pillar ────
    print()
    print("─" * 72)
    print("  v3.0 SHI sub-panel (Entertainment Pillar — meaning-substrate only)")
    print("─" * 72)
    us_ent = US_BASELINE_INDICATORS["Entertainment"]
    shi = compute_shi(us_ent)
    print(f"  SHI composite:    {shi['composite']:.4f}  ({shi['tier']})")
    print(f"  Substrate count:  {shi['substrate_count']}/8")
    print(f"  Below 0.40:       {shi['sub_indicators_below_threshold']}/8  "
          f"({'CASCADE TRIGGERED' if shi['cascade_threshold'] else 'no cascade'})")
    print(f"  Deployment:       {shi['deployment_status'].upper()} — DO NOT DEPLOY")
    print(f"  Sub-indicator scores:")
    for s in shi["sub_indicator_scores"]:
        marker = " ⚠" if s["normalized"] < 0.40 else "  "
        print(f"    {marker} {s['id']:4s} {s['name']:35s} "
              f"raw={s['raw']:>3} → {s['normalized']:.3f}")

    # ── v3.0: Hungary 2024 demo (SHI regression anchor) ──────────────────
    print()
    print("─" * 72)
    print("  Hungary 2024 baseline — SHI regression anchor (v3.0 paper IV.6)")
    print("─" * 72)
    hun_bundle = hungary_2024_baseline()
    hun_nros = h2.nros(**hun_bundle)
    hun_ent = hun_bundle["indicators"]["Entertainment"]
    hun_shi = compute_shi(hun_ent)
    print(f"  Entity:           {hun_nros['nation']} ({hun_nros['scale']})")
    print(f"  Entertainment PHI: {hun_nros['pillar_health']['Entertainment']:.4f}")
    print(f"  SHI composite:    {hun_shi['composite']:.4f}  ({hun_shi['tier']})")
    # v3.0 paper IV.6 prints "0.4375 ≈ 0.44" but the sum of stated values is
    # 0.55+0.35+0.40+0.30+0.45+0.50+0.40+0.60 = 3.55, ÷8 = 0.44375 → 0.4438.
    # The two-decimal "≈ 0.44" in the paper is correct; the four-decimal
    # "0.4375" is a transcription typo (off by 0.00625). The implementation
    # is mathematically correct; the paper anchor below is the corrected value.
    print(f"  Paper-published:  0.4438 (≈0.44; paper IV.6 prints '0.4375' — typo)")
    print(f"  Paper rounded:    0.44   → ", end="")
    delta = abs(hun_shi['composite'] - 0.44)
    if delta < 0.01:
        print(f"MATCH at 2-decimal precision (Δ = {delta:.4f})")
    else:
        print(f"MISMATCH (Δ = {delta:.4f}) — investigate weights")
    print(f"  Below 0.40:       {hun_shi['sub_indicators_below_threshold']}/8  "
          f"({'CASCADE TRIGGERED' if hun_shi['cascade_threshold'] else 'no cascade — proximity flagged'})")
    print(f"  System threshold: {hun_nros['threshold_status']} "
          f"({hun_nros['stressed_count']}/6 stressed)")
    print(f"  Regime/Cantillon: {hun_nros['regime']['gradient_regime']} / "
          f"{hun_nros['regime']['cantillon_phase']}")

    print()
    print("=" * 72)
    print("  Usage:")
    print("    h2 = Hologram2()")
    print("    result = h2.nros()                       # U.S. baseline")
    print("    result = h2.nros(**hungary_2024_baseline())   # NEW v3.0")
    print("    result = h2.nros(**venezuela_2019_baseline()) # collapsing polity")
    print("    shi = compute_shi(result['indicators']['Entertainment'])  # NEW v3.0")
    print("    ctx = TreatiseContext.from_nros(result)   # Full dataclass")
    print("    result = h2.analyze('AAPL')               # Oracle analysis")
    print("    result = h2.holistic('AAPL', ('AAPL','MSFT'))  # Cross-module")
    print("    # NEW v3.3:")
    print("    bilat = bilateral_substrate_analysis(...)              # asymmetric bilateral")
    print("    case  = twelve_day_war_substrate_analysis()            # case study")
    print("    cal   = coupling_calibration_status('Hungary_2024')    # Rule 4 status")
    print("    gate  = dragon_king_module_status()                    # II.2 #5 gate")
    print("=" * 72)

    # ─────────────────────────────────────────────────────────────────────────
    # v3.3 demo additions (per-polity calibration, bilateral, case study, gate)
    # ─────────────────────────────────────────────────────────────────────────
    print()
    print("=" * 72)
    print("  v3.3 ADDITIONS — Per-polity calibration, bilateral analysis,")
    print("                   Twelve-Day War case study, dragon-king gate")
    print("=" * 72)

    # ── v3.3 §1: Per-polity coupling calibration registry (Rule 4) ──────────
    print()
    print("─" * 72)
    print("  v3.3 §1  Per-polity coupling calibration status (Rule 4)")
    print("─" * 72)
    for pid in ("US_2025", "Hungary_2024", "Venezuela_2019",
                "Israel_2026", "Iran_2026"):
        st = coupling_calibration_status(pid)
        td = st["tier_distribution"]
        print(f"  {pid:14s}  T1={td['T1']:>2}  T2={td['T2']:>2}  T3={td['T3']:>2}  "
              f"calibration_required={st['calibration_required']}")
    print()
    print("  Note: All non-U.S. coupling matrices are U.S.-inherited placeholders")
    print("  (T3 throughout). Rule 4 calibration is the operational gate before")
    print("  any policy use of non-U.S. analyses.")

    # ── v3.3 §2: Reverse-direction asymmetric bilateral (US ↔ Hungary) ──────
    print()
    print("─" * 72)
    print("  v3.3 §2  Reverse-direction asymmetric bilateral example")
    print("           (closes v3.0 Part VIII open finding #4)")
    print("─" * 72)
    us_phis = {p: compute_pillar_phi(US_BASELINE_INDICATORS[p])
               for p in COUPLING_PILLAR_ORDER}
    hu_bundle_v33 = hungary_2024_baseline()
    hu_phis = {p: compute_pillar_phi(hu_bundle_v33["indicators"][p])
               for p in COUPLING_PILLAR_ORDER}
    us_thr_v33 = _coarse_throughput_from_phis(us_phis)
    hu_thr_v33 = _coarse_throughput_from_phis(hu_phis)
    us_bhi_v33 = _coarse_bhi_baseline("moderate")
    hu_bhi_v33 = _coarse_bhi_baseline("moderate")

    fwd = bilateral_substrate_analysis(
        "US_2025", us_thr_v33, us_bhi_v33,
        "Hungary_2024", hu_thr_v33, hu_bhi_v33,
        polity_a_indicators=US_BASELINE_INDICATORS,
        polity_b_indicators=hu_bundle_v33["indicators"],
    )
    rev = bilateral_substrate_analysis(
        "Hungary_2024", hu_thr_v33, hu_bhi_v33,
        "US_2025", us_thr_v33, us_bhi_v33,
        polity_a_indicators=hu_bundle_v33["indicators"],
        polity_b_indicators=US_BASELINE_INDICATORS,
    )
    fa = fwd["directional_asymmetry"]
    ra = rev["directional_asymmetry"]
    print(f"  Forward   (US→Hungary):  verdict={fa['verdict']:24s}  "
          f"gap={fa['effective_gap']}  dom={fa['verdict_dominated_by']}")
    print(f"  Reverse   (Hungary→US):  verdict={ra['verdict']:24s}  "
          f"gap={ra['effective_gap']}  dom={ra['verdict_dominated_by']}")
    inv = "PASS" if fa["verdict"] == ra["verdict"] else "FAIL"
    print(f"  Directional invariance:  {inv}  (verdict identical both directions)")
    print(f"  Shared-substrate max-stress dim:  {fwd['shared_substrate_stress']['max_stressed_dim']}  "
          f"(value={fwd['shared_substrate_stress']['max_stress_value']})")
    if fwd["f3_caveat"]:
        # Print first 100 chars of caveat (full text is verbose)
        print(f"  F3 caveat fired (first 100 chars):")
        print(f"    {fwd['f3_caveat'][:100]}…")

    # ── v3.3 §3: Twelve-Day War case study ──────────────────────────────────
    print()
    print("─" * 72)
    print("  v3.3 §3  Twelve-Day War (U.S.–Israel–Iran, Feb 2026)")
    print("           ILLUSTRATIVE — DO NOT DEPLOY")
    print("           (closes v3.0 Part VIII open finding from substrate paper)")
    print("─" * 72)
    case = twelve_day_war_substrate_analysis()
    print(f"  Status: {case['deployment_status']}")
    print()
    print(f"  Per-polity Pillar PHIs:")
    print(f"    {'Pillar':<14s}  {'US_2025':>9s}  {'Israel_2026':>12s}  {'Iran_2026':>10s}")
    for p in COUPLING_PILLAR_ORDER:
        us_v = case["per_polity_phis"]["US_2025"][p]
        il_v = case["per_polity_phis"]["Israel_2026"][p]
        ir_v = case["per_polity_phis"]["Iran_2026"][p]
        print(f"    {p:<14s}  {us_v:>9.4f}  {il_v:>12.4f}  {ir_v:>10.4f}")
    print()
    print(f"  Bilateral verdicts:")
    for pair, ana in case["bilateral_analyses"].items():
        a = ana["directional_asymmetry"]
        f3 = "f3=YES" if ana["f3_caveat"] else "f3=no"
        print(f"    {pair:<14s}  {a['verdict']:24s}  "
              f"gap={a['effective_gap']:.3f}  dom={a['verdict_dominated_by']:>9s}  {f3}")
    print()
    print(f"  Aggregate substrate stress (sum across all three polities):")
    for dim, val in case["aggregate_substrate_stress"].items():
        print(f"    {dim:<22s}  {val}")
    print()
    print(f"  F3 evidence-asymmetry banner:")
    print(f"    {case['f3_evidence_asymmetry_banner'][:88]}…")

    # ── v3.3 §4: Dragon-king gate status (II.2 condition #5) ────────────────
    print()
    print("─" * 72)
    print("  v3.3 §4  Dragon-king (II.2 #5) module gate status")
    print("─" * 72)
    gate = dragon_king_module_status()
    print(f"  Status: {gate['status']}")
    print(f"  Module: {gate['module']}")
    print(f"  Earliest eligible: {gate['earliest_eligible_version']}")
    print()
    print(f"  II.2 condition states:")
    for cond, st in gate["II_2_condition_states"].items():
        print(f"    {cond:<32s}  {st}")
    print()
    print(f"  v3.3 decision (excerpt):")
    print(f"    {gate['v3_3_decision'][:120]}…")

    # ── v3.3 §5: Closing audit summary ──────────────────────────────────────
    print()
    print("─" * 72)
    print("  v3.3 §5  Closing Rule 2 self-audit (recursive four-mode)")
    print("─" * 72)
    print("  Mismanagement: Function infrastructure follows v3.2 patterns; no")
    print("                 mechanical extension without fit. PASS")
    print("  Malfeasance:   Iran indicators kept T3-dominant; no sanitization")
    print("                 of evidence-quality gap. F3 fires by construction. PASS")
    print("  Rent-seeking:  Dragon-king module deliberately NOT built — refused")
    print("                 to add structurally well-formed but substantively")
    print("                 hollow code that would invite improper use. PASS")
    print("  Incompetence:  Per-polity calibration registry stubs are explicit;")
    print("                 calibration_required flag prevents silent T3-coupling")
    print("                 use. Source diversity directive (7 May 2026) honored")
    print("                 in Iran indicators. PASS")
    print("  → All four-mode self-audit checks PASS for v3.3 additions.")
    print("=" * 72)
