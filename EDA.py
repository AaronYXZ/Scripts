## Correlation Map (Heatmap)

corr = df.corr()
f. ax = plt.subplots(figsize = (15,15))
cmap = sns.diverging_palette(150, 20, as_cmap=True)
sns.heatmap(corr, cbar = True, annot = True, square = True, fmt = '.2f',annot_kws={'size': 18}, cmap = cmap)

## set legend location
plt.legend(loc='lower right') #('upper left')
