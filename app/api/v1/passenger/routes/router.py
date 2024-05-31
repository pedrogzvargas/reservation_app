from fastapi import APIRouter
from fastapi import status
from fastapi import Response
from app.api.v1.passenger.models import PassengerModel
from app.api.v1.passenger.models import PatchPassengerModel
from app.api.v1.passenger.models import ListResponseBody
from app.api.v1.passenger.models import CreateResponseBody
from app.api.v1.passenger.models import DeleteResponseBody
from modules.passenger.domain import PassengerExistException
from modules.passenger.domain import PassengerDoesNotExistException
from modules.passenger.infraestructure import CreatePassengerController
from modules.passenger.infraestructure import PatchPassengerController
from modules.passenger.infraestructure import AllPassengerController
from modules.passenger.infraestructure import DeletePassengerController


router = APIRouter(prefix="/passengers", tags=["passengers"], )


@router.get("/", response_model=ListResponseBody, status_code=status.HTTP_200_OK)
def list(response: Response):
    try:
        all_passenger_controller = AllPassengerController()
        all_passenger = all_passenger_controller()
    except Exception:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"message": "INTERNAL_SERVER_ERROR", "data": []}
    else:
        return {"message": "OK", "data": all_passenger}


@router.post("/", response_model=CreateResponseBody, status_code=status.HTTP_201_CREATED)
def create(passenger: PassengerModel, response: Response):
    try:
        create_passenger_controller = CreatePassengerController()
        create_passenger_controller(
            id=passenger.id,
            name=passenger.name,
            last_name=passenger.last_name,
        )
    except PassengerExistException as exception:
        response.status_code = status.HTTP_406_NOT_ACCEPTABLE
        return {"message": exception.__str__()}
    else:
        return {"message": "OK"}


@router.patch("/{passenger_id}", response_model=CreateResponseBody, status_code=status.HTTP_200_OK)
def patch(passenger_id, passenger: PatchPassengerModel, response: Response):
    try:
        patch_passenger_controller = PatchPassengerController()
        patch_passenger_controller(
            passenger_id=passenger_id,
            passenger_data=passenger.model_dump(exclude_none=True),
        )
    except PassengerExistException as exception:
        response.status_code = status.HTTP_406_NOT_ACCEPTABLE
        return {"message": exception.__str__()}
    else:
        return {"message": "OK"}


@router.delete("/{passenger_id}", response_model=DeleteResponseBody, status_code=status.HTTP_200_OK)
def delete(passenger_id, response: Response):
    try:
        delete_passenger_controller = DeletePassengerController()
        delete_passenger_controller(passenger_id)
    except PassengerDoesNotExistException as exception:
        response.status_code = status.HTTP_406_NOT_ACCEPTABLE
        return {"message": exception.__str__()}
    else:
        return {"message": "OK"}
