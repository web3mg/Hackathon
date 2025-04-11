# action_extractor_agent.py

import re
from typing import List

class ActionExtractorAgent:
    def __init__(self):
        # Define basic keyword-action mapping
        self.action_keywords = {
            "refund": ["refund", "money back", "charged twice", "double charge"],
            "technical_support": ["not working", "issue", "problem", "error", "bug"],
            "billing_issue": ["billing", "invoice", "charged", "payment error"],
            "escalate": ["manager", "supervisor", "escalate", "complaint"],
            "follow_up": ["follow up", "get back", "respond later"]
        }

    def extract_actions(self, text: str) -> List[str]:
        actions_found = set()
        text_lower = text.lower()

        for action, keywords in self.action_keywords.items():
            for keyword in keywords:
                if re.search(rf"\\b{re.escape(keyword)}\\b", text_lower):
                    actions_found.add(action)
                    break  # Avoid duplicates

        return list(actions_found)


if __name__ == "__main__":
    # Example test
    text = (
        "I was charged twice and the system is giving an error. Please refund the extra amount or escalate the issue."
    )

    agent = ActionExtractorAgent()
    print("Actions Extracted:", agent.extract_actions(text))
