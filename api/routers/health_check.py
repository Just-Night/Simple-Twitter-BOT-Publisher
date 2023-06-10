from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi import status


router = APIRouter(prefix='/api', tags=['example'])


@router.get('/health-check')
async def health_check():
    """Health check

    Returns:
        dict: status
    """
    return JSONResponse({"status": "ok"}, status_code=status.HTTP_200_OK)
