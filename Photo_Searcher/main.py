from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

import wikipedia
import requests

Builder.load_file('frontend.kv')


class FirstScreen(Screen):

    def get_image_link(self):
        # Get user query from TextInput
        query = self.manager.current_screen.ids.user_query.text
        # Get wikipedia page and the first image link
        page = wikipedia.page(query, auto_suggest=False)
        image_link = page.images[0]
        return image_link

    def download_image(self):
        # Download the image
        req = requests.get(self.get_image_link(), headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36"})
        image_path = 'files/image.jpg'

        with open(image_path, 'wb') as file:
            file.write(req.content)
        return image_path

    def set_image(self):
        # Set the image in the Image Widget
        self.manager.current_screen.ids.img.source = self.download_image()


class RootWidget(ScreenManager):
    pass


class MainApp(App):

    def build(self):
        return RootWidget()


MainApp().run()
