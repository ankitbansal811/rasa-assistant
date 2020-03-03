## happy path
* greet
  - utter_greet
* react_positive
  - utter_happy

## sad path 1
* greet
  - utter_greet
* react_negative
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
* greet
  - utter_greet
* react_negative
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## say goodbye
* bye
  - utter_goodbye

## bot challenge
* ask_isbot
  - utter_iamabot
