from fastapi import Depends
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter

from nepali_dictionary.core.search.service import SearchService
from nepali_dictionary.mixins.database import DBMixin

router = InferringRouter()


@cbv(router)
class SearchCBV(DBMixin):
    search_service: SearchService = Depends(SearchService)

    @router.get("/")
    def meaning(self, query: str):
        result = self.search_service.search(query, self.session, self.engine)
        return {"data" : result}
