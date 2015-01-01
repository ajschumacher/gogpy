import requests

def gog(x, url="http://localhost:4808/data", visible=False):
    """
    This function takes takes a pandas DataFrame and sends it to
    a gog server. The gog server is responsible for passing the data
    to a gog frontend for visualization.

    Parameters
    ----------
    x : a pandas DataFrame
    url : the gog /data endpoint to send to
    visible : whether to return the response
    """
    text = x.to_json(orient='records')
    response = requests.post(url, data=text)
    if visible:
        return Response
    else:
        return None
