# AI-Driven Customer Support System

An intelligent, multi-agent AI system designed to automate and optimize customer support operations. It processes incoming customer queries through five specialized agents to deliver faster, more consistent, and cost-effective support.

---

##  Features
- Summarizes long customer queries into concise summaries
- Extracts key action items (like follow-ups, escalations)
- Recommends solutions using historical ticket data
- Automatically routes queries to the right team or department
- Estimates resolution time based on past cases

---

##  AI Agents
1. **Summarizer Agent** – Generates a summary of the customer’s message  
2. **Action Extractor Agent** – Identifies key actions required  
3. **Recommendation Agent** – Suggests resolutions using vector similarity (FAISS)  
4. **Routing Agent** – Determines the best department/team to handle the issue  
5. **Time Estimator Agent** – Predicts how long it will take to resolve the issue

---

##  Tech Stack
- **Python** – Core language  
- **FastAPI** – Backend framework for API development  
- **Transformers (MiniLM)** – For summarization and action extraction  
- **FAISS + Sentence Transformers** – For semantic search in recommendations  
- **Uvicorn** – ASGI server for running the app  
- **Pydantic** – Data validation

---

##  Project Structure
├── agents │ ├── summarizer_agent.py │ ├── action_extractor_agent.py │ ├── recommendation_agent.py │ ├── routing_agent.py │ └── time_estimator_agent.py ├── backend_main.py ├── requirements.txt └── README.md


---

##  API Endpoint
### POST `/process_ticket`
**Request:**
```json
{
  "message": "My internet is not working since yesterday and I need urgent help."
}

##Response:

{
  "summary": "Customer reports internet issues since yesterday.",
  "actions": ["urgent help"],
  "recommendations": ["Restart router", "Check outage in the area"],
  "route": "Technical Support",
  "estimated_resolution_time": "2 hours"
}

##How to Run
Clone the repository

Install dependencies: pip install -r requirements.txt

Run the backend: uvicorn backend_main:app --reload

Access API at: http://127.0.0.1:8000

##Target Audience
Enterprises with large support teams

E-commerce platforms

SaaS and telecom companies

Support outsourcing firms

##Future Improvements
Build a frontend dashboard

Integrate with real-world CRM tools (e.g., Zendesk)

Add analytics and feedback loop

##License
This project is built for educational and demonstration purposes as part of a hackathon. Feel free to build upon it!


---

If you still want a downloadable file, I can also email it or use another method—just let me know what works best for you! &#8203;:contentReference[oaicite:0]{index=0}&#8203;

