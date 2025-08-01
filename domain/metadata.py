from dataclasses import dataclass
from typing import Dict, Any

@dataclass
class Metadata:
    data: Dict[str, Any]

    def get(self, key: str) -> Any:
        return self.data.get(key)

    def set(self, key: str, value: Any) -> None:
        self.data[key] = value