from pymongo import MongoClient

#client = MongoClient("34.84.195.184", "17017")

DB_HOST = 'XXX.XX.XX.XXX:27017'
DB_ID = 'root'
DB_PW = 'PW'

client = MongoClient('mongodb://%s:%s@%s' % (DB_ID, DB_PW, DB_HOST))


db = client["DB_이름"]
collection = db["coll_이름"]


import datetime 
post = { 
"author" : "Mike", 
"text" : "My first blog post!", 
"tags" : ["mongodb", "python", "pymongo"], 
"date": datetime.datetime.utcnow() 
}

coll = db.collection
coll.insert(post)


import pytorch
import pytorch.nn



def __call__(self):
    # 기능 구현
    self.forward(*input. **kargurs)
    


class MLP(nn.Module):
    def __init__(self, config):
        super().__init__(config)
        ffn = nn.Linear(hidden_size, output_size)

    def forward(self):
        output = self.ffn(hidden)
        output = 
        
        return output
        
