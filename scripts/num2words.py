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
    "5": "חמש" ,
    "6": "שש",
    "7": "שבע",
    "8": "שמונה",
    "9": "תשע",
    "10": "עשר",
}
decadesDict = {
        "2": "עשרים",
    "3": "שלושים",
    "4": "ארבעים",
    "5": "חמישים" ,
    "6": "שישים",
    "7": "שבעים",
    "8": "שמונים",
    "9": "תשעים",
}
teenDictF = {
    "1": "אחת",
    "2": "שתיים",
    "3": "שלוש",
    "4": "ארבע",
    "5": "חמיש",
    "6": "שש",
    "7": "שבע",
    "8": "שמונה",
    "9": "תשע",
    "10": "עשר",
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
adjBaseDictfemale = {
    "1":"אחת",
    "2": "שתיים",
    "3": "שלושת",
    "4": "ארבעת",
    "5": "חמשת" ,
    "6": "ששת",
    "7": "שבעת",
    "8": "שמונת",
    "9": "תשעת",
    "10": "עשרת",
}



def baseNum2words(num, flag=False):
    """

    """
    words = []
    if num >=100:
        flag = True
        if num>=300:
            words.append(baseDictfemale[str(int(num/100))]+" ")
            words.append("מאות ")
        elif num>=200 and num<300:
            words.append("מאתיים ")
        elif num < 200 and num >= 100:
            words.append("מאה ")
        num = num % 100
    if num >= 20:
        words.append(decadesDict[str(int(num/10))]+" ")
        num = num % 10
        if num>0:
            words.append("ו")
            words.append(baseDictfemale[str(int(num))])
    elif num < 20 and num > 0:
        if flag:
            words.append("ו")
        words.append(teenDictF[str(num)])

    #words = "".join(words)
    return words

def num2words1m(num):

    if num>=1000 and num<2000:
        words = ["אלף "]+baseNum2words(num%1000, True)
    elif num<3000:
        words = ["אלפיים "] + baseNum2words(num % 1000, True)
    elif num<11000:
        words = [adjBaseDictfemale[str(int(num/1000))]+" "]+["אלפים "] + baseNum2words(num % 1000, True)
    else:
        words = baseNum2words(int(num / 1000)) + [" אלף "] + baseNum2words(num % 1000, True)
    return words

def num2words(num):
    if num < 1000:
        words =  baseNum2words(num)
    elif num<1000000:
        words = num2words1m(num)
    return words


for i in range(1,10000):
    print("".join(num2words(i)))


