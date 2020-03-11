## out of scope
* out_of_scope
    - respond_out_of_scope
    - utter_possibilities

## say enter data outside the flows
* greet
    - action_greet_user
* enter_data
    - utter_not_sure
    - utter_possibilities

## say confirm outside the flows 2
* greet
    - action_greet_user
* affirm
    - utter_thumbsup

## say greet outside the flows
* greet
    - action_greet_user
* greet OR enter_data{"name": "akela"}
    - action_greet_user

## greet + oos
* greet
    - action_greet_user
* out_of_scope
    - respond_out_of_scope

## oos + confirm
* greet
    - action_greet_user
* out_of_scope
    - respond_out_of_scope
* affirm
    - utter_thumbsup
    - utter_anything_else

