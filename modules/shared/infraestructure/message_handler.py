from modules.passenger.infraestructure import PassengerCreatedSubscriber
from modules.passenger.infraestructure import PassengerPatchedSubscriber


message_handler = {
    "passenger_app.passenger_created": PassengerCreatedSubscriber,
    "passenger_app.passenger_patched": PassengerPatchedSubscriber,
}
