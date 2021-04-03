import pickle

favorite_group = {'group_name': 'Операция пластилин', 'track': ['маяк', 'заткнись и целуй меня', ],
                  'Albums': ['Маяк', 'юность', 'рейв']}
with open('music_group.py', 'wb') as f:
    pickle.dump(favorite_group, f)

print('файл записан')