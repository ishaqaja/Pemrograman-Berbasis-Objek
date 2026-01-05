from .base_repository import BaseRepository
from typing import List, Any

# Implementasi penyimpanan sederhana (List)
class MemoryRepository(BaseRepository):
    def __init__(self):
        self._storage = []

    def add(self, item: Any):
        self._storage.append(item)

    def get_all(self) -> List[Any]:
        return self._storage
    
    def find_by_id(self, uid: str):
        for item in self._storage:
            if item.uid == uid:
                return item
        return None