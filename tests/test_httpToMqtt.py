# mqttClient -> httpServer
# mqttBroker <-> [ mqttClient -> httpServer ] <-> browser
import paho.mqtt.publish as publish
import requests
from src.gateway import *
from src.ports import *
from src.connectors import *
import time

from logging import info, debug, warning, error, basicConfig, DEBUG
basicConfig(format='%(levelname)s:%(message)s', level=DEBUG)

import paho.mqtt.subscribe as subscribe

TEST_BROKER = "127.0.0.1"

def clearTopic(topic: str):
    publish.single(topic, "", hostname=TEST_BROKER, retain=True)

def publishMessage(topic: str, payload: str):
    publish.single(topic, payload, hostname=TEST_BROKER, retain=True)

def httpGet(url: str) -> str:
    response = requests.get(f"http://127.0.0.1:8080/{url}", timeout=2, verify=False)
    return response.text

def test_simpleHttpGetRequest():
    address = "my/funky/address"
    payload = "mySecret"

    # Prepare mqtt broker with message
    clearTopic(address)
    publishMessage(address, payload)

    # Initialize gateway
    gateway = Gateway(InputPort(), OutputPort())
    gateway.setConnector(SideType.LEFTSIDE, MqttClientConnector)
    gateway.setConnector(SideType.RIGHTSIDE, HttpConnector)

    # Ask over http for payload
    time.sleep(2)
    httpResponse = httpGet(address)

    assert payload == httpResponse
    info("Test succeeded!")
