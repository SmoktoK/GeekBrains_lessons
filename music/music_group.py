import json
import pickle

favorite_group = {'group_name': 'Операция пластилин', 'track': ['маяк', 'заткнись и целуй меня', ],
                  'Albums': ['Маяк', 'юность', 'рейв']}

print(favorite_group)
j_group = json.dumps(favorite_group)
print(j_group)
p_group = pickle.dumps(favorite_group)
print(p_group)
with open('group.json', 'w', encoding='utf-8') as f:
    json.dump(favorite_group, f)

with open('group.pickle', 'wb') as f:
    pickle.dump(favorite_group, f)