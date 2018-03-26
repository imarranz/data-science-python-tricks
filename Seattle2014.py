import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt
import seaborn as sns

data = pd.read_csv('Seattle2014.csv')


data['DATE'] = data['DATE'].astype(str)


dt.datetime.strptime(data.loc[1,'DATE'], '%Y%m%d')


data['DATE2'] =  pd.to_datetime(data['DATE'], format='%Y%m%d')


data['MONTH'] = data['DATE2'].dt.month




data['MONTH'] = pd.to_datetime(data['DATE'], format = '%Y%m%d').dt.month




print(data.head(5))

print(data.groupby('MONTH')['TMIN', 'TMAX'].mean()

)

data.boxplot(column = ['TMIN','TMAX'], by = 'MONTH')





aux1 = pd.concat([data[['TMIN']].melt(), data[['MONTH']]], axis = 1)

aux2 = pd.concat([data[['TMAX']].melt(), data[['MONTH']]], axis = 1)

aux3 = pd.concat([aux1, aux2])



aux3.boxplot(column = ['value'], by = ['MONTH', 'variable'])

aux3.boxplot(column = ['value'], by = ['MONTH', 'variable'], figsize = (10,7))

print(aux3.head(5))

sns.factorplot(x = 'MONTH', y = 'value', hue = 'variable', data = aux3)

sns.factorplot(x = 'MONTH', y = 'value', hue = 'variable', data = aux3, kind = 'box')

sns.factorplot(x = 'MONTH', y = 'value', hue = 'variable', data = aux3, kind = 'box', palette = 'Set1')

sns.factorplot(x = 'MONTH', y = 'value', hue = 'variable', data = aux3, kind = 'box', palette = 'Set1', linewidth = 2.5)

sns.factorplot(x = 'MONTH', y = 'value',\
		hue = 'variable', data = aux3, \
		kind = 'box', palette = 'Set1', \
		linewidth = 2.5)

sns.factorplot(x = 'MONTH', y = 'value',\
		hue = 'variable', data = aux3, \
		kind = 'box', palette = 'Set1', \
		linewidth = 0.5, size = 3, aspect = 2)

# https://seaborn.pydata.org/tutorial/aesthetics.html#seaborn-figure-styles

sns.set(style="darkgrid")

# https://seaborn.pydata.org/generated/seaborn.FacetGrid.html
# http://seaborn.pydata.org/tutorial/axis_grids.html#mapping-custom-functions-onto-the-grid

g = sns.FacetGrid(aux3, row = 'variable', col = 'MONTH', margin_titles = True)
bins = np.linspace(aux3['value'].min(), aux3['value'].max(), 25)
g.map(plt.hist, 'value', color = 'steelblue', bins = bins, lw = 0)
g.set_titles(col_template = 'Mes: {col_name}', row_template = 'Temperatura: {row_name}')

# https://stackoverflow.com/questions/31632372/customizing-annotation-with-seaborns-facetgrid

aux3['MONTH'] = aux3['MONTH'].map({1: 'Enero', 2: 'Febrero', 3: 'Marzo', 4: 'Abril', 5: 'Mayo', 6: 'Junio', 7: 'Julio', 8: 'Agosto', 9: 'Septiembre', 10: 'Octubre', 11: 'Noviembre', 12: 'Diciembre'})

g = sns.FacetGrid(aux3, row = 'variable', col = 'MONTH', margin_titles = True)
bins = np.linspace(aux3['value'].min(), aux3['value'].max(), 25)
g.map(plt.hist, 'value', color = 'steelblue', bins = bins, lw = 0)
g.set_titles(col_template = 'Mes: {col_name}', row_template = 'Temperatura: {row_name}')



g = sns.FacetGrid(aux3, col = 'MONTH', margin_titles = True, col_wrap = 4)
bins = np.linspace(aux3['value'].min(), aux3['value'].max(), 25)
g.map(plt.hist, 'value', color = 'steelblue', bins = bins, lw = 0)
g.set_titles(col_template = 'Mes: {col_name}')


g = sns.FacetGrid(aux3, col = 'MONTH', margin_titles = True, col_wrap = 4, hue = 'variable')
bins = np.linspace(aux3['value'].min(), aux3['value'].max(), 25)
g.map(plt.hist, 'value', bins = bins, lw = 0, alpha = 0.7)
g.set_titles(col_template = 'Mes: {col_name}')
g.add_legend(title = 'Temperatura')


g = sns.FacetGrid(aux3, col = 'MONTH', margin_titles = True, col_wrap = 4, hue = 'variable')
bins = np.linspace(aux3['value'].min(), aux3['value'].max(), 25)
g.map(plt.hist, 'value', bins = bins, lw = 0, alpha = 0.7)
plt.subplots_adjust(top = 0.90, bottom = 0.1)
g.fig.suptitle('Histograma mensual')
g.set_titles(col_template = 'Mes: {col_name}')
g.fig.legend(handles = g._legend_data.values(),\
		labels = g._legend_data.keys(),\
		loc = 'lower center', ncol = 2)
#g.add_legend(title = 'Temperatura')

print(g._legend_data.values())
print(g._legend_data.keys())



data['MONTH'] = data['MONTH'].map({1: 'Enero', 2: 'Febrero', 3: 'Marzo', 4: 'Abril', 5: 'Mayo', 6: 'Junio', 7: 'Julio', 8: 'Agosto', 9: 'Septiembre', 10: 'Octubre', 11: 'Noviembre', 12: 'Diciembre'})

g = sns.FacetGrid(data, col = 'MONTH', margin_titles = True, col_wrap = 4, hue = 'WSF2')
g.map(plt.scatter, 'TMIN', 'TMAX', lw = 3)
plt.subplots_adjust(top = 0.90, bottom = 0.1)
g.fig.suptitle('Scatter plot mensual')
g.set_titles(col_template = 'Mes: {col_name}')
g.add_legend()
g.axes[8].set_xlabel('Temperatura Mínima')
g.axes[9].set_xlabel('Temperatura Mínima')
g.axes[10].set_xlabel('Temperatura Mínima')
g.axes[11].set_xlabel('Temperatura Mínima')

g.axes[0].set_ylabel('Temperatura Máxima')
g.axes[4].set_ylabel('Temperatura Máxima')
g.axes[8].set_ylabel('Temperatura Máxima')
