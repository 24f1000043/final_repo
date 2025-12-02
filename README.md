# Equipment Efficiency Rate — 2024 Quarterly Analysis

**Author / Contact:** 24f1000043@ds.study.iitm.ac.in

## Summary
Quarterly equipment efficiency rates for 2024:
- Q1: 69.28
- Q2: 73.52
- Q3: 80.54
- Q4: 75.51

**Computed average (2024)**: **74.71**

> (Average calculation: (69.28 + 73.52 + 80.54 + 75.51) / 4 = 74.7125 → rounded to 74.71)

**Industry target:** 90

## Key findings
1. The plant's average efficiency (74.71) is 15.29 percentage points below the industry target of 90.
2. Q3 shows a temporary improvement (80.54) but the value falls back in Q4 — suggesting transient fixes or seasonal effects rather than systemic improvement.
3. Overall trend shows volatility; long-term step-ups are required rather than ad-hoc fixes.

## Business implications
- Sustained under-performance implies higher operating cost, increased downtime and maintenance spend.
- At current efficiency, the company risks lower throughput, missed delivery targets, and higher per-unit cost.

## Recommendation (summary)
**Implement a predictive maintenance program** with phased rollout:
1. Pilot on 5 critical machines (3 months) using vibration + temperature sensors.
2. Build a simple anomaly detection model (historical sensor vs. downtime) — use alerts to schedule maintenance.
3. Track KPIs: Uptime %, Mean Time Between Failures (MTBF), Mean Time To Repair (MTTR), Maintenance cost per operating hour.
4. Expand to full plant after pilot if MTBF improves by ≥25% and unscheduled downtime reduces by ≥30%.

## What’s included in this PR
- `analysis.py` : script that computes the average and saves `figures/efficiency_trend.png`.
- `figures/efficiency_trend.png` : visualization of quarterly trend vs. benchmark.
- This `README.md` : contains the data story, findings, and recommendations.
