from tinydb import TinyDB, Query
from time import time

from model import Track, TrackLists

class DB():
    def __init__(self):
        self.db = TinyDB("db.json")

    def set(self, tracklists):
        data = self.get(tracklists.trackId)
        print(data)
        self.db.insert(
            {
                "trackId": tracklists.trackId,
                "update_at": int(time()),
                "data": data.append(tracklists)
            }
        )

    def get(self, trackId):
        que = Query()
        try:
            return self.db.search(que.trackId == trackId)[0]
        except:
            return []

    def get_latest(self, get_count=10, page=0):
        que = Query()
        try:
            return self.db.all()[(page*get_count):(page*get_count+get_count)]
        except IndexError:
            return []



    def delete(self, trackId, update_at):
        que = Query()
        self.db.remove(que.trackId == trackId and que.update_at == update_at)

    def update(self, trackId):
        pass         

if __name__ == "__main__":
    db = DB()
    print("get latest")
    print(db.get_latest())
    print("set")
    db.set(TrackLists(
        trackId = "test",
        trackName = "トラック名",
        tracks = [Track(name="intro",time= 0)]
    ))
    print("get latest")
    print(db.get_latest())
