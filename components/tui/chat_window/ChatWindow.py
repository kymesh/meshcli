from textual.widgets import Static, Input
from textual.containers import Vertical
from textual.app import ComposeResult


class ChatWindow(Vertical):
    """
    A chat window for a selected contact.
    """

    def __init__(self, longname: str, **kwargs):
        super().__init__(**kwargs)
        self.longname = longname
        self.messages = []
        self.message_display = Static()
        self.input_box = Input(placeholder="Type a message and press Enter...")
        self.input_box.border_title = f"Chat with {longname}"

    def compose(self) -> ComposeResult:
        yield self.message_display
        yield self.input_box

    def on_input_submitted(self, event: Input.Submitted) -> None:
        message = event.value.strip()
        if message:
            self.messages.append(f"You: {message}")
            self.update_display()
            self.input_box.value = ""

    def update_display(self):
        self.message_display.update("\n".join(self.messages))
