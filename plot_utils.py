import seaborn as sns 
import matplotlib.pyplot as plt

LINE_PLOT_CONFIG = {"x_name":None,
              "y_name":None,
              "hue_name":None,
              "title":None,
              "save_path":None,
              "use_grid": False}

def config_plot(use_grid):
    sns.set(font_scale=2.2,rc={"lines.linewidth": 3})
    if use_grid:
        sns.set_style("whitegrid")
    else: 
        sns.set_style("white")
    plt.figure(figsize=(12, 8))
    
def plot_lines(data,plot_config):
    config_plot(plot_config['use_grid'])
    x_name = plot_config["x_name"]
    y_name = plot_config["y_name"]
    hue_name = plot_config["hue_name"]
    title = plot_config["title"]
    save_path = plot_config["save_path"]
    ax = sns.lineplot(x=x_name, y=y_name,
                      hue=hue_name,style=hue_name,data=data)
    ax.set_title(title)
    if save_path:
        plt.savefig(save_path)
    return ax