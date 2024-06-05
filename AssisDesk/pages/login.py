"""The home page of the app."""
import reflex as rx
from AssisDesk_API.templates import template
import requests


class LoginState(rx.State):
    username: str = ""
    password: str = ""
    token: str = ""
    is_logged_in: bool = False

    def login(self):
        response = requests.post("http://localhost:8000/token", data={"username": self.username, "password": self.password})
        if response.status_code == 200:
            self.token = response.json()["access_token"]
            self.is_logged_in = True
        else:
            rx.window_alert("Invalid credentials")


@template(route="/login", title="Log In")
def login() -> rx.Component:

    return rx.card(
        rx.vstack(
            rx.center(
                rx.image(
                    src="/logo.jpg",
                    width="2.5em",
                    height="auto",
                    border_radius="25%",
                ),
                rx.heading(
                    "Sign in to your account",
                    size="6",
                    as_="h2",
                    text_align="center",
                    width="100%",
                ),
                direction="column",
                spacing="5",
                width="100%",
            ),
            rx.vstack(
                rx.text(
                    "Email address",
                    size="3",
                    weight="medium",
                    text_align="left",
                    width="100%",
                ),
                rx.input(
                    placeholder="user@reflex.dev",
                    type="email",
                    size="3",
                    width="100%",
                    on_blur=LoginState.set_username
                ),
                justify="start",
                spacing="2",
                width="100%",
            ),
            rx.vstack(
                rx.hstack(
                    rx.text(
                        "Password",
                        size="3",
                        weight="medium",
                    ),
                    rx.link(
                        "Forgot password?",
                        href="#",
                        size="3",
                    ),
                    justify="between",
                    width="100%",
                ),
                rx.input(
                    placeholder="Enter your password",
                    type="password",
                    size="3",
                    width="100%",
                    on_blur=LoginState.set_password
                ),
                spacing="2",
                width="100%",
            ),
            rx.button("Sign in", on_click=LoginState.login, size="3", width="100%"),
            rx.center(
                rx.text("New here?", size="3"),
                rx.link("Sign up", href="#", size="3"),
                opacity="0.8",
                spacing="2",
                direction="row",
            ),
            spacing="6",
            width="100%",
        ),
        size="4",
        max_width="28em",
        width="100%",
    )
