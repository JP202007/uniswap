from graphqlclient import GraphQLClient
import pandas as pd
import json

#2nd version of uniswap
client2 = GraphQLClient('https://api.thegraph.com/subgraphs/name/uniswap/uniswap-v2')
#1st version of uniswap
client1 = GraphQLClient('https://api.thegraph.com/subgraphs/name/graphprotocol/uniswap')

result = client2.execute('''
{
 uniswapDayDatas(first:1000, orderBy: date, orderDirection: desc, 
 ) {
    id
    date
    totalLiquidityUSD
    totalLiquidityETH
    dailyVolumeETH
    dailyVolumeUSD
 }
}

''')
print(result)
#Convert into dataframe
l=[(pair['id'],pair['date'],pair['dailyVolumeETH'],pair['dailyVolumeUSD'],pair['totalLiquidityUSD'],pair['totalLiquidityETH']) for pair in json.loads(result)['data']['uniswapDayDatas']]

df = pd.DataFrame(l)
df.columns=['id','date','dailyVolumeETH','dailyVolumeUSD','totalLiquidityUSD','totalLiquidityEth'] #Rename the columns
df.head()

from datetime import datetime
df["date"] = [datetime.fromtimestamp(timestamp) for timestamp in df["date"]]

df.to_csv('uniswap total v2'+'.csv')

