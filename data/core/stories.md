## happy path
* greet
  - action_greet_user
* react_positive
  - utter_react_positive

## sad path 1
* greet
  - action_greet_user
* react_negative
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
* greet
  - action_greet_user
* react_negative
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_bye

## say goodbye
* bye
  - utter_bye

## bot challenge
* ask_isbot
  - utter_ask_isbot
