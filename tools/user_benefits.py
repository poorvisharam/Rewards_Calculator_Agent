from models.benefits import Benefits_Data, Benefits
from models.user import Users, User, get_cards_user_has

def get_user_benefits(user_id: str) -> list[Benefits]:
    cards_user_has = get_cards_user_has(user_id)
    benefits = []
    if cards_user_has == None:
        return []
    for b in Benefits_Data:
        if b.card_name in cards_user_has.cards:
            benefits.append(b)
    return benefits
    
    