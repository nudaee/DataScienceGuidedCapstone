#%%

import pandas as pd
import pickle
#%%
#data = pd.read_pickle(r'C:\Users\Duane\OneDrive\Documents\Springboard\GithubRepositorys\DataScienceGuidedCapstone\models\ski_resort_pricing_model.pkl')
# %%
# %%
with open('C:\Users\Duane\OneDrive\Documents\Springboard\GithubRepositorys\DataScienceGuidedCapstone\models\ski_resort_pricing_model.pkl', 'rb') as file:
    data = pickle.load(file)


# %%
df = pd.DataFrame(data)
# %%
data.head
# %%
