# stockinfoapp
Utilizing TDA-API, python package to pull in specific markets information for Object Oriented class project.

## Summary of Python Package Project - Stock Information Pull 

Please run main.py

## Install & Run Instructions 

1. Create a python virtual environment, and use "pip install -r requirements.txt" to download all necessary packages

2. Then, make sure your TD Ameritrade account is set up. You will need a regular account as well as a developer account

3. To create a developer account, click register and use the same email that you used for your TDA account

4. Once you login to your TDA Developer account, click on "My Apps" in the top menu bar, then click "Add a new app"

5. Set your redirect url to https://localhost

6. Take your generated API Key and your account id (which you get from your regular TDA account).

7. Place those both into the config.py in their respective location (Important: for the API Key make sure '@AMER.OAUTHAP' is appended to the key that you got from your dev account)

8. Once that is complete, run the token_gen.py (which needs chromium installed) and login to your TDA account using the login flow.

9. Then, the token file will be generated and you can now run the main.py

## Code & What it does 

    from tda import auth, client
    from flask import Flask, jsonify, session, redirect
    from auth import config

    #authenticate client
    c = auth.client_from_token_file(config.token_path, config.api_key)

    #pull last closing price for a specific ticker 
    def get_close(ticker):
    #get complete quote info for give token
    r = c.get_quote(ticker)

    #throw error if get quote fails 
    assert r.status_code == 200, r.raise_for_status()

    #return hhtpx response as dict 
    tickerDict = r.json()

    return tickerDict[ticker]["lastPrice"]

    #pull data on last prices of stocks from a selected sector 
    def get_sector(sector):

    if sector.upper() == "TECH":
        
        #create basket of stocks and initalize doc to store prices
        tech = ["XLK", "MSFT", "GOOGL", "AAPL", "NFLX"]
        lastPrices = {}

        #pull data for select companies in sector and store in dict
        for company in tech:
            lastPrices[company] = get_close(company)
        
        print(lastPrices)
        #return dict
        return lastPrices
    
    elif sector.upper() == "FIN":
                
        #create basket of stocks and initalize doc to store prices
        finance = ["XLF", "BAC", "JPM", "WFC", "C"]
        lastPrices = {}

        #pull data for select companies in sector and store in dict
        for company in finance:
            lastPrices[company] = get_close(company)

        
        print(lastPrices)
        #return dict 
        return lastPrices
    
    #throw error if sector not found 
    else:
        return{
            "error": "sector not found"
        }
        get_sector("fin")

1)Import Package - TDA API
2)Authenticate Client via "Auth" - This basically allows one to create a token to assign to an actual account with username and password from exisiting TD Ameritrade free brokerage account.
3)Than, you can pull the last closing price on the specific stock ticker, followed by a couple of error prompt if quote failes.
4)Than, you can pull data on last prices of stocks from a selected sector
5)In this case I have determined the sector to be TECH - the five tech stocks inlude XLK, Microsoft, Google, Apple & Netflix
6)Allows you to get end of day quote of the stock
7)The alternative sector is FIN - so you can see the stock end of day quotes for XLF, BAC, JPM, WFC, C.
8)This script allows you to pull info directly from TD America's real-time financial platform so that you can automate data pull on straightforward stock quote information.

## Future Idea
   
We can use this existing script as a base for future complex scripts that can pull more informatuon from the TD Ameritrade data-set on real-time financial markets information. Here we only use one metric from TD - which is the stock quote "end of day" price. There are dozens of other metrics we can pull from a particular stock(s) and leverage that information to derive insights. 

A future idea includes, looking into more sectors and industries. Pulling information from ETF's or Indexes or other type of public funds. And automating the information pull to specific scenarios in ultimately making the user experience easier for a user to pull and retrive specific data points quickly.


## Supported Features & Best–Practices

tda-api is an unofficial wrapper around the TD Ameritrade APIs. It strives to be as thin and unopinionated as possible, offering an elegant programmatic interface over each endpoint. Notable functionality includes:

Login and authentication
Quotes, fundamentals, and historical pricing data
Options chains
Streaming quotes and order book depth data
Trades and trade management
Account info and preferences


## API Reference and User Guide available on [Read the Docs]

https://pypi.org/project/tda-api/

API Documentation: https://tda-api.readthedocs.io/en/latest/

