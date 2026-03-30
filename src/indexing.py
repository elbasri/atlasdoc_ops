# indexing.py

def define_search_schema() -> dict:
    """
    Define the search schema for AtlasDoc.
    
    Returns:
        dict: The search schema definition.
    """
    return {
        "title": "AtlasDoc",
        "type": "object",
        "properties": {
            "id": {"type": "integer"},
            "title": {"type": "string"},
            "content": {"type": "string"}
        },
        "required": ["id", "title"]
    }


def create_index_strategy() -> str:
    """
    Outline the index strategy for AtlasDoc.
    
    Returns:
        str: The index strategy description.
    """
    return "Create an inverted index based on document titles and content."
