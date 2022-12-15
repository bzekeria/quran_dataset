# Quran (Islam)

## Overview
The Quran is the official religious text of Islam. The one and only book for Muslims which has been read and memorized by thousands across the globe in the Arabic language. 

*The goal for this repository to get the Quran in a readeable data format and apply a data science question.*

In this repository, some variable names will be in *Arabic* though written in *English*. Here's a glossary of the variable names:

Structure of the Quran
- ```Surah```: Chapter (e.g. The Quran has a total of 114 surahs)
- ```Ayahs```: Verse
- ```Juz```: Part (i.e. The Quran is divided into 30 parts)

```bash
├── data
│   ├── holy_quran.json 
├── README.md
├── quran_json_df.ipynb # in-progress
└── quran_json_download.py 
```

## Disclaimer
The purpose and intent of this repository is aid in the *understanding* of the Quran. 

What do I mean by *understanding*? As in there's many data science tools/method one can explore by using this data NOT understanding the text in it of itself as the data compiled here has no features related to that. For instance, one can get into the nitty gritty details of the various stylistic word choices or understanding the differences based off where the surah was revelated. 

The data compiled here (```holy_quran.json```) is derived from [Al Quran Cloud API](https://alquran.cloud/api). If there's an error (e.g., missing a word, vowelization), one should consult the Quran. **The data presented does not and will never proceed the Quran.**

## Other Related Work
- [Unique Words for Each Surah](https://github.com/mmayet/quran_sandbox)
- [Similar Verses in the Quran](https://github.com/jawadshuaib/quran-similarity-search-jupyter-notebooks)
