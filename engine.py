"""
Money Minds — Personal Finance Decision Engine
Processes user financial events and generates personalized recommendations.
"""

import json
from dataclasses import dataclass, field
from typing import List, Dict
from datetime import datetime


@dataclass
class FinancialEvent:
    category: str        # e.g. "food", "rent", "income", "entertainment"
    amount: float
    event_type: str      # "expense" or "income"
    timestamp: str = field(default_factory=lambda: datetime.now().strftime("%Y-%m-%d"))


@dataclass
class UserProfile:
    name: str
    monthly_income: float
    savings_goal: float
    events: List[FinancialEvent] = field(default_factory=list)
    score: int = 100


class DecisionEngine:
    """
    Rule-based decision engine that scores user financial behavior
    and generates personalized recommendations.
    """

    CATEGORY_LIMITS = {
        "food":          0.15,   # max 15% of income
        "entertainment": 0.10,
        "shopping":      0.10,
        "transport":     0.10,
        "rent":          0.35,
        "utilities":     0.10,
    }

    SCORE_PENALTIES = {
        "food":          8,
        "entertainment": 10,
        "shopping":      10,
        "transport":     5,
    }

    SCORE_REWARDS = {
        "savings":       15,
        "investment":    20,
    }

    def __init__(self, profile: UserProfile):
        self.profile = profile
        self.recommendations: List[str] = []
        self.alerts: List[str] = []

    def process_event(self, event: FinancialEvent):
        """Process a single financial event and update score."""
        self.profile.events.append(event)

        if event.event_type == "expense":
            limit = self.CATEGORY_LIMITS.get(event.category)
            if limit:
                allowed = self.profile.monthly_income * limit
                if event.amount > allowed:
                    penalty = self.SCORE_PENALTIES.get(event.category, 5)
                    self.profile.score = max(0, self.profile.score - penalty)
                    self.alerts.append(
                        f"High {event.category} spend: ${event.amount:.2f} "
                        f"(limit ${allowed:.2f})"
                    )

        elif event.event_type == "income":
            if event.category in ("savings", "investment"):
                reward = self.SCORE_REWARDS.get(event.category, 10)
                self.profile.score = min(100, self.profile.score + reward)

    def process_bulk(self, events: List[FinancialEvent]):
        """Process multiple events."""
        for event in events:
            self.process_event(event)

    def get_spending_summary(self) -> Dict[str, float]:
        """Return total spending per category."""
        summary: Dict[str, float] = {}
        for e in self.profile.events:
            if e.event_type == "expense":
                summary[e.category] = summary.get(e.category, 0) + e.amount
        return summary

    def generate_recommendations(self) -> List[str]:
        """Generate personalized recommendations based on spending patterns."""
        self.recommendations = []
        summary = self.get_spending_summary()
        income = self.profile.monthly_income

        for category, total in summary.items():
            limit = self.CATEGORY_LIMITS.get(category)
            if limit and total > income * limit:
                pct = (total / income) * 100
                self.recommendations.append(
                    f"Reduce {category} spending — currently {pct:.1f}% of income "
                    f"(recommended max {limit*100:.0f}%)"
                )

        total_expenses = sum(summary.values())
        savings_rate = (income - total_expenses) / income if income > 0 else 0
        if savings_rate < 0.20:
            self.recommendations.append(
                f"Your savings rate is {savings_rate*100:.1f}% — aim for at least 20%"
            )

        if self.profile.score >= 80:
            self.recommendations.append(
                "Great financial health! Consider investing surplus in an index fund."
            )
        elif self.profile.score >= 60:
            self.recommendations.append(
                "Moderate score — focus on reducing your top overspend category."
            )
        else:
            self.recommendations.append(
                "Score needs attention — start by tracking every expense this week."
            )

        return self.recommendations

    def report(self) -> str:
        """Generate a full text report."""
        self.generate_recommendations()
        summary = self.get_spending_summary()
        lines = [
            f"=== Money Minds Report: {self.profile.name} ===",
            f"Financial Health Score: {self.profile.score}/100",
            f"Monthly Income:         ${self.profile.monthly_income:,.2f}",
            f"Savings Goal:           ${self.profile.savings_goal:,.2f}",
            "",
            "--- Spending Summary ---",
        ]
        for cat, total in sorted(summary.items()):
            pct = (total / self.profile.monthly_income) * 100
            lines.append(f"  {cat:<16} ${total:>8.2f}  ({pct:.1f}%)")

        if self.alerts:
            lines += ["", "--- Alerts ---"]
            for a in self.alerts:
                lines.append(f"  ! {a}")

        lines += ["", "--- Recommendations ---"]
        for r in self.recommendations:
            lines.append(f"  > {r}")

        return "\n".join(lines)
