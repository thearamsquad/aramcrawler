from crawler.schema.common import *

SCHEMA = {
    'MatchDetails':
    {
        'matchId':
        {
            'type':'BIGINT UNSIGNED PRIMARY KEY',
            # function, *args, **kwargs
            GAME:FuncSig(readDictByArray,{'a':['gameId']})
        },
        'mapId':
        {
            'type':'TINYINT UNSIGNED',
            GAME:FuncSig(readDictByArray,{'a':['mapId']})
        },
        'matchCreation':
        {
            'type':'BIGINT UNSIGNED',
            MATCH:FuncSig(readDictByArray,{'a':['matchCreation']})
        },
        'matchDuration':
        {
            'type':'INT UNSIGNED',
            MATCH:FuncSig(readDictByArray,{'a':['matchDuration']})
        },
        'matchMode':
        {
            'type':'VARCHAR(24)',
            'require':'ARAM',
            GAME:FuncSig(readDictByArray,{'a':['gameMode']})
        },
        'matchType':
        {
            'type':'VARCHAR(24)',
            'require':'MATCHED_GAME',
            GAME:FuncSig(readDictByArray,{'a':['gameType']})
        },
        'matchVersion':
        {
            'type':'VARCHAR(24)',
            MATCH:FuncSig(readDictByArray,{'a':['matchVersion']})
        },
        'platformId':
        {
            'type':'VARCHAR(8)',
            MATCH:FuncSig(readDictByArray,{'a':['platformId']})
        },
        'queueType':
        {
            'type':'VARCHAR(24)',
            'require':'ARAM_5x5',
            MATCH:FuncSig(readDictByArray,{'a':['queueType']})
        },
        'region':
        {
            'type':'VARCHAR(4)',
            MATCH:FuncSig(readDictByArray,{'a':['region']})
        },
        'season':
        {
            'type':'VARCHAR(24)',
            MATCH:FuncSig(readDictByArray,{'a':['season']})
        },
        'firstBlood':
        {
            'type':'TINYINT UNSIGNED',
            MATCH:FuncSig(getFirstBlood,{})
        },
        'firstInhibitor':
        {
            'type':'TINYINT UNSIGNED',
        },
        'firstTower':
        {
            'type':'TINYINT UNSIGNED',
        },
        'team1inhibitorKills':
        {
            'type':'INT UNSIGNED',
        },
        'team2inhibitorKills':
        {
            'type':'INT UNSIGNED',
        },
        'team1towerKills':
        {
            'type':'TINYINT UNSIGNED',
        },
        'team2towerKills':
        {
            'type':'TINYINT UNSIGNED',
        },
        'winner':
        {
            'type':'TINYINT UNSIGNED',
            GAME:FuncSig(getWinner,{'endpoint':GAME})

        }
    },
    'Participants':
    {
        'id':
        {
            'type':'BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY',
        },
        'matchId':
        {
            'type':'BIGINT UNSIGNED',
            GAME:FuncSig(readDictByArray,{'a':['gameId']})
        },
        'participantId':
        {
            'type':'TINYINT UNSIGNED',
        },
        'championId':
        {
            'type':'INT UNSIGNED',
        },
        'highestAchievedSeasonTier':
        {
            'type':'VARCHAR(24)',
        },
        'spell1Id':
        {
            'type':'TINYINT UNSIGNED',
        },
        'spell2Id':
        {
            'type':'TINYINT UNSIGNED',
        },
        'teamId':
        {
            'type':'TINYINT UNSIGNED',
        },
        'assists':
        {
            'type':'INT UNSIGNED',
        },
        'champLevel':
        {
            'type':'TINYINT UNSIGNED',
        },
        'deaths':
        {
            'type':'INT UNSIGNED',
        },
        'doubleKills':
        {
            'type':'INT UNSIGNED',
        },
        'firstBloodAssist':
        {
            'type':'BIT(1)',
        },
        'firstBloodKill':
        {
            'type':'BIT(1)',
        },
        'firstInhibitorAssist':
        {
            'type':'BIT(1)',
        },
        'firstInhibitorKill':
        {
            'type':'BIT(1)',
        },
        'firstTowerAssist':
        {
            'type':'BIT(1)',
        },
        'firstTowerKill':
        {
            'type':'BIT(1)',
        },
        'goldEarned':
        {
            'type':'INT UNSIGNED',
        },
        'goldSpent':
        {
            'type':'INT UNSIGNED',
        },
        'inhibitorKills':
        {
            'type':'INT UNSIGNED',
        },
        'item0':
        {
            'type':'INT UNSIGNED',
        },
        'item1':
        {
            'type':'INT UNSIGNED',
        },
        'item2':
        {
            'type':'INT UNSIGNED',
        },
        'item3':
        {
            'type':'INT UNSIGNED',
        },
        'item4':
        {
            'type':'INT UNSIGNED',
        },
        'item5':
        {
            'type':'INT UNSIGNED',
        },
        'item6':
        {
            'type':'INT UNSIGNED',
        },
        'killingSprees':
        {
            'type':'INT UNSIGNED',
        },
        'kills':
        {
            'type':'INT UNSIGNED',
        },
        'largestCriticalStrike':
        {
            'type':'INT UNSIGNED',
        },
        'largestKillingSpree':
        {
            'type':'INT UNSIGNED',
        },
        'largestMultiKill':
        {
            'type':'INT UNSIGNED',
        },
        'magicDamageDealt':
        {
            'type':'INT UNSIGNED',
        },
        'magicDamageDealtToChampions':
        {
            'type':'INT UNSIGNED',
        },
        'magicDamageTaken':
        {
            'type':'INT UNSIGNED',
        },
        'minionsKilled':
        {
            'type':'INT UNSIGNED',
        },
        'pentaKills':
        {
            'type':'INT UNSIGNED',
        },
        'physicalDamageDealt':
        {
            'type':'INT UNSIGNED',
        },
        'physicalDamageDealtToChampions':
        {
            'type':'INT UNSIGNED',
        },
        'physicalDamageTaken':
        {
            'type':'INT UNSIGNED',
        },
        'quadraKills':
        {
            'type':'INT UNSIGNED',
        },
        'totalDamageDealt':
        {
            'type':'INT UNSIGNED',
        },
        'totalDamageDealtToChampions':
        {
            'type':'INT UNSIGNED',
        },
        'totalDamageTaken':
        {
            'type':'INT UNSIGNED',
        },
        'totalHeal':
        {
            'type':'INT UNSIGNED',
        },
        'totalTimeCrowdControlDealt':
        {
            'type':'INT UNSIGNED',
        },
        'totalUnitsHealed':
        {
            'type':'INT UNSIGNED',
        },
        'towerKills':
        {
            'type':'TINYINT UNSIGNED',
        },
        'tripleKills':
        {
            'type':'INT UNSIGNED',
        },
        'trueDamageDealt':
        {
            'type':'INT UNSIGNED',
        },
        'trueDamageDealtToChampions':
        {
            'type':'INT UNSIGNED',
        },
        'trueDamageTaken':
        {
            'type':'INT UNSIGNED',
        },
        'unrealKills':
        {
            'type':'INT UNSIGNED',
        },
        'winner':
        {
            'type':'TINYINT UNSIGNED',
        }
    },
    'Summoners':
    {
        'summonerId':
        {
            'type':'BIGINT UNSIGNED PRIMARY KEY',
            GAME:FuncSig(readDictByArray,{'a':['summonerId']})
        },
        'lastQueried':
        {
            'type':'BIGINT UNSIGNED',
            MATCH:FuncSig(lambda d:datetime.datetime.now(),{})
        }
    }
}
