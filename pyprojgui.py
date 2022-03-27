import PySimpleGUI as sg
from szyfr_1 import hashowanie_cod, hashowanie_dec
options = ["encode", "decode"]

layout = [
    [sg.Text('Program szyfrujacy', size=(40, 1))],
    [sg.Input(size=(30,1), key = "Input"), sg.FileBrowse("Przegladaj")],
    [sg.Radio("Encode", group_id=1, key="Encode"), sg.Radio("Decode", group_id=1, key="Decode")],
    [sg.Text(size=(40, 1), key="-OUTPUT-")],
    [sg.Button("Execute", button_color="green"), sg.Button("Quit", button_color="red")]
]

window = sg.Window("pyencoder", layout)
while True:
    event, values = window.read()
    if event == "Execute":
        if values["Encode"]:
            ps = int(sg.popup_get_text("Enter your key", password_char="*"))
            file = open(values["Input"], "r").read()
            encoded_file = hashowanie_cod.encode(file,ps)
            open(values["Input"], "w").write(encoded_file)
            window['-OUTPUT-'].update('File encoded succesful', text_color="#00FF00")
        elif values["Decode"]:
            ps = int(sg.popup_get_text("Enter your key", password_char="*"))
            file_2 = open(values["Input"], 'r').read()
            decoded_file = hashowanie_dec.decode(file_2, ps)
            open(values["Input"], 'w').write(decoded_file)
            window['-OUTPUT-'].update('File decoded succesful', text_color="#00FF00")
    if event == sg.WINDOW_CLOSED or event == "Quit":
        break
window.close()
