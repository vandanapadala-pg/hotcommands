from fastapi import APIRouter

router = APIRouter(prefix="/api", tags=["Spaces"])

@router.get("/spaces/ping")
async def ping():
    return {"message": "Spaces router connected!"}
