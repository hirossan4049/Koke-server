from pydantic import BaseModel
from typing import List

class Track(BaseModel):
    name: str
    time: int

#@dataclass_json
#@dataclass
class TrackLists(BaseModel):
    trackId: str
    trackName: str
    tracks: List[Track]
