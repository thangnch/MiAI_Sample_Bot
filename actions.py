# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
import json
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class act_color(Action):

    def name(self) -> Text:
        return "act_color"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        message = {
            "text": "Select your color:",
            "quick_replies": [
                {
                    "content_type": "text",
                    "title": "Red",
                    "payload": "red",

                },
                {
                    "content_type": "text",
                    "title": "Blue",
                    "payload": "blue",
                },
                {
                    "content_type": "text",
                    "title": "Green",
                    "payload": "green",
                }
            ]
        }



        dispatcher.utter_message(json_message=message)

        return []


class act_contact(Action):

    def name(self) -> Text:
        return "act_contact"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        button = {
            "type": "phone_number",
            "title": "Call hotline",
            "payload": "1900588856"
        }

        button1 = {
            "type": "web_url",
            "url": "https://miai.vn",
            "title": "Website"
        }
        button2 = {
            "type": "postback",
            "title": "Need more?",
            "payload": "more"
        }
        ret_text = "Hi! You can contact us via below methods:"
        dispatcher.utter_message(text=ret_text, buttons=[button, button1, button2])

        return []


class act_shirt(Action):

    def name(self) -> Text:
        return "act_shirt"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # These should be get from server , do not do like this :D
        shirt_list = []
        shirt0 = {
            "name": "Blue shirt ",
            "image_url": "https://s3.amazonaws.com/pix.iemoji.com/images/emoji/apple/ios-12/256/t-shirt.png",
            "intro": "Great blue shirt",
            "link": "https://miai.vn",

        }
        shirt_list.append(shirt0)
        shirt1 = {
            "name": "Red shirt ",
            "image_url": "https://pbs.twimg.com/profile_images/613199418049716224/PoQ0ti9f_400x400.png",
            "intro": "Great red shirt",
            "link": "https://miai.vn",

        }
        shirt_list.append(shirt1)
        shirt2 = {
            "name": "Green shirt ",
            "image_url": "https://icons.iconarchive.com/icons/google/noto-emoji-people-clothing-objects/256/12177-t-shirt-icon.png",
            "intro": "Great green shirt",
            "link": "https://miai.vn",

        }
        shirt_list.append(shirt2)



        template_items = []
        for shirt in shirt_list:

            template_item = {
                "title": shirt['name'],
                "image_url": shirt['image_url'],
                "subtitle": shirt['intro'],
                "default_action": {
                    "type": "web_url",
                    "url": shirt['link'],
                    "webview_height_ratio": "full"
                },
                "buttons": [
                    {
                        "type": "web_url",
                        "url": shirt['link'],
                        "title": "Xem ngay"
                    }
                ]
            }
            template_items.append(template_item)

        message_str = {
            "attachment": {
                "type": "template",
                "payload": {
                    "template_type": "generic",
                    "elements": template_items

                }
            }
        }
        ret_text = "Hi! You can choose from below items:"
        print(message_str)
        dispatcher.utter_message(text=ret_text, json_message=message_str)

        return []

class act_receipt(Action):

    def name(self) -> Text:
        return "act_receipt"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # These should be get from server , do not do like this :D
        shirt_list = []
        shirt0 = {
            "title":"Classic White T-Shirt",
            "subtitle":"100% Soft and Luxurious Cotton",
            "quantity":2,
            "price":50,
            "currency":"USD",
            "image_url":"http://petersapparel.parseapp.com/img/whiteshirt.png"

        }
        shirt_list.append(shirt0)
        shirt1 = {
            "title":"Classic Gray T-Shirt",
            "subtitle":"100% Soft and Luxurious Cotton",
            "quantity":1,
            "price":25,
            "currency":"USD",
            "image_url":"http://petersapparel.parseapp.com/img/grayshirt.png"

        }
        shirt_list.append(shirt1)


        cust_info = {
            "name":"Chien Thang",
            "address": {
                "street_1":"1 Hacker Way",
                  "street_2":"",
                  "city":"Menlo Park",
                  "postal_code":"94025",
                  "state":"CA",
                  "country":"US"
            },
            "total_buy" :
                {
                    "subtotal": 75.00,
                    "shipping_cost": 4.95,
                    "total_tax": 6.19,
                    "total_cost": 56.14
                }
        }

        message_str = {
            "attachment": {
                "type": "template",
                "payload": {
                    "template_type":"receipt",
                    "recipient_name":cust_info['name'],
                    "order_number":"12345678902",
                    "currency":"USD",
                    "payment_method":"Visa 2345",
                    "order_url":"http://miai.vn/order?order_id=123456",
                    "timestamp":"1428444852",
                    "address": cust_info['address'],
                    "summary": cust_info['total_buy'],
                    "elements": shirt_list

                }
            }
        }
        print(message_str)
        result = json.dumps(message_str)
        dispatcher.utter_message(json_message=result)

        return []

class act_guide(Action):

    def name(self) -> Text:
        return "act_guide"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # These should be get from server , do not do like this :D

        dispatcher.utter_message(text="Your guide book:",
                                 image="https://i.pinimg.com/originals/0c/50/bf/0c50bf4195aa282bcef92b4e35aee93d.png");


        return []

class act_bye(Action):

    def name(self) -> Text:
        return "act_bye"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        clip_list = []
        clip = {
            "name": "Super Fun Clips",
            "image_url": "https://i.pinimg.com/564x/1e/1e/f7/1e1ef72685a6127e71257f9a18cdbecc.jpg",
            "intro": "Fun clips",
            "link": "https://www.youtube.com/watch?v=S1_kV_iYzDA",

        }
        clip_list.append(clip)


        template_items = []
        for clip in clip_list:
            template_item = {
                "title": clip['name'],
                "image_url": clip['image_url'],
                "subtitle": clip['intro'],
                "default_action": {
                    "type": "web_url",
                    "url": clip['link'],
                    "webview_height_ratio": "full"
                },
                "buttons": [
                    {
                        "type": "web_url",
                        "url": clip['link'],
                        "title": "Xem ngay"
                    }
                ]
            }
            template_items.append(template_item)

        message_str = {
            "attachment": {
                "type": "template",
                "payload": {
                    "template_type": "generic",
                    "elements": template_items

                }
            }
        }
        ret_text = "Hi! Goodbye with funs:"
        dispatcher.utter_message(text=ret_text,
                                 json_message=message_str,
                                 image="https://i.pinimg.com/originals/fd/3c/cd/fd3ccd7b49e366b4206f5ac7f8fa8dac.gif")
        return []
