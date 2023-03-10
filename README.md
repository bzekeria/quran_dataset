# Quran

## Table of Contents
1. [Overview](#overview)
   - [Structure of the Quran](#structure)
   - [Directory Tree](#directory)
2. [Instructions](#instructions)
3. [Disclaimer](#disclaimer)
4. [Other Related Work](#related_work)

<a id='overview'></a>
## Overview
The Quran is the official religious text of Islam. The one and only book for Muslims which has been read and memorized by thousands across the globe in the Arabic language. 

*The goal for this repository is to have the Quran in a readeable data format to apply a data science question.*

In this repository, some words in this ```README.md``` and variable names in the respective ```.ipynb```/```.py``` files will be in *Arabic* though written in *English*. Here's a glossary of those terms:

<a id='structure'></a>
### Structure of the Quran
- ```Surah```: Chapter (e.g. The Quran has a total of 114 chapters)
- ```Ayah```: Verse
- ```Juz```: Part (i.e. The Quran is divided into 30 parts)

![Image](img/quran_data_ch_1-2.png)
*Mock data. See ```data``` folder for updated dataset*

<a id='directory'></a>
### Directory Tree
```bash
quran_dataset
├── data
│   ├── holy_quran.json 
│   ├── surahs # CSV file for all 114 surahs
├── img
│   ├── quran_data_ch_1-2.png # for README.md
├── README.md
├── quran_df.ipynb # in-progress
├── quran_df.py # in-progress
├── quran_json_download.py 
├── surah_df.ipynb
└── surah_df.py 
```

<a id='instructions'></a>
## Instructions
1. Create the following folders/subfolders locally
   - ```data```
   - ```data/surahs```
1. Install the following libraries: ```json```, ```numpy```, ```pandas```, ```requests```, ```scipy```
1. Run ```quran_df.py``` (Quran CSV file) and/or ```surah_df.py``` (Surah CSV file. If you want data for multiple surahs, simply run the file again)

<a id='disclaimer'></a>
## Disclaimer
The data compiled here (```holy_quran.json```) is derived from [Al Quran Cloud API](https://alquran.cloud/api). 

The purpose and intent of this repository is to aid in the *understanding* of the Quran. 

What do I mean by *understanding*? There are many data science tools/methods one can explore by using this data, NOT understanding the text itself, as the data compiled here has no related features. 

If there's an error in the ```ayahs``` column (e.g., missing a word, تشكيل/Tashkil (i.e. Arabic vowelization), ayahs being out of order, etc.), one should consult the Quran as that's the only correct source. 

**The data presented does not and will never precede the Quran.**

<a id='related_work'></a>
## Other Related Work
- [Unique Words for Each Surah](https://github.com/mmayet/quran_sandbox)
- [Quran Similarity Search](https://github.com/jawadshuaib/quran-similarity-search)
