mintAddress = '0x905D8dbdF4C06Fb2Fd7C6D1376A2Af6d6C6A6d4C'
mintAbi = [{"constant":True,"inputs":[],"name":"creator","outputs":[{"name":"","type":"address"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":False,"inputs":[{"name":"_spender","type":"address"},{"name":"_value","type":"uint256"}],"name":"approve","outputs":[{"name":"","type":"bool"}],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":True,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":False,"inputs":[{"name":"_from","type":"address"},{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transferFrom","outputs":[{"name":"","type":"bool"}],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":False,"inputs":[{"name":"_value","type":"uint256"}],"name":"burnFrom","outputs":[{"name":"success","type":"bool"}],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":True,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":False,"inputs":[{"name":"_to","type":"address[]"},{"name":"_value","type":"uint256[]"}],"name":"transferMulti","outputs":[{"name":"success","type":"bool"}],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":False,"inputs":[{"name":"_spender","type":"address"},{"name":"_subtractedValue","type":"uint256"}],"name":"decreaseApproval","outputs":[{"name":"success","type":"bool"}],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":True,"inputs":[{"name":"_owner","type":"address"}],"name":"balanceOf","outputs":[{"name":"balance","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":False,"inputs":[{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transfer","outputs":[{"name":"","type":"bool"}],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":False,"inputs":[{"name":"_spender","type":"address"},{"name":"_addedValue","type":"uint256"}],"name":"increaseApproval","outputs":[{"name":"success","type":"bool"}],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":True,"inputs":[{"name":"_owner","type":"address"},{"name":"_spender","type":"address"}],"name":"allowance","outputs":[{"name":"remaining","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"},{"inputs":[{"name":"initialSupply","type":"uint256"},{"name":"_creator","type":"address"}],"payable":False,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":False,"inputs":[{"indexed":True,"name":"from","type":"address"},{"indexed":False,"name":"value","type":"uint256"}],"name":"Burn","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"name":"owner","type":"address"},{"indexed":True,"name":"spender","type":"address"},{"indexed":False,"name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"name":"from","type":"address"},{"indexed":True,"name":"to","type":"address"},{"indexed":False,"name":"value","type":"uint256"}],"name":"Transfer","type":"event"}]

factoryAddress = '0x13cB939F7efAbA6498CdCAB363D9D4FCeeFA2B06'
factoryAbi = [{"constant":True,"inputs":[],"name":"noOfUsers","outputs":[{"name":"","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[{"name":"_userID","type":"uint256"}],"name":"lookupUserMeta","outputs":[{"name":"userAddress","type":"address"},{"name":"totalAmountSpent","type":"uint256"},{"name":"totalAmountReturned","type":"uint256"},{"name":"noOfBlueprintsCreated","type":"uint256"},{"name":"noOfBlueprintsPurchased","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[],"name":"creationPrice","outputs":[{"name":"","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":False,"inputs":[{"name":"_blueprintID","type":"uint256"}],"name":"claimReturns","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":True,"inputs":[{"name":"_blueprintID","type":"uint256"}],"name":"lookupBlueprintMeta","outputs":[{"name":"blueprintAddress","type":"address"},{"name":"ticker","type":"string"},{"name":"margin","type":"uint256"},{"name":"expirationTimestamp","type":"uint256"},{"name":"creationTimestamp","type":"uint256"},{"name":"creatorID","type":"uint256"},{"name":"creatorAddress","type":"address"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":False,"inputs":[{"name":"_walletAddresses","type":"address[]"}],"name":"removeValidatedUsers","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":False,"inputs":[{"name":"_walletAddresses","type":"address[]"}],"name":"reValidateUsers","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":True,"inputs":[{"name":"","type":"address"}],"name":"blueprintID","outputs":[{"name":"","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":False,"inputs":[{"name":"_walletAddresses","type":"address[]"}],"name":"addValidatedUsers","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":False,"inputs":[{"name":"_ticker","type":"string"},{"name":"_entryTkrPrice","type":"uint256"},{"name":"_exitTkrPrice","type":"uint256"},{"name":"_expirationTimestamp","type":"uint256"}],"name":"createBlueprint","outputs":[],"payable":True,"stateMutability":"payable","type":"function"},{"constant":False,"inputs":[{"name":"_blueprintID","type":"uint256"}],"name":"purchaseBlueprint","outputs":[],"payable":True,"stateMutability":"payable","type":"function"},{"constant":False,"inputs":[{"name":"_purchasePrice","type":"uint256"}],"name":"changePurchasePrice","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":True,"inputs":[],"name":"noOfBlueprints","outputs":[{"name":"","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[],"name":"purchasePrice","outputs":[{"name":"","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":False,"inputs":[{"name":"_creationPrice","type":"uint256"}],"name":"changeCreationPrice","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":True,"inputs":[{"name":"","type":"address"}],"name":"userID","outputs":[{"name":"","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":False,"inputs":[{"name":"_rblxOracleAddress","type":"address"}],"name":"changeOracleAddress","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"inputs":[{"name":"_rblxTokenAddress","type":"address"},{"name":"_rblxOracleAddress","type":"address"},{"name":"_creationPrice","type":"uint256"},{"name":"_purchasePrice","type":"uint256"}],"payable":False,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":False,"inputs":[{"indexed":False,"name":"creator","type":"address"},{"indexed":False,"name":"blueprint","type":"address"},{"indexed":False,"name":"creationPrice","type":"uint256"}],"name":"BlueprintCreated","type":"event"},{"anonymous":False,"inputs":[{"indexed":False,"name":"buyer","type":"address"},{"indexed":False,"name":"blueprint","type":"address"},{"indexed":False,"name":"purchasePrice","type":"uint256"}],"name":"BlueprintPurchased","type":"event"},{"anonymous":False,"inputs":[{"indexed":False,"name":"receipiant","type":"address"},{"indexed":False,"name":"blueprint","type":"address"},{"indexed":False,"name":"amount","type":"uint256"}],"name":"ReturnClaimed","type":"event"}]
blueprintAbi = [{"constant":True,"inputs":[],"name":"creator","outputs":[{"name":"userID","type":"uint256"},{"name":"userAddress","type":"address"},{"name":"amountStaked","type":"uint256"},{"name":"amountReturned","type":"uint256"},{"name":"stakeTimestamp","type":"uint256"},{"name":"returnTimestamp","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":False,"inputs":[{"name":"_userAddress","type":"address"}],"name":"returnToBuyer","outputs":[{"name":"returnMade","type":"uint256"}],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":True,"inputs":[],"name":"creationPrice","outputs":[{"name":"","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[],"name":"noOfBuyers","outputs":[{"name":"","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":False,"inputs":[{"name":"_periodHigh","type":"uint256"},{"name":"_highTimestamp","type":"uint256"},{"name":"_periodLow","type":"uint256"},{"name":"_lowTimestamp","type":"uint256"}],"name":"confirmPrediction","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":True,"inputs":[{"name":"","type":"address"}],"name":"buyerID","outputs":[{"name":"","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":False,"inputs":[{"name":"_userAddress","type":"address"}],"name":"returnToCreator","outputs":[{"name":"returnMade","type":"uint256"}],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":True,"inputs":[],"name":"margin","outputs":[{"name":"","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":False,"inputs":[],"name":"emptyUnclaimedTokens","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":True,"inputs":[],"name":"noOfViews","outputs":[{"name":"","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[],"name":"purchasePrice","outputs":[{"name":"","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":False,"inputs":[],"name":"viewPrediction","outputs":[{"name":"entryTkrPrice","type":"uint256"},{"name":"exitTkrPrice","type":"uint256"}],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":False,"inputs":[{"name":"_userID","type":"uint256"},{"name":"_userAddress","type":"address"}],"name":"addBuyer","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":True,"inputs":[{"name":"","type":"uint256"}],"name":"buyers","outputs":[{"name":"userID","type":"uint256"},{"name":"userAddress","type":"address"},{"name":"amountStaked","type":"uint256"},{"name":"amountReturned","type":"uint256"},{"name":"stakeTimestamp","type":"uint256"},{"name":"returnTimestamp","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"},{"inputs":[{"name":"_creatorID","type":"uint256"},{"name":"_creatorAddress","type":"address"},{"name":"_purchasePrice","type":"uint256"},{"name":"_creationPrice","type":"uint256"},{"name":"_ticker","type":"string"},{"name":"_entryTkrPrice","type":"uint256"},{"name":"_exitTkrPrice","type":"uint256"},{"name":"_expirationTimestamp","type":"uint256"},{"name":"_oracleAddress","type":"address"},{"name":"_rblxToken","type":"address"}],"payable":False,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":False,"inputs":[{"indexed":False,"name":"Previously","type":"uint8"},{"indexed":False,"name":"Now","type":"uint8"}],"name":"StateChange","type":"event"},{"anonymous":False,"inputs":[{"indexed":False,"name":"receipiant","type":"address"},{"indexed":False,"name":"blueprint","type":"address"},{"indexed":False,"name":"amountRefunded","type":"uint256"}],"name":"RefundClaimed","type":"event"},{"anonymous":False,"inputs":[{"indexed":False,"name":"blueprint","type":"address"},{"indexed":False,"name":"amount","type":"uint256"}],"name":"BlueprintEmptied","type":"event"}]
