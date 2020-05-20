from commands import *
import json

# list = list_videos("IB3900")
# pp.pprint(list)

# todo - how to parse through lists in videos
# todo - run through each page of videos and add to pandas?
# todo - find a way to display category directories that enable easy renaming and categorisation

# create_top_level_category("test category")

categories = list_categories()
categories_obj = json.loads(categories)
for key in categories_obj['data']:
    # print(categories_obj['data'][0]['id'])
    # print(len(key))
    print(len(key))
    # for i in len(range(key)):
    #     print(i + ':', value[i])


# create_subcategory("test sub", 10127)


video_dict = {
    "data":[
        {
            "id":21565695,
            "title":"IB92X0 - Y Yang - Day 4_AI and Services - ' 'Machine ' 'Learning",
            "description":"",
            "state":"ready",
            "private":False,
            "user_id":106443,
            "user_login":"elearning",
            "account_id":80122,
            "account_name":"WBS","duration":2001.2,
            "created_at":"2020-05-20T10:01:47.000Z",
            "updated_at":"2020-05-20T10:02:01.000Z",
            "url":"https://vzaar.com/videos/21565695",
            "asset_url":"https://view.vzaar.com/21565695/video",
            "poster_url":"https://view.vzaar.com/21565695/image",
            "thumbnail_url":"https://view.vzaar.com/21565695/thumb",
            "categories":[],
            "adverts":[]
        }
            ]
            }


# print(video_dict.items())
# print(video_dict['data'][0]['id'])