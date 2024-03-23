import json
from typing import Any, Dict
from logging import info, debug, warning, error

CONFIG_FILE = 'config.json'

# TODO dynamic global config file
jsonConfig: Dict[str, Any] = {
    "mqttClient": {
        "url": "mqtt.eclipseprojects.io",
        "port": 1883
    },

    "http": {
        "url": "127.0.0.1",
        "port": 8080
    }
}

def readConfig() -> Dict[str, Any]:
    with open(CONFIG_FILE) as f:
        return json.load(f)

def writeConfig(config: Dict[str, Any]) -> None:
    with open(CONFIG_FILE, 'w') as f:
        json.dump(config, f)

def loadConfig():
    jsonConfig = readConfig()
    globals().update(jsonConfig)
    info(f"Loaded config in {CONFIG_FILE}: {jsonConfig}")