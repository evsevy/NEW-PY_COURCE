#https://www.geeksforgeeks.org/automated-trading-using-python/

import pandas as pd
import quandl as qd

qd.ApiConfig.api_key = "API KEY"

msft_data = qd.get("EOD/MSFT",
				start_date="2022-03-01",
				end_date="2023-04-04")
print(msft_data.head())
