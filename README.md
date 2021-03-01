# Election_Analysis
Automating election results
## Overview of Election Audit
The overview of this election audit was to create a new way of analyzing voting data for a congressional election in Colorado. The goal was to create a Python script to determine the winner of the election that can also be used in other districts and for the senate elections. The files used are listed below.  
Election data: ![election_results](Resources/election_results.csv)  
Python script: ![PyPoll.py](Challenge/PyPoll_Challenge.py)  
Analysis: ![election_analysis](Analysis/election_analysis.txt)  
## Election Audit Results
* Total number of votes cast in the election: 369,711  
* County breakdown and percentages:   
  * Jefferson: 10.5% (38,855)  
  * Denver: 82.8% (306,055)  
  * Arapahoe: 6.7% (24,801) 
* County with most votes: Denver  
* Breakdown of votes and percentages by candidate: 
  * Charles Casper Stockham: 23.0% (85,213)  
  * Diana DeGette: 73.8% (272,892)  
  * Raymon Anthony Doane: 3.1% (11,606)  
* Winning candidate, percentage, and number of votes: Diana DeGette: 73.8% (272,892)  
## Election Audit Summary
This script can be used in any election with the modification of some variable names but with the format and logic of the code remaining the same. For example, the trackers can be renamed to represent any variable that you are interested in tracking. 
