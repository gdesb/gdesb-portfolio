# Portfolio


In this portfolio I am sharing some of the projects I completed for the MIT xPRO Professional Certificate in Data Engineering.

  - [City bus transit data application](#city-bus-transit-data-application)
  - [US retail sales data - Extract-Transform-Load and data analyses](#us-retail-sales-data---extract-transform-load-and-data-analyses)
  - [Predicting housing prices using linear and log-linear regression](#predicting-housing-prices-using-linear-and-log-linear-regression)

## City bus transit data application 
___using Python, Jupyter Notebook, Docker, MySQL, MongoDB, Maven, Debezium, Mapbox, Flask, APIs___

The full code is in this [repo](https://github.com/gdesb/gdesb-portfolio/blob/main/city-bus-transit-data/).
- Wrote Python code to call an API that provides the position (longitude and latitude) of buses along a city bus route every 10 seconds
- In a Flask web application, added Python code to plot the buses on a map using Mapbox
- Parsed the incoming JSON data and stored it in a MySQL database
- Performed change data capture (CDC) on the MySQL database using Debezium and propagated changes to a MongoDB database (using Docker containers)
- Collected over 60 hours of real-world, public, transit data from this bus route
- Wrote Python code in a [Jupyter notebook](https://github.com/gdesb/gdesb-portfolio/blob/main/city-bus-transit-data/city-bus-transit-data-analyses.ipynb) to analyze the data, with summary statistics of the total duration of the bus route, graphs, and brief discussion
 
## US retail sales data - Extract-Transform-Load and data analyses
___using Python, pandas, numpy, matplotlib, seaborn, Jupyter Notebook, MySQL___

The full code is in this [repo](https://github.com/gdesb/gdesb-portfolio/blob/main/us-retail-sales-etl-data-analyses/).
- Extracted the latest data from the Monthly Retail Trade Survey (MRTS) from the US Census Bureau
- Wrote Python code to transform the data into a DataFrame, clean it, and export it both as a comma-separated values (CSV) file and as a table in MySQL
- Wrote Python code to analyze the data and visualize the results using matplotlib and seaborn

## Predicting housing prices using linear and log-linear regression
___using Python, Jupyter Notebook, scikit-learn, numpy, pandas, matplotlib___

The full project, which I coded in Python in a Jupyter notebook, is in this [repo](https://github.com/gdesb/gdesb-portfolio/blob/main/predicting-housing-prices-using-regression/).
- Loaded the Ames housing database (available on Kaggle)
- Performed data exploration and found that the distribution of the dependent variable (house sale price) is skewed and that a log-transform may be beneficial
- Explored which variables would be good candidates as independent variables for linear regression
- Processed missing data: dropped columns that had lots of missing data, performed linear interpolation otherwise
- Tested 6 different versions of the regression model -- using 7, 14, or 20 independent variables, and with or without log-transforming the dependent variable.
