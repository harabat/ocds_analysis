# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.14.0
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% [markdown] toc=true
# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Prep" data-toc-modified-id="Prep-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Prep</a></span></li><li><span><a href="#Comparing-csv-and-excel" data-toc-modified-id="Comparing-csv-and-excel-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Comparing <code>csv</code> and <code>excel</code></a></span><ul class="toc-item"><li><span><a href="#Load-data" data-toc-modified-id="Load-data-2.1"><span class="toc-item-num">2.1&nbsp;&nbsp;</span>Load data</a></span></li><li><span><a href="#Initial-comparison" data-toc-modified-id="Initial-comparison-2.2"><span class="toc-item-num">2.2&nbsp;&nbsp;</span>Initial comparison</a></span></li><li><span><a href="#Standardise-columns" data-toc-modified-id="Standardise-columns-2.3"><span class="toc-item-num">2.3&nbsp;&nbsp;</span>Standardise columns</a></span></li></ul></li><li><span><a href="#json" data-toc-modified-id="json-3"><span class="toc-item-num">3&nbsp;&nbsp;</span><code>json</code></a></span><ul class="toc-item"><li><span><a href="#Load" data-toc-modified-id="Load-3.1"><span class="toc-item-num">3.1&nbsp;&nbsp;</span>Load</a></span></li><li><span><a href="#uri,-license,-version,-publisher,-extensions,-publicationPolicy" data-toc-modified-id="uri,-license,-version,-publisher,-extensions,-publicationPolicy-3.2"><span class="toc-item-num">3.2&nbsp;&nbsp;</span><code>uri</code>, <code>license</code>, <code>version</code>, <code>publisher</code>, <code>extensions</code>, <code>publicationPolicy</code></a></span></li><li><span><a href="#releases" data-toc-modified-id="releases-3.3"><span class="toc-item-num">3.3&nbsp;&nbsp;</span><code>releases</code></a></span><ul class="toc-item"><li><span><a href="#Flatten-JSON" data-toc-modified-id="Flatten-JSON-3.3.1"><span class="toc-item-num">3.3.1&nbsp;&nbsp;</span>Flatten JSON</a></span></li><li><span><a href="#Explore-a-release" data-toc-modified-id="Explore-a-release-3.3.2"><span class="toc-item-num">3.3.2&nbsp;&nbsp;</span>Explore a release</a></span></li></ul></li></ul></li><li><span><a href="#Quality-control" data-toc-modified-id="Quality-control-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>Quality control</a></span><ul class="toc-item"><li><span><a href="#Non-unique-ocid,-release_id,-id-values" data-toc-modified-id="Non-unique-ocid,-release_id,-id-values-4.1"><span class="toc-item-num">4.1&nbsp;&nbsp;</span>Non-unique <code>ocid</code>, <code>release_id</code>, <code>id</code> values</a></span></li><li><span><a href="#bids.details" data-toc-modified-id="bids.details-4.2"><span class="toc-item-num">4.2&nbsp;&nbsp;</span><code>bids.details</code></a></span></li><li><span><a href="#planning.budget.id" data-toc-modified-id="planning.budget.id-4.3"><span class="toc-item-num">4.3&nbsp;&nbsp;</span><code>planning.budget.id</code></a></span></li></ul></li><li><span><a href="#Winner-and-loser-provinces" data-toc-modified-id="Winner-and-loser-provinces-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>Winner and loser provinces</a></span><ul class="toc-item"><li><span><a href="#Clean" data-toc-modified-id="Clean-5.1"><span class="toc-item-num">5.1&nbsp;&nbsp;</span>Clean</a></span><ul class="toc-item"><li><span><a href="#Parties" data-toc-modified-id="Parties-5.1.1"><span class="toc-item-num">5.1.1&nbsp;&nbsp;</span>Parties</a></span></li><li><span><a href="#Localities" data-toc-modified-id="Localities-5.1.2"><span class="toc-item-num">5.1.2&nbsp;&nbsp;</span>Localities</a></span></li><li><span><a href="#Cities" data-toc-modified-id="Cities-5.1.3"><span class="toc-item-num">5.1.3&nbsp;&nbsp;</span>Cities</a></span></li><li><span><a href="#Regions" data-toc-modified-id="Regions-5.1.4"><span class="toc-item-num">5.1.4&nbsp;&nbsp;</span>Regions</a></span></li><li><span><a href="#Save-to-pickle" data-toc-modified-id="Save-to-pickle-5.1.5"><span class="toc-item-num">5.1.5&nbsp;&nbsp;</span>Save to pickle</a></span></li></ul></li><li><span><a href="#Insight" data-toc-modified-id="Insight-5.2"><span class="toc-item-num">5.2&nbsp;&nbsp;</span>Insight</a></span></li></ul></li><li><span><a href="#Lucky-tenderers" data-toc-modified-id="Lucky-tenderers-6"><span class="toc-item-num">6&nbsp;&nbsp;</span>Lucky tenderers</a></span><ul class="toc-item"><li><span><a href="#Clean" data-toc-modified-id="Clean-6.1"><span class="toc-item-num">6.1&nbsp;&nbsp;</span>Clean</a></span><ul class="toc-item"><li><span><a href="#Extract-roles" data-toc-modified-id="Extract-roles-6.1.1"><span class="toc-item-num">6.1.1&nbsp;&nbsp;</span>Extract roles</a></span></li><li><span><a href="#Save-to-pickle" data-toc-modified-id="Save-to-pickle-6.1.2"><span class="toc-item-num">6.1.2&nbsp;&nbsp;</span>Save to pickle</a></span></li></ul></li><li><span><a href="#Insight" data-toc-modified-id="Insight-6.2"><span class="toc-item-num">6.2&nbsp;&nbsp;</span>Insight</a></span></li></ul></li><li><span><a href="#Common-contract-amounts" data-toc-modified-id="Common-contract-amounts-7"><span class="toc-item-num">7&nbsp;&nbsp;</span>Common contract amounts</a></span><ul class="toc-item"><li><span><a href="#Clean" data-toc-modified-id="Clean-7.1"><span class="toc-item-num">7.1&nbsp;&nbsp;</span>Clean</a></span></li><li><span><a href="#Insight" data-toc-modified-id="Insight-7.2"><span class="toc-item-num">7.2&nbsp;&nbsp;</span>Insight</a></span></li></ul></li><li><span><a href="#Number-of-tenderers-vs-amount" data-toc-modified-id="Number-of-tenderers-vs-amount-8"><span class="toc-item-num">8&nbsp;&nbsp;</span>Number of tenderers vs amount</a></span></li></ul></div>

# %% [markdown]
# # OCDS analysis

# %% [markdown] heading_collapsed=true
# ## Prep

# %% hidden=true
import pandas as pd # data analysis

import seaborn as sns # data viz
import altair as alt # data viz

from altair_saver import save # save charts

from pathlib import Path # read and write files

import math # rounding operation

import re # regexes

# %% hidden=true
alt.data_transformers.disable_max_rows()

# %% [markdown] heading_collapsed=true
# ## Comparing `csv` and `excel`

# %% [markdown] hidden=true
# ### Load data

# %% hidden=true
data_xlsx = pd.read_excel('./data/releases_2022.xlsx', sheet_name=None)

# %% hidden=true
data_xlsx.keys()

# %% hidden=true
for key in data_xlsx.keys():
    print(
        f'{key}\n'
        f'\t{data_xlsx[key].columns}\n'
    )


# %% [markdown] heading_collapsed=true hidden=true
# ### Initial comparison

# %% hidden=true
def diff_csv_xlsx(csv_dir='./csv/', data_xslx=data_xlsx):
    '''Find differences between 2 DataFrames.'''

    # dict that will contain diffs
    differences = dict()

    # directory with csv files
    csv_dir = Path(csv_dir)

    # iterate over csv files and compare to xlsx
    for file in csv_dir.iterdir():
        file_name = str(file.relative_to(csv_dir)).replace('_2022.csv', '').capitalize()

        if file_name == 'Suppliers':
            file_name = 'AwardSuppliers'

        data_csv = pd.read_csv(file)

        difference = data_csv.compare(data_xlsx[file_name])

        if difference.shape[0] != 0:
            print(file_name)
            differences[file_name] = difference
            
    return differences


# %% hidden=true
differences = diff_csv_xlsx()

# %% [markdown] hidden=true
# Let's look at the files one by one. 

# %% hidden=true
differences['Awards']

# %% hidden=true
differences['Awards']['description'].dropna().values

# %% [markdown] hidden=true
# For `Awards`, the differences seem to be different types and float precision. 

# %% hidden=true
differences['Contracts']


# %% [markdown] hidden=true
# Same for `Contacts`. 

# %% [markdown] heading_collapsed=true hidden=true
# ### Standardise columns

# %% [markdown] hidden=true
# Let's standardise the columns to better compare them. 

# %% hidden=true
def standardise_col(df):
    '''Standardise dtypes and float precision in a DataFrame.'''
    
    # infer datatypes
    df = df.convert_dtypes()
    
    # fill missing values with pd.NA
    df = df.fillna(pd.NA)

    for col in df.columns:
        try:
            # try converting to numerical dtype
            df[col] = pd.to_numeric(df[col])
            # round to 2 decimal places
            df[col] = df[col].apply(lambda x: round(x, 2) if pd.notna(x) else x)
        except:
            # if error, convert to string
            df[col] = df[col].apply(str)    
    
    return df


# %% hidden=true
def diff_csv_xlsx(csv_dir='./data/csv/', data_xslx=data_xlsx):
    '''Find differences between 2 DataFrames.'''

    # dict that will contain diffs
    differences = dict()

    # directory with csv files
    csv_dir = Path(csv_dir)

    # iterate over csv files and compare to xlsx
    for file in csv_dir.iterdir():
        file_name = str(file.relative_to(csv_dir)).replace('_2022.csv', '').capitalize()

        if file_name == 'Suppliers':
            file_name = 'AwardSuppliers'

        data_csv = pd.read_csv(file)
        
        data_csv_std = standardise_col(data_csv)
        data_xlsx_std = standardise_col(data_xlsx[file_name])

        difference = data_csv_std.compare(data_xlsx_std)

        if difference.shape[0] != 0:
            print(file_name)
            differences[file_name] = difference
            
    return differences


# %% hidden=true
differences = diff_csv_xlsx()

# %% [markdown] hidden=true
# `Planning` and `Tender` still seem to be problematic here. 

# %% hidden=true
differences['Planning'].head()

# %% hidden=true
print(
    f"N of differences in `Planning`: {len(differences['Planning'].iloc[:, :2].dropna())}\n"
    f'Examples:'
)


for i in differences['Planning'].iloc[:, :2].dropna().iloc[0]:
    print('\t', i)

# %% hidden=true
differences['Tender'].head()

# %% hidden=true
print(
    f"N of differences in `Tender`: {len(differences['Tender'].iloc[:, :2].dropna())}\n"
    f'Examples:'
)


for i in differences['Tender'].iloc[:, :2].dropna().iloc[0]:
    print('\t', i)

# %% [markdown] hidden=true
# The `rationale` differences seem to be due to minor encoding problems, so we'll leave this here for now. 

# %% [markdown]
# ## `json`

# %% [markdown]
# ### Load

# %% language="bash"
#
# ocdskit detect-format releases_2022.json

# %% [markdown]
# `releases_2022.json` is a JSON array of [releases](https://standard.open-contracting.org/latest/en/schema/reference/). 

# %%
data_json = pd.read_json('./data/releases_2022.json')

# %%
data_json.shape

# %%
# dtypes
data_json.convert_dtypes().info()

# %%
# count unique values
for col in data_json.columns:
    print(
        f'{col}: {len(data_json[col].apply(str).unique())} unique values'
    )

# %% [markdown]
# Only `releases` and `publishedDate` have more than 1 unique value. Let's have a look at the other columns first. 

# %% [markdown]
# ### `uri`, `license`, `version`, `publisher`, `extensions`, `publicationPolicy`

# %%
data_json['uri'][0]

# %%
data_json['license'][0]

# %%
data_json['version'][0]

# %%
pd.json_normalize(data_json['publisher']).drop_duplicates().transpose()

# %%
data_json['extensions'][0]

# %%
data_json['publicationPolicy'][0]

# %% [markdown]
# ### `releases`

# %% [markdown]
# #### Flatten JSON

# %%
print(
    f'Releases:\n'
    f"    - Type: {set(type(i) for i in data_json['releases'])}\n"
    f"    - Length: {set(len(i) for i in data_json['releases'])}\n"
)

# %% [markdown]
# `releases` are lists of 1 element.

# %%
# flatten and extract releases
releases = pd.json_normalize(
    data_json['releases'].apply(lambda x: x[0])
)

# %%
# releases.to_pickle('./data/releases.pkl')

releases = pd.read_pickle('./data/releases.pkl')

# %% [markdown]
# #### Explore a release

# %%
releases.fillna(method='ffill').fillna(method='bfill').head().transpose()

# %%
releases['awards'][2]

# %%
releases['auctions'][2]

# %%
releases['parties'][2]

# %%
releases['contracts'][2]

# %%
releases['tender.tenderers'][2]

# %%
releases['tender.lots'][2]

# %% [markdown]
# ## Quality control

# %% [markdown]
# ### Non-unique `ocid`, `release_id`, `id` values

# %%
for file in Path('./data/csv/').iterdir():
    data_csv = pd.read_csv(file)
    print(f"Total length of {file}: {len(data_csv)}")

    for col in data_csv.columns:
        if 'id' in col.lower():
            print(
                f"\tDistinct {col}: {len(data_csv[col].unique())}"
            )
    print()

# %% [markdown]
# ### `bids.details`

# %%
duplicates = 0
total = 0

for i,row in pd.json_normalize(releases['bids.details'].dropna()).iterrows():
    total += 1
    distinct = len(row.dropna().drop_duplicates(keep=False))
    
    if distinct == 0:
        duplicates += 1

print(
    f'{duplicates / total:.0%} of bids.details records have duplicate values'
     )

# %%
duplicates = 0
total = 0

for i,row in pd.json_normalize(releases['bids.statistics'].dropna()).iterrows():
    total += 1
    distinct = len(row.dropna().drop_duplicates(keep=False))
    
    if distinct == 0:
        duplicates += 1

print(
    f'{duplicates / total:.0%} of bids.statistics records have duplicate values'
)

# %% [markdown]
# ### `planning.budget.id`

# %%
releases['planning.budget.id'].dropna().sample(20)

# %% [markdown]
# The format of `planning.budget.id` is very lenient. 

# %% [markdown]
# ## Winner and loser provinces

# %% [markdown]
# ### Clean

# %% [markdown]
# #### Parties

# %%
# create a dataframe with all 'parties'
parties = releases.loc[
    releases['tender.procurementMethod'] == 'open',
    'parties'
].dropna().reset_index(drop=True)

# %%
# example of a 'parties' value
parties[0]


# %% [markdown]
# #### Localities

# %%
def extract_localities(parties):
    '''Extract locality from list of `parties`.'''
    
    localities = []
    
    for release in parties:
        r_localities = set()
        
        for party in release:
            p_id = party['id']
            try:
                p_locality = party['address']['locality']
            except:
                p_locality = pd.NA
            try:
                p_region = party['address']['region']
            except:
                p_region = pd.NA
            try:
                p_country = party['address']['countryName']
            except:
                p_country = pd.NA
            for role in set(party['roles']):
                r_localities.add((p_id, p_locality, p_region, p_country, role))
                
        localities.extend(r_localities)
        
    return localities


# %%
# extract localities from 'parties'
localities = extract_localities(parties)

# %%
# convert to dataframe
localities = pd.DataFrame(
    localities,
    columns=['id', 'city', 'region', 'country', 'role']
)

# %%
# preview of localities
localities.dropna().head()

# %% [markdown]
# #### Cities

# %%
# count city/role combinations
cities_roles = localities[['city', 'role', 'country']].groupby(
    ['city', 'role'], as_index=False
).count()

# titlecase city names
cities_roles['city'] = cities_roles['city'].apply(str.title)

# rename column
cities_roles = cities_roles.rename(columns={'country': 'count'})

# preview of 'cities_roles'
cities_roles.head()

# %%
# empty Series to hold 'ranks' values
ranks = pd.Series()

for role in cities_roles['role'].unique():
    # rank each city for each role
    rank = cities_roles.loc[
        cities_roles['role'] == role,
        'count'
    ].rank(ascending=False)
    
    # concatenate existing 'ranks' data and new data
    ranks = pd.concat([ranks, rank])

# %%
# create new 'ranks' column
cities_roles['rank'] = ranks

# %%
# preview
cities_roles.head()

# %% [markdown]
# #### Regions

# %%
# count region/role combinations
regions_roles = localities[['region', 'role', 'country']].groupby(
    ['region', 'role'], as_index=False
).count()

# titlecase region names
regions_roles['region'] = regions_roles['region'].apply(str.title)

# rename column
regions_roles = regions_roles.rename(columns={'country': 'count'})

# preview
regions_roles.head()

# %%
# empty Series to hold 'ranks' values
ranks = pd.Series()

for role in regions_roles['role'].unique():
    # rank each region for each role
    rank = regions_roles.loc[
        regions_roles['role'] == role,
        'count'
    ].rank(ascending=False)
    
    # concatenate existing 'ranks' data and new data
    ranks = pd.concat([ranks, rank])

# %%
# create new 'ranks' column
regions_roles['rank'] = ranks

# %%
# preview
regions_roles.head()

# %% [markdown]
# #### Save to pickle

# %%
# cities_roles.to_pickle('./data/cities_roles.pkl')
# regions_roles.to_pickle('./data/regions_roles.pkl')

cities_roles = pd.read_pickle('./data/cities_roles.pkl')
regions_roles = pd.read_pickle('./data/regions_roles.pkl')

# %% [markdown]
# ### Insight

# %%
# plot tenderers' cities vs suppliers' cities
chart_cities_roles = alt.Chart(
    data=cities_roles.pivot(index='city', columns='role', values='rank').reset_index()
)\
.mark_circle()\
.encode(
    alt.X('tenderer:Q', title='Rank among tenderers'),
    alt.Y('supplier:Q', title='Rank among supplier'),
    tooltip='city:N'
)\
.properties(
    title='Prevalence of cities among tenderers and suppliers'
)

save(chart_cities_roles, './assets/cities_roles.png')

chart_cities_roles

# %%
# plot tenderers' regions vs suppliers' regions
chart_regions_roles = alt.Chart(
    data=regions_roles.pivot(index='region', columns='role', values='rank').reset_index()
)\
.mark_circle()\
.encode(
    alt.X('tenderer:Q', title='Rank among tenderers'),
    alt.Y('supplier:Q', title='Rank among supplier'),
    alt.Color('region:N'),
    tooltip='region:N'
)\
.properties(
    title='Prevalence of regions among tenderers and suppliers'
)

save(chart_regions_roles, './assets/regions_roles.png')

chart_regions_roles


# %% [markdown]
# `Bolivar` is an outlier here: we would have expected it to be much closer to the other provinces in terms of number of suppliers depending on number of tenderers coming from this province. 
#
# Given that it ranks 10 among the most common regions that tenderers come from, it should have been closer to being 10 for the most common regions for suppliers. Instead, it is 23rd, or second to last. 
#
# By contrast, `Sucumbios` is an outlier in the other direction: given how it ranks among tenderers' provinces, it would have been expected to rank much more poorly among suppliers' provinces. 
#
# The agency could use this insight to determine why Bolivar appears so disadvantaged when it comes to open procedures. 
#
# Cross-checking this information with [various economic indicators for Ecuador provinces](https://www.scribd.com/document/398970547/Indice-de-Desarrollo-Humano-en-Ecuador) might also be an interesting exploration. 

# %% [markdown]
# ## Lucky tenderers

# %% [markdown]
# ### Clean

# %% [markdown]
# #### Extract roles

# %%
def extract_roles(parties):
    '''Extract roles from list of `parties`.'''
    
    roles = []
    
    for release in parties:
        r_roles = set()
        
        for party in release:
            p_id = party['id']
            
            p_name = party['name']
            
            for role in set(party['roles']):
                r_roles.add((p_id, p_name, role))
                
        roles.extend(r_roles)
        
    return roles


# %%
roles = extract_roles(parties)

# %%
# convert to dataframe
roles = pd.DataFrame(
    roles,
    columns=['id', 'name', 'role']
)

# %%
roles_ranks = roles.value_counts().reset_index()

roles_ranks = roles_ranks.rename(columns={0: 'count'})

roles_ranks['name'] = roles_ranks['name'].apply(str.title)

roles_ranks.head()

# %%
# empty Series to hold 'ranks' values
ranks = pd.Series()

for role in roles_ranks['role'].unique():
    # rank each city for each role
    rank = roles_ranks.loc[
        roles_ranks['role'] == role,
        'count'
    ].rank(ascending=False)
    
    # concatenate existing 'ranks' data and new data
    ranks = pd.concat([ranks, rank])
    
# create new 'ranks' column
roles_ranks['rank'] = ranks

# preview
roles_ranks.head()

# %%
# example
roles_ranks.loc[roles_ranks['id'] == 'EC-RUC-1711820116001-994410']

# %%
roles_ranks.loc[roles_ranks['role'] == 'supplier'].head()

# %% [markdown]
# #### Save to pickle

# %%
# roles_ranks.to_pickle('./data/roles_ranks.pkl')

roles_ranks = pd.read_pickle('./data/roles_ranks.pkl')

# %% [markdown]
# ### Insight

# %%
# plot tenderers' regions vs suppliers' regions
chart_ranks_roles = alt.Chart(
    data=roles_ranks.pivot_table(
        index='name', columns='role', values='rank'
    ).reset_index()
)\
.mark_circle()\
.encode(
    alt.X('tenderer:Q', title='Rank among tenderers'),
    alt.Y('supplier:Q', title='Rank among suppliers'),
    tooltip='name:N'
)\
.properties(
    title='Prevalence of specific parties among tenderers and suppliers'
)

save(chart_ranks_roles, './assets/roles_ranks.png')

chart_ranks_roles

# %% [markdown]
# This plot is similar to the previous one: we counted all the occurrences where a party has answered a tender and all the occurrences where it became a supplier, and plotted the former against the latter for each party. 
#
# Each dot is a party. The further the dot is to the left, the more times the party has answered a tender. The further the dot is to the bottom, the more times the party has become a supplier (ie won the tender). The aligned dots are due to the way we're assigning ranks: all the top line dots have only been a supplier once, and their rank is an average rank. The second line corresponds to the parties that have been a supplier twice, etc. 
#
# The chart shows that there is a positive correlation between tendering and being a supplier (getting contracts): the parties that answer tenders the most are also the ones most likely to be winning contracts. 
#
# In a competitive process, one would expect that most businesses would have to answer many tenders before getting a contract. This is what we see with almost all the dots being in the top left half of the plot. 
#
# By contrast, any party that is often a supplier but doesn't tender often is unlikely to exist in a competitive market: here, we have only a few dots [0] [1] in the bottom right half of the plot. This could mean many things: it could indicate that the business is extremely good at focusing on the tenders it's most likely to win, or that the business has few competitors for the service that it provides, or, of course, that it is benefitting from corruption. 
#
# We would have to look into this more to know. 
#
# [0]: https://ecuadornegocios.com/info/sacancela-quishpe-robert-cristobal-1749263
# [1]: https://ecuadornegocios.com/info/textidor-4379978

# %% [markdown]
# ## Common contract amounts

# %% [markdown] heading_collapsed=true
# ### Clean

# %% hidden=true
contracts = releases.loc[
    releases['tender.procurementMethod'] == 'open',
    'contracts'
]

contracts = contracts.dropna()

contracts.head()

# %% hidden=true
contracts[2]


# %% hidden=true
def extract_contract_info(contracts):
    
    contract_info = dict()
    
    for i, record in contracts.items():
        contract_info[i] = dict()
        
        amounts = 0
        periods = set()
        
        for contract in record:
            amount = contract['value']['amount']
            amounts += amount
            
            period = contract['period']['durationInDays']
            periods.add(period)
            
        contract_info[i]['amounts'] = amounts
        contract_info[i]['periods'] = max(periods)
        
    contract_info = pd.DataFrame(contract_info).transpose()
    
    return contract_info


# %% hidden=true
contract_info = extract_contract_info(contracts)

# %% hidden=true
contract_info.sort_values('amounts')

# %% [markdown]
# ### Insight

# %%
chart_amounts = alt.Chart(contract_info)\
.mark_bar()\
.encode(
    alt.X('amounts:Q', title='Amounts', scale=alt.Scale(type='log')),
    alt.Y('count()', title='Counts'),
)\
.properties(
    title='Amounts awarded in contracts, log scale',
    width=600
)

save(chart_amounts, './assets/amounts.png')

chart_amounts

# %% [markdown]
# This chart aims to show the distribution of contract amounts on open procedures in 2022. 
#
# Because the smallest contracts are a few USD, while the few largest are in the dozens of millions of USD, it is easier to see the distribution with a log scale. 
#
# Here, we observe that the amounts stated in contracts are clustering around 10k-100k USD, approximatively. 

# %% [markdown] heading_collapsed=true
# ## Number of tenderers vs amount

# %% hidden=true
tenders = pd.read_csv('./csv/tender_2022.csv')

tenders = tenders.loc[tenders['procurementMethod'] == 'open']

tenders = tenders[['value_amount', 'numberOfTenderers']].dropna()

# tenders = tenders.loc[tenders['value_amount'] < 500000]

sns.scatterplot(
    data=tenders,
    x='numberOfTenderers',
    y='value_amount',
)
