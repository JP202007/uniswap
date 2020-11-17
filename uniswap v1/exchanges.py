from graphqlclient import GraphQLClient
import pandas as pd
import json

#2nd version of uniswap
client2 = GraphQLClient('https://api.thegraph.com/subgraphs/name/uniswap/uniswap-v2')
#1st version of uniswap
client1 = GraphQLClient('https://api.thegraph.com/subgraphs/name/graphprotocol/uniswap')

result = client1.execute('''
{
  exchanges(orderBy:combinedBalanceInUSD,orderDirection:desc){
    tokenAddress
    tokenSymbol
    startTime

    ethLiquidity
    tokenLiquidity
    ethBalance
    tokenBalance
    combinedBalanceInEth
    combinedBalanceInUSD
    totalUniToken

    addLiquidityCount
    removeLiquidityCount
    sellTokenCount
    buyTokenCount

    lastPrice
    price
    tradeVolumeToken
    tradeVolumeEth
    totalValue
    weightedAvgPrice
  }
}

''')
#print(result)
#Convert into dataframe
l=[(exchange['tokenSymbol'],exchange['startTime'],exchange['ethLiquidity'],exchange['tokenLiquidity'],exchange['ethBalance'],exchange['tokenBalance'],
    exchange['combinedBalanceInEth'],exchange['combinedBalanceInUSD'],exchange['totalUniToken'],exchange['tradeVolumeToken'],
    exchange['tradeVolumeEth'],exchange['totalValue']) for exchange in json.loads(result)['data']['exchanges']]

df = pd.DataFrame(l)
df.columns=['tokenSymbol','startTime','ethLiquidity','tokenLiquidity','ethBalance','tokenBalance','combinedBalanceInEth',
            'combinedBalanceInUSD','totalUniToken','tradeVolumeToken','tradeVolumeEth','totalValue'] #Rename the columns

from datetime import datetime
df["date"] = [datetime.fromtimestamp(timestamp) for timestamp in df["date"]]

df.head()
# error:most recent call last? only got 218 results
df.to_csv('exchanges v1'+'.csv')

