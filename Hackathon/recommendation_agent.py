# recommendation_agent.py

from sentence_transformers import SentenceTransformer, util
import faiss
import numpy as np
import json

class RecommendationAgent:
    def __init__(self):
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        self.index = faiss.IndexFlatL2(384)  # Vector dimension for MiniLM is 384
        self.tickets = []  # Store original tickets
        self.embeddings = []  # Store corresponding embeddings

    def load_historical_tickets(self, ticket_data):
        """
        ticket_data: List of dicts with keys: 'query' and 'resolution'
        """
        self.tickets = ticket_data
        texts = [ticket['query'] for ticket in ticket_data]
        self.embeddings = self.model.encode(texts, convert_to_numpy=True)
        self.index.add(np.array(self.embeddings))

    def recommend(self, query, top_k=3):
        query_vec = self.model.encode([query], convert_to_numpy=True)
        D, I = self.index.search(query_vec, top_k)

        recommendations = []
        for i in I[0]:
            recommendations.append(self.tickets[i]['resolution'])
        return recommendations


if __name__ == "__main__":
    # Sample historical ticket dataset
    historical_tickets = [
        {"query": "I was charged twice for my subscription.", "resolution": "Refunded extra charge and updated billing system."},
        {"query": "App crashes every time I open it.", "resolution": "Advised user to reinstall app and clear cache."},
        {"query": "I want to speak to a supervisor.", "resolution": "Escalated the ticket to the support manager."},
    ]

    query = "The app isn’t working properly and keeps crashing."

    agent = RecommendationAgent()
    agent.load_historical_tickets(historical_tickets)
    print("Recommendations:")
    for rec in agent.recommend(query):
        print("-", rec)
