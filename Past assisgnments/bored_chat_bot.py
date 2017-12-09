class Chatbot:
    """ An object that can engage in rudimentary conversation with a human. """

    def __init__(self, name):
        self.name = name

    def greeting(self):
        """ Returns the Chatbot's way of introducing itself. """
        return "Hello, my name is " + self.name

    def response(self, prompt_from_human):
        """ Returns the Chatbot's response to something the human said. """
        return "It is very interesting that you say: '" + prompt_from_human + "'"

class Boredchatbot(Chatbot):
    #add a new method called response that will overwrite chatbot response
    def response(self, prompt_from_human):
        # count the chars in prompt_from_human and if more than 21 give the bored statement
        # if the char count ins less than 22 then give the normal response
        statement_lenght = len(prompt_from_human)
        if statement_lenght > 21:
            return "zzz... Oh excuse me, I dozed off reading your essay."
        else:
            return "It is very interesting that you say: '" + prompt_from_human + "'"

# make a Boredchatbot
mark = Boredchatbot("Mark")
# introduce the chatbot and allow the user to say something
human_message = input(mark.greeting())
# respond to the user after determining lenght of message.
print(mark.response(human_message))