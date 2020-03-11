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

## out of scope
* out_of_scope
    - respond_out_of_scope
    - utter_possibilities
