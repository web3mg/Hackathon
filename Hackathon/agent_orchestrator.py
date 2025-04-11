# agent_orchestrator.py

from summarizer_agent import SummarizerAgent
from action_extractor_agent import ActionExtractorAgent
from recommendation_agent import RecommendationAgent
from routing_agent import RoutingAgent
from time_estimator_agent import TimeEstimatorAgent

# Initialize agents
summarizer = SummarizerAgent()
action_extractor = ActionExtractorAgent()
recommender = RecommendationAgent()
routing = RoutingAgent()
time_estimator = TimeEstimatorAgent()

# Load historical tickets (can be replaced by DB in real app)
historical_data = [
    {"query": "Charged twice for my subscription", "resolution": "Refund issued and billing fixed."},
    {"query": "App crashes when opening", "resolution": "Suggested reinstalling and clearing cache."},
    {"query": "Want to speak to supervisor", "resolution": "Escalated to support lead."},
]
recommender.load_historical_tickets(historical_data)

def process_ticket(customer_query: str) -> dict:
    summary = summarizer.summarize(customer_query)
    actions = action_extractor.extract_actions(customer_query)
    recommendations = recommender.recommend(summary)
    assigned_team = routing.route(actions)
    estimated_time = time_estimator.estimate_time(actions, summary)

    return {
        "summary": summary,
        "actions": actions,
        "recommendations": recommendations,
        "assigned_team": assigned_team,
        "estimated_time_hours": estimated_time
    }

if __name__ == "__main__":
    query = (
        "Hello, I was double charged on my card and now the app is not even opening. Please fix this quickly or escalate."
    )
    result = process_ticket(query)
    for key, value in result.items():
        print(f"{key}: {value}\n")