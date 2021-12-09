from fastapi import FastAPI, HTTPException
import aiofiles
import re

app = FastAPI()


async def get_data():
    file = dict()
    prg = re.compile("(.*\s),\s(.*)\s,(.*)")
    async with aiofiles.open("./nepali-dictionary/database/data.csv") as fp:
        for line in await fp.readlines():
            m = prg.match(line)
            s = m.group(2).strip(), m.group(3).strip()

            file[m.group(1).strip()] = s

    return file


@app.get("/v1/{word}")
async def meaning(word: str):
    data = await get_data()
    query = word.strip().lower()

    result = data.get(query)
    if result is None:
        raise HTTPException(
            status_code=404, detail=f"No meaning of word {query} found in the database."
        )

    return {"word": query, "meaning": f"({result[0]}) {result[1]}"}
