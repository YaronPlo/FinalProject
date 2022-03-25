import json
from utils import routes


# this function get rules from GUI and sets them into a Json file.
def writeAnalystRules(analystID, date, wsm, confidentiality, integrity, availability, includeKwords, excludeKeywords):
    newRules = {
        "date": date.isChecked(),  # True/ False
        "wsm": wsm.isChecked(),  # True/ False
        "confidentiality": confidentiality.isChecked(),  # True/ False
        "integrity": integrity.isChecked(),  # True/ False
        "availability": availability.isChecked(),  # True/ False
        "include": includeKwords.text(),  # Text
        "exclude": excludeKeywords.text(),  # Text
    }
    with open(routes.rulesFile) as rules:
        rulesDB = json.load(rules)
    rulesDB[analystID] = newRules
    with open(routes.rulesFile, 'w') as rules:
        json.dump(rulesDB, rules, indent=2)
