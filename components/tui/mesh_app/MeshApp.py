from textual.widgets import Header, Footer, ListView, ListItem, Label, Static
from textual.containers import Horizontal
from textual.app import App, ComposeResult

from components.data.ChatDB import ChatDB
from components.mesh_conn.MeshConn import MeshConn
from components.tui.chat_window.ChatWindow import ChatWindow
from datetime import datetime


class MeshApp(App):
    """
    Main app.
    """

    BINDINGS = [("d", "toggle_dark", "Toggle dark mode")]

    def __init__(self):
        super().__init__()
        self.db = ChatDB()
        self.conn = MeshConn(on_message_callback=self.handle_incoming_message)
        self.chat_window = ChatWindow("Select a contact", send_callback=self.send_message)
        self.contact_list = ListView()
        self.connection_label = Static()
    
    def handle_incoming_message(self, longname, message):
        self.call_later(self._display_incoming_message, longname, message)

    async def _display_incoming_message(self, longname, message):
        if self.chat_window.longname == longname:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.chat_window.messages.append(f" [dim]{timestamp}[/dim]\n[red] {longname}[/red]: {message}\n")
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
                self.chat_window.messages.append(f" [dim]{timestamp}[/dim]\n[blue] You[/blue]: {msg}\n")
            else:
                self.chat_window.messages.append(f" [dim]{timestamp}[/dim]\n[red] {sender}[/red]: {message}\n")
        
        self.chat_window.update_display()
    
    async def send_message(self, longname: str, message: str):
        await self.conn.send_message(longname, message)
        self.db.save_message(longname, "You", message)
