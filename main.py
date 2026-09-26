from PySide6.QtWidgets import *
from PySide6.QtCore import *
from __feature__ import snake_case, true_property
import sys
from styles import background_style, frames_style, music_slider_style,music_name_style

imageDir = "granOla"

class myFirstWindow(QMainWindow):
    def setupUI(self,ancho,altura):
        
        self.size = QSize(ancho,altura)


        self.root_layout = QVBoxLayout()

        self.frame_music_display = QFrame()
        self.frame_music_status = QFrame()
        self.frame_music_options = QFrame()
        self.frame_catalog = QFrame()

        self.style_sheet = background_style

        self.frame_catalog.set_fixed_height(altura * 0.06)

        self.root_layout.add_widget(self.frame_music_display,50)
        self.root_layout.add_widget(self.frame_music_status,20)
        self.root_layout.add_widget(self.frame_music_options,30)


        self.widget = QWidget()
        self.widget.set_layout(self.root_layout)
        self.widget.minimum_height = 470

        self.set_central_widget(self.widget)


        self.setup_music_options_frame()
        self.setup_music_status_frame()
        self.setup_music_display_frame()
    
    def setup_music_display_frame (self):
        global imageDir
        self.music_image = QFrame()
        self.music_image.style_sheet = f"border-image: url(./{imageDir}) 0 0 0 0 stretch stretch;"

        self.music_image_layout = QVBoxLayout()

        self.music_image_layout.add_widget(self.music_image)
        self.frame_music_display.set_layout(self.music_image_layout)

        self.frame_music_display.style_sheet = frames_style

    def setup_music_status_frame (self):
        self.music_name = QLabel("La gran ola", alignment = Qt.AlignCenter)
        self.music_slider = QSlider(Qt.Horizontal)
        self.remaining_time = QLabel("1:30")
        self.start_time = QLabel("0:00")

        self.music_status_layout = QHBoxLayout()

        self.music_status_layout.add_widget(self.start_time) 
        self.music_status_layout.add_widget(self.music_slider)
        self.music_status_layout.add_widget(self.remaining_time)

        self.big_music_status_layout = QVBoxLayout()

        self.big_music_status_layout.add_widget(self.music_name)
        self.big_music_status_layout.add_layout(self.music_status_layout)

        self.frame_music_status.set_layout(self.big_music_status_layout)

        self.frame_music_status.style_sheet = frames_style
        self.music_slider.style_sheet = music_slider_style
        self.music_name.style_sheet = music_name_style

    def setup_music_options_frame (self):
        self.play_button = QPushButton()
        self.next_button = QPushButton()
        self.last_button = QPushButton()
        self.volume_dial = QDial()

        self.play_button.pressed.connect(self.playLogic)
        self.next_button.pressed.connect(self.nextLogic)
        self.last_button.pressed.connect(self.lastLogic)

        for btn in (self.play_button, self.next_button, self.last_button):
            btn.set_fixed_size(60, 60)
        
        self.volume_dial.set_fixed_size (120,120)
            

        self.buttons_layout = QHBoxLayout()

        self.buttons_layout.add_widget(self.last_button)
        self.buttons_layout.add_widget(self.play_button)
        self.buttons_layout.add_widget(self.next_button)
        self.buttons_layout.add_widget(self.volume_dial)

        self.frame_music_options.set_layout(self.buttons_layout)

        self.frame_music_options.style_sheet = frames_style

        self.last_button.style_sheet = frames_style + "margin-left: 20px;"

    def playLogic (self):
        print("Play/stop")

    def nextLogic (self):
        print("next")

    def lastLogic (self):
        print("previous")
    


app = QApplication(sys.argv)

ventana = myFirstWindow()
ventana.setupUI(370,540)
ventana.show()

sys.exit(app.exec_())