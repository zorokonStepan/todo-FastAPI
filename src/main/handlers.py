from fastapi import APIRouter


main_router = APIRouter()


@main_router.get("/")
async def welcome() -> dict:
    return {"message": "Hello!"}
