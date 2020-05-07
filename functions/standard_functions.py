# Function --- print basic info of a data frame
# flag_print_info: if set to 0, do not print anything
# num_rows: numbner of rows to print from the data frame (excluding the first row)


################################################################
#                   The Timer
################################################################

def tic():
    global global_tic_timer_start
    global_tic_timer_start = time.time()
    print("\nTimer starting!")

def toc():
    end = time.time()
    print 'Total time is: ' + str(end - global_tic_timer_start)

## Import up sound alert dependencies
from IPython.display import Audio, display

def allDone():
  display(Audio(url='https://sound.peal.io/ps/audios/000/000/537/original/woo_vu_luvub_dub_dub.wav', autoplay=True))
## Insert whatever audio file you want above

################################################################
#               Plotting or Displaying Information
################################################################

def rush_hour_shade():
    for week in range(7):
        plt.axvspan(7+week*24, 9+week*24, alpha = 0.1, color='black')
        plt.axvspan(17+week*24, 19+week*24, alpha = 0.1, color='green')

def gray_markers(inds):
    i_ind = 0
    for ind in inds:
        plt.axvspan(ind-0.1, ind+0.1, alpha = 0.2, color = 'black')

def colored_markers(inds, colors):
    i_ind = 0
    for ind in inds:
        plt.axvspan(ind-0.1, ind+0.1, alpha = 0.2, color = colors[i_ind])
        i_ind = i_ind + 1

def print_df_info(data_frame, flag_print_info, num_rows):
    if flag_print_info:
        print 'data type: '+ type(data_frame).__name__
        print 'length of data: ' + str(len(data_frame))
        print 'number of columns: ' + str(len(data_frame.columns))
        print

        print data_frame.columns
        print 

        if num_rows > 0:
            print data_frame[:num_rows]

def print_cols(input_df):
    for col in input_df.columns:
        print '\t\item\code{' + col + '}'
        # print '\t' + col   

def print_full(x):
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)
    print(x)
    pd.reset_option('display.max_columns')
    pd.reset_option('display.max_rows')   


linestyles = ['-', '--', '-.', ':']

def plot_metric_comparison(input_df, metric, groups_to_plot, group_names_list, the_xlabel, the_ylabel, title, ylim):
    plt.figure(figsize=(12, 4))

    for i_group in groups_to_plot:            
        plt.plot(input_df[i_group].index, input_df[i_group][metric], 
                 label = group_names_list[i_group], linestyle = linestyles[i_group], color = sns.color_palette()[i_group])

        plt.fill_between(input_df[i_group].index, 
                         input_df[i_group][metric] - input_df[i_group][metric + '_stderr'], 
                         input_df[i_group][metric] + input_df[i_group][metric + '_stderr'],
                         alpha = 0.2, color = sns.color_palette()[i_group])

    if group_by_metric in ['offer_woy_local', 'job_created_woy_local', 'woy']:
        colored_markers(list_dates_to_mark, list_colors)

    if group_by_metric in ['offer_how_local', 'job_created_how_local']:
        rush_hour_shade()
        plt.xticks(np.arange(0, 24*7, 12)) 
        plt.grid(True,which='major', axis='x', alpha = 0.4)        
        
    if ylim != None:
        plt.ylim(ylim)
        
    plt.xlabel(the_xlabel)
    plt.ylabel(the_ylabel)
    plt.title(title)
    # plt.legend(loc='upper left')
    plt.legend()
    plt.show()


def plot_metric_gap(input_df, metric, groups, gap_suffix, the_xlabel, the_ylabel, the_title, ylim):
    plt.figure(figsize = (12, 4))

    plt.plot(input_df[groups[0]].index, input_df[groups[0]][metric] - input_df[groups[1]][metric], 
             label = metric + gap_suffix)

    plt.grid(True, which='major', axis='y', alpha = 0.4)
    
    if group_by_metric in ['offer_woy_local', 'job_created_woy_local', 'woy']:
        colored_markers(list_dates_to_mark, list_colors)

    if group_by_metric in ['offer_how_local', 'job_created_how_local']:
        rush_hour_shade()
        plt.xticks(np.arange(0, 24*7, 6)) 
        plt.grid(True,which='major', axis='x', alpha = 0.4)  

    if ylim != None:
        plt.ylim(ylim)
        
    plt.xlabel(the_xlabel)
    plt.ylabel(the_ylabel)
    plt.title(the_title)

    plt.legend(loc='upper left')

    plt.show()


def hist_metric_comparison(input_df, metrics, groups_to_plot, group_names_list, the_xlabels, the_ylabels, titles, 
                           bins_list, xlims, ylims, add_suffix, filename = None):
    

    n_hist = len(metrics)
    f = plt.figure(figsize=(n_hist * 5.5, 4))


    for i_hist in range(n_hist):
        plt.subplot(1, n_hist, i_hist+1)
        groups_to_plot_current = groups_to_plot[i_hist]

        for i_group in groups_to_plot_current:
            plt.hist(input_df[i_group][metrics[i_hist] + add_suffix], bins = bins_list[i_hist], 
                alpha = 0.4, label = group_names_list[i_group], color = sns.color_palette()[i_group])
            plt.xlabel(the_xlabels[i_hist])
            plt.ylabel(the_ylabels[i_hist])
            plt.title(titles[i_hist])
            plt.legend()

            if xlims[i_hist] != None:
                plt.xlim(xlims[i_hist])  

            if ylims[i_hist] != None:
                plt.ylim(ylims[i_hist])
              
    plt.show()

    if flag_save_figures:
        if filename is None:
            f.savefig("temp_fig.png", bbox_inches='tight')
        else:
            f.savefig(figure_dir + filename + '.pdf', bbox_inches='tight')
            f.savefig(figure_dir + 'png/' + filename + '.png', bbox_inches='tight', dpi=600)
            # f.savefig(filename + '.eps', bbox_inches='tight')

    # return f        

def scatter_metric_comparison(input_df, metrics_x, metrics_y, groups_to_plot, group_names_list, the_xlabels, 
                              the_ylabels, titles, size_col, size_normalization, xlims, ylims, input_alpha, add_suffix, 
                              filename = None):

    n_hist = len(metrics_x)
    f = plt.figure(figsize=(n_hist * 5.5, 4))

    for i_hist in range(n_hist):
        groups_to_plot_current = groups_to_plot[i_hist]
        plt.subplot(1, n_hist, i_hist+1)
        for i_group in groups_to_plot_current:
            plt.scatter(input_df[i_group][metrics_x[i_hist] + add_suffix],
                        input_df[i_group][metrics_y[i_hist] + add_suffix],
                        s = input_df[i_group][size_col + add_suffix] * 1.0 /size_normalization, 
                        alpha = input_alpha, label = group_names_list[i_group],
                        color = sns.color_palette()[i_group])
            
            plt.xlabel(the_xlabels[i_hist])
            plt.ylabel(the_ylabels[i_hist])
            plt.title(titles[i_hist])
            plt.legend()
            
            if xlims[i_hist] != None:
                plt.xlim(xlims[i_hist])  

            if ylims[i_hist] != None:
                plt.ylim(ylims[i_hist])
    
    plt.show()
    if flag_save_figures:
        if filename is None:
            f.savefig("temp_fig.png", bbox_inches='tight')
        else:
            f.savefig(figure_dir + filename + '.pdf', bbox_inches='tight')
            f.savefig(figure_dir + 'png/' + filename + '.png', bbox_inches='tight', dpi=600)    


def scatter_reg_metrics(input_df, metric_x, metric_y, groups_to_plot, group_names_list, 
                        xlims, ylims, add_suffix, input_alpha, size_col, size_normalization, filename = None):
    
    for i_hist in groups_to_plot:               
        f = sns.jointplot(metric_x + add_suffix, metric_y + add_suffix, data = df_by_group[i_hist], kind="reg", 
                      xlim = xlims[i_hist], ylim = ylims[i_hist], height = 4, 
                      label = group_names_list[i_hist], color = sns.color_palette()[i_hist],
                     joint_kws = {'scatter_kws':dict(alpha = input_alpha, 
                                                     s = input_df[i_hist][size_col + add_suffix] * 1.0 /size_normalization)})
        plt.legend(loc='upper left') # frameon=False,

        if flag_save_figures:
            if filename is None:
                f.savefig("temp_fig.png", bbox_inches='tight')
            else:
                f.savefig(figure_dir + filename + '_' + group_names_list[i_hist] + '.pdf', bbox_inches='tight')
                f.savefig(figure_dir + 'png/' + '_' + group_names_list[i_hist] + filename + '.png', bbox_inches='tight', dpi=600)

    plt.show()

###############################################################
#       Average and standard error of the mean by group 
###############################################################

def by_group_metric_processing(input_df, label_col, label_list, group_by_metric, 
                               metric_per_driver, metric_per_online_driver, count_col):
    # Make a copy of the input data frame, since we're making some 
    input_df = input_df.copy()
    
    # Total number of labels
    n_labels = len(label_list)
    
    # Compute how many total "things" (drivers, or jobs, etc) there are per label
    # Each row of the input data should be an individual "thing", with some label, and group_by_metric 
    # The "metric_per_driver" only makes sense if we're looking at drivers, and not jobs
    unique_drivrs_per_group = []     
    
    # The list of unique metrics to aggregate
    list_unique_metrics = list_dedup(metric_per_driver + metric_per_online_driver)
    
    # Force the type as float to deal with the non-numerical aggragation issues of Pandas
    for this_metric in list_unique_metrics:
        input_df[this_metric] = input_df[this_metric].astype(float)
        
    
    ###### Calculate the averages and standard deviations #######
    group_by_columns = [group_by_metric, label_col]    
    all_relevant_cols = list_dedup(list_unique_metrics + group_by_columns)
    
    # The sum by (label, group_by_metric), which is the sum across all "things" in each pair
    by_metric = input_df[all_relevant_cols].groupby(group_by_columns).sum().reset_index()
    
    # The STD by label and group_by_metric
    by_metric_std = input_df[all_relevant_cols].groupby(group_by_columns).std().reset_index()
    by_metric = by_metric.merge(by_metric_std, 
                          left_on = group_by_columns, right_on = group_by_columns, 
                          how = 'left', suffixes = ('_sum', '_std'))    
    
    # Number of Unique "things" in each (label, group_by_metric) pair
    by_metric_driver_count = input_df.groupby(group_by_columns).agg({count_col:'nunique'}).reset_index()
    by_metric = by_metric.merge(by_metric_driver_count, 
                          left_on = group_by_columns, right_on = group_by_columns, how = 'left')    
    
    
    ######### The Output Data  ######## 
    
    global output_df
    output_df = []

    for i_label in range(n_labels):

        # All input data corresponding to this label
        this_label_df = input_df[input_df[label_col] == label_list[i_label]]    
        unique_drivrs_per_group.append(this_label_df[count_col].nunique())          
        
        # Select aggregated data corresponding to the current label
        temp_df = by_metric[by_metric[label_col] == label_list[i_label]].copy()

        # Fraction of Drivers who are Online
        temp_df['fraction_online'] = (temp_df[count_col] / unique_drivrs_per_group[i_label])
        # Estimator 1: easy but slightly biased
        # temp_df['fraction_online_stderr'] = np.sqrt(
        #    (temp_df['fraction_online'] * (1 - temp_df['fraction_online'])) / (unique_drivrs_per_group[i_label]-1))
        # Estimator 2: should be the unbiased estimator; the only difference is the normalization by n-1 and not n
        temp_df['fraction_online_stderr'] = np.sqrt(
            temp_df[count_col] * (1 - temp_df['fraction_online'])**2 + 
            (unique_drivrs_per_group[i_label] - temp_df[count_col]) * (temp_df['fraction_online'])**2
        ) /  (unique_drivrs_per_group[i_label] - 1)
        
        ########### Metric per Driver: Mean and STDERR ##########
        
        # Compute the averages per driver
        for this_metric in metric_per_driver:
            temp_df[this_metric] = (temp_df[this_metric + '_sum'] / unique_drivrs_per_group[i_label])

        #### Compute the standard error of the mean per driver: need to consider drivers who didn't appear ###
        
        # The raw data for each group 
        # this_label_df = input_df[input_df[label_col] == label_list[i_label]]
        this_label_df = this_label_df[metric_per_driver + group_by_columns]
        
        # Merge it with the per driver average
        temp_df_relevant_cols = group_by_columns + metric_per_driver
        this_label_df = this_label_df.merge(temp_df[temp_df_relevant_cols], 
                                      left_on = group_by_columns, right_on = group_by_columns, 
                                      how = 'left', suffixes = ('', '_mean'))
        
        # Compute the sum of observations minus average squared
        for this_metric in metric_per_driver:
            this_label_df[this_metric + '_minus_mean_squared'] = (
                (this_label_df[this_metric] - this_label_df[this_metric + '_mean']) ** 2    
            )
        
        # The sum of the minus mean squared
        cols_to_keep = []
        for col in metric_per_driver:
            cols_to_keep.append(col + '_minus_mean_squared')
            
        this_label_df = this_label_df[cols_to_keep + [group_by_metric]]
        this_label_df_grouped = this_label_df.groupby(group_by_metric).sum().reset_index()
        

        # Merge with the df that contains the rest of the averages and std, etc
        temp_df = temp_df.merge(this_label_df_grouped, left_on = group_by_metric, right_on = group_by_metric, 
                                how = 'left')
        
        # The standard error of the mean: sum of the square deviation divided by sample size
        for this_metric in metric_per_driver:
            temp_df[this_metric + '_stderr'] = np.sqrt(
                (temp_df[this_metric + '_minus_mean_squared'] + 
                 (unique_drivrs_per_group[i_label] - temp_df[count_col]) * (temp_df[this_metric])**2
                ) 
                ) / (unique_drivrs_per_group[i_label] - 1)
            
            
        ########### Metric per Online Driver: Mean and STDERR ########
        
        this_label_df = input_df[input_df[label_col] == label_list[i_label]]
        this_label_df = this_label_df[metric_per_online_driver + group_by_columns]
        
        # add columns corresponding to the metrics being not null
        for this_metric in metric_per_online_driver:
            this_label_df[this_metric + '_not_nan'] = (~this_label_df[this_metric].isna())
            
        # Total number of entries that are not null
        this_label_df_grouped = this_label_df.groupby(group_by_metric).sum().reset_index()

        cols_to_keep = []
        for col in metric_per_online_driver:
            cols_to_keep.append(col + '_not_nan')

        # print temp_df.shape[0]

        # print this_label_df_grouped.columns
        temp_df = temp_df.merge(this_label_df_grouped[cols_to_keep + [group_by_metric]], 
                                left_on = group_by_metric, right_on = group_by_metric, 
                                how = 'left')        
        
        # Normize only by the entries that are actuall not null
        
        for this_metric in metric_per_online_driver:
            if this_metric in metric_per_driver:
                temp_df[this_metric + '_per_online_driver'] = (
                    temp_df[this_metric + '_sum'] / temp_df[this_metric + '_not_nan']
                )
                temp_df[this_metric + '_per_online_driver_stderr'] = (
                    temp_df[this_metric + '_std'] / np.sqrt(temp_df[this_metric + '_not_nan'] - 1)) 
                
            else:
                temp_df[this_metric] = (temp_df[this_metric + '_sum'] / temp_df[this_metric + '_not_nan'])
                temp_df[this_metric + '_stderr'] = (temp_df[this_metric + '_std'] / np.sqrt(temp_df[this_metric + '_not_nan'] - 1)) 
            
        temp_df.set_index(group_by_metric, inplace = True)
        
        output_df.append(temp_df.copy())    

    gc.collect()

    print label_list
    print unique_drivrs_per_group 
    
    return output_df


def mixed_rows_to_suffix(input_df, group_name_col, group_names_list, metric_list, merge_on_col):

    global output_df
    
    # Number of groups
    n_groups = len(group_names_list)
    
    # The first group
    output_df = input_df[input_df[group_name_col] == group_names_list[0]].copy()
    for col in metric_list:
        output_df.rename(columns = {col : col + '_' + group_names_list[0]}, inplace = True)
    
    output_df.pop(group_name_col)
    
    # The remaining groups
    for i_group in range(1, n_groups, 1):
        temp_df = input_df[input_df[group_name_col] == group_names_list[i_group]].copy()
        
        if 'treatment_group_key' in temp_df.columns:
            temp_df.pop('treatment_group_key')

        for col in metric_list:
            temp_df.rename(columns = {col : col + '_' + group_names_list[i_group]}, inplace = True)
        
        if group_name_col in temp_df.columns:
            # print temp_df.columns
            temp_df.pop(group_name_col)

        output_df = output_df.merge(temp_df, how = 'outer', 
                                    left_on = merge_on_col, right_on = merge_on_col)
        
    # output_df.head()
    
    return output_df    

################################################################
#               Loading and Processing Data
################################################################

def result_df(res):
    data = {}
    for row in res:
        for key in row:
            try:
                data[key].append(row[key])
            except:
                data[key] = [row[key]]
    return pd.DataFrame(data)


def cols_add_prefix(input_df, prefix):
    for col in df.columns:
        input_df.rename(columns = {col: prefix + col}, inplace = True)


def get_file_list_in_dir(subdir, file_extension):
    current_dir = os.getcwd();
    data_dir = os.getcwd() + subdir

    file_list = []

    os.chdir(data_dir)
    for file in glob.glob('*.' + file_extension):
        file_list.append(file)
        # print(file)
        
    os.chdir(current_dir)
 
    file_list.sort(reverse=False)
    return file_list


def csv_list_to_df(data_dir, file_list, flat_display_info):
    global dtemp_df_for_loading_dataf 
    temp_df_for_loading_data = pd.DataFrame()

    for this_file in file_list:

        print 'Loading file: ' + this_file

        temp_df = pd.read_csv(data_dir + this_file)
        if flat_display_info:
            print 'Number of rows =' + str(temp_df.shape[0])
            print 

        temp_df_for_loading_data = temp_df_for_loading_data.append(temp_df, ignore_index = True)

    if flat_display_info:
        print 'Total rows = ' + str(temp_df_for_loading_data.shape[0])

    gc.collect()

    return temp_df_for_loading_data
        

################################################################
#                      Operations to lists
################################################################

def list_dedup(input_list):
    # list_dedup gets rid of redundant elements from a list
    global output_list
    output_list = []
    
    for item in input_list:
        if item not in output_list:
            output_list.append(item)
    return output_list


def list_replace(input_list, from_item, to_item):
    global output_list 
    output_list = []
    
    for item in input_list:
        if item == from_item:
            output_list.append(to_item)
        else:
            output_list.append(item)

    return output_list

##########################################################################################
############################ COMPUTATION OF WEIGHTED AVERAGE #############################
##########################################################################################

def weighted_average(input_dataframe, group_by_cols, dataCols, weightCols):
# weighted_average computes the weighted average of columns in dataCols of input_dataframe, grouped by groups, weighted by weightCol
# output: a dataframe with the weighted averages
# input:
#   input_dataframe: the input dataframe!
#   groups: list of colums to group data to compute weighted average
#   dataCols: list of columns that contain data on which we would like to compute weighted average for
#   weightCol: a single column that contains the weights. If not, will add a "count" column where the couts are set to be 1

    # Make a copy of the input dataframe
    input_dataframe = input_dataframe.copy()

    flag_debug = 0
    
    # Set the weights to ones if we don't have weights
    weight_default_name = 'counts'    
    if weightCols == None:
        if flag_debug:
            print 'No weight columns! Setting all to ' + weight_default_name
        weightCols = []
        for i in range(len(dataCols)):
            weightCols.append(weight_default_name)
        if flag_debug:    
            print weightCols

    
    # Create a column called counts if there isn't one
    if ~(weight_default_name in input_dataframe.columns):
        input_dataframe[weight_default_name] = 1
        if flag_debug:
            print '\nNo column named counts! Creating one with all 1s!'        
            print input_dataframe.columns
    
    # Replace all None elements in weightCols by the default counts
    weightCols = list_replace(weightCols, None, weight_default_name)
    
    # If there's no grouping
    if group_by_cols == None:
        if flag_debug:    
            print '\nNo Groups are given! Creating one called dummy!'
        input_dataframe['dummy_group'] = 'dummy'
        group_by_cols = ['dummy_group']     
    

    # Take only the relevant columns
    relevalt_cols = group_by_cols + dataCols + weightCols
    if flag_debug: 
        print '\nRelevant columns:'    
        print relevalt_cols
    
    # Deduplicate the relevant columns
    relevalt_cols = list_dedup(relevalt_cols)
    if flag_debug:
        print '\nDeduped relevant columns'
        print relevalt_cols
    
    # Make a copy of the input dataframe
    input_dataframe = input_dataframe[relevalt_cols]
    
    # Compute data multiplied by weights
    for i in range(len(dataCols)):
        weighted_col_name = dataCols[i] + '_mult_weight'
        input_dataframe[weighted_col_name] = input_dataframe[dataCols[i]] * input_dataframe[weightCols[i]]
    
    if flag_debug:
        print '\nColumns of the DF with weighted entries'
        print input_dataframe.columns
    
    # Compute the sum of each group
    global dataframe_average
    dataframe_average = input_dataframe.groupby(group_by_cols).sum().reset_index()

    if flag_debug:
        print '\nColumns after group by:'
        print dataframe_average.columns
    
    # Divide the sum by the total weight, and rename the columns
    for i in range(len(dataCols)):
        # print dataCols[i]        
        weighted_col_name = dataCols[i] + '_mult_weight'
        if flag_debug:
            print weighted_col_name
        dataframe_average[weighted_col_name] = dataframe_average[weighted_col_name] / dataframe_average[weightCols[i]]
        dataframe_average.rename(columns={weighted_col_name: 'mean_' + dataCols[i], 
                                         dataCols[i] : 'sum_' + dataCols[i]}, inplace=True)

    # Rename the total counts column
    for col in weightCols:
        dataframe_average.rename(columns={col: 'sum_' + col}, inplace=True)

    # Pop the dummy group if there is any
    if 'dummy_group' in group_by_cols:
        dataframe_average.pop('dummy_group')

    # Return the weighted average
    return dataframe_average

##########################################################################################
############################ Hexagon -> Hexcluster -> Hexagon  ###########################
##########################################################################################
def cluster_level_sum(input_df, cluster_col, group_cols, data_cols, weight_cols, cluster_mapping):
    global agg_df 
    
    flag_debug = 0
    
    # Add the cluster to the colums to group by
    group_cols.append(cluster_col)
    if flag_debug:
        print group_cols
    
    # Compute the group sums
    agg_df = weighted_average(input_df, group_cols, data_cols, weight_cols)
    
    # Keep only the relevant columns
    list_relevant_cols = group_cols
    for col in data_cols:
        list_relevant_cols.append('sum_' + col)
    if flag_debug:
        print list_relevant_cols
    
    agg_df = agg_df[list_relevant_cols].copy()
    
    for col in data_cols:
        agg_df.rename(columns = {'sum_' + col : col}, inplace=True)

    if flag_debug:
        print agg_df.head()
        
    # Merge with the cluster-hexagon mapping
    agg_df = agg_df.merge(cluster_mapping, left_on = cluster_col, right_on = 'hexcluster_uuid', how = 'inner')
    agg_df.pop('hexcluster_uuid')
    
    if flag_debug:
        print agg_df.head()
        
    return agg_df
