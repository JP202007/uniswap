import pandas as pd
from graphqlclient import GraphQLClient
import json

#2nd version of uniswap
client2 = GraphQLClient('https://api.thegraph.com/subgraphs/name/uniswap/uniswap-v2')
#1st version of uniswap
client1 = GraphQLClient('https://api.thegraph.com/subgraphs/name/graphprotocol/uniswap')

#DAI/WETH pair
result = client2.execute('''
{
 pairDayDatas(first:1000, orderBy: date, orderDirection: desc,
   where: {
     pairAddress: "0xdc98556ce24f007a5ef6dc1ce96322d65832a819",
   }
 ) {
     id
     date
     token0{
      symbol
    }
     token1{
      symbol
    }
     dailyVolumeToken0
     dailyVolumeToken1
     dailyVolumeUSD
     dailyTxns
     reserve0
     reserve1
     reserveUSD
 }
}

''')
print(result)

l=[(pair['id'],pair['date'],pair['token0']['symbol'],pair['token1']['symbol'],pair['dailyVolumeToken0'],pair['dailyVolumeToken1'],pair['dailyVolumeUSD'],pair['reserve0'],pair['reserve1'],pair['reserveUSD']) for pair in json.loads(result)['data']['pairDayDatas']]


df = pd.DataFrame(l)
df.columns=['id','date','token0','token1','dailyVolumeToken0','dailyVolumeToken1','dailyVolumeUSD','reserve0','reserve1','reserveUSD'] #Rename the columns
df.head()

from datetime import datetime
df["date"] = [datetime.fromtimestamp(timestamp) for timestamp in df["date"]]

df.to_csv(pair['token0']['symbol']+'-'+pair['token1']['symbol']+'.csv')

