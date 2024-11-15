from typing import Annotated
from fastapi import APIRouter, Depends
from starlette.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT

from wapang.app.order.dto.requests import PlaceOrderRequest
from wapang.app.order.dto.responses import OrderDetailResponse
from wapang.app.order.service import OrderService
from wapang.app.user.models import User
from wapang.app.user.views import login_with_header


order_router = APIRouter()


@order_router.post("/orders", status_code=HTTP_201_CREATED)
def place_order(
    user: Annotated[User, Depends(login_with_header)],
    order_service: Annotated[OrderService, Depends()],
    place_order_request: PlaceOrderRequest,
) -> OrderDetailResponse:
    return order_service.place_order(user.id, place_order_request)


@order_router.get("/orders/{order_id}", status_code=HTTP_200_OK)
def search_order(
    order_id: int,
    order_service: Annotated[OrderService, Depends()],
) -> OrderDetailResponse:
    return order_service.search_order(order_id)


@order_router.delete("/orders/{order_id}", status_code=HTTP_204_NO_CONTENT)
def cancel_order(
    user: Annotated[User, Depends(login_with_header)],
    order_id: int,
    order_service: Annotated[OrderService, Depends()],
) -> None:
    order_service.cancel_order(user.id, order_id)


@order_router.post("/orders/{order_id}/complete", status_code=HTTP_204_NO_CONTENT)
def confirm_order(
    user: Annotated[User, Depends(login_with_header)],
    order_id: int,
    order_service: Annotated[OrderService, Depends()],
) -> None:
    order_service.confirm_order(user.id, order_id)