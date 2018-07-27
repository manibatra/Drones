from channels.testing import WebsocketCommunicator
from drones.consumers import DroneConsumer, DashboardConsumer
from channels.testing import HttpCommunicator
import pytest

@pytest.mark.asyncio
async def test_my_consumer():

    communicator = WebsocketCommunicator(DroneConsumer, "/testws/")
    connected, subprotocol = await communicator.connect()
    assert connected

    d_communicator = WebsocketCommunicator(DashboardConsumer, "/testws/")
    d_connected, d_subprotocol = await d_communicator.connect()
    assert d_connected
    # Test sending text
    await communicator.send_json_to({ "id" : 0,
                                      "lat": 32,
                                      "long": 32,
                                      "speed": 10})

    response = await d_communicator.receive_json_from()
    # response = await communicator.receive_from()
    assert response == { "id" : 0,
                         "latitude": 32,
                         "longitude": 32,
                         "speed": 10}
    # Close
    await communicator.disconnect()
    await d_communicator.disconnect()
