from unittest.mock import Mock
from modules.shared.infraestructure import RabbitEventPublisher


import pytest


@pytest.mark.skip(reason="Only for test with rabbit running")
def test_rabbit_event_publisher():
    rabbit_event_publisher = RabbitEventPublisher()
    rabbit_event_publisher.publish = Mock(return_value=None)
    rabbit_event_publisher.publish({"id": "test"})
