from PySide6.QtWidgets import *
from PySide6.QtCore import *
from __feature__ import snake_case, true_property
import sys
from styles import background_style

class catalogWindow(QMainWindow):
    def setupUI(self,ancho,altura):
        
        self.size = QSize(ancho,altura)


        self.root_layout = QHBoxLayout()
        
        self.frame_general = QFrame()

        self.style_sheet = background_style

        self.root_layout.add_widget(self.frame_general)

        self.widget = QWidget()
        self.widget.set_layout(self.root_layout)
        self.widget.minimum_height = 470

        self.set_central_widget(self.widget)

        def setup_general_frame(self):
            self.back_button = QPushButton()
            self.next_button = QPushButton()

            self.catalog_frame = QGridLayout()

            self.



app = QApplication(sys.argv)

ventana = catalogWindow()
ventana.setupUI(540,540)
ventana.show()

sys.exit(app.exec_())