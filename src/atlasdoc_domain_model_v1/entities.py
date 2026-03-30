from typing import Optional

class Document:
    def __init__(self, title: str, content: str):
        self.title = title
        self.content = content

    def update_content(self, new_content: str) -> None:
        self.content = new_content