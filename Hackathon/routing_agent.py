from typing import List

class RoutingAgent:
    def __init__(self):
        self.routing_rules = {
            "technical_support": "Tech Team",
            "refund": "Billing Team",
            "billing_issue": "Billing Team",
            "escalate": "Management",
            "follow_up": "Support Team"
        }

    def route(self, actions: List[str]) -> str:
        team_priority = [
            "escalate",
            "technical_support",
            "refund",
            "billing_issue",
            "follow_up"
        ]

        for action in team_priority:
            if action in actions:
                return self.routing_rules.get(action, "Support Team")

        return "Support Team"  # Default fallback


if __name__ == "__main__":
    actions = ["refund", "technical_support"]
    agent = RoutingAgent()
    print("Assigned Team:", agent.route(actions))
