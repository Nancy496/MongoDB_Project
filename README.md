# MongoDB_Project
## Importing Pymongo
     import pymongo
     import pandas as pd
     import dns
     import webbrowser
## Connecting to Mongo Atlas
      conn = pymongo.MongoClient("mongodb+srv://nancywachira:nancy@cluster0.pfwwi.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
## Creating Database called Health and Hospital Table
     #Create database
     db = conn["Health"]
     #Create hospital collection
     mycol1 = db["Hospital"]
 ## Adding Hospital Collection
     #def createcols():
     # records  entered
     mydata1 = [{"Hospital_Id": "11", "Hospital_Name": "Kitale_District", "Address": "Kitale"},
               {"Hospital_Id": "12", "Hospital_Name": "Mt_Elgon", "Address": "Kapenguria"},
               {"Hospital_Id": "13", "Hospital_Name": "Kisumu_Hospital", "Address": "Siaya"}]
    
    # Insert records to collection
    data = mycol1.insert_many(mydata1)
  ## Creating Doctor Table and adding records 
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
    
## Creating the patient table and adding the table collection

       mydata3 = [
        {"Patient_Id": 31,"Patient_Name": "Fancy Kinde", "Age": 42, "Gender":"F", "Hospital_Id": "13","Inpatient":True, "Outpatient":False },
        {"Patient_Id": 32,"Patient_Name": "Daniel Mainge", "Age": 52, "Gender":"M", "Hospital_Id": "12",   "Inpatient":False, "Outpatient":True },
        {"Patient_Id": 33,"Patient_Name": "Aggrey Mwasambu", "Age": 38, "Gender":"M", "Hospital_Id": "11","Inpatient":True, "Outpatient":False },
        {"patient_id": 34,"Patient_Name": "Pauline Wangui", "Age": 40, "Gender":"F", "Hospital_Id": "12","Inpatient":False, "Outpatient":True },
        {"Patient_Id": 35,"Patient_Name": "Ndungu Nyoro", "Age": 32, "Gender":"M", "Hospital_Id": "13","Inpatient":False, "Outpatient":True }
    ]
    # Insert records to collection
     data3 = mycol3.insert_many(mydata3)
    
 ## creating dataframe
hospital = pd.DataFrame(list(mycol1.find()))
hospital
![Hospital Dataframe](https://user-images.githubusercontent.com/75600702/114001177-126f4180-9832-11eb-9e95-b7768e5beb07.PNG)

## ![Patient Dataframe](https://user-images.githubusercontent.com/75600702/114002170-046df080-9833-11eb-8407-6282465b8622.PNG)

## Creating Doctor Dataframe![Doct Dataframe](https://user-images.githubusercontent.com/75600702/114001479-5a8e6400-9832-11eb-8d44-fa37d044c983.PNG)


## ![Join the table](https://user-images.githubusercontent.com/75600702/114002026-e0aaaa80-9832-11eb-8000-cd50d2043c6d.PNG)
 ## ![Output of joining the tables](https://user-images.githubusercontent.com/75600702/114002445-4139e780-9833-11eb-9a4a-ec9d505c361e.PNG)
