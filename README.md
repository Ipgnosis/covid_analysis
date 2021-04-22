# covid_analysis

This is a work in progress...

A Jupyter Notebook for covid analysis.

Like many others, I have been fascinated (not to mention horrified) by the Covid-19 pandemic.  What I knew about virology and epidemiology before 2020 could be written on a postage stamp, but now I am as up to speed as any layperson on these topics.  But, I have many (many) questions for which I am unable to find answers.

## Data Source:

So... I decided to kick of an analysis, but first needed some (reliable) data.  I found 'Our World in Data' (i.) (https://ourworldindata.org/coronavirus) which is a project based at the Oxford Martin School at the University of Oxford, UK.  As described here (https://ourworldindata.org/covid-sources-comparison), this data is based on a range of sources, but particularly the European Center for Disease Control and Prevention as well as Johns Hopkins University.

The full data can be downloaded from https://ourworldindata.org/coronavirus-source-data or https://github.com/owid/covid-19-data/tree/master/public/data.  The data is available in either .json, .csv or .xlsx format and is updated at least once per day.

## Hypotheses:
	1. Economic strength correlates to high performance in pandemic management
	2. Population density correlates to contagion
	3. Underlying health has had an effect on infection and death
	4. Government policy has affected infection & death rates
    5. National culture has an effect on contagion
	6. Winter means more cases
	7. Islands are better at managing infection?

## Questions:
	1. How have counties performed overall?
	2. How has country performance changed over time?
	3. Has GDP had any effect on performance?
	4. Has geography, population density, culture and seasons played a role in contagion?

## Goal(s):

    1. Write some articles on the findings from above
    2. Build a website providing (interactive?) analysis from the above and supporting the article(s)
    3. Build an API to support the website, since the data is too large to download within a page (currently approaching 50Mb).  A prototype is up and running on Azure.  I'll probably post that code in another repo.


(i.) Max Roser, Hannah Ritchie, Esteban Ortiz-Ospina and Joe Hasell (2020) - "Coronavirus Pandemic (COVID-19)". Published online at OurWorldInData.org. Retrieved from: 'https://ourworldindata.org/coronavirus' [Online Resource]
