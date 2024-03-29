import os

from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware

from app.model import Track, TrackLists
from app.db import DB

print("SVARA_PASS =================")
if SVARA_PASS := os.environ.get("SVARA_PASS"):
    print(SVARA_PASS)
else:
    print("$SVARA_PASS をセットしてください。")
print("============================")

app = FastAPI()
db = DB()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get("/")
async def root(response_class=HTMLResponse):
    return HTMLResponse(content="""
<html>
<head><title>omg!</title></head>
<body>
<script type="text/javascript">
(async function() {
    const joke = await fetch("https://icanhazdadjoke.com/", {headers: {Accept: "text/plain"}})
    document.body.innerText = await joke.text()
})()
</script>
</body>
</html>
""", status_code=200)

@app.get("/latest-tracklists")
async def get_latest_tracklists():
    return JSONResponse(content=jsonable_encoder(db.get_latest()))

@app.get("/tracklists/{trackId}")
async def get_tracklists(trackId: str):
    data = db.get(trackId)
    print(data)
    return JSONResponse(content=jsonable_encoder(data))

@app.post("/tracklists/update/{trackId}")
async def post_update_tracklists(trackId: str, tracklists: TrackLists):
    db.set(tracklists)
    print(tracklists)
    return {"status": "success"}

@app.delete("/tracklists/{trackId}")
async def delete_tracklists(trackId: str, password: str, isAll: bool = False):
    print(password, SVARA_PASS)
    if password == SVARA_PASS:
        try:
            if isAll:
                db.deleteAll(trackId)
            else:
                db.delete(trackId)
        except Exception as e:
            print("error", e)
            return {"status": "fail"}
        return {"status": "success"}
    else:
        return {"status": "fail"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app)
