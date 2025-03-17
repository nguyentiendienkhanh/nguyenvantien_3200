import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui.caesar import Ui_MainWindow
import requests

class MyApp(QMainWindow):
    def __init__(self):  
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_encrypt.clicked.connect(self.call_api_encrypt)
        self.ui.btn_decrypt.clicked.connect(self.call_api_decrypt)
    
    def call_api_encrypt(self):
        url = "http://127.0.0.1:5000/api/caesar/encrypt"
        payload = {
            "plain_text": self.ui.plainTextEdit.toPlainText(),
            "key": self.ui.textEdit.toPlainText()
        }

        print("\n🔹 Sending request to:", url)  # Debug request
        print("🔹 Payload:", payload)

        try:
            response = requests.post(url, json=payload)
            print("🔹 Response status:", response.status_code)

            if response.status_code == 200:
                data = response.json()
                self.ui.plainTextEdit_2.setPlainText(data["encrypted_message"])
                QMessageBox.information(self, "Success", "Encryption successful")
            else:
                print("❌ Error: API returned status", response.status_code)
        except requests.exceptions.RequestException as e:
            print("❌ Request failed:", str(e))

    def call_api_decrypt(self):
        url = "http://127.0.0.1:5000/api/caesar/decrypt"
        payload = {
            "cipher_text": self.ui.plainTextEdit_2.toPlainText(),
            "key": self.ui.textEdit.toPlainText()
        }

        print("\n🔹 Sending request to:", url)
        print("🔹 Payload:", payload)

        try:
            response = requests.post(url, json=payload)
            print("🔹 Response status:", response.status_code)

            if response.status_code == 200:
                data = response.json()
                self.ui.plainTextEdit.setPlainText(data["decrypted_message"])
                QMessageBox.information(self, "Success", "Decryption successful")
            else:
                print("❌ Error: API returned status", response.status_code)
        except requests.exceptions.RequestException as e:
            print("❌ Request failed:", str(e))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
