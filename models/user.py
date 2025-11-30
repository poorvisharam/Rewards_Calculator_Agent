from pydantic import BaseModel

class User(BaseModel):
    user_id: str
    cards: set[str]
    
Users = []

def populate_dummy_users():
    Users.append(
        User(
            user_id="user1",
            cards=[
                "saffire-reserve",
                "freedom"
            ]
        )
    )
    Users.append(
        User(
            user_id="user2",
            cards=[
                "venture-X",
                "freedom"
            ]
        )
    )
    Users.append(
        User(
            user_id="user3",
            cards=[
                "freedom"
            ]
        )
    )

def get_cards_user_has(user_id) -> User:
    for u in Users:
        if user_id == u.user_id:
            return u
    print("user not found")
    return None