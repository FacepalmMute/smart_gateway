import paho.mqtt.publish as publish

publish.single("paho/test/topic", "payload", hostname="127.0.0.1")