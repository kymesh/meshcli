from datetime import datetime
from typing import override

from textual.app import ComposeResult
from textual.containers import Vertical, VerticalScroll
from textual.events import Callback
from textual.widgets import Input, Static


class ChatWindow(Vertical):
    longname: str
    messages: list[str]
    message_scroll: VerticalScroll
    message_display: Static
    input_box: Input

    def __init__(self, longname: str, send_callback=None, **kwargs):
        super().__init__(**kwargs)
        self.longname = longname
        self.messages = []
        self.send_callback = send_callback

        self.message_scroll = VerticalScroll()
        self.message_scroll.styles.width = "100%"

        self.message_display = Static()

        self.input_box = Input()

    @override
    def compose(self) -> ComposeResult:
        yield self.message_scroll
        yield self.input_box

    async def on_mount(self):
        await self.message_scroll.mount(self.message_display)

    def on_input_submitted(self, event: Input.Submitted) -> None:
        message = event.value.strip()
        if message:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.messages.append(
                f" [dim]{timestamp}[/dim]\n[blue] You[/blue]: {message}\n"
            )
            self.update_display()
            self.input_box.value = ""
            if self.send_callback and self.longname:
                _ = self.app.call_later(self.send_callback, self.longname, message)

    def update_display(self):
        self.message_display.update("\n".join(self.messages))
        self.message_scroll.scroll_end(animate=False)
