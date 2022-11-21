import tweepy 
import logging
import time
import json
import requests

client = tweepy.Client(bearer_token, api_key, api_secret, access_token, access_token_secret, wait_on_rate_limit=True)

auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
api = tweepy.API(auth) 



def create_url():
    # Specify the usernames that you want to lookup below
    # You can enter up to 100 comma-separated values.
    usernames = "usernames=1inch,88mphapp,aaveaave,MIM_Spell,acryptosx,AdamantVault,AlchemixFi,AlpacaFinance,alphaventuredao,AngleProtocol,ApertureFinance,ape_swap,armorfi,astroport_fi,AuctusOptions,AugurProject,autofarmnetwork,AutoSharkFin,bprotocoleth,babyswap_bsc,badgerdao,bagelsfinance,BalancerLabs,Bancor,BaoCommunity,Barn_Bridge,BasedFinance_io,beefyfinance,beethoven_x,BELT_Finance,BenqiFinance,Biswap_DEX,bscstation,bunnypark_bsc,CreamdotFinance,cafeswapfinance,compoundfinance,ConvexFinance,CoverProtocol,CurveFinance,defisaver,DefiKingdoms,definerorg,Defrost_Finance,dForcenet,_dfyn,dHedgeOrg,BreederDodo,dopex_io,dydx,element_fi,ellipsisfi,enzymefinance,FEGtoken,flexaHQ,ForTubeFi,fraxfinance,friktion_labs,futureswapx,GearboxProtocol,GeistFinance,GMX_IO,gnosisdao,goldfinch_fi,Gravity_Finance,financegrim,harvest_finance,HegicOptions,Helmet_insure,HoneyFarmFi,HopProtocol,idexio,idlefinance,ImpermaxFinance,ImpossibleFi,instadapp,InsurAce_io,InverseFinance,IronFinance,Jetfuelfinance,Jetfuelfinance,KalmyAPP,Katana_HQ,kebabfinance,keep_project,thekeep3r,KineProtocol,KlimaDAO,KyberNetwork,lidofinance,liquityprotocol,loopringorg,macaronswap,QiDaoProtocol,MakerDAO,maplefinance,MarinadeFinance,Mdextech"
    user_fields = "user.fields=description,created_at,public_metrics"
    # User fields are adjustable, options include:
    # created_at, description, entities, id, location, name,
    # pinned_tweet_id, profile_image_url, protected,
    # public_metrics, url, username, verified, and withheld
    url = "https://api.twitter.com/2/users/by?{}&{}".format(usernames, user_fields)
    return url


def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """

    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2UserLookupPython"
    return r


def connect_to_endpoint(url):
    response = requests.request("GET", url, auth=bearer_oauth,)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(
                response.status_code, response.text
            )
        )
    return response.json()


def main():
    url = create_url()
    json_response = connect_to_endpoint(url)
    with open('1inch_Mdextech.json', 'w') as outfile:
        json.dump(json_response, outfile, indent=4, sort_keys=True)
    #print(json.dumps(json_response, indent=4, sort_keys=True))
    


if __name__ == "__main__":
    main()
