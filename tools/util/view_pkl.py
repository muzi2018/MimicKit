import pickle

def read_pickle(path):
    """
    Reads and returns the content of a .pkl file.
    """
    with open(path, "rb") as f:
        data = pickle.load(f)
    return data

if __name__ == "__main__":
    # Example: change this to your file path
    file_path = "/home/wang/MimicKit/data/motions/urdf0924/walk1_subject1_urdf0924.pkl"

    content = read_pickle(file_path)
    print("Loaded content:")
    print(content)
