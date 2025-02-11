from typing import List, Dict, Optional

class DataProcessor:
    def __init__(self):
        self.data: List[Dict] = []

    def add_item(self, item: Dict) -> None:
        self.data.append(item)

    def get_item(self, index: int) -> Optional[Dict]:
        return self.data[index] if 0 <= index < len(self.data) else None

    def process_data(self) -> List[Dict]:
        return [item for item in self.data if item.get('active', False)]
