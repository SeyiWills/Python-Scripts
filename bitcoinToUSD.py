def bitcoinToUSD(bitcoin_amount, bitcoin_value_usd):

  usd_value = (bitcoin_amount * bitcoin_value_usd)
  return usd_value

amount_and_price = bitcoinToUSD(2, 3000)

if amount_and_price <= 30000:
  print("The Bitcoin Price is " + str(amount_and_price))
  