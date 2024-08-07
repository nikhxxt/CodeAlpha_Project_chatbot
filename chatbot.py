import spacy
import random


nlp = spacy.load("en_core_web_sm")


responses = {
  "greetings": ["Hello","Hi there", "Hey! How can I help you?", "Greetings!", Nice to see you!"]
               ["Goodbye!", "See you soon!", "Bye! Have a great dat", "Take care








def classify_input(user_input):
    doc = nlp(user_input.loer()):
    for token in doc:
        if token.lemma_ in ["hello, "hi", "hey"]:
           return "greetings"
        elif token.lemma_ in ["bye, "goodbye", "later"]:
           return "farewell"
         elif token.lemma_ in ["name", "who"]:
           return "name_query"
        elif  token.lemma_ in ["thanks, "thank"]:
           return "thanks"
        elif  token.lemma_ in ["how, "hi", "hey"]:
              if any(t.lemma_ == "you" for t in doc):
                  return "how_are_you"
        elif  token.lemma_ in ["my", "i"]:
             if any(t.lemma_ == "name" for t in doc):
                return "name_provide"
    return "default"


def generate_response(classsfication, user_input=none):
    if classification == "name_provie":
       name = user_input.spilt()[-1]
       return random.choice(responses[classification]).format(name=name)
    return random.choice(responses[classification]


def chatbot():
    print("ChatBot: Hello!How can i assist you today?")
    while true:
        user_input = input("you: ")
        if user_input.lower() in ["exit", "quit", "bye", "goodbye"]:
           print("ChatBot: goodbye! Have a great day!")
           break
         classification = classify_input(user_input)
         response = generate_rsponse(classification, user_ input)
         print(f"ChatBot: {response}")

if __name__ == "__main__":
  chatbot()
        
    
