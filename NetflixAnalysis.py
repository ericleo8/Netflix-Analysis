import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pandas_profiling as pp
from pandas_profiling import ProfileReport 
import seaborn as sns
import pycountry


df = pd.read_csv("data_TV.csv")
df=pd.DataFrame(df)
df.head(5)

profile = ProfileReport(df, title="Summary of Data", html={'style' : {'full_width':True}})
profile.to_file(output_file="file.html") 
profile

#find the country with the keycode
def findCountryOfficialName (country_code):
    try:
        return pycountry.countries.get(alpha_2=country_code).name
    except:
        return ("Country Not Found!")

df['official_name'] = df.apply(lambda row: findCountryOfficialName(row.origin_country) , axis = 1)
df.head()

df_origin_country_full = df["official_name"].value_counts()
df_origin_country_full

df_country_counts = pd.DataFrame(df_origin_country_full)
df_country_resets = df_country_counts.reset_index()
df_country_resets.columns = ['country_name', 'number_of_shows'] # change column names
df_country_resets


##############################################################################################

df_origin_country = df["origin_country"].value_counts().head(5)
df_origin_country

df_val_counts = pd.DataFrame(df_origin_country)
df_value_counts_reset = df_val_counts.reset_index()
df_value_counts_reset.columns = ['country', 'number_of_shows'] # change column names
df_value_counts_reset



plt.figure(figsize=(12,6))
plt.title("Shows Productions in Top 5 Country", fontsize=18, fontweight="bold")
plt.xlabel("Country",fontsize=14)
plt.ylabel("Number of Shows",fontsize=14)

plots = plt.bar(df_value_counts_reset['country'],df_value_counts_reset['number_of_shows'])
plt.bar_label(plots)
plt.show()




