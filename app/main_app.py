from fastapi import FastAPI

from app.api.v1.reservation.routes import reservation_router
from app.api.v1.passenger.routes import passenger_router

app = FastAPI(root_path="/api/v1", title="Traxion-Reservation-App")

app.include_router(reservation_router)
app.include_router(passenger_router)
