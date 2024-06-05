"""The home page of the app."""

import reflex as rx

from AssisDesk_API.components.login_card import login_card
from AssisDesk_API.templates import template


@template(route="/login", title="Log In")
def login() -> rx.Component:
    """The home page.

    Returns:
        The UI for the home page.
    """

    return rx.center(
        login_card()
    )