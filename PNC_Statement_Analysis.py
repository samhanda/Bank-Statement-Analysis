import numpy as np
import pandas as pd
import re

data = pd.read_excel("PNC_CC_Data.xlsx")

df = pd.DataFrame(data)

#If value in Amount is less than 0 then it assigns refund or regular transaction under
#the category Transaction Type. Vice versa for greater than 0

df.loc[df["Amount"] < 0, "Transaction Type"] = "Refund"
df.loc[df["Amount"] > 0, "Transaction Type"] = "Regular Transaction"

merchandise_items = ("gov|namecheap|walgreens|costco|wal-mart|reverb|amazon|ace|bestbuy|supercenter|amzn|usps|apple|eyebuydirec|harbor freight tools|sport clips|ebay|ncdmv")
bank_items = ("pmt|pnc")
medical_items = ("defy|fastmed|expressscri")
gas_items = ("exxon|circle|fast lube|sheetz|oil")

dining_items = ("jersey|pizza|neomonde|sassool|uber|potbelly|five guys|"
                "chickfila|greek fiesta|bibibop|penn station|chicken salad|sushioki|tazikis|jasmin")

grocery_items = ("grand asia market|publix|harris|whole foods|wholefds|wegmans|trader|aldi")

entertainment_items =  ("guitar|total wine|harris|triangle wine company|"
                        "releaf|steam|monoprice|thomann|name-cheap|wake county abc|sweetwater|gmg inc|rondo music|bottles and cans|focusrite")

df.loc[df["Description"].str.contains(merchandise_items, flags = re.IGNORECASE), "Category"] = "Merchandise"
df.loc[df["Description"].str.contains(medical_items, flags = re.IGNORECASE), "Category"] = "Medical"
df.loc[df["Description"].str.contains(dining_items, flags = re.IGNORECASE), "Category"] = "Dining"
df.loc[df["Description"].str.contains(grocery_items, flags = re.IGNORECASE), "Category"] = "Grocery"
df.loc[df["Description"].str.contains(entertainment_items, flags = re.IGNORECASE), "Category"] = "Entertainment"
df.loc[df["Description"].str.contains(gas_items, flags = re.IGNORECASE), "Category"] = "Gas/Automotive"
df.loc[df["Description"].str.contains(bank_items, flags = re.IGNORECASE), "Category"] = "Bank Related"

df.to_excel("PNC_Statement_Modified.xlsx")

print(df)
