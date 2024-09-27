from fastapi import Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError

async def custom_exception_handler(request: Request, exc: RequestValidationError):
    for error in exc.errors():
        if error["msg"] == "Input should be greater than 0":
            return JSONResponse(status_code=402,
                                content={"status": "error", "message": "ID should be greater than 0"}
                                )
        if error["msg"] == "Input should be a valid dictionary or object to extract fields from":
            return JSONResponse(status_code=402,
                                content={"status": "error", "message": "ID should be json"}
                                )
        else:
            return JSONResponse(status_code=402,
                                content={"status": "error", "message": error["msg"]}
                                )