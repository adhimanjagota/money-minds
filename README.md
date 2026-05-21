# Money Minds — Personal Finance Decision Engine

A rule-based decision engine that processes user financial events, scores financial health in real time, and delivers personalized recommendations.

Built with Python — no external dependencies required.

---

## What it does

- Ingests financial events (expenses, income, savings) and tracks spending per category
- Scores financial health (0–100) based on rule-based logic — penalties for overspending, rewards for saving
- Detects budget limit violations across 6 spending categories
- Generates personalized, actionable recommendations based on individual patterns
- Produces a full financial health report per user

---

## Demo output

```
=== Money Minds Report: Alex Johnson ===
Financial Health Score: 67/100
Monthly Income:         $4,000.00
Savings Goal:           $800.00

--- Spending Summary ---
  entertainment    $500.00  (12.5%)
  food             $820.00  (20.5%)
  rent           $1,200.00  (30.0%)
  savings          $200.00  (5.0%)
  shopping         $430.00  (10.8%)
  transport        $300.00  (7.5%)

--- Alerts ---
  ! High food spend: $820.00 (limit $600.00)
  ! High entertainment spend: $500.00 (limit $400.00)
  ! High shopping spend: $430.00 (limit $400.00)

--- Recommendations ---
  > Reduce food spending — currently 20.5% of income (recommended max 15%)
  > Reduce entertainment spending — currently 12.5% of income (recommended max 10%)
  > Your savings rate is 14.0% — aim for at least 20%
  > Moderate score — focus on reducing your top overspend category.
```

---

## How to run

```bash
git clone https://github.com/adhimanjagota/money-minds.git
cd money-minds
python main.py
```

No pip installs needed — pure Python 3.

---

## Project structure

```
money-minds/
├── engine.py    # Core decision engine — event processing, scoring, recommendations
├── main.py      # Demo script with sample user and events
└── README.md
```

---

## Key design decisions

- **Dataclasses** for clean, typed data models (`UserProfile`, `FinancialEvent`)
- **Configurable rule tables** — category limits and score weights are defined as class constants, easy to extend
- **Separation of concerns** — event processing, scoring, and report generation are independent methods
- **Edge-case handling** — score is clamped between 0–100, zero-division protected

---

## Tech stack

- Python 3.8+
- Standard library only (`dataclasses`, `datetime`, `typing`)

---

## Author

Adhiman Jagota — Data Science & Applied Math @ University of Washington Seattle  
adhimanj@uw.edu
