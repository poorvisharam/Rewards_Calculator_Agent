from google.adk.agents import Agent
from google.adk.models.google_llm import Gemini
from google.adk.tools.function_tool import FunctionTool
from models.best_card import BestCardOutput
from tools.user_benefits import get_user_benefits


# class BestCardInputs(BaseModel):
#     purchase_reward_category: str
#     benefits_user_has: list[Benefits]
#     amount: int = None

reward_calculator_agent = Agent(
    name="reward_calculator_agent",
    model=Gemini(
        model="gemini-2.5-flash-lite",
    ),
    description="That displays all inputs",
    instruction="""
You are a rewards calculator agent.
You will be returing the highest benefit card name to use for this purchase.
You are given:
    A. User ID
    B. User purchasing sentence (eg."I like to buy banana from HEB for $5)
    C. Amount (optional)
Your Tasks:
    1. call get_user_benefits() by passing given user ID as parameter
        1A.If User ID is not given --> Ask for User ID.
    2. use {classified_marketplace_reward} for mapping the reward category.
        2A. If the user doesnot have matching category benefits --> calculate rewards based on "other" category
    3. You calculate the rewards based on the user benefits. (points = amount x reward value)
        3A. Use rewards as it is, and not as percentage for point calculation
    4. Based on the rewards, return the best card as your recommendation

Please explain how you came up with the number
Verify again for calculated points
Show only points and not the dollar amount
    """,
    tools=[FunctionTool(get_user_benefits)],
    # input_schema=BestCardInputs,
    output_schema=BestCardOutput,
    #output_key="best_2_cards_selected"
)
