# time_estimator_agent.py

from typing import List

class TimeEstimatorAgent:
    def __init__(self):
        # Average time in hours for different actions
        self.time_estimates = {
            "escalate": 48,
            "technical_support": 36,
            "refund": 24,
            "billing_issue": 20,
            "follow_up": 12
        }

    def estimate_time(self, actions: List[str], summary: str) -> int:
        base_time = 8  # Default base time in hours
        total = base_time

        for action in actions:
            total += self.time_estimates.get(action, 0)

        # Adjust based on length of summary (longer might mean more complexity)
        word_count = len(summary.split())
        if word_count > 50:
            total += 12
        elif word_count > 30:
            total += 6

        return total


if __name__ == "__main__":
    actions = ["refund", "technical_support"]
    summary = "Customer reported a technical issue with the application crashing and also requested a refund for double billing."
    agent = TimeEstimatorAgent()
    print("Estimated Resolution Time (hrs):", agent.estimate_time(actions, summary))