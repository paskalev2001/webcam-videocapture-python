import PySimpleGUI as sg
import videoCapture as vc

sg.theme('Dark')
sg.set_options(element_padding=(2, 2))

BTN_RECORD = 'Start Recording'
BTN_TEST = 'Test Camera'
BTN_EXIT = 'Exit'

def main_window():
    layout = [
        [sg.Text('Video Source:', size=(15, 1)), sg.Input(key="-SRC-", size=(2, 1), default_text='0')],
        [sg.Text('File Name:', size=(15, 1)), sg.Input(key="-NAME-", default_text='output')],
        [sg.Button(BTN_RECORD), 
        [sg.Text('Width:', size=(15, 1)), sg.Input(key="-W-", default_text=640, size=(8, 1))],
        [sg.Text('Height:', size=(15, 1)), sg.Input(key="-H-", default_text=480, size=(8, 1))],
        ],
        [sg.Button(BTN_TEST)],
        [sg.Button(BTN_EXIT)]
    ]

    window = sg.Window(
        'Camera Scanner',
        layout,
    )

    while True:
        event, values = window.read()
        src = int(values['-SRC-'])
        w = int(values['-W-'])
        h = int(values['-H-'])

        if event == BTN_RECORD:
            vc.capture_to_video_file(
                src,
                path = "./storage/"+values['-NAME-'],
                width = w,
                height = h
                )

        if event == BTN_TEST:
            vc.loopback_camera(src, w, h)

        if event in (sg.WIN_CLOSED, BTN_EXIT):
            break
