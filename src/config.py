"""
    Input Rules for Dates extraction
"""

def config_rules() -> dict:  

    config = {"rules": [r"\b[0-9]{2}[/-][0-3][0-9][/-][1-2](0|1|9)[0-9]{2}\b", 
                        r"\b[0-9][/-][0-3][0-9][/-][1-2](0|1|9)[0-9]{2}\b", 
                        r"\b[0-9][/-][1-9][/-][1-2](0|1|9)[0-9]{2}\b",
                        r"(\d{1,2}[-/]\d{1,2}[/-]\d{2,4})|(\d{1,2}/\d{4})|((?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*[ -.]*\d{2}[thsdn, .-]*\d{4})"
                        ]
             }

    return config

if __name__ == '__main__':
    pass