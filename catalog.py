from PySide6.QtWidgets import *
from PySide6.QtCore import QSize
from PySide6.QtCore import *
from __feature__ import snake_case, true_property
import sys
from styles import background_style,frames_top_style,frames_bottom_style

from pathlib import Path

class catalogWindow(QMainWindow):
    def setupUI(self,ancho,altura):
        
        self.size = QSize(ancho,altura)


        self.root_layout = QVBoxLayout()
        
        self.frame_top = QFrame()
        self.frame_center = QFrame()

        self.style_sheet = background_style

        self.root_layout.add_widget(self.frame_top,25)
        self.root_layout.add_widget(self.frame_center,75)

        self.widget = QWidget()
        self.widget.set_layout(self.root_layout)
        self.widget.minimum_height = 470

        self.set_central_widget(self.widget)

        self.setup_top_frame()
        self.setup_center_frame()


    def setup_top_frame(self):
        self.frame_top.style_sheet = frames_top_style
        self.button_back_album = QPushButton()
        self.button_next_album = QPushButton()
        
        self.top_box_layout = QHBoxLayout()

        self.albums_buttons = []

        self.top_box_layout.add_widget (self.button_back_album)

        for i in range(album_number()):         #It saves the albums portraits and "links" as buttons
            boton = QPushButton()
            boton.set_fixed_size(100, 100)

            self.albums_buttons.append(boton)
            
            i = i+1
            boton.clicked.connect(lambda checked, idx=i: print(f"albumBoton:{idx}"))     #Cambiar aqui para poner album
            boton.style_sheet = f'''border-image: url(./musica/portadas/id_{i}.jpg) 0 0 0 0 stretch stretch;border-radius: 0px;'''

            self.top_box_layout.add_widget(boton)

        self.top_box_layout.add_widget (self.button_next_album)

        self.frame_top.set_layout(self.top_box_layout)
    
    def setup_center_frame(self):
        self.frame_center.style_sheet = frames_bottom_style
        self.center_big_layout = QHBoxLayout()
        self.center_songs_layout = QGridLayout()

        self.button_back_songs = QPushButton()
        self.button_next_songs = QPushButton()

        self.songs = []

        self.center_big_layout.add_widget(self.button_back_songs)
        self.center_big_layout.add_layout(self.center_songs_layout)
        self.center_big_layout.add_widget(self.button_next_songs)

        self.frame_center.set_layout(self.center_big_layout)

        self.setup_center_songs_layout()
    
    def setup_center_songs_layout(self):
        songN = songs_number()
        for i in range(5):
            for j in range(4):
                if(i+1*j+1<=songN):
                    self.add_song_center(i,j)
                else:
                    return

    def add_song_center(self,row,column):
        coordinates = f'{row},{column}'
        button = QPushButton()
        button.clicked.connect(lambda checked: print(f"albumBoton:{row}-{column}"))
        self.center_songs_layout.add_widget(button,row,column)
        self.songs.append((button,coordinates))









def album_number():     #This counts the number of lines/albums in albumReferences
    referencesArchive = Path("musica/albumReferences.txt")
    number = 0
    with referencesArchive.open("r", encoding="utf-8") as f:
        for linea in f:
            if not(linea.strip() == ""):
                number = number+1

    return number

def songs_number():     #This gets the number of lines/songs in songReferences
    referencesArchive = Path("musica/songReferences.txt")
    number = 0
    with referencesArchive.open("r", encoding="utf-8") as f:
        for linea in f:
            if not(linea.strip() == ""):
                number = number+1

    return number

def song_portrait(id):      #This gives the route of the songs portrait based on its id or ERROR404 if it doesnt finds it
    if (Path("musica/portadas/"+id)).exists():
        return ("musica/portadas/"+id)
    else:
        return "ERROR404"

app = QApplication(sys.argv)

ventana = catalogWindow()
ventana.setupUI(540,540)
ventana.show()

sys.exit(app.exec_())