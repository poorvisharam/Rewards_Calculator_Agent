import asyncio
import json

from pydantic import ValidationError
import models
from models.best_card import BestCardOutput
from tools import user_benefits
from google.adk.runners import InMemoryRunner
from agents import best_card
from dotenv import load_dotenv

load_dotenv()

# populating dummy data
models.benefits.populate_dummy_benefits()
models.user.populate_dummy_users()

runner = InMemoryRunner(agent=best_card.best_card_agent, app_name="agents")

async def agent_runner():
    events = await runner.run_debug(
        user_messages="""
User ID: user1
Purchasing: iphone
Marketplace: Best Buy
Amount: $1000
"""
    )
    best_card_result = None
    for event in events:
        if hasattr(event, "content") and event.content and event.content.parts and len(event.content.parts) > 0:
            for part in event.content.parts:
                if part.text:  # make sure text is not None
                    if "best_card_name" in part.text:
                        best_card_result = part.text
                        break

    return best_card_result

result = asyncio.run(agent_runner())
try:
    json_result = BestCardOutput.model_validate_json(result)

    if json_result:
        print("Best card:", json_result.best_card_name)
        print("Reward points:", json_result.reward_points)
except ValidationError:
    print("No structured output returned from agent.")
