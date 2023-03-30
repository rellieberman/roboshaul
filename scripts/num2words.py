import os


baseDictMale = {
    "1":"אחד",
    "2": "שניים",
    "3": "שלושה",
    "4": "ארבעה",
    "5": "חמישה" ,
    "6": "שישה",
    "7": "שבעה",
    "8": "שמונה",
    "9": "תשעה",
    "10": "עשרה",
}
baseDictfemale = {
    "1":"אחת",
    "2": "שתיים",
    "3": "שלוש",
    "4": "ארבע",
    "5": "חמיש" ,
    "6": "שיש",
    "7": "שבע",
    "8": "שמונ",
    "9": "תשע",
    "10": "עשר",
}
decadesDict = {
        "20": "עשרים",
    "30": "שלושים",
    "40": "ארבעים",
    "50": "חמישים" ,
    "60": "שישים",
    "70": "שבעים",
    "80": "שמונים",
    "90": "תשעים",
}
teenDictF = {
        "11": "אחת עשרה",
    "12": "שתים עשרה",
    "13": "שלוש עשרה",
    "14": "ארבע עשרה",
    "15": "חמש עשרה" ,
    "16": "שש עשרה",
    "17": "שבע עשרה",
    "18": "שמונה עשרה",
    "19": "תשע עשרה",
}

teenDictM = {
        "11": "אחד עשר",
    "12": "שנים עשר",
    "13": "שלושה עשר",
    "14": "ארבעה עשר",
    "15": "חמשה עשר" ,
    "16": "ששה עשר",
    "17": "שבעה עשר",
    "18": "שמונה עשר",
    "19": "תשעה עשר",
}

centDict ={
    "1": "מאה",
    "2": "מאתיים"
}



for i in range(9,-1, -1):
    print(i)
def num2words(num):
    """

    """
    if num<=10:
        return baseDictfemale[str(num)]
    elif 21>num and num>10:
        return teenDictF[str(num)]
    elif
