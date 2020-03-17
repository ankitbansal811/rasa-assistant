FROM rasa/rasa-sdk:latest
USER root
RUN apt-get update && apt-get upgrade -y
RUN pip install --no-cache-dir pandas
USER 1001


#rasa_actions image