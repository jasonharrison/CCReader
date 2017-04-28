import getpass
import re

visa = "^4[0-9]{12}(?:[0-9]{3})?$"
mastercard = "^5[1-5][0-9]{14}$"
american_express = "^3[47][0-9]{13}$"
diners_club = "^3(?:0[0-5]|[68][0-9])[0-9]{11}$"
discover = "^6(?:011|5[0-9]{2})[0-9]{12}$"
jcb = "^(?:2131|1800|35\d{3})\d{11}$"


def parsecard(data):
    try:
        data = data.replace("\n", "")
        number = data.split("%B")[1].split("^")[0]
        raw_name = data.split("^")[1].split("^")[0]
        exp_month = data.split("^")[2][:4][2:]
        exp_year = data.split("^")[2][:2]
        try:
            name = raw_name.split("/")[1]
            name += " " + raw_name.split("/")[0]
        except IndexError:
            name = raw_name
        name = " ".join(name.split())
        if re.search(visa, number):
            type = "Visa"
        elif re.search(mastercard, number):
            type = "MasterCard"
        elif re.search(american_express, number):
            type = "American Express"
        elif re.search(diners_club, number):
            type = "Diners Club"
        elif re.search(discover, number):
            type = "Discover"
        elif re.search(jcb, number):
            type = "JCB"
        else:
            type = None
        result = {"number": number, "raw_name": raw_name, "name": name, "exp_month": exp_month,
                  "exp_year": "20" + exp_year}
        if type:
            result['type'] = type
        return result
    except IndexError:
        return None


def swipecard():
    result = None
    attempt = 0
    while result is None:
        attempt += 1
        if attempt == 1:  # first try
            data = getpass.getpass("Swipe card.")
        else:
            data = getpass.getpass("Error.  Swipe card again.")
        result = parsecard(data)
    return result


if __name__ == "__main__":
    print(swipecard())
