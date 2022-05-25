import os


class Response:
    def __init__(self, host, code, text):
        self.host = host
        self.code = code
        self.text = text


def ping(host):

    command = f"ping -c 1 {host} >/dev/null 2>&1"
    resultCode = os.system(command)
    resultText = ""

    # Handle ping result
    if (0 == resultCode):
        resultText = "Online"

    elif (256 == resultCode):
        resultText = "Destination Unreachable"

    elif (512 == resultCode):
        resultText = "Name or Service Unknown"

    else:
        resultText = "Unknown Error"

    return Response(host, resultCode, resultText)
