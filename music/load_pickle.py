import pickle

with open('music_group.py', 'rb') as f:
    totall = pickle.load(f)

print(totall)