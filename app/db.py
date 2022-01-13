from tinydb import TinyDB, Query
from time import time
from pprint import pprint # debug

from app.model import Track, TrackLists

class DB():
    def __init__(self):
        self.db = TinyDB("db.json")

    def set(self, tracklists):
        #data = self.get(tracklists.trackId)
        #print(data)
        tracks = []
        for item in tracklists.tracks:
            tracks.append({"name": item.name, "time": item.time})

        self.db.insert({
            "trackId": tracklists.trackId,
            "trackName": tracklists.trackName,
            "update_at": time(),
            "tracks": tracks
        })

    def get(self, trackId):
        que = Query()
        try:
            data = self.db.search(que.trackId == trackId)[-1]
            tracks = []
            for item in data["tracks"]:
                tracks.append(
                    Track(
                        name = item["name"],
                        time = item["time"]
                    )
                )

            tl = TrackLists(
                trackId = data["trackId"],
                trackName = data["trackName"],
                tracks = tracks
            )
            return tl
        except:
            return None

    def get_latest(self, get_count=10, page=0):
        que = Query()
        try:
            #return self.db.all()[(page*get_count):(page*get_count+get_count)]
            datas = self.db.all()
            pprint(datas)
            print("======================")
            ids = list(set([e["trackId"] for e in datas]))[(page*get_count):(page*get_count+get_count)]
            # FIXME: 適当
            result = []
            for i in ids:
                result.append(self.get(i))
            #aaa = [e for i, e in enumerate(datas) if e['track_id'] not in ids[0:i]]
            #pprint(aaa)
            return result
        except IndexError:
            return []

    def delete(self, trackId):
        que = Query()                                           
        data = self.db.search(que.trackId == trackId)[-1]
        print(data)
        self.db.remove(que["update_at"] == data["update_at"])

    def deleteAll(self, trackId):
        que = Query()                                           
        self.db.remove(que.trackId == trackId)


    def update(self, trackId):
        pass         

if __name__ == "__main__":
    db = DB()
    print("get latest")
    pprint(db.get_latest())
    print("set")
    db.set(TrackLists(
        trackId = "test",
        trackName = "トラック名",
        tracks = [Track(name="intro",time= 0)]
    ))
    print("set2")
    db.set(TrackLists(
        trackId = "dabadaba",
        trackName = "うんこ",
        tracks = [Track(name="intro",time= 2)]
    ))
    pprint(db.get_latest())
    print("get latest")
    pprint(db.get("test"))
