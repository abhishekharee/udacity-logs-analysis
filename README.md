# Project: Logs Analysis

## Description
This project creates a tool using a python script (LogsAnalysis.py) that prints answers to the following questions, based on data stored in the 'news' database - a database supplied by Udacity:

1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

## Prerequisites
This project requires the following to be in place prior to successful execution:
- Ubuntu 16.04 LTS (available [here](http://releases.ubuntu.com/16.04/))
- Python 2.7.12 (available [here](https://www.python.org/downloads/release/python-2712/))
- PostgreSQL 9.5 (available [here](https://www.enterprisedb.com/downloads/postgres-postgresql-downloads))
- The 'news' database (availalable [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)).
- The Python script included in this repository ([LogsAnalysis.py](https://github.com/abhishekharee/udacity-logs-analysis/blob/master/LogsProject.py)). **This file must be stored in the same direcotry as the 'news' database.**

_Note: The above set up can be achieved via a virtual machine. Set up of a virtual machine is optional, and beyond the scope of this README._

## Set up
1. Download and install the first three dependencies above, if not available already.
2. Open the terminal.
3. Load the news database into PostgreSQL by executing the command `psql -d news -f newsdata.sql`.

## Execution
After downloading and installing the prerequisites, and after setting up the 'news' database (both as described above), the tool can be run to retrieve the answers to the stated questions at the top of this README.

Run the tool by running the following command in terminal (from the directory where the 'news' database and LogsAnalysis.py file are stored):

`python LogsAnalysis.py`

This command will print the answers to the above three questions in the terminal window. These results are also stored in the LogsAnalysisOutputs.txt file in this repository.
