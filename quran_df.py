import json

import numpy as np
import pandas as pd
from scipy.stats import mode

### 1. Read in ```holy_quran.json```

f = open("data/holy_quran.json", "r", encoding="utf-8")

data = json.load(f)

### 2. Convert JSON string to pandas object

df = pd.read_json("data/holy_quran.json")

## Quran ```DataFrame()```

surah_lst = []
for chapter in range(0, 114):
    surah_lst.append(df["data"]["surahs"][chapter]["name"])

surah_english_lst = []
for chapter in range(0, 114):
    surah_english_lst.append(df["data"]["surahs"][chapter]["englishName"])

surah_english_translation_lst = []
for chapter in range(0, 114):
    surah_english_translation_lst.append(
        df["data"]["surahs"][chapter]["englishNameTranslation"])

revelation_type_lst = []
for chapter in range(0, 114):
    revelation_type_lst.append(df["data"]["surahs"][chapter]["revelationType"])

num_ayahs_lst = []
for chapter in range(0, 114):
    num_ayahs_lst.append(len(df["data"]["surahs"][chapter]["ayahs"]))

juz_lst = []
for chapter in range(0, 114):
    surah_juz_lst = []
    for ayah in range(0, len(df["data"]["surahs"][chapter]["ayahs"])):
        surah_juz_lst.append(
            df["data"]["surahs"][chapter]["ayahs"][ayah]["juz"])
    # calculate the mode (returns the smallest mode if there are multiple modes)
    juz_lst.append(mode(surah_juz_lst)[0][0])

ayahs_lst = []
for chapter in range(0, 114):
    surah_ayahs_lst = []
    for ayah in df["data"]["surahs"][chapter]["ayahs"]:
        surah_ayahs_lst.append(ayah["text"])
    ayahs_lst.append(surah_ayahs_lst)

quran_df = pd.DataFrame({"surah_no": [i for i in range(1, 115)],
                         "surah_name_arabic": surah_lst,
                         "surah_name_english": surah_english_lst,
                         "surah_name_english_translation": surah_english_translation_lst,
                         "revelation_type": revelation_type_lst,
                         "num_ayahs": num_ayahs_lst,
                         "juz": juz_lst,
                         "ayahs": ayahs_lst
                         })

#### surah_name_arabic
quran_df["surah_name_arabic"] = quran_df["surah_name_arabic"].apply(
    lambda x: " ".join(x.split("سُورَةُ")[1:]))

#### ayahs
# convert series object to a list
quran_df["ayahs"] = quran_df["ayahs"].apply(lambda x: [i for i in x])

# fix this

### Export ```quran_df```

quran_df.to_csv("data/holy_quran.csv", index=False)
