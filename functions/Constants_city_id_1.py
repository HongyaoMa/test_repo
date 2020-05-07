

##### Folders #####
data_dir = '../data_SF/'

working_data_dir = data_dir + 'working_data/'
intermediate_data_dir = data_dir + 'intermediate_data/'

trips_data_dir = data_dir + 'trips/'
offers_data_dir = data_dir + 'offers/processed_production_only/'
raw_offers_data_dir = data_dir + 'offers/raw_production_only/'
assigned_offers_data_dir = data_dir + 'offers/raw_assigned/'

drivers_data_dir = data_dir + 'drivers'

earnings_data_dir = data_dir +  'earnings/raw/'                     
earnings_data_from_query = data_dir +  'earnings/merged_query/'


###
fop_v1_cluster = data_dir + 'clustering/SF_fop_v1_hexagon_to_hexcluster_mapping.csv'

ab_labels_raw = data_dir + 'drivers/SF_luigi_exp_driver_treatment_raw.csv'
ab_labels_cleaned = data_dir + 'drivers/SF_luigi_exp_driver_treatment.csv'

### 

city_time_zone = 'America/Los_Angeles'


### 

group_names_list = ['full_trip_info_with_fare', 'full_trip_info_without_fare', 'control', 'Unassigned']
list_treament_labels = ['full_trip_info_with_fare', 'full_trip_info_without_fare']
list_control_labels = ['control']

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

####

exp_weeks = range(49, 53, 1)

dates = [
    '2019-12-03',
    '2020-01-06',
]

list_colors = ['green','black']

list_dates_to_mark = []
for this_date in dates:
    this_datetime = pd.to_datetime(datetime.strptime(this_date, '%Y-%m-%d'))
    list_dates_to_mark.append(this_datetime.weekofyear + 52 * (this_datetime.year == 2020))


##### Constants #####

uberx_vvid = 8
uberx_diamond = 20014645
uberx_comfort = 20017885
uberx_select = 2930
uberx_trip_slim_vvid = 20005409
uberpool_vvid = 20005011
uberpool_vvid_2 = 1491
uberxl_vvid = 942
uber_black = 1
uber_black_suv = 2
uber_assist_vvid = 5101
uber_assist_vvid_2 = 4651
uber_wav = 1930

taxi_vvid = 69
uberx_atg_dev = 10002112

# 20002283 cannot tell what this is from Allen Key

rush_vvid_1 = 11587


list_uber_x_vvids = [uberx_vvid, uberx_diamond, uberx_comfort, uberx_select, uberx_trip_slim_vvid]
list_uber_pool_vvids = [uberpool_vvid, uberpool_vvid_2]

list_rides_vvids = [uberx_vvid, uberx_diamond, uberx_comfort, uberx_select, uberx_trip_slim_vvid, uberpool_vvid, uberpool_vvid_2,
					uberxl_vvid, uber_black, uber_black_suv, 
                    uber_assist_vvid, uber_assist_vvid_2, uber_wav]

list_delivery_vvids = [rush_vvid_1]


###

exp_stage_index_column = 'offer_date'
exp_start_indicator = '2019-12-03'
exp_end_indicator = '2020-01-06'


sfo_cluster = '7f6cc381-c37e-4136-846e-10ce74b5c8f6'
sfo_hexagons = [
 '89283092e23ffff',
 '89283092e3bffff',
 '89283092e37ffff',
 '892830928cbffff',
 '89283092a97ffff',
 '89283092e2fffff',
 '89283092853ffff',
 '89283092e2bffff',
 '89283092e33ffff',
 '89283092e67ffff',
 '89283092e27ffff',
 '8928309285bffff']

fidi_clusters = [
	'0fa3b382-ba2c-4960-afc6-9644ced746a4', # 45017
	'f6dbac8f-8a7b-43f4-ad48-f944eddb7fb5', # 4396	
	'a14c891f-eaac-4c11-8895-4eca3a15548e', # 31061
	'48f8152a-a88e-4302-b11f-0e570cf478be', # 9642
	'7d84d8c8-19b6-44dc-896f-dd2e1dba68ea', # 22797		
	'c2dda47e-217b-4157-b7b0-def7b6ee4d04', # 179			
	'65f6c62a-bf9c-4698-810c-d676ffeb2b8a', # 2146
	'2f39b4ce-2bc2-4ae1-ae35-778189d6b64c', # 13009
	'90c18fb1-e750-4c19-9be6-57251005d0ee', # 904
	'cd3a07bf-2f1b-4552-b3b8-d82e51e757aa', # 2301
	'0b6b41cf-9276-4066-a1e7-b3fa3751c89d', # 2798
	'4dece1a5-86df-40a0-b442-5eb218d10fe4', # 20888
	'0f0da34d-efaa-4486-af5c-16de118d31b1', # 2163
]   

fidi_hexagons = [
 '89283082abbffff',
 '892830801abffff',
 '89283082a63ffff',
 '89283082a77ffff',
 '8928308052fffff',
 '89283082a0bffff',
 '8928308012bffff',
 '892830806b3ffff',
 '89283080307ffff',
 '89283080563ffff',
 '892830800cfffff',
 '892830803cfffff',
 '89283080037ffff',
 '89283080513ffff',
 '89283080447ffff',
 '892830805cfffff',
 '8928308011bffff',
 '89283082bcfffff',
 '89283082a43ffff',
 '89283080097ffff',
 '89283080353ffff',
 '89283080067ffff',
 '89283080397ffff',
 '89283082a53ffff',
 '89283080c83ffff',
 '89283082bcbffff',
 '8928308002bffff',
 '8928308042fffff',
 '89283080407ffff',
 '892830803a3ffff',
 '892830801b3ffff',
 '892830801c3ffff',
 '892830800d7ffff',
 '8928308286bffff',
 '89283082a47ffff',
 '89283082b17ffff',
 '89283080027ffff',
 '89283080113ffff',
 '8928308018fffff',
 '89283080cdbffff',
 '89283080313ffff',
 '89283082a2bffff',
 '892830801cbffff',
 '89283080117ffff',
 '89283080c87ffff',
 '89283082aa7ffff',
 '89283082bc7ffff',
 '89283082b9bffff',
 '8928308286fffff',
 '89283082a3bffff',
 '8928308288fffff',
 '89283082a57ffff',
 '8928308284bffff',
 '89283082b1bffff',
 '89283082a2fffff',
 '8928308046fffff',
 '892830800c3ffff',
 '8928308000bffff',
 '8928308056fffff',
 '892830800d3ffff',
 '89283080c53ffff',
 '89283080437ffff',
 '89283082a67ffff',
 '89283080477ffff',
 '89283080033ffff',
 '892830801afffff',
 '89283082bdbffff',
 '8928308002fffff',
 '8928308043bffff',
 '89283080057ffff',
 '89283080503ffff',
 '89283082a7bffff',
 '89283080153ffff',
 '892830805cbffff',
 '89283080137ffff',
 '89283082a33ffff',
 '89283082813ffff',
 '8928308052bffff',
 '89283082bc3ffff',
 '89283082b57ffff',
 '89283082a0fffff',
 '89283080547ffff',
 '8928308019bffff',
 '892830806a7ffff',
 '8928308018bffff',
 '89283080433ffff',
 '892830828c7ffff',
 '8928308281bffff',
 '8928308288bffff',
 '8928308280fffff',
 '89283082aa3ffff',
 '89283082807ffff',
 '89283082bd7ffff',
 '89283082a37ffff',
 '89283080073ffff',
 '89283080507ffff',
 '8928308030fffff',
 '892830801d7ffff',
 '892830800c7ffff',
 '89283082833ffff',
 '8928308283bffff',
 '89283082863ffff',
 '8928308008fffff',
 '8928308010fffff',
 '8928308003bffff',
 '892830803b3ffff',
 '89283080427ffff',
 '89283080383ffff',
 '89283080197ffff',
 '89283082aabffff',
 '89283082a4bffff',
 '89283080cd3ffff',
 '89283082b8fffff',
 '8928308056bffff',
 '89283080467ffff',
 '89283082a4fffff',
 '892830803c7ffff',
 '89283082a5bffff',
 '8928308006fffff',
 '8928308050bffff',
 '8928308040fffff',
 '89283080553ffff',
 '89283080557ffff',
 '892830800bbffff',
 '8928308038fffff',
 '89283080177ffff',
 '8928308050fffff',
 '89283080013ffff',
 '89283080143ffff',
 '89283080187ffff',
 '8928308014bffff',
 '89283080083ffff',
 '89283080373ffff',
 '89283080387ffff',
 '892830801bbffff',
 '89283080577ffff',
 '89283082873ffff',
 '89283082a6fffff',
 '8928308054bffff',
 '8928308053bffff',
 '892830801d3ffff',
 '892830803cbffff',
 '89283080103ffff',
 '89283082ab3ffff',
 '89283082853ffff',
 '89283082a87ffff',
 '89283082a03ffff',
 '89283082b8bffff',
 '89283082e27ffff',
 '892830803b7ffff',
 '89283082aafffff',
 '89283082b83ffff',
 '89283082803ffff',
 '89283082a1bffff',
 '89283082bd3ffff',
 '89283080193ffff',
 '89283080183ffff',
 '8928308007bffff',
 '8928308051bffff',
 '89283080173ffff',
 '8928308008bffff',
 '892830803dbffff',
 '89283080ccfffff',
 '89283080157ffff',
 '892830803abffff',
 '89283082a07ffff',
 '89283082ac3ffff',
 '8928308013bffff',
 '89283080cd7ffff',
 '89283080573ffff',
 '892830800a3ffff',
 '8928308042bffff',
 '89283080347ffff',
 '89283082857ffff',
 '892830801cfffff',
 '8928308009bffff',
 '89283080003ffff',
 '8928308030bffff',
 '89283080cc3ffff',
 '8928308284fffff',
 '89283082b93ffff',
 '8928308282bffff',
 '89283080093ffff',
 '89283080017ffff',
 '8928308039bffff',
 '89283080ccbffff',
 '89283080c8fffff',
 '89283080c9bffff',
 '89283082b5bffff',
 '89283082a83ffff',
 '89283082817ffff',
 '89283080023ffff',
 '892830803d7ffff',
 '89283080473ffff',
 '892830801dbffff',
 '89283082847ffff',
 '89283080077ffff',
 '89283080063ffff',
 '892830800afffff',
 '89283080127ffff',
 '8928308001bffff',
 '89283080047ffff',
 '8928308031bffff',
 '89283080087ffff',
 '8928308282fffff',
 '89283082827ffff',
 '892830828cfffff',
 '89283082ab7ffff',
 '89283082843ffff',
 '89283082b13ffff',
 '89283082a17ffff',
 '89283080567ffff',
 '892830800b7ffff',
 '892830801a3ffff',
 '89283080007ffff',
 '89283082a6bffff',
 '89283082a73ffff',
 '89283080133ffff',
 '89283080c97ffff',
 '892830803c3ffff',
 '892830801b7ffff',
 '8928308000fffff',
 '89283080423ffff',
 '89283080393ffff',
 '8928308287bffff',
 '89283082acfffff',
 '8928308280bffff',
 '89283080c93ffff',
 '89283082823ffff',
 '892830801a7ffff',
 '8928308055bffff',
 '8928308015bffff',
 '892830800a7ffff',
 '89283082a8bffff',
 '89283082ac7ffff',
 '89283082867ffff',
 '89283082877ffff',
 '89283082a8fffff',
 '89283082a97ffff',
 '89283080317ffff',
 '8928308054fffff',
 '89283080303ffff',
 '8928308017bffff',
 '89283080107ffff',
 '89283082e2fffff',
 '8928308285bffff',
 '89283080463ffff',
 '8928308057bffff',
 '89283080147ffff',
 '892830800abffff',
 '8928308010bffff',
 '8928308046bffff',
 '8928308014fffff',
 '892830801c7ffff',
 '892830803bbffff',
 '892830803d3ffff',
 '89283080543ffff',
 '89283082b53ffff',
 '89283082a27ffff',
 '89283082837ffff',
 '892830806b7ffff',
 '89283080123ffff',
 '89283080357ffff',
 '892830800b3ffff',
 '8928308044fffff',
 '8928308047bffff',
 '89283080333ffff',
 '89283082a13ffff',
 '89283082a23ffff',
 '8928308012fffff',
 '892830805c7ffff',
 '8928308038bffff',
 '8928308006bffff']    
