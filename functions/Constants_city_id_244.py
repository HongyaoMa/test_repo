# Constants relevant to Birmingham, UK
# Hongyao Ma
# 11/04/2019


##### Folders #####
data_dir = '../data_Brimingham/'
working_data_dir = data_dir + 'working_data/'
intermediate_data_dir = data_dir + 'intermediate_data/'

trips_data_dir = data_dir + 'trips/'
offers_data_dir = data_dir + 'offers/processed_production_only/'
raw_offers_data_dir = data_dir + 'offers/raw_production_only/'
assigned_offers_data_dir = data_dir + 'offers/raw_assigned/'

drivers_data_dir = data_dir + 'drivers'

earnings_data_dir = data_dir +  'earnings/raw/'                     
earnings_data_from_query = data_dir +  'earnings/merged_query/'


##### Files #####
# driver_ab_raw = data_dir +  '../data-Brimingham/drivers/Birmingham_UFD_driver_AB_raw.csv'
zipcode_cluster = data_dir +  'clustering/Birmingham_postcode_districts_dense_only.csv'
birmingham_city_center = data_dir +  'clustering/Birmingham_city_center.csv'

ab_labels_raw = drivers_data_dir + '/Birmingham_UFD_driver_AB_raw.csv'
ab_labels_cleaned = drivers_data_dir + '/Birmingham_UFD_driver_AB.csv'


### 

city_time_zone = 'Europe/London'

### 

group_names_list = ['Treatment', 'Control', 'Unassigned']

###


hod_list_morning = [6, 7, 8, 9]
hod_list_evening = [17, 18, 19]
hod_list_late_night = [23, 0, 1, 2, 3]

morning_rush_hours = []
evening_rush_hours = []
late_night_hours = []

for i in range(5):
    for hod in hod_list_morning:
        morning_rush_hours.append(hod + i * 24)
    for hod in hod_list_evening:
        evening_rush_hours.append(hod + i * 24)

for i in range(7):
    for hod in hod_list_late_night:
        late_night_hours.append(hod + i * 24)        
        
FS_evening = [114, 115, 116, 117, 118, 138, 139, 140, 141, 142]

bar_hours = [119, 120, 121, 122, 143, 144, 145, 146, 147, 148]



##### Constants #####
city_id = 244

uberx_vvid = 2561
uberpool_vvid = -1
uberxl_vvid = 2921
uber_assist_vvid = 10423
uber_access_vvid = 20001023
uber_black_exec_vvid = 736
uber_black_lux_vvid = -1


rush_vvid_1 = 20003877
rush_vvid_2 = 10003096
eats_vvid = 10003092
delivery_vvid_1 = 20003881
delivery_vvid_2 = 20003873
delivery_vvid_3 = 20016885
delivery_vvid_4 = 20016887
delivery_vvid_5 = 20017395

list_uber_x_vvids = [uberx_vvid]
list_uber_pool_vvids = [uberpool_vvid]

list_rides_vvids = [uberx_vvid, uberxl_vvid, uber_black_exec_vvid, uber_black_lux_vvid, 
                    uber_assist_vvid, uber_access_vvid]

list_delivery_vvids = [rush_vvid_1, rush_vvid_2, eats_vvid, delivery_vvid_1, delivery_vvid_2, delivery_vvid_3, 
                        delivery_vvid_4, delivery_vvid_5]

# lat_long_origin = h3core.geo_to_h3(0, 0, 9)


######################## UFD Experiment Dates ##########################

pre_exp_weeks = range(26)
# initialization_weeks = []
exp_weeks = range(26, 74, 1)
post_exp_weeks = range(74, 52*2+2, 1)


exp_stage_index_column = 'offer_woy_local'
# list_exp_stages = ['pre', 'exp', 'post']
# list_exp_stage_ranges = [pre_exp_weeks, exp_weeks, post_exp_weeks]
exp_start_indicator = 26
exp_end_indicator = 74

dates = [
    '2018-06-28',
    '2018-09-01',
    '2019-01-01',
    '2019-05-31',
    '2019-06-25'
]

list_colors = ['black','green','blue','green','red']

list_dates_to_mark = []
for this_date in dates:
    this_datetime = pd.to_datetime(datetime.strptime(this_date, '%Y-%m-%d'))
    list_dates_to_mark.append(this_datetime.weekofyear + 52 * (this_datetime.year == 2019))

# list_dates_to_mark

####################################

city_core_clusters = [
    'c45a3727-acc2-4800-a994-b65cb556ff80',
    '467b81e2-0f4c-46bd-8350-cc21cffcc63a',
    'd486fa06-2f55-4b0f-bddc-e976771ea4d1',
    '15fadfa9-4392-40de-9d01-6d9f304cb3bf',
    '8b03dab9-3614-4dd9-8040-ade4f3bbebb5',
]


Birmingham_core_hexagons = [
 '89195c0592bffff',
 '89195c059cfffff',
 '89195c05b13ffff',
 '89195c0594fffff',
 '89195c05babffff',
 '89195c059c7ffff',
 '89195c059dbffff',
 '89195c0590fffff',
 '89195c0582fffff',
 '89195c05907ffff',
 '89195c05b83ffff',
 '89195c05bbbffff',
 '89195c05b9bffff',
 '89195c05b0bffff',
 '89195c05967ffff',
 '89195c05bb3ffff',
 '89195c05977ffff',
 '89195c3a6dbffff',
 '89195c3a6d7ffff',
 '89195c05903ffff',
 '89195c05867ffff',
 '89195c3a6d3ffff',
 '89195c05b17ffff',
 '89195c058afffff',
 '89195c05b97ffff',
 '89195c05b8fffff',
 '89195c05943ffff',
 '89195c0590bffff',
 '89195c05b03ffff',
 '89195c05b93ffff',
 '89195c05877ffff',
 '89195c05ba7ffff',
 '89195c05b0fffff',
 '89195c05bd7ffff',
 '89195c0586fffff',
 '89195c05947ffff',
 '89195c0593bffff',
 '89195c0583bffff',
 '89195c05863ffff',
 '89195c05b87ffff',
 '89195c0595bffff',
 '89195c05823ffff',
 '89195c05953ffff',
 '89195c0582bffff',
 '89195c05bb7ffff',
 '89195c0591bffff',
 '89195c05963ffff',
 '89195c05837ffff',
 '89195c0596bffff',
 '89195c3a693ffff',
 '89195c05b07ffff',
 '89195c05bafffff',
 '89195c05973ffff',
 '89195c05827ffff',
 '89195c05b1bffff',
 '89195c05b8bffff',
 '89195c0596fffff',
 '89195c05833ffff',
 '89195c0594bffff',
 '89195c3a69bffff',
 '89195c059cbffff',
 '89195c059c3ffff',
 '89195c05bc7ffff',
 '89195c05957ffff',
 '89195c05b33ffff',
 '89195c0597bffff',
 '89195c05913ffff',
 '89195c05ba3ffff'
]

Coventry_core_hexagons = [
 '89195cadc57ffff',
 '89195cadc0fffff',
 '89195cadcc3ffff',
 '89195cadc13ffff',
 '89195cadc07ffff',
 '89195cadc53ffff',
 '89195cadc73ffff',
 '89195cadccbffff',
 '89195cadc8bffff',
 '89195cadccfffff',
 '89195cadcd7ffff',
 '89195cadc17ffff',
 '89195cadc43ffff',
 '89195cadc47ffff',
 '89195cadcc7ffff',
 '89195cadc1bffff',
 '89195cadc8fffff',
 '89195cadc03ffff',
 '89195cadc0bffff'
]


