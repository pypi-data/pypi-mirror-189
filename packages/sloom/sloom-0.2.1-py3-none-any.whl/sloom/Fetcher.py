import requests
from .RequestError import *
from .Response import *
from .Responses import *



class Fetcher:
    """
    Fetch a url and its contents
    methods:
    - get_page(url: String) -> Response
    - get_all_pages(urls: [String]) -> Responses
    """
    def __init__(self) -> None:
        pass

    def get_page(self, url):
        """
        Retrive a single page
        """
        try:
            r = requests.get(url)
        except:
            return RequestError(404, url)
        status_code = r.status_code
        html_content = r.text
        return Response(html_content, url) if status_code == 200 else RequestError(status_code, url)

    def get_all_pages(self, urls):
        """
        Retrive all pages
        """
        contents = Responses()
        for url in urls:
            response = self.get_page(url)
            contents.append(response)
        return contents