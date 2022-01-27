import re
import fire
from dateutil import parser
from datetime import datetime
from datetime import date
from dateutil.parser import parse
import logging
from config import config_rules

logger = logging.getLogger(__name__)

class Pipeline(object):

    config = config_rules()

    def __init__(self) -> None:
        self.initialize()
    
    def initialize(self):
        try:
            # Set up logging
            logging.basicConfig(format="%(asctime)s - %(levelname)s - %(filename)s -   %(message)s",datefmt="%d/%m/%Y %H:%M:%S",level=logging.INFO)
        except Exception as e:
            logging.exception("### Error occurred while initializing pipeline. Info: " + str(e))
            exit()

    def is_date(self,string, fuzzy=True):
        """
            Return whether the string can be interpreted as a date.

            :param string: str, string to check for date
            :param fuzzy: bool, ignore unknown tokens in string if True
        """
        try: 
            parse(string, fuzzy=fuzzy)
            return True
        except ValueError:
            return False

    
    def format_date(self,date):
        """
            Format any date input to a standard date format

            Inputs:
                * date: string containing dates

        """
        if re.search("Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec", date): 
            dt = date.split()
            months = {"jan":"01","feb":"02", "mar": "03", "apr":"04", "may":"05", "jun":"06", "jul":"07", "aug":"08", "sep":"09", "oct":"10", "nov":"11", "dec":"12"}
            month = months[dt[0][0:3].lower()]
            day = int(dt[1].lower().replace(",","").replace("th","").replace("st",""))
            year = int(dt[2])
            if int(month) >12:
                day_b = day
                day = month
                month = day_b
            date =  str(month) + "/" + str(day) + "/" + str(year)

        try:
            dt = date.replace("-","/").split("/")
            d1,d2,d3 = int(dt[0]), int(dt[1]), int(dt[2])
            day = d2 if d1 <=12 else d1
            month = d1 if d1 <=12 else d2
            d =  str(month) + "/" + str(day) + "/" + str(d3)
            return datetime.strptime(d, "%m/%d/%Y").strftime("%Y-%m-%d")
        except Exception as e:
            return date


    def regex_matches(self,text:str, rule:str=r"\b[0-9]{2}[/-][0-3][0-9][/-][1-2](0|1|9)[0-9]{2}\b"):
        """
            Giver a text and which rule to use, return all matches 

            Inputs:
                * text: A full text to be used for rules extraction
                * rule: Regex rule to be used
        """
        matches = []
        for match in re.finditer(
                rule,
                text,
        ):
            start, end = match.start(), match.end()
            if self.is_date(text[start:end]):
                matches.append(
                    {
                        "start": start,
                        "end": end,
                        "token": text[start:end],
                        "source": "Regex",
                        "type": "Dates",
                    }
                )
        return matches

    def match_dates(self,text:str,format=True,eightify=False):
        """
            Match any date of a giving text 

                Find all regex matches, based on a given rule

                Inputs:
                    * text: a full text to be annalysed
                    * format: whether or not to format the output to string
                    * eightify: change all number to 8 (helps on de-identification)
                    * rules: Please provide your rule-based rules inside of config.py
                    return:
                        * matches: A list of dictionaries containing all regex matches, with start, end, and token
                    * 
        """

        all_dates = []

        for rule in self.config["rules"]:
            dates = self.regex_matches(text,rule)
            for date in dates:
                token = date['token']

                if format:
                    token = self.format_date(token)
                if eightify:
                    try:
                        token = re.sub(r'\d', u'8',token)
                    except Exception as e:
                        token = date['token']

                new_match = {"regex_output":date,"token":token}
                if new_match not in all_dates:
                            all_dates.append(new_match)

        return all_dates

if __name__ == "__main__":

    fire.Fire(Pipeline)


