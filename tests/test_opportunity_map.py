# Tests for AtlasDoc Phase-2 Opportunity Map

import pytest
from src.atlasdoc_ops.phase2.opportunity_map import generate_opportunity_map

def test_generate_opportunity_map(capsys):
    """
    Test the opportunity map generation.
    """
    generate_opportunity_map()
    captured = capsys.readouterr()
    assert captured.out == 'Generating opportunity map...\n'