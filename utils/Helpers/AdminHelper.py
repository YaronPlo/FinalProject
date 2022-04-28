import json
from utils import routes

__all__ = ["writeAnalystRules", "slide_it", "changeVerticalStatus"]


# this function sets the % of the vertical slider.
def slide_it(lbl, val):
    lbl.setText(f'{val * 25}%')


def changeVerticalStatus(*args):
    isChecked = args[0]
    for ver in args[1:]:
        if isChecked:
            ver.setEnabled(True)
        else:
            ver.setEnabled(False)


# this function get rules from GUI and sets them into a Json file.
def writeAnalystRules(analystID, date, wsm, vSlider1, vSlider2, vSlider3, vSlider4, confidentiality, integrity,
                      availability, includeKwords, excludeKeywords):
    newRules = {
        "date": date.isChecked(),  # True/ False
        "wsm": {"state": wsm.isChecked(), "slider1": vSlider1.value(), "slider2": vSlider2.value(),
                "slider3": vSlider3.value(), "slider4": vSlider4.value()},
        "confidentiality": confidentiality.isChecked(),  # True/ False
        "integrity": integrity.isChecked(),  # True/ False
        "availability": availability.isChecked(),  # True/ False
        "include": includeKwords.text(),  # Text
        "exclude": excludeKeywords.text(),  # Text
        "avg_per_task": "",
        "avg_per_day": ""
    }
    with open(routes.rulesFile) as rules:
        rulesDB = json.load(rules)
    rulesDB[analystID] = newRules
    with open(routes.rulesFile, 'w') as rules:
        json.dump(rulesDB, rules, indent=2)
