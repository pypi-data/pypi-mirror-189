## Overview

The report package provides command-line interface to get 
information about Monaco Race 2019:
* date of the race ;
* start time of the race;
* number of the racers;
* report of the race;
* information about driver;
* list of all racers in the race;
* list of all teams in the race;
* list of all racers in specific team;

## System Requirements

report is written for Python 3. The following
sub-versions are supported:

* Python 3.9
* Python 3.10

## Install

`pip install report`

## CLI Usage Example

For all reports `--files` argument is required.
`--files` argument is path of directory where report files are located.
Example of the report files:
* `abbreviations.txt` (contains information about racer in a form `SVF_Sebastian Vettel_FERRARI`)
* `start.log` (contains Q1 start time of racers in a form `SVF2018-05-24_12:02:58.917`)
* `end.log` (contains Q1 finish time of racers in a form `SVF2018-05-24_12:04:03.332`)

**_NOTE:_** Name of the files and content form should be exactly as in example.


More information about usage
`pyhton -m report.report -h`

Date of the race:
`python -m report.report -f <path> --date`

Start time of the race:
`python -m report.report -f <path> --time`

Number of the racers:
`python -m report.report -f <path> --racers-number`

Report of the race:
`python -m report.report -f <path> --report`

Information about driver:
`python -m report.report -f <path> --driver <full name>`

List of the racers:
`python -m report.report -f <path> --racers <[asc, desc]>`

List of the teams:
`python -m report.report -f <path> --teams <[asc, desc]>`

List of the racers from specific team:
`python -m report.report -f <path> --team-racers <team name>`


**_NOTE:_** More than one argument can be passed in one time. Example:
`python -m report.report -f <path> --report -d -t --racers asc`


Package can be used in your project:
```python
from report_race import race

race_valid = race.LogFilesValidator("path/to/directory")
race = race_valid.init_race()
```
Ande then you can use it like that:
```python
race.get_racer("name_of_the_racer")
race.get_number_of_racers()
```
