# als_etl_exercise

This is the documentation for the *constituents* data wrangling exercise. I chose to use *Pandas*, *Python* and *Jupyter Notebook* (optional) 
as per recommendation. The code is rather simple and does all the cleansing and writing in a single file, `etl.py`.

## Files and directories
- `etl.py` reads in data from `data/` for *constituents*, *subscriptions* and *emails*; cleanses and saves reports
- `data_exploration.ipynb` file I used as a "scratch pad" to get a feel of the data and do rough drafts of the cleansing
- `data/` directory where the raw input CSVs should be

## preflight instructions
1) ensure *Pandas* is installed locally `pip install pandas` or `conda install pandas`
2) optional, if you wish to view the Jupyter notebook, `pip install jupyter` or `conda install jupyter`. Invoke in working directory of cloned repo with `jupyter notebook` which should provide a URL which you can paste into your browser. Ex:
```
To access the notebook, open this file in a browser:                           
file:///C:/Users/Grantitup/AppData/Roaming/jupyter/runtime/nbserver-17532-open.html 
Or copy and paste one of these URLs:                                           
http://localhost:8888/?token=8ccd5ffb2c141d5a464d2aac3f33e7b777cca09eed8f1bb3
```
From there, click on the file `data_exploration.ipynb`

3) create a directory called `data` in the working directory, download and store the linked data in it:
- [cons](https://als-hiring.s3.amazonaws.com/fake_data/2020-07-01_17%3A11%3A00/cons.csv)
- [emails](https://als-hiring.s3.amazonaws.com/fake_data/2020-07-01_17%3A11%3A00/cons_email.csv)
- [email chapter subscriptions](https://als-hiring.s3.amazonaws.com/fake_data/2020-07-01_17%3A11%3A00/cons_email_chapter_subscription.csv)

4) run the *ETL* script, `python etl.py`, *people* and *acquisition_facts* CSVs will be generated in the working directory.
