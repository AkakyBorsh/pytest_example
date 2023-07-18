from requests import Response, exceptions

def check_status(resp: Response, *args, **kwargs):
    resp.raise_for_status()
