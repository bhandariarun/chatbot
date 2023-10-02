from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class CheckBalance(Action):

    def name(self) -> Text:
        return "action_check_balance_entity"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        balance_entity = next(traker.get_latest_entity_values('balance'), None)

        if balance_entity:
            dispatcher.utter_message(text=f"You have {balance_entity} in your account")
        else:
            dispatcher.utter_message(text="Sorry! You don't have balance")

        return[]
