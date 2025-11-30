from pydantic import BaseModel

class BestCardOutput(BaseModel):
    best_card_name: str
    reward_points: str