from fastapi import FastAPI

from nepali_dictionary.core.search.views import router as search

app = FastAPI()

app.include_router(search, prefix="/search")
