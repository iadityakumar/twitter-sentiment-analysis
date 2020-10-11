# Twitter Sentiment Analysis
This script can tell you the sentiments of people for predicting US Presidential Election Result using Twitter Sentiment Analysis with Python



## Getting Started
First of all login from your Twitter account and goto Twitter Apps. Create a new app (How to create twitter app) and goto Keys and access tokens and copy Consumer Key, Consumer Secret, Access Token and Access Token Secret. We will need them later.

Installation
Download or Clone the repo, Navigate to the directory containing the files and run

pip install -r requirements.txt
or if you have different versions of python installed then

pip3 install -r requirements.txt
to install the dependencies.

## Usage
Once you have created an app on twitter and installed all the dependencies by running requirements.txt, open TweetReplies.py and paste your Consumer Key, Consumer Secret, Access Token and Access Token Secret , or can put these keys in .env file and use it from there. After that save and run the script. Currently its taking 1000 tweets, but you can edit the code to change  the number of tweets you want to analyze. After this run Sentiment_analysis.ipynb and FinalAnalysis.ipynb .Once the analysis is completed, a pie chart will be generated disclosing the results of analysis.

## Word Cloud generated
Trump
![Screenshot from 2020-10-11 20-40-27](https://user-images.githubusercontent.com/4803451/95685785-a52e7b00-0c17-11eb-8097-ee82aa79272a.png)
Biden
![Screenshot from 2020-10-11 20-40-39](https://user-images.githubusercontent.com/4803451/95685789-a95a9880-0c17-11eb-8eaa-31243b91318f.png)

## Barchart
![Screenshot from 2020-10-11 20-41-13](https://user-images.githubusercontent.com/4803451/95685830-ffc7d700-0c17-11eb-9ccb-fe00e5dfd514.png)

## PieChart
![Screenshot from 2020-10-11 20-41-35](https://user-images.githubusercontent.com/4803451/95685832-01919a80-0c18-11eb-9d4f-3001ad142848.png)
![Screenshot from 2020-10-11 20-41-45](https://user-images.githubusercontent.com/4803451/95685834-02c2c780-0c18-11eb-9d81-55ab5a003895.png)

## Built With
Python 3.6
tweepy
textblob
matplotlib
## Contributing
Fork it
Create your feature branch: git checkout -b my-new-feature
Commit your changes: git commit -am 'Add some feature'
Push to the branch: git push origin my-new-feature
Submit a pull request
## Authors
Aditya Kumar
