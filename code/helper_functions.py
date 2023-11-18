def hist(data, x=None,title='', xlabel='', ylabel='', color=None, element='bars'):
    plt.figure()
    
    if element != 'bars':
        
        sns.histplot(data=data, x=x, element='bars', kde=True, bins=20, color=color)
    else:
        sns.histplot(data=data, x=x, element='poly', kde=True, bins=96, color=color)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.style.use('code/dark.mplstyle')
    plt.show()
    
def scatter(data, x='', y='',x2='', y2='', ylabel='',title1='',title2='', subplot_title='', color=None, hue=''):
    
    plt.style.use('code/dark.mplstyle')
    palette = sns.color_palette('Accent', n_colors=len(data['Country'].unique()))
    
    plt.figure(figsize=(20,8))
    
    ax=plt.subplot(1,2,1)
    plt.suptitle(subplot_title, font='Arial', fontsize=20,y=0.9, x=0.5, va='bottom', color='#ab106d')
    scatterplot = sns.scatterplot(data=data, x=x, y=y, color=color, hue=hue, palette=palette)
    
    plt.title(title1)
    plt.ylabel(ylabel, labelpad=15)
    sns.move_legend(ax, 'upper left', bbox_to_anchor=(0,2))
    
    # subplot 2
    plt.subplot(1,2,2)
    #ax.subplot(1,2,2)
    
    sns.scatterplot(data=data, x=x2, y=y2,hue=hue, palette=palette)
    sns.move_legend(ax, 'center left', bbox_to_anchor=(0,0.4))
    
    plt.title(title2)
    plt.subplots_adjust(top=0.83, left=0.1, wspace=0.2)
    scatterplot.legend_.remove()
    legend.get_frame().set_alpha(0.4)
    
    return plt.showw(), plt.close('all')
    
def bar(data, x, y, yscale, title, palette, fill=True, color=None):
    
    fig = plt.figure(figsize=(12,5))
    plt.style.use('code/dark.mplstyle')
    sns.barplot(data=data, x=x, y=y, palette=palette)
    plt.title(title)
    
    return plt.show(),plt.close('all')