from fastapi import APIRouter

router = APIRouter(prefix="/api", tags=["Hot Commands"])

@router.get("/hotcommands/ping")
async def ping():
    return {"message": "Hot Commands router connected!"}
