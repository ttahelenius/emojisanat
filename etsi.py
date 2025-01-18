#!/usr/bin/python
# -*- coding: utf-8 -*-

emojiosat = {"A": "🅰", "B": "🅱", "AB": "🆎", "CL": "🆑", "O": "🅾", "SOS": "🆘", "WC": "🚾", "P": "🅿",
             "NG": "🆖", "OK": "🆗",  "0": "0️⃣", "1": "1️⃣", "2": "2️⃣", "3": "3️⃣", "4": "4️⃣", "5": "5️⃣",
             "6": "6️⃣", "7": "7️⃣", "8": "8️⃣", "9": "9️⃣", "10": "🔟", "C": "©", "R": "®", "TM": "™",
             "END": "🔚", "BACK": "🔙", "SOON": "🔜", "TOP": "🔝", "COOL": "🆒", "NEW": "🆕",
             "FREE": "🆓", "ABC": "🔤", "M": "Ⓜ", "UP": "🆙", "ON": "🔛", "I": "ℹ", "ID": "🆔",
             "VS": "🆚"}

def emojifioi(str, aiemmatOsat=""):
    if len(str) == 0:
        return [aiemmatOsat]
    lista = []
    for osa in emojiosat:
        if str.upper().startswith(osa):
            tulos = emojifioi(str[len(osa):], aiemmatOsat + emojiosat[osa])
            lista.extend(tulos)
    return lista

if __name__ == "__main__":
    sanalista = open("nykysuomensanalista2022.txt", "r", encoding='utf-8')
    for sana in sanalista:
        sana = sana[:-1] # rivivaihto pois
        osat = emojifioi(sana)
        for osa in osat:
            print(osa)
    sanalista.close()