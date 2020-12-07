# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
# from rasa_sdk.forms import FormAction
from pathlib import Path
from rasa_sdk.knowledge_base.storage import InMemoryKnowledgeBase
from rasa_sdk.knowledge_base.actions import ActionQueryKnowledgeBase
import json
from json import load, dumps


#
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


# -------------------------------------------------------------
# ---------------------Mein erstes Programm-------------------#
# -------------------------------------------------------------

#
class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        print("aus actions.py file")
        dispatcher.utter_message(text="Hallo aus meinem ersten Programm !")

        return []


class ActionProfessor(Action):
    Namenfile = Path("data/Namen.txt").read_text().split("\n")

    def name(self) -> Text:
        return "action_such_Professor"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        entities = tracker.latest_message['entities']
        print(entities)

        print("aus actions.py file")
        for e in entities:
            if e['entity'] == "Prof":
                name = e['value']

                if name in self.Namenfile:
                    message = f"Ja {name} ist ein Student an der Hochschule Kempten"

                elif name == "rasa":
                    message = "Rasa ist ein Chatbot"
                else:
                    message = f"ich kenne disen Namen {name} noch nicht :("

        dispatcher.utter_message(text=message)
        print(message)

        return []


# -----------------------------------------------------------------------
class ActionInfo(Action):
    with open("data/Namen.json") as file:
        Info = json.load(file)

    def name(self) -> Text:
        return "action_Info_professor"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        entities = tracker.latest_message['entities']
        # print(entities)
        print("aus actions.py file")
        # print(self.Info["Studenten"][0]["Vorname"])
        info = None

        for i in entities:
            if i['entity'] == "info":
                info = i['value']
        for data in self.Info["Studenten"]:
            if data["Vorname"] == info.title():
                print(data)
                message = "Vorname : " + data["Vorname"] + "\n" + "Nachname : " + data[
                    "Nachname"] + "\n" + "Fakultät : " + data["Fakultat"]



        dispatcher.utter_message(text=message)

        dispatcher.utter_message(text="Hallo aus meinem dritten Programm !")

        return []
