# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"
import pandas as pd
import json
from typing import Any, Text, Dict, List, Union
#
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet, EventType, ConversationPaused, UserUtteranceReverted
from rasa_sdk.forms import FormAction

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
        if intent == "greet" or (intent == "enter_data" and name_entity):
            if name_entity:
                dispatcher.utter_message(template="utter_greet_name", name=name_entity)
            else:
                dispatcher.utter_message(template="utter_greet_noname")

            if not shown_privacy:
                dispatcher.utter_message(template="utter_inform_privacypolicy")
                return [SlotSet("shown_privacy", True)]
        return []


class ActionDefaultAskAffirmation(Action):
    """Asks for an affirmation of the intent if NLU threshold is not met."""

    def name(self) -> Text:
        return "action_default_ask_affirmation"

    def __init__(self) -> None:
        import pandas as pd

        self.intent_mappings = pd.read_csv("intent_description_mapping.csv")
        self.intent_mappings.fillna("", inplace=True)
        self.intent_mappings.entities = self.intent_mappings.entities.map(
            lambda entities: {e.strip() for e in entities.split(",")}
        )

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[EventType]:

        intent_ranking = tracker.latest_message.get("intent_ranking", [])
        if len(intent_ranking) > 1:
            diff_intent_confidence = intent_ranking[0].get("confidence") - intent_ranking[1].get("confidence")
            if diff_intent_confidence < 0.2:
                intent_ranking = intent_ranking[:2]
            else:
                intent_ranking = intent_ranking[:1]
        first_intent_names = [
            intent.get("name", "")
            for intent in intent_ranking
            if intent.get("name", "") != "out_of_scope"
        ]

        message_title = (
            "Sorry, I'm not sure I've understood " "you correctly 🤔 Do you mean..."
        )

        entities = tracker.latest_message.get("entities", [])
        entities = {e["entity"]: e["value"] for e in entities}

        entities_json = json.dumps(entities)

        buttons = []
        for intent in first_intent_names:
            # logger.debug(intent)
            # logger.debug(entities)
            buttons.append(
                {
                    "title": self.get_button_title(intent, entities),
                    "payload": "/{}{}".format(intent, entities_json),
                }
            )

        # /out_of_scope is a retrieval intent
        # you cannot send rasa the '/out_of_scope' intent
        # instead, you can send one of the sentences that it will map onto the response
        buttons.append(
            {
                "title": "Something else",
                "payload": "I am asking you an out of scope question",
            }
        )
        dispatcher.utter_message(text='action_default_ask_affirmation is running')
        dispatcher.utter_message(text=message_title, buttons=buttons)
        return []

    def get_button_title(self, intent: Text, entities: Dict[Text, Text]) -> Text:
        default_utterance_query = self.intent_mappings.intent == intent
        utterance_query = (self.intent_mappings.entities == entities.keys()) & (default_utterance_query)
        utterances = self.intent_mappings[utterance_query].button.tolist()

        if len(utterances) > 0:
            button_title = utterances[0]
        else:
            utterances = self.intent_mappings[default_utterance_query].button.tolist()
            button_title = utterances[0] if len(utterances) > 0 else intent

        return button_title.format(**entities)


class ActionDefaultFallback(Action):
    def name(self) -> Text:
        return "action_default_fallback"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[EventType]:

        # Fallback caused by TwoStageFallbackPolicy
        if (
            len(tracker.events) >= 4
            and tracker.events[-4].get("name") == "action_default_ask_affirmation"
        ):

            dispatcher.utter_message(template="utter_restart_with_button")

            return [SlotSet("feedback_value", "negative"), ConversationPaused()]

        # Fallback caused by Core
        else:
            dispatcher.utter_message(template="utter_default")
            return [UserUtteranceReverted()]


class SuggestionForm(FormAction):
    """Accept free text input from the user for suggestions"""

    def name(self) -> Text:
        return "suggestion_form"

    @staticmethod
    def required_slots(tracker) -> List[Text]:
        return ["person_name", "business_email", "suggestion"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        return {
            "suggestion": self.from_text(),
            "person_name": [
                self.from_entity(entity="name"),
                self.from_text(intent="enter_data"),
            ],
            "business_email": [
                self.from_entity(entity="email"),
                self.from_text(intent="enter_data"),
            ],
            }

    def validate_business_email(
        self, value, dispatcher, tracker, domain
    ) -> Dict[Text, Any]:
        """Check to see if an email entity was actually picked up by duckling."""

        if any(tracker.get_latest_entity_values("email")):
            # entity was picked up, validate slot
            return {"business_email": value}
        else:
            # no entity was picked up, we want to ask again
            dispatcher.utter_message(template="utter_no_email")
            return {"business_email": None}

    def submit(self, dispatcher, tracker, domain) -> List[EventType]:
        dispatcher.utter_message(template="utter_thank_suggestion")
        return []