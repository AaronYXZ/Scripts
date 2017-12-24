
## Line and marker styles

x = np.linspace(0, 5, 10)
colors = sns.color_palette('husl')


fig, ax = plt.subplots(figsize=(12,6))

ax.plot(x, x+2, color=colors[0], linewidth=0.50)
ax.plot(x, x+4, color=colors[0], linewidth=2.00)

# possible linestype options ‘-‘, ‘--’, ‘-.’, ‘:’, ‘steps’
ax.plot(x, x+5, color=colors[1], lw=2, linestyle='-')
ax.plot(x, x+6, color=colors[1], lw=2, ls='-.')
ax.plot(x, x+7, color=colors[1], lw=2, ls=':')

# possible marker symbols: marker = '+', 'o', '*', 's', ',', '.', '1', '2', '3', '4', ...
ax.plot(x, x+ 9, color=colors[2], lw=2, ls='--', marker='+')
ax.plot(x, x+10, color=colors[2], lw=2, ls='--', marker='o')
ax.plot(x, x+11, color=colors[2], lw=2, ls='--', marker='s')
ax.plot(x, x+12, color=colors[2], lw=2, ls='--', marker='1')

# marker size and color
ax.plot(x, x+13, color=colors[3], lw=1, ls='-', marker='o', markersize=2)
ax.plot(x, x+15, color=colors[3], lw=1, ls='-', marker='o', markersize=4, markerfacecolor="red")
ax.plot(x, x+16, color=colors[3], lw=1, ls='-', marker='s', markersize=4, 
        markerfacecolor="yellow", markeredgewidth=2, markeredgecolor="blue");

## rotation
plt.xticks(rotation = "vertical")
plt.xticks(rotation = 45)
plt.xticks(rotation = -45)


## set 

ax.set_xlim([0.5, 4.5])
ax.set_ylim([-2, 8])
ax.set_title('An Example Axes')
ax.set_ylabel('Y-Axis')
ax.set_xlabel('X-Axis')


## Set color palette
sns.set_palette("husl")

## Set color palette and choose one for ploting
colors = sns.color_palette()
sns.countplot(x="class", data=titanic, color = colors[1)

## tight layout
                                                          
fig.tight_layout()
                                                      
## Countplot
                                                      
sns.countplot(x = 'class', data = tiantic)

## Barplot
 
sns.barplot(x="day", y="total_bill", data=tips)
            
## Correlation Map (Heatmap)

corr = df.corr()
f. ax = plt.subplots(figsize = (15,15))
cmap = sns.diverging_palette(150, 20, as_cmap=True)
sns.heatmap(corr, cbar = True, annot = True, square = True, fmt = '.2f',annot_kws={'size': 18}, cmap = cmap)

## set legend location
plt.legend(loc='lower right') #('upper left')
