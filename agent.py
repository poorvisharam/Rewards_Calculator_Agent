# loading env
from dotenv import load_dotenv
load_dotenv()

def main():
    from models.benefits import populate_dummy_benefits
    from models.user import populate_dummy_users

    # populating dummy data
    populate_dummy_benefits()
    populate_dummy_users()

    import asyncio

    from pydantic import ValidationError
    from .models.best_card import BestCardOutput
    from google.adk.runners import InMemoryRunner
    from .agents import best_card
    print("called main")
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

if __name__ == "__main__":
    main()
else:
    from .models.benefits import populate_dummy_benefits
    from .models.user import populate_dummy_users

    # populating dummy data
    populate_dummy_benefits()
    populate_dummy_users()

    from google.adk.agents import SequentialAgent
    from google.adk.models.google_llm import Gemini
    from .agents.marketplace import marketplace_classifier
    from .agents.reward_calculator import reward_calculator_agent
    root_agent = SequentialAgent(
        name="root_agent",
        sub_agents=[marketplace_classifier, reward_calculator_agent],
    )