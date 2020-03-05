# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
#
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet, EventType

#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []


class ActionChitchat(Action):
    """Returns the chitchat utterance dependent on the intent"""

    def name(self) -> Text:
        return "action_chitchat"

    def run(self, dispatcher, tracker, domain) -> List[EventType]:
        intent = tracker.latest_message["intent"].get("name")

        # retrieve the correct chitchat utterance dependent on the intent
        if intent in [
            "ask_builder",
            "ask_howdoing",
            "ask_whatspossible",
            "ask_whatisrasa",
            "ask_isbot",
            "ask_howold",
            "ask_languagesbot",
            "ask_restaurant",
            "ask_time",
            "ask_wherefrom",
            "handleinsult",
            "nicetomeeyou",
            "telljoke",
            "ask_howbuilt",
            "ask_whoisit",
        ]:
            dispatcher.utter_message(template=f"utter_{intent}")
        return []


class ActionFaqs(Action):
    """Returns the chitchat utterance dependent on the intent"""

    def name(self) -> Text:
        return "action_faqs"

    def run(self, dispatcher, tracker, domain) -> List[EventType]:
        intent = tracker.latest_message["intent"].get("name")

        # logger.debug("Detected FAQ intent: {}".format(intent))

        # retrieve the correct chitchat utterance dependent on the intent
        if intent in [
            "ask_faq_languages"
        ]:
            dispatcher.utter_message(template=f"utter_{intent}")
        return []


class ActionGreetUser(Action):
    """Greets the user with/without privacy policy"""

    def name(self) -> Text:
        return "action_greet_user"

    def run(self, dispatcher, tracker, domain) -> List[EventType]:
        intent = tracker.latest_message["intent"].get("name")
        shown_privacy = tracker.get_slot("shown_privacy")
        name_entity = next(tracker.get_latest_entity_values("name"), None)
        dispatcher.utter_message(template="utter_greet_noname")
        if intent == "greet" or (intent == "enter_data" and name_entity):
            dispatcher.utter_message(template="utter_greet_noname")
            if name_entity:
                dispatcher.utter_message(template="utter_greet_name", name=name_entity)
            else:
                dispatcher.utter_message(template="utter_greet_noname")
            
            if not shown_privacy:
                dispatcher.utter_message(template="utter_inform_privacypolicy")
                return [SlotSet("shown_privacy", True)]
        return []
