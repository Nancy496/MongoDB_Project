#!/usr/bin/env python
# coding: utf-8

# In[35]:


import pymongo
import pandas as pd
import dns
import webbrowser


# In[36]:


conn = pymongo.MongoClient("mongodb+srv://nancywachira:nancy@cluster0.pfwwi.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
#conn = pymongo.MongoClient("mongodb+srv://nancywachira:nancy@cluster0.pfwwi.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
#conn = pymongo.MongoClient("mongodb+srv://nancywachira:nancy@cluster0.pfwwi.mongodb.net/test")


# In[48]:


#Create database
db = conn["Health"]
#Create hospital collection
mycol1 = db["Hospital"]


# In[49]:


# Create doctor's collection
mycol2 = db["Doctor"]
#create patients collection
mycol3 = db['Patients']


# In[44]:


print(conn.list_database_names())


# In[45]:


search = mycol2.find()
    # print list line by line
for s in search:
    print(s)


# In[50]:


#def createcols():
    # records  entered
mydata1 = [{"Hospital_Id": "11", "Hospital_Name": "Kitale_District", "Address": "Kitale"},
               {"Hospital_Id": "12", "Hospital_Name": "Mt_Elgon", "Address": "Kapenguria"},
               {"Hospital_Id": "13", "Hospital_Name": "Kisumu_Hospital", "Address": "Siaya"}]
    
    # Insert records to collection
data = mycol1.insert_many(mydata1)


# In[110]:


#mydata1 = mycol1.insert_one(mydata1)


# In[111]:


print(data.inserted_ids)


# In[51]:


# records to be added to doctor collection
mydata2 = [
        {"Doctor_Id": 21, "Doctor_Name": "Osagi_Peter", "Hospital_Id": "11", "Date_Joined": "2011-04-12",
         "Speciality": "Oncology", "Salary": 70000, "Experience": 5},
        {"Doctor_Id": 22, "Doctor_Name": "Kibet_Emmanuel", "Hospital_Id": "12", "Date_Joined": "2013-05-18",
         "Speciality": "Nurse", "Salary": 120000, "Experience": 10},
        {"Doctor_Id": 23, "Doctor_Name": "Mugambi_Kim", "Hospital_Id": "13", "Date_Joined": "2015-02-06",
         "Speciality": "Pediatrics", "Salary": 30000, "Experience": 4}
    ]
#Insert records to collection    
data2 = mycol2.insert_many(mydata2)


# In[113]:


print(data2.inserted_ids)


# In[52]:



mydata3 = [
        {"Patient_Id": 31,"Patient_Name": "Fancy Kinde", "Age": 42, "Gender":"F", "Hospital_Id": "13","Inpatient":True, "Outpatient":False },
        {"Patient_Id": 32,"Patient_Name": "Daniel Mainge", "Age": 52, "Gender":"M", "Hospital_Id": "12",   "Inpatient":False, "Outpatient":True },
        {"Patient_Id": 33,"Patient_Name": "Aggrey Mwasambu", "Age": 38, "Gender":"M", "Hospital_Id": "11","Inpatient":True, "Outpatient":False },
        {"patient_id": 34,"Patient_Name": "Pauline Wangui", "Age": 40, "Gender":"F", "Hospital_Id": "12","Inpatient":False, "Outpatient":True },
        {"Patient_Id": 35,"Patient_Name": "Ndungu Nyoro", "Age": 32, "Gender":"M", "Hospital_Id": "13","Inpatient":False, "Outpatient":True }
    ]

# Insert records to collection
data3 = mycol3.insert_many(mydata3)


# In[53]:


print(data3.inserted_ids)


# In[54]:


#create dataframe
hospital = pd.DataFrame(list(mycol1.find()))
hospital


# In[56]:


#hospitaldf.columns
hospital.info


# In[57]:


hospital.columns


# In[58]:


#set index
#hospital.set_index( 'Hospital_id', inplace= True)
#setvalue//0ZQ9IsSVt5Un2Cq6
#hospitaldf.reset_index(inplace=True)
hospital


# In[59]:


#create dataframe
doctordf = pd.DataFrame(list(mycol2.find()))
#set index
doctordf.set_index('Doctor_Id', inplace= True)
#remove automated id
doctordf.drop( '_id', inplace=True, axis=1)
#display
doctordf


# In[60]:


#create dataframe
patientdf = pd.DataFrame(list(mycol3.find()))
#set index
patientdf.set_index('Patient_Id', inplace= True)
#remove automated id
patientdf.drop( '_id', inplace=True, axis=1)
#display
patientdf


# In[61]:


# Insert data into the collections
def insert_data():
    x = mycol1.insert_many(Hospital)
    y = mycol2.insert_many(Doctor)


#insert_data()

# Join the data
cursor = db.Hospital.aggregate([
    {
        "$lookup":
            {
                "from": "Doctors",
                "localField": "Hospital_Id",
                "foreignField": "Hospital_Id",
                "as": "Hospital_info"
            }
    }])

for values in cursor:
    print(values)


# In[ ]:




