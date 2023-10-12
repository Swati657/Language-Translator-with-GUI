#!/usr/bin/env python
# coding: utf-8

# In[12]:


import tkinter as tk
from tkinter import ttk
from googletrans import Translator, LANGUAGES

class LanguageTranslatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Language Translator")
        
        self.translator = Translator()
        self.languages = list(LANGUAGES.values())  # List of language names
        
        self.create_widgets()
        
    def create_widgets(self):
        self.label = tk.Label(self.root, text="Enter text to translate:")
        self.label.pack(pady=10)
        
        self.input_text = tk.Text(self.root, height=5, width=40)
        self.input_text.pack()
        
        self.language_label = tk.Label(self.root, text="Select destination language:")
        self.language_label.pack(pady=5)
        
        self.language_dropdown = ttk.Combobox(self.root, values=self.languages)
        self.language_dropdown.pack()
        
        self.translate_button = tk.Button(self.root, text="Translate", command=self.translate)
        self.translate_button.pack(pady=5)
        
        self.output_label = tk.Label(self.root, text="Translated text:")
        self.output_label.pack(pady=10)
        
        self.output_text = tk.Text(self.root, height=5, width=40)
        self.output_text.pack()
        
    def translate(self):
        input_text = self.input_text.get("1.0", "end-1c")
        dest_language = self.language_dropdown.get()
        if input_text and dest_language:
            dest_language_code = [code for code, name in LANGUAGES.items() if name == dest_language][0]
            translated = self.translator.translate(input_text, dest=dest_language_code)
            self.output_text.delete("1.0", "end")
            self.output_text.insert("1.0", translated.text)
        
if __name__ == "__main__":
    root = tk.Tk()
    app = LanguageTranslatorApp(root)
    root.mainloop()



# In[ ]:





# In[ ]:




