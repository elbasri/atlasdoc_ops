from .entities import Document

class DocumentStateMachine:
    def __init__(self, document: Document):
        self.document = document
        self.state = 'draft'

    def submit_for_review(self) -> None:
        if self.state == 'draft':
            self.state = 'review'

    def publish(self) -> None:
        if self.state == 'review':
            self.state = 'published'