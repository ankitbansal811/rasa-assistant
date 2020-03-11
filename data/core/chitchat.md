## chitchat
* ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot OR ask_time OR ask_wherefrom OR handleinsult OR nicetomeeyou OR telljoke OR ask_howbuilt OR ask_whatspossible
    - action_chitchat

## deny ask_whatspossible
* ask_whatspossible
    - action_chitchat
* deny
    - utter_nohelp

## more chitchat
* greet
    - action_greet_user
* ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot OR ask_time OR ask_wherefrom OR handleinsult OR nicetomeeyou OR telljoke OR ask_howbuilt
    - action_chitchat
* ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot OR ask_time OR ask_wherefrom OR handleinsult OR nicetomeeyou OR telljoke OR ask_howbuilt
    - action_chitchat

## ask_whatspossible
* greet
    - action_greet_user
* ask_whatspossible
    - action_chitchat

## ask_whatspossible more
* greet
    - action_greet_user
* ask_whatspossible
    - action_chitchat
* ask_whatspossible
    - action_chitchat

## chitchat confirm
* greet
    - action_greet_user
* ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot OR ask_time OR ask_wherefrom OR handleinsult OR nicetomeeyou OR telljoke OR ask_howbuilt
    - action_chitchat
* affirm
    - utter_thumbsup
    - utter_anything_else

## just chitchat, continue, + confirm
* greet
    - action_greet_user
* ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot OR ask_time OR ask_wherefrom OR handleinsult OR nicetomeeyou OR telljoke OR ask_howbuilt OR ask_whatspossible
    - action_chitchat
* affirm
    - utter_great
    - utter_ask_feedback
* affirm
    - utter_thumbsup
    - utter_anything_else

## just newsletter, don't continue, + confirm
* greet
    - action_greet_user
* ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot OR ask_time OR ask_wherefrom OR handleinsult OR nicetomeeyou OR telljoke OR ask_howbuilt OR ask_whatspossible
    - action_chitchat
* deny
    - utter_thumbsup
    - utter_ask_feedback
* affirm
    - utter_thumbsup
    - utter_anything_else