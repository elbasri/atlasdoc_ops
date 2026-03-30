# State Machines

class DocumentStateMachine:
    def __init__(self, document: 'Document'):
        self.document = document
        self.state = 'draft'