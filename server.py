#from dataclasses import dataclass

from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

from model import Track, Tracklists

#from dataclasses_json import dataclass_json

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get("/latest-tracklists")
async def get_latest_tracklists():
    tl = [
        TrackLists(trackId="EPYsq5InQyQ", trackName="Vintage Culture live at @ So Track Boa Festival - São Paulo 2019 FULL SHOW", tracks=[]),
        TrackLists(trackId="zbqSOzLE8YI", trackName="【LIVE】ひきこもりでもLIVEがしたい！～すーぱーまふまふわーるど2021＠東京ドーム～ONLINE", tracks=[]),
        TrackLists(trackId="0RDufdbphBE", trackName="Oliver Heldens - Live at Tomorrowland (Heldeep Stage)", tracks=[]),
        TrackLists(trackId="L4bNpQSKTAg", trackName="Krush by KVSH #4 (Nov. 14, 2021)", tracks=[]),
        TrackLists(trackId="", trackName="", tracks=[]),
        TrackLists(trackId="", trackName="", tracks=[]),
        TrackLists(trackId="", trackName="", tracks=[]),
        TrackLists(trackId="", trackName="", tracks=[]),
        TrackLists(trackId="", trackName="", tracks=[]),
    ]
    return JSONResponse(content=jsonable_encoder(tl))

@app.get("/tracklists/{trackId}")
async def get_tracklists(trackId: str):
    if trackId == "zbqSOzLE8YI":
        tracks = [
                Track(name="ベルセルク", time=200), 
                Track(name="最終宣告", time=408),
                Track(name="罰ゲーム ", time=641),
                Track(name="アルターエゴ", time=1049),
                Track(name="悔やむと書いてミライ", time=2147),
                Track(name="携帯恋話", time=2559),
                Track(name="デジャヴ", time=3230),
                Track(name="おとといきやがれ", time=3723),
                Track(name="女の子になりたい", time=4545),
                Track(name="忍びのすすめ", time=5503),
                Track(name="イカサマダンス", time=5959),
                Track(name="ユウレイ", time=10435),
                Track(name="さえずり", time=10944),
                Track(name="ひともどき", time=11712),
                Track(name="生まれた意味などなかった", time=12203),
                Track(name="命に嫌われている", time=12714),
                Track(name="輪廻転生", time=13134),
                Track(name="拝啓ドッペルゲンガー", time=13559),
                Track(name="曼珠沙華", time=14552),
                Track(name="夜空のクレヨン", time=15003),
                Track(name="夢のまた夢", time=15440),
                ]
        tl = TrackLists(trackId="zbqSOzLE8YI", trackName="【LIVE】ひきこもりでもLIVEがしたい！～すーぱーまふまふわーるど2021＠東京ドーム～ONLINE", tracks=tracks)
        return JSONResponse(content=jsonable_encoder(tl))

    tracks = [
            Track(name="Vintage Culture - Free (feat. Fancy Inc & Roland Clark)", time=1), 
            Track(name=" Sofi Tukker - Drinkee (Vintage Culture & John Summit Remix)", time=418),
            Track(name=" Ben Sterling - Dimensions (Original Mix)", time=825),
            Track(name="Darude - Sandstorm (Vintage Culture Unrealesed Remix)", time=1300),
            Track(name="Chris Lake - A Drug From God (Original Mix)", time=1551),
            ]
    tl = TrackLists(trackId="ああ", trackName="Vintage Culture live at Laroc", tracks=tracks)
    #return tl.to_json(ensure_ascii=False)
    return JSONResponse(content=jsonable_encoder(tl))

@app.post("/tracklists/update/{trackId}")
async def post_update_tracklists(trackId: str, tracklists: TrackLists):
    return {"status": "fail"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app)
