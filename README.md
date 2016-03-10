# twitter_search.py
twitter_search is a Python script which searches for a tweet that contains a user-specified keyword, using Twitter's Search API. The script also makes note of all links posted within the content of the tweet as well as its uploaded media. 

## Dependencies
1. Python 2.7.6
2. [oauth2](https://github.com/joestump/python-oauth2)

## Setup & Usage

With the dependencies, init a new git repository in your desired directory and pull: 
```
$ git pull https://github.com/savvaspetridis/TwitterSearch/
```
Since twitter_search uses Twitter's API, you will need to register a project on Twitter's website and acquire a consumer key, consumer secret, access key, and access secret. You will need to input your own keys/secrets in the appropriate fields at the top of the script. Once your specific values are added, you can run the script! Below you can find twitter_search's usage and sample output: 
```
$ python twitter_search.py <keyword>
@username: tweet that contains <keyword>
media: <link(s)> ( if any )
```
