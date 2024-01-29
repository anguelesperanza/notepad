import flet as ft

textfield = ft.TextField(multiline=True, autofocus=True, border=ft.InputBorder.NONE, min_lines=40, content_padding=30, cursor_color='yellow')

def main(page: ft.Page):
    textfield.on_change = save_text
    page.add(textfield)

def save_text(e:ft.ControlEvent):
    print(textfield.value)
    with open('save.txt', 'w') as f:
        f.write(textfield.value)

def load_text():
    try:
        with open('save.txt', 'r') as f:
            textfield.value = f.read()
    except FileNotFoundError:
        textfield.hint_text = "Welcome to the text editor"

load_text()
ft.app(target=main)
