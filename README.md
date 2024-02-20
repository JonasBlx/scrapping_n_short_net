# Scrapped data available on this link :
https://drive.google.com/drive/folders/1CdBSJm8qG70b2SO4-wPK63-kriW0F-_Q?usp=sharing

### Environnement

#### 1. To create the environment
```
python -m venv env
```
#### 2. Activate the environment
```
.\env\Scripts\Activate.ps1
```
#### 3.Install the modules
```
pip install -r requirements.txt
```

---

### Project Structure:

#### 1. scraper/
Description: Contains scripts or modules dedicated to collecting data from online sources. This includes Python scripts using Selenium.

#### 2. data/
raw/ : Stores data as it is collected by the scraping scripts, without modification. In this case, it's mainly PDFs.
processed/ : Contains data that has been cleaned, transformed, or enriched after scraping, ready for analysis, here they are in CSV format.
external/ : For additional data obtained from external sources, which are not the result of scraping but are necessary for the analysis. For example, a file for converting Company Name<>Ticker.

#### 3. notebooks/
Used for data exploration, exploratory analysis, and visualization. Jupyter Notebooks are particularly useful here for documenting the analysis process step by step.

#### 4. src/
utils/ : Contains reusable utility functions, such as data cleaning functions, transformations, or connectors to databases.
analysis/ : Python modules for specific analyses, which can be run independently or used in notebooks.

####5. output/
results/ : For the results of the analysis, such as CSV files.
figures/ : For generated visualizations, like graphs or maps saved in image format.

#### 6. docs/
For project documentation, including scraping methodology, data descriptions, and analysis conclusions.

####7. requirements.txt
To list all the dependencies necessary for running the project, facilitating the replication of the development environment.

#### 8. .gitignore
To exclude sensitive or large files (like raw scraped data) from version control.

---

### How to resolve merging conflict in jupyter notebooks :
https://www.linkedin.com/pulse/resolve-conflict-jupyter-notebook-dhiraj-patra/
