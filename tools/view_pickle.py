import pickle

path = "data/motions/humanoid/humanoid_spinkick.pkl"

with open(path, "rb") as f:
    motion = pickle.load(f)

print(type(motion))
print(motion.keys())
