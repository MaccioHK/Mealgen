from dataclasses import dataclass
from typing import List, Optional

@dataclass(frozen=True)
class GenerateRequest:
    category: str                      # "seafood" | "meat"
    exclusions: List[str]              # ["beef","pork",...]
    persons: int                       # 1..12 (you can adjust)
    meal_type: str                     # "daily" | "special" | "festival"
    special_kind: Optional[str] = None # "anniversary"|"wedding"|"friends"
    festival_kind: Optional[str] = None# "easter"|"christmas"
