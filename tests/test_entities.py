# Tests for Entities

from src.atlasdoc_domain_model_v1.entities import Document
import pytest

def test_document_initialization():
    doc = Document(title='Test Doc', content='Initial content')
    assert doc.title == 'Test Doc'
    assert doc.content == 'Initial content'

def test_document_update_content():
    doc = Document(title='Test Doc', content='Initial content')
    doc.update_content('Updated content')
    assert doc.content == 'Updated content'