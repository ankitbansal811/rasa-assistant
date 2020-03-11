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

## thanks
* thank
    - utter_noworries
    - utter_anything_else

## bye
* bye
    - utter_bye

## greet
* greet OR enter_data{"name": "akela"}
    - action_greet_user

## anything else? - yes
    - utter_anything_else
* affirm
    - utter_what_help

## anything else? - no
    - utter_anything_else
* deny
    - utter_thumbsup

## anything else?
    - utter_anything_else
* enter_data
    - utter_not_sure
    - utter_possibilities

## positive reaction
* react_positive
    - utter_react_positive

## negative reaction
* react_negative
    - utter_react_negative

## human handoff
* human_handoff
    - utter_contact_email

## greet handoff
* greet
    - action_greet_user
* human_handoff
    - utter_contact_email

## greet isBot handoff
* greet
    - action_greet_user
* ask_isbot
    - action_chitchat
* human_handoff
    - utter_contact_email

## faqs
* ask_faq_languages
    - action_faqs

## out of scope non english
* out_of_scope/non_english
    - utter_non_english

## out of scope other
* out_of_scope/other
    - utter_oos

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
    - utter_thumbsup

## sad path 2
* greet
    - action_greet_user
* react_negative
    - utter_cheer_up
    - utter_did_that_help
* deny
    - utter_bye

## bot challenge
* ask_isbot
    - utter_ask_isbot
