from google.adk.agents import SequentialAgent
from google.adk.models.google_llm import Gemini
from agents.marketplace import marketplace_classifier
from agents.reward_calculator import reward_calculator_agent
best_card_agent = SequentialAgent(
    name="best_card",
    sub_agents=[marketplace_classifier, reward_calculator_agent],
)