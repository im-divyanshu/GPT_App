import openai
from settings import settings
import pyttsx3
from kivy.lang import Builder
from kivy.app import App 
from kivy.uix.widget import Widget
from kivy.properties import StringProperty

engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voices',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

openai.api_key="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"


class MainLayout(Widget):
    answer_text=StringProperty("")
    font_color=settings["font_color"]
    font_size=int(settings['font_size'])
    token_count=int(settings["tokens"])
    token_text=StringProperty("tokens: "+str(token_count)) 
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.text=""

    def generate_response(self,):
        self.answer(self.text,self.token_count)

    def update_text(self,widget):
        self.text=widget.text

    def decrease(self):
        self.token_count-=1
        self.token_text="tokens: "+str(self.token_count)

    def increase(self):
        self.token_count+=1
        self.token_text="tokens: "+str(self.token_count)

    def answer(self,prompt,tokens):
        response=openai.Completion.create(engine="text-davinci-001",prompt=prompt,max_tokens=tokens)
        print(response)
        speak(response["choices"][0]['text'])
        self.answer_text=response["choices"][0]['text']


kv=Builder.load_file("AI.kv")

class AIApp(App):
    def build(self):
        return kv

App=AIApp()
App.run()


# engine=pyttsx3.init()
# voices=engine.getProperty('voices')
# engine.setProperty('voices',voices[1].id)

# def speak(audio):
#     engine.say(audio)
#     engine.runAndWait()

# openai.api_key="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"
# prompt=input("enter the querry : ")

# response=openai.Completion.create(engine="text-davinci-001",prompt=prompt,max_tokens=40)
# print(response)
# speak(response["choices"][0]['text'])