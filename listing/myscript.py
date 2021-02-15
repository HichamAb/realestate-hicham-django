
import json
import lorem
import random
x = []
y = {}
z = []
model = ""
pk      =""
fields = {}
name = ""
index = 0
status = True 
pk2=1
i = 0
for i in range(1,200) :
    pk = 111
    
    y = {}
    fields = {}
    fields["title"] = lorem.sentence()
    fields["transaction_type"] = random.randrange(1,4) 
    fields["state"] = random.randrange(1,48)
    fields["city"] = random.randrange(1,550)
    fields["neiborhood"] =lorem.sentence()
    fields["square_meter"] = float(random.randint(1,500))
    fields["description"] = lorem.paragraph()
    fields["n_bedrooms"] = random.randrange(1,7)
    fields["n_bathrooms"] = random.randrange(1,3)
    fields["realtor"] =1
    fields["slug"] = fields["title"].replace(" ","-")
    fields["added_on"] = "2021-02-09T23:28:50.264Z"
    fields["updated_on"] = "2021-02-09T23:28:50.264Z"

    y["model"] = "listing.listing"
    y["pk"] = pk 
    y["fields"]= fields
    
    x.append(y)
    
    pk += 1 


with open("newlistings.json","w") as outfile : 
    json.dump(x,outfile,ensure_ascii=False)
    outfile.close()
