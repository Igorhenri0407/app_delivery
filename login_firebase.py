import pyrebase


class Accont:
    def __init__(self):
        firebaseConfig = {'apiKey': "AIzaSyBd_byUcdsHRpPpa618dWeWyDx9g6TOoNY",
            'authDomain': "seu-delivery-f6355.firebaseapp.com",
            'databaseURL': "https://seu-delivery-f6355-default-rtdb.firebaseio.com",
            'projectId': "seu-delivery-f6355",
            'storageBucket': "seu-delivery-f6355.appspot.com",
            'messagingSenderId': "886626882033",
            'appId': "1:886626882033:web:e798a08bd4b82a059ef450"
};

        firebase = pyrebase.initialize_app(firebaseConfig)
        self.auth = firebase.auth()

    def sign_in(self, email, password):
        try:
            self.auth.sign_in_with_email_and_password(email, password)
            return True

        except:
            return False

    def sing_up(self, email, password):
        try:
            self.auth.create_user_with_email_and_password(email, password)
            return True

        except:
            return False

    def reset_password(self, email):
        try:
            self.auth.send_password_reset_email(email)
            return True

        except:
            return False