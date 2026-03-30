# Tests for State Machines

from src.atlasdoc_domain_model_v1.state_machines import DocumentStateMachine
from src.atlasdoc_domain_model_v1.entities import Document
import pytest

def test_document_state_machine_initialization():
    doc = Document(title='Test Doc', content='Initial content')
    state_machine = DocumentStateMachine(doc)
    assert state_machine.state == 'draft'

def test_document_publish_transition():
    doc = Document(title='Test Doc', content='Initial content')
    state_machine = DocumentStateMachine(doc)
    state_machine.publish()
    assert state_machine.state == 'published'

@pytest.mark.parametrize('initial_state', ['published', 'archived'])
def test_document_publish_invalid_transition(initial_state):
    doc = Document(title='Test Doc', content='Initial content')
    state_machine = DocumentStateMachine(doc)
    state_machine.state = initial_state
    with pytest.raises(ValueError):
        state_machine.publish()