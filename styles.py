frames_style = '''
    QFrame {
        background: grey;
        border-radius: 12px;
    }

    QPushButton {
        background: #eaeaea;
        border-radius: 40px;
    }

    QPushButton:hover {
        background: #b1b1b1;
    }

    QPushButton:pressed {
        background: #b1b1b1;
        padding-top: 2px;
    }

    QLabel{
        color: white;
    }
'''

background_style = "background: black" #black grey

music_slider_style = """
    QSlider {
        background: transparent;
    }
    QSlider::groove:horizontal {
        height: 6px;
        background: #444;
        border-radius: 3px;
    }
    QSlider::sub-page:horizontal {
        background: green;
        border-radius: 3px;
    }
    QSlider::add-page:horizontal {
        background: #444;
        border-radius: 3px;
    }
    QSlider::handle:horizontal {
        background: white;
        width: 14px;
        height: 14px;
        margin: -5px 0;
        border-radius: 7px;
    }
"""

music_name_style = '''
    QLabel{
        font-family: 'Georgia';
        color: blue;
        font-size: 25px;
        font-style: italic;
    }
'''