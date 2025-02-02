# **Tarkoitus**

```etsi.py``` on simppeli Python-scripti, joka pyrkii listaamaan kaikki suomen kielen sanat, jotka voidaan kokonaan koostaa emojeista. Esim. pomppia (🅿️🅾️Ⓜ️🅿️🅿️ℹ️🅰️) tai bingo (🅱️ℹ️🆖🅾️).

# **Emojien valinnasta**

Lienee mielipidekysymys mitkä tässä lasketaan emojeiksi. Esimerkkejä rajatapauksista:
* Esim. ©️, ®️ ja ℹ️ tulostuvat joissain konteksteissa merkkeinä ©, ® ja ℹ
* Emojit kuten ™️ ja 🔙 sisältävät tekstin aika pienessä roolissa. Jälkimmäisessä teksti ei edes sisälly kaikkiin emojin laitekohtaisiin versioihin.
* Emojit 🔛 ja 🆙 sisältävät tekstin lisäksi huutomerkin, joten on vähän kyseenalaista kannattaako ne olla mukana.

Tämä on kuitenkin oma valintani ja sitä on helppoa tarvittaessa muuttaa. Käytettyjen emojien joukko saattaa myös olla puutteellinen ja jäänee päivittämättä jos sopivia emojeja lisätään standardiin.

# **Asentaminen**

```bash
git clone https://github.com/ttahelenius/emojisanat.git
```

Huom: Python 3.9+ vaadittu.

# **Sana-aineiston tekijänoikeudet**

```nykysuomensanalista2022.txt``` on adaptoitu Kotimaisten kielten keskuksen Nykysuomen sanalistasta 2022. Saatavissa https://kaino.kotus.fi/lataa/nykysuomensanalista2022.csv

# **Briefly in English**

This Python script attempts to list all Finnish words that can be represented by emojies. The source code is written in and for Finnish but is simple enough to be adapted to any language with an appropriate replacement for the word list file.
