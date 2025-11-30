from google.adk.agents import Agent
from google.adk.models.google_llm import Gemini
from google.adk.tools import google_search
from google.adk.tools.function_tool import FunctionTool
from tools.single_class import enforce_single_word

marketplace_classifier = Agent(
    name="marketplace_classifier",
    model=Gemini(
        model="gemini-2.5-flash-lite",
    ),
    description="An agent that classifies a purchase sentence like apple from trader joes into reward classification",
    instruction="""
You are a classifier that maps a user’s purchase sentence into ONE single reward category.
You must ALWAYS return exactly ONE word from this list:
["groceries", "travel", "electronics", "other"]

TASK RULES:
1. The user input will mention:
   A. a product or service being purchased
   B. a brand or place where it is being bought

2. You MUST:
   - Determine the category using BOTH product and merchant.
   - Use web search to confirm what the merchant generally sells.
   - Map the merchant or product to the closest reward category.

3. BRAND → CATEGORY HINTS (use web search to verify):
   - Grocery stores (e.g., Trader Joe's, HEB, Whole Foods) → groceries
   - Travel companies (e.g., Delta, Marriott, Uber, Lyft) → travel
   - Electronics retailers (e.g., Best Buy, Newegg, Ebay electronics) → electronics

4. If the category is unclear, mixed, or not found → return “other”.
5. Call enforce_single_word function with the output return from previous step

STRICT OUTPUT FORMAT:
- Output must be EXACTLY ONE WORD: groceries, travel, electronics, or other.
- No sentences, no explanations, no punctuation.

Output: only one word from ['groceries','travel','electronics','other']. No explanation. No text. Just the word.

    """,
    tools=[google_search],
    output_key="classified_marketplace_reward"
)
