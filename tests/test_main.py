import pytest
from src.main import DataProcessor

def test_add_item():
    processor = DataProcessor()
    test_item = {'id': 1, 'active': True}
    processor.add_item(test_item)
    assert processor.data[0] == test_item

def test_get_item():
    processor = DataProcessor()
    test_item = {'id': 1, 'active': True}
    processor.add_item(test_item)
    assert processor.get_item(0) == test_item
    assert processor.get_item(1) is None

def test_process_data():
    processor = DataProcessor()
    items = [
        {'id': 1, 'active': True},
        {'id': 2, 'active': False},
        {'id': 3, 'active': True}
    ]
    for item in items:
        processor.add_item(item)
    
    processed = processor.process_data()
    assert len(processed) == 2
    assert all(item['active'] for item in processed)
