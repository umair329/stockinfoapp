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