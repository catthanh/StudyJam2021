## Qwiklabs completed courses checker

### From GDSC VNU with ♥

### Features
* This script is a web crawler which help us to get the completed courses from Qwiklabs profile links and check if these courses is in the accepted courses.
* The imported and exported data type is .csv  
### Running
You must install [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) library first.

```bash
pip install beautifulsoup4
```
in.csv format:
|email|name|profile_qwiklabs|
|-----|----|-----------------|
|example@e.com|Ironman sucks|https://www.qwiklabs.com/public_profiles/xxxxxxxx-1eaa-4e3f-801a-4e611cf8da42|
|example@e.net|Batman is cool|https://www.qwiklabs.com/public_profiles/xxxxxxxx-1eaa-4e3f-801a-4e611cf8da42|

to run the script
```bash
python check.py
```

