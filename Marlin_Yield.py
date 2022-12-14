import datetime
import tweepy 
import logging
import time
import json
import requests
import shutil
from datetime import datetime
import os
import glob

api_key = 'XXX'
api_secret = 'XXX'
access_token = 'XXX'
access_token_secret = 'XXX'
bearer_token = r'XXX'

client = tweepy.Client(bearer_token, api_key, api_secret, access_token, access_token_secret, wait_on_rate_limit=True)

auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
api = tweepy.API(auth) 


# Build string for directory to hold files
# Output Configuration
#   drive_letter = Output device location (hard drive)
#   folder_name = directory (folder) to receive and store PDF files

drive_letter = r'XXX'
folder_name = r''
folder_time = datetime.now().strftime("%Y-%m-%d_%I-%M-%S_%p")
folder_to_save_files = drive_letter + folder_name + folder_time



# IF no such folder exists, create one automatically
if not os.path.exists(folder_to_save_files):
    os.mkdir(folder_to_save_files)


def create_url():
    # Specify the usernames that you want to lookup below
    # You can enter up to 100 comma-separated values.
    usernames = "usernames=MarlinProtocol,moola_market,mstable_,NexusMutual,NotionalFinance,o3_labs,OlympusDAO,OpenOceanGlobal,opyn_,orca_so,OriginProtocol,orion_protocol,toadnetwork,paint_swap,PancakeBunnyFin,hunnyfinance,pancakeswap,pangolindex,pantherswap,paraswap,peakdefi,PerlinNetwork,perpprotocol,picklefinance,PieDAO_DeFi,planet_finance,Platypusdefi,PolycatFinance,polydexfi,polyquity_org,PoolTogether_,PopsicleFinance,port_finance,PremiaFinance,pylon_protocol,QuarryProtocol,QubitFin,QuickswapDEX,0xRabbitDAO,RampNetwork,RariCapital,RaydiumProtocol,Reaper_Farm,finance_ref,reflexerfinance,ribbonfinance,saddlefinance,saffronfinance_,projectserum,setprotocol,ShapeShift,ShibaSwapDEX,snowballdefi,solacefi,solarbeamio,solendprotocol,SolidexFantom,Spirit_Swap,spookyswap,StakeDAOHQ,stakewise_io,StargateFinance,StellaSwap,sushiswap,SwerveFinance,synthetix_io,TarotFinance,terraswap_io,tetu_io,tokenreactor,tombfinance,tornadocash,mycelium_xyz,traderjoe_xyz,tranchess,treedefi,trisolarislabs,TrueFiDAO,TulipProtocol,ubeswap,unFederalreser1,unifiprotocol,uniswap,unitradeapp,value_defi,VenusProtocol,VesperFi,VVS_finance,Wault_Finance,Wing_Finance,wonderland_fi,YamFinance,yaxis_project,iearnfinance,yield"
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
    with open('Marlin_Yield.json', 'w') as outfile:
        json.dump(json_response, outfile, indent=4, sort_keys=True)
    #print(json.dumps(json_response, indent=4, sort_keys=True))


if __name__ == "__main__":
    main()


source = 'XXX'
destination = folder_to_save_files
#
# gather all files
allfiles = glob.glob(os.path.join(source, '*_*'), recursive=True)
print("Files to move", allfiles)

# iterate on all files to move them to destination folder
for file_path in allfiles:
    dst_path = os.path.join(destination, os.path.basename(file_path))
    shutil.move(file_path, dst_path)
    print(f"Moved {file_path} -> {dst_path}")
