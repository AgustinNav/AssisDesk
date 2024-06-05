"""Welcome to Reflex!."""

# Import all the pages.
from AssisDesk_API.pages import *

import reflex as rx


class LoginState(rx.State):
    username: str = ""
    password: str = ""
    is_logged_in: bool = False

    def login(self):
        if self.username == "admin" and self.password == "password":
            self.is_logged_in = True
        else:
            rx.window_alert("Invalid credentials")


# Create the app.
app = rx.App()
