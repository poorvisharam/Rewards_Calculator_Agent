from google.adk.agents import SequentialAgent
from marketplace import marketplace_classifier
from reward_calculator import reward_calculator_agent

best_card_agent = SequentialAgent(
    name="best_card",
    sub_agents=[marketplace_classifier, reward_calculator_agent],
)