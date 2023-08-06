from bs4 import BeautifulSoup
from .Topic import *
from .Core.List import *
from .Core.Terminal import *
from .href import href

BS4_FEATURES = "lxml"

class Scraper:
    """
    Param:
        response: Response
    Attributes:
        title: str
        topic: [Topic]
        date: datetime
        url: str
    """
    def __init__(self, resonpse) -> None:
        self.response = resonpse
        self.topic = List(Topic)
        self.date = None
        self.url = resonpse.url
        self.origin = self.response.origin
        self.subdomain = self.response.subdomain
        self._soup = BeautifulSoup(resonpse.text, features = BS4_FEATURES)
        self.title = self.getTitle()

    def getTitle(self) -> str:
        """
        Get The title of a webpage
        """
        for title in self._soup.find_all("title"):
            return title.text
            
    
    def getTopics(self):
        """
        Get topics of a webpage
        """
        pass
    
    def getDate(self):
        """
        Gets date of webpage
        """
        pass

    
    def clean(self):
        """
        Remove all style and js tags
        """
        # parse html content
    
        for data in self._soup(['style', 'script']):
            # Remove tags
            data.decompose()
    
        # return data by retrieving the tag content
        return ' '.join(self._soup.stripped_strings)

    def gethref(self) -> List:
        """
        Returns a list of links
        """
        hrefList = List(href)
        hrefList.extend([href(a['href'], self.origin, self.subdomain) for a in self._soup.find_all('a', href = True)])
        return hrefList

    def __str__(self):
        return f"""
        title = {self.title}
        topic = {self.topic}
        date = {self.date}
        url = {self.url}
        origin = {self.origin}
        """

