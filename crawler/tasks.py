from crawler import database
from crawler.schema.match import SCHEMA as CRAWLER_SCHEMA
from crawler.schema.static import SCHEMA as STATIC_SCHEMA
import config
import logging
# tasks are the top-level of this program
# each api query type

# static-data tasks
def getChampData():
    # - Champions
    pass
def getItemData():
    # - Items
    pass

# crawl-games tasks
# start with 1 getGames task per api key
def getGames(apiKey, conn): # returns 0-10 ARAMs, 5-40 summoners
    # get games, put a getMatchDetail in the queue for each ARAM we got
    # if no arams, put another getGames in the queue for each api key
    pass
    # - MatchDetails
    # - PlayerStats
    # - Summoners

def getMatchDetail(apiKey, conn):
    """gets details of 1 ARAM"""
    ENDPOINT = 'match-v2.2'
    # get match details
    # if queue is empty, put a getGames in the queue for each api key
    # - MatchDetails
    # - PlayerStats
    # TODO: use cache etc to get best matchId
    matchId = 160652569
    data = queryApi(ENDPOINT, apiKey, matchId)
    processData(ENDPOINT, data, "UPDATE", conn)

def processData(endpoint, data, sqlCommand, conn):
    queries = []
    # make a new sql query for each table
    for tableName, fields in CRAWLER_SCHEMA.items():
        #logging.info("doing table: " + tableName)
        # check each field to see if there's a function mapped to this endpoint
        rows = []
        values = []
        for fieldName, field in fields.items():
            #logging.info("   doing field: " + fieldName)
            if endpoint in field.keys():
                # execute said function, giving it the api data
                fSig = field[endpoint]
                fSig.kwargs['d'] = data
                values.append(str(fSig.function(**fSig.kwargs)))
                rows.append(fieldName)
        sql = sqlCommand+" `"+tableName+"` (`"+'`,`'.join(rows)+'`) VALUES ('+','.join(values)+')'
        queries.append(sql)
    logging.info(queries)
    #database.updateTable(queries, conn)

def queryApi(endpoint, key, params):
    import urllib.request, json
    prts = endpoint.split('-')
    # match-v2.2, params -> v2.2/match/params
    ext = '/'.join([prts[1],prts[0],str(params)])
    url = config.apiUrl+ext+'?api_key='+key
    logging.info("Querying: "+url)
    data = json.loads(urllib.request.urlopen(url, None).read())
    logging.info("Got data!")
    #logging.info("**************** data ****************\n"+str(data)+"\n***************************")
    return data

# setup-tables tasks
def setupTables():
    pass
