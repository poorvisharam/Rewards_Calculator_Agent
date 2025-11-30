from pydantic import BaseModel

class Benefits(BaseModel):
    card_name: str
    issuer: str
    rewards: dict[str, float]

Benefits_Data = []

def populate_dummy_benefits():
    Benefits_Data.append(
        Benefits(
            card_name="saffire-reserve",
            issuer="chase",
            rewards={
                "groceries": 5.0,
                "travel": 8.0,
                "other": 2.0
            }
        )
    )
    Benefits_Data.append(
        Benefits(
            card_name="freedom",
            issuer="chase",
            rewards={
                "groceries": 3.0,
                "travel": 2.0,
                "other": 1.0
            }
        )
    )
    Benefits_Data.append(
        Benefits(
            card_name="venture-X",
            issuer="capital-one",
            rewards={
                "groceries": 2.0,
                "travel": 5.0,
                "other": 1.5
            }
        )
    )
