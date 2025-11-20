from fastapi import APIRouter

from app.schemas.products import ProductCreate
from app.schemas.general import CreateSuccess
from app.services.products import create_product

router = APIRouter(prefix="/v1/products")

@router.post("/create")
async def create_product(data: ProductCreate) -> CreateSuccess:
    return await create_product(data)
