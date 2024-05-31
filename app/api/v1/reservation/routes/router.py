from fastapi import APIRouter
from fastapi import status
from fastapi import Response
from app.api.v1.reservation.models import ReservationModel
from app.api.v1.reservation.models import ListResponseBody
from app.api.v1.reservation.models import CreateResponseBody
from app.api.v1.reservation.models import DeleteResponseBody
from modules.reservation.domain import ReservationExistException
from modules.reservation.domain import ReservationDoesNotExistException
from modules.reservation.infraestructure import ReservationCreatorController
from modules.reservation.infraestructure import AllReservationController
from modules.reservation.infraestructure import DeleteReservationController
from modules.passenger.domain import PassengerDoesNotExistException


router = APIRouter(prefix="/reservations", tags=["reservations"], )


@router.get("/", response_model=ListResponseBody, status_code=status.HTTP_200_OK)
def list(response: Response):
    try:
        all_reservation_controller = AllReservationController()
        all_reservations = all_reservation_controller()
    except Exception:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"message": "INTERNAL_SERVER_ERROR", "data": []}
    else:
        return {"message": "OK", "data": all_reservations}


@router.post("/", response_model=CreateResponseBody, status_code=status.HTTP_201_CREATED)
def create(reservation: ReservationModel, response: Response):
    try:
        reservation_creator_controller = ReservationCreatorController()
        reservation_creator_controller(
            id=reservation.id,
            passenger_id=reservation.passenger_id,
            seat=reservation.seat,
        )
    except (ReservationExistException, PassengerDoesNotExistException) as exception:
        response.status_code = status.HTTP_406_NOT_ACCEPTABLE
        return {"message": exception.__str__()}
    else:
        return {"message": "OK"}


@router.delete("/{reservation_id}", response_model=DeleteResponseBody, status_code=status.HTTP_200_OK)
def delete(reservation_id, response: Response):
    try:
        delete_reservation_controller = DeleteReservationController()
        delete_reservation_controller(reservation_id)
    except ReservationDoesNotExistException as exception:
        response.status_code = status.HTTP_406_NOT_ACCEPTABLE
        return {"message": exception.__str__()}
    else:
        return {"message": "OK"}
