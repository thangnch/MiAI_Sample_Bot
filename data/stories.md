## happy path
* greet
  - utter_greet
* mood_great
  - utter_happy

## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - act_bye

## say goodbye
* goodbye
  - act_bye

## bot challenge
* bot_challenge
  - utter_iamabot


## choose color
* ask_color
  - act_color
 
## choose contact
* ask_contact
  - act_contact

## choose shirt
* ask_shirt
  - act_shirt

## receipt
* ask_receipt
  - act_receipt
  
## guide
* ask_guide
  - act_guide