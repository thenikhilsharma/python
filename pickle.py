import pickle

def storeData(inp):
    inp = {'key':inp,'name':inp}

    db = {}
    db["inp"] = inp

    dbfile = open('example2Pickle','ab')

    pickle.dump(db, dbfile)
    dbfile.close()

def loadData():
    # for reading also binary mode is important
    dbfile = open('examplePickle', 'rb')     
    db = pickle.load(dbfile)
    for keys in db:
        print(keys, '=>', db[keys])
    dbfile.close()
  
if __name__ == '__main__':
    storeData("Nick")
    loadData()