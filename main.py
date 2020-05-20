from commands import *
import json

# list = list_videos("IB3900")
# pp.pprint(list)

# todo - how to parse through lists in videos
# todo - run through each page of videos and add to pandas?
# todo - find a way to display category directories that enable easy renaming and categorisation

# create_top_level_category("test category")

# categories = list_categories()
# categories_obj = json.loads(categories)
# listing = categories_obj['data'][0]

# for key in listing:
#     print(listing[key])


# for key in categories_obj['data']:
    # print(categories_obj['data'][0]['id'])
    # print(key['id'])
    # print(key['title'])

    # for i in len(range(key)):
    #     print(i + ':', value[i])


# create_subcategory("test sub", 10127)


# category_dict = {
    # "data":[
    #     {
    #         'id': 10127, 
    #         'account_id': 80122, 
    #         'user_id': 106443, 
    #         'name': 'Warwick', 
    #         'description': None, 
    #         'parent_id': None, 
    #         'depth': 0, 
    #         'node_children_count': 5, 
    #         'tree_children_count': 11, 
    #         'node_video_count': 0, 
    #         'tree_video_count': 56, 
    #         'created_at': '2017-09-19T08:42:13.000Z', 
    #         'updated_at': '2020-05-19T11:46:24.000Z'}
    #         ]
    #         }


# print(video_dict.items())
# print(video_dict['data'][0]['id'])


videos = list_videos()
videos_obj = json.loads(videos)
listing = videos_obj['data'][0]

for list in listing:
    print(str(list) + ' : \n' + str(listing[list]))




# for key in listing:
#     print(listing[key])