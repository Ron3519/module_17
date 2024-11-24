from fastapi import APIRouter



router = APIRouter(tags=["task"], prefix="/task")

@router.get("/")
async def all_task():
    pass

@router.get("/user_id")
async def task_by_id():
    pass

@router.post("/create")
async def create_task():
    pass

@router.put("/update")
async def update_task():
    pass

@router.delete("/delete")
async def delete_task():
    pass