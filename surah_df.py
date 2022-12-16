import json

import pandas as pd

### 1. Read in ```holy_quran.json```

f = open("data/holy_quran.json", "r", encoding="utf-8")

data = json.load(f)

### 2. Convert JSON string to pandas object

df = pd.read_json("data/holy_quran.json")


## ```DataFrame()``` for each Surah

def surah_df(surah_no):
    surah_no = int(surah_no) - 1

    # ayahs
    surah_ayahs_lst = []
    for ayah in df["data"]["surahs"][surah_no]["ayahs"]:
        surah_ayahs_lst.append(ayah["text"])

    # whether there's a sajda in the respective ayah
    sajda_ayahs_lst = []
    for ayah in df["data"]["surahs"][surah_no]["ayahs"]:
        sajda_ayahs_lst.append(ayah["sajda"])

    surah_df = pd.DataFrame({"ayahs": surah_ayahs_lst,
                             "ayah_no": [i for i in
                                         range(1, len(surah_ayahs_lst) + 1)],
                             "sajda": sajda_ayahs_lst})

    # rename values
    surah_df["sajda"] = surah_df["sajda"].replace({True: "Yes", False: "No"})

    # export df to csv

    surah_df.to_csv(
        f"data/surahs/{surah_no + 1}_{df['data']['surahs'][surah_no]['englishName']}.csv",
        index=False)

    return surah_df


while True:
    try:
        ask_user = input("Which Quran chapter would you like to download? ")
        surah_df(int(ask_user))
        print("-- Surah",
              df['data']['surahs'][int(ask_user) - 1]['englishName'],
              "Download Complete!")
        print("-- File Name:",
              f"data/surahs/{int(ask_user)}_{df['data']['surahs'][int(ask_user) - 1]['englishName']}.csv")
        break
    except:
        print("No chapter found. Please choose a number between 1 to 114 \n")
        continue
