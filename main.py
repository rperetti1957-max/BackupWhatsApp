import os
import shutil
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class WhatsAppMoverApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        self.status_label = Label(text="Pronto per il trasferimento", font_size=18)
        
        self.move_btn = Button(
            text="Trasferisci Media WhatsApp", 
            background_color=(0, 0.7, 0.3, 1),
            font_size=20
        )
        self.move_btn.bind(on_press=self.sposta_file)
        
        self.layout.add_widget(self.status_label)
        self.layout.add_widget(self.move_btn)
        return self.layout

    def sposta_file(self, instance):
        # Percorso standard Android 11+
        sorgente = "/storage/emulated/0/Android/media/com.whatsapp/WhatsApp/Media/"
        # Cartella di destinazione chiamata "whatsapp"
        destinazione = "/storage/emulated/0/whatsapp/" 

        if not os.path.exists(sorgente):
            self.status_label.text = "Errore: Cartella WhatsApp originale non trovata!"
            return

        try:
            if not os.path.exists(destinazione):
                os.makedirs(destinazione)
            
            for item in os.listdir(sorgente):
                s = os.path.join(sorgente, item)
                d = os.path.join(destinazione, item)
                if os.path.isdir(s):
                    if os.path.exists(d):
                        shutil.rmtree(d)
                    shutil.copytree(s, d)
            
            self.status_label.text = "Trasferimento completato con successo!"
        except Exception as e:
            self.status_label.text = f"Errore: {str(e)}"

if __name__ == "__main__":
    WhatsAppMoverApp().run()
