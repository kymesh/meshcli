from textual.widgets import Static, Input
from textual.containers import Vertical
from textual.app import ComposeResult
from datetime import datetime


class ChatWindow(Vertical):
    """
    A chat window for a selected contact.
    """

    def __init__(self, longname: str, send_callback=None, **kwargs):
        super().__init__(**kwargs)
        self.longname = longname
        self.messages = []
        self.send_callback = send_callback
        self.message_display = Static()
        self.input_box = Input(placeholder="Type a message and press Enter...")
        self.input_wrapper = Static(self.input_box)
        self.input_wrapper.border_title = f"Chat with {longname}"

    def compose(self) -> ComposeResult:
        yield self.message_display
        yield self.input_box

    def on_input_submitted(self, event: Input.Submitted) -> None:
        message = event.value.strip()
        if message:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.messages.append(f" [dim]{timestamp}[/dim]\n[blue] You[/blue]: {message}\n")
            self.update_display()
            self.input_box.value = ""
            if self.send_callback and self.longname:
                self.app.call_later(self.send_callback, self.longname, message)

    def update_display(self):
        self.message_display.update("\n".join(self.messages))
