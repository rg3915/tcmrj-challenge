from ninja import NinjaAPI

from backend.call.api import router as call_router

api = NinjaAPI()

api.add_router("/call/", call_router)
