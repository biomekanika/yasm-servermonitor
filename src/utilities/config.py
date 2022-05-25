import yaml


class HostConfig:
    def __init__(self, name, host, port):
        self.name = name
        self.host = host
        self.port = port


def getHosts(configFile):    

    with open(configFile, 'r') as file:
        config = yaml.safe_load(file)

    returnList = []
    for item in config['hosts']:
        returnList.append(HostConfig(item['name'], item['host'], item['port']))

    return returnList