from textual.widgets import Header, Footer, ListView, ListItem, Label
from textual.containers import Horizontal
from textual.app import App, ComposeResult

from components.mesh_conn.MeshConn import MeshConn
from components.tui.chat_window.ChatWindow import ChatWindow


class MeshApp(App):
    """
    Main app.
    """

    BINDINGS = [("d", "toggle_dark", "Toggle dark mode")]

    def __init__(self):
        super().__init__()
        self.conn = MeshConn()
        self.chat_window = ChatWindow("Select a contact")
        self.contact_list = ListView()

    def compose(self) -> ComposeResult:
        yield Header()
        with Horizontal():
            yield self.contact_list
            yield self.chat_window
        yield Footer()

    async def on_mount(self) -> None:
        """Populate the ListView after widgets are mounted."""
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
        self.chat_window.update_display()
