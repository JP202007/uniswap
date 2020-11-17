from graphqlclient import GraphQLClient
import pandas as pd
import json

#2nd version of uniswap
client2 = GraphQLClient('https://api.thegraph.com/subgraphs/name/uniswap/uniswap-v2')
#1st version of uniswap
client1 = GraphQLClient('https://api.thegraph.com/subgraphs/name/graphprotocol/uniswap')

result = client1.execute('''
{
  uniswapDayDatas(first:1000,orderBy:date,orderDirection:desc) {
    date
    dailyVolumeInETH
    dailyVolumeInUSD
    totalVolumeInEth
    totalVolumeUSD
    totalLiquidityInEth
    totalLiquidityUSD
    totalTokenSells
    totalTokenBuys
    totalAddLiquidity
    totalRemoveLiquidity
  }
}
''')
#print(result)
#Convert into dataframe
l=[(pair['date'],pair['dailyVolumeInETH'],pair['dailyVolumeInUSD'],pair['totalVolumeInEth'],pair['totalVolumeUSD'],pair['totalLiquidityInEth'],pair['totalLiquidityUSD']) for pair in json.loads(result)['data']['uniswapDayDatas']]

df = pd.DataFrame(l)
df.columns=['date','dailyVolumeInETH','dailyVolumeInUSD','totalVolumeInEth','totalVolumeUSD','totalLiquidityInEth','totalLiquidityUSD'] #Rename the columns

from datetime import datetime
df["date"] = [datetime.fromtimestamp(timestamp) for timestamp in df["date"]]

df.head()

df.to_csv('uniswap total v1'+'.csv')

