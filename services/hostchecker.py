import utilities.serverping as serverping
import utilities.config as config


def pingHost(host):

    return serverping.ping(host)


def getHostStatus(hostList):

    responseList = []
    for host in hostList:
        response = serverping.ping(host.host)
        host.code = response.code
        host.text = response.text
        responseList.append(host)

    return responseList
