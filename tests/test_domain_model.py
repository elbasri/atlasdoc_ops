# Tests for Domain Model
import pytest
from src.atlasdoc.domain_model.entities import Document
from src.atlasdoc.domain_model.state_machines import DocumentStateMachine

def test_document_creation():
    doc = Document(title='Test Doc', content='Initial content')
    assert doc.title == 'Test Doc'
    assert doc.content == 'Initial content'

def test_document_update_content():
    doc = Document(title='Test Doc', content='Initial content')
    doc.update_content('Updated content')
    assert doc.content == 'Updated content'

def test_state_machine_transitions():
    doc = Document(title='Test Doc', content='')
    sm = DocumentStateMachine(doc)
    sm.submit_for_review()
    assert sm.state == 'review'
    sm.approve()
    assert sm.state == 'approved'

if __name__ == '__main__':
    pytest.main()