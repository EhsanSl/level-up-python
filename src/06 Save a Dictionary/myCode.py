import pickle


def save_dict(mydict, fname):
    with open(fname, 'wb') as f:
        pickle.dump(mydict, f)
    return None


def load_dict(fname):
    with open(fname, 'rb') as f:
        mydict = pickle.load(f)
        return mydict


if __name__ == '__main__':
    my_dict = {'name': 'ehsan', 'age': 24}

    fname = input("Enter File name:\n")
    save_dict(my_dict, fname)

    fname = input("Enter File Name To Load: \n")
    loaded_dict = load_dict(fname)

    print(f'dict {loaded_dict}')
