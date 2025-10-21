import pickle

# Load your .pkl motion
with open('/home/wang/MimicKit/data/motions/g1/g1_run.pkl', 'rb') as f:
    motion_data = pickle.load(f)

# See the type
print((motion_data))
