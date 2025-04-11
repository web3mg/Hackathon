from transformers import pipeline

class SummarizerAgent:
    def __init__(self, model_name="facebook/bart-large-cnn"):
        self.summarizer = pipeline("summarization", model=model_name)

    def summarize(self, text):
        if len(text.split()) < 20:
            return text  # Not enough content to summarize

        summary = self.summarizer(text, max_length=100, min_length=30, do_sample=False)
        return summary[0]['summary_text']


if __name__ == "__main__":
    # Example test
    text = (
        "Hello, I am facing issues with my billing. I was charged twice for the same service, "
        "and I need someone to look into it urgently. I also tried calling support, but the call got disconnected. "
        "Please help me with a refund or clarification on this."
    )

    agent = SummarizerAgent()
    print("Summary:\n", agent.summarize(text))
