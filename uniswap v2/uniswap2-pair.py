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
  pairs(first: 1000,orderBy:reserveUSD,orderDirection:desc) {
    id
    token0{
      symbol
    }
    token1{
      symbol
    }
    reserve0
    reserve1
    totalSupply
    reserveETH
    reserveUSD
    trackedReserveETH
    token0Price
    token1Price
    volumeToken0
    volumeToken1
    volumeUSD
    createdAtTimestamp
    createdAtBlockNumber
    liquidityProviderCount
    }   
  }
 
''')

l=[(pair['id'],pair['token0']['symbol'],pair['token1']['symbol'],pair['reserve0'],pair['reserve1'],pair['totalSupply'],
    pair['reserveETH'],pair['reserveUSD'],pair['token0Price'],pair['token1Price'],pair['trackedReserveETH'],pair['volumeToken0'],
    pair['volumeToken1'],pair['volumeUSD'],pair['createdAtTimestamp'],pair['createdAtBlockNumber'],pair['liquidityProviderCount']) for pair in json.loads(result)['data']['pairs']]


df = pd.DataFrame(l)
df.columns=['id','token0','token1','reserve0','reserve1','totalSupply','reserveETH','reserveUSD','token0Price','token1Price',
            'trackedReserveETH','volumeToken0','volumeToken1','volumeUSD','createdAtTimestamp','createdAtBlockNumber','liquidityProviderCount'] #Rename the columns
df.head()


df.to_csv('v2 pairs.csv')

