import os
import string

import cv2
import hidden_watermark
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QFileDialog, QMainWindow
# importe le module vigenere :)
from vigenere import vigenere


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        uic.loadUi(os.path.join(os.path.split(__file__)
                   [0], "watermark_front.ui"), self)

        self.browse_button.clicked.connect(self.browse_image)
        self.watermark_button.clicked.connect(self.watermark_image)
        self.extract_message_button.clicked.connect(self.extract_message)

    def browse_image(self):
        self.image_path, _ = QFileDialog.getOpenFileName(
            self, 'Selectionne une image', '', 'All Files (*)')
        self.image_label.setPixmap(QPixmap(self.image_path))
        self.watermark_button.setEnabled(True)
        self.extract_message_button.setEnabled(True)

    def watermark_image(self):
        message = self.message_plain_text_edit.toPlainText()

        password = "LeRoiLouis6legros"  # super ce mot de passe
        encrypted_message = vigenere(message, password, ciffer=True)

        hidden_watermark.lsb1_stegano(self.image_path, encrypted_message)

    def extract_message(self):
        hidden_message = hidden_watermark.lsb1_extract_message(self.image_path)

        # il faut bien le mdp pour décrypter le message :)
        password = "LeRoiLouis6legros"
        decrypted_message = vigenere(hidden_message, password, ciffer=False)

        self.message_plain_text_edit.setPlainText(decrypted_message)
