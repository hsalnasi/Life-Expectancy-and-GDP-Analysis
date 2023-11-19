def hist(data, x=None,title='', xlabel='', ylabel='', color=None, element='bars'):
    #create main figure
    plt.figure()
    
    #checking element parameter:
    if element != 'bars':
        sns.histplot(data=data, x=x, element='bars', kde=True, bins=20, color=color)
    else:
        sns.histplot(data=data, x=x, element='poly', kde=True, bins=96, color=color)
        
    # setting title and labels for the hist.    
    plt.title(title)
    plt.xlabel(xlabel)
    plt.style.use('code/dark.mplstyle')
    plt.show()
    
    return 'Histogram Was Created!'
    
def scatter(data, x='', y='',x2='', y2='', ylabel='',title1='',title2='', subplot_title='', color=None, hue=''):
    #initlize custom style
    plt.style.use('code/dark.mplstyle')
    palette = sns.color_palette('Accent', n_colors=len(data['Country'].unique()))
    
    #create main figure and axis object.
    plt.figure(figsize=(20, 8))
    
    ax = plt.subplot(1, 2, 1)
    plt.suptitle(subplot_title, font='Arial', fontsize=20, y=0.9, x=0.5, va='bottom', color='#ab106d')
    scatterplot = sns.scatterplot(data=data, x=x, y=y, color=color, hue=hue, palette=palette)
    
    #setting up the titles and labels
    plt.title(title1)
    plt.ylabel(ylabel, labelpad=15)
    ax.get_legend().remove()  # Remove legend from the first subplot
    
    # create second scatterplot.
    plt.subplot(1, 2, 2)
    scatterplot = sns.scatterplot(data=data, x=x2, y=y2, hue=hue, palette=palette)
    
    plt.title(title2)
    plt.subplots_adjust(top=0.83, left=0.1, wspace=0.2)
    legend = scatterplot.get_legend()
    legend.get_frame().set_alpha(0.4)  # Adjust alpha for the legend
    
    plt.show(), plt.close('all')
    return 'Plot displayed successfully!'

def bar(data, x, y, yscale, title, palette, fill=True, color=None):
    '''a function that creates a bar plot ''' 
    
    fig = plt.figure(figsize=(12,5))
    plt.style.use('code/dark.mplstyle')
    sns.barplot(data=data, x=x, y=y, palette=palette)
    plt.title(title)
    
    plt.show(),plt.close('all')
    
    return '---------'