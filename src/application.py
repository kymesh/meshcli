from datetime import datetime

from .chat_db import ChatDB
from .mesh_connection import MeshConn
from .chat_window import ChatWindow

from textual.app import App, ComposeResult
from textual.containers import Horizontal
from textual.widgets import Footer, Header, Label, ListItem, ListView, Static


class MeshCLI(App):
    BINDINGS = [("d", "toggle_dark", "Toggle dark mode")]

    def __init__(self):
        super().__init__()
        self.db: ChatDB = ChatDB()
        self.conn: MeshConn = MeshConn(on_message_callback=self.handle_incoming_message)
        self.chat_window: ChatWindow = ChatWindow(
            "Select a contact", send_callback=self.send_message
        )
        self.contact_list = ListView()
        self.connection_label = Static()

    def handle_incoming_message(self, longname, message):
        self.call_later(self._display_incoming_message, longname, message)

    async def _display_incoming_message(self, longname, message):
        if self.chat_window.longname == longname:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.chat_window.messages.append(
                f" [dim]{timestamp}[/dim]\n[red] {longname}[/red]: {message}\n"
            )
            self.chat_window.update_display()
            self.db.save_message(longname, longname, message)

    def compose(self) -> ComposeResult:
        yield Header()
        self.contact_list.styles.width = "35%"
        self.chat_window.styles.width = "65%"
        yield self.connection_label
        with Horizontal():
            yield self.contact_list
            yield self.chat_window
        yield Footer()

    async def on_mount(self) -> None:
        node_name = self.conn.get_this_node()
        self.connection_label.update(f"[bold green]Connected to:[/] {node_name}")

        for name in self.conn.get_long_names():
            # Don't select our own node
            if name != node_name:
                await self.contact_list.append(ListItem(Label(name)))

    def action_toggle_dark(self) -> None:
        self.theme = (
            "textual-dark" if self.theme == "textual-light" else "textual-light"
        )

    async def on_list_view_selected(self, message: ListView.Selected) -> None:
        selected_label = message.item.query_one(Label)
        name = str(selected_label.renderable)
        self.chat_window.longname = name
        self.chat_window.input_box.border_title = f"Chat with {name}"
        self.chat_window.messages = []

        for sender, msg, timestamp in self.db.load_messages(name):
            timestamp = timestamp[0:10] + " " + timestamp[11:19]
            if sender == "You":
                self.chat_window.messages.append(
                    f" [dim]{timestamp}[/dim]\n[blue] You[/blue]: {msg}\n"
                )
            else:
                self.chat_window.messages.append(
                    f" [dim]{timestamp}[/dim]\n[red] {sender}[/red]: {message}\n"
                )

        self.chat_window.update_display()

    async def send_message(self, longname: str, message: str):
        await self.conn.send_message(longname, message)
        self.db.save_message(longname, "You", message)
