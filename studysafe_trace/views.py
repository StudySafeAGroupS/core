from asyncio import constants
from django.http import HttpResponse
from django.shortcuts import render
from studysafe_trace.forms import ContactForm

import datetime

import requests
import json

#hardcoded details, since there is no input field
HKU_id = '3025704501'
date_of_diagnosis = '2022-05-05'


def base(request):

	return render(request, 'base.html', {'subject': HKU_id, 'date': date_of_diagnosis})

def contacts(request):    
  device_list = json.loads(requests.get("https://damp-falls-81241.herokuapp.com/api/devices/?format=json").text)
  # member_list = json.loads(requests.get("https://damp-falls-81241.herokuapp.com/api/members/?format=json").text)
  entryRecord = {}
  tod = datetime.datetime.strptime(date_of_diagnosis, "%Y-%m-%d")
  d = datetime.timedelta(days = 2)
  d = tod - d
  d = d.strftime("%Y-%m-%dT%H:%M:%SZ")
  # print('*'*100)
  # print(d)
  for device in device_list:
    if (d <= device["time_of_record"]):
      if (device["hku_id"] not in entryRecord):
        entryRecord[device["hku_id"]] = []
      entryRecord[device["hku_id"]].append([device["venue_code"],device["time_of_record"]])
  for entry in entryRecord:
    for i in range(len(entryRecord[entry]) - 1):
      for j in range(i, len(entryRecord[entry]) - 1):
        if (entryRecord[entry][j][1] >= entryRecord[entry][j+ 1][1]):
          tmp = entryRecord[entry][j]
          entryRecord[entry][j] = entryRecord[entry][j+1]
          entryRecord[entry][j+1] = tmp
  # print(json.dumps(entryRecord,sort_keys=True, indent=4))
  # print('*'*100)

  contacts_list = []
  for entry in entryRecord:
    if (entry != HKU_id):
      for covidGuyEntry in range(len(entryRecord[HKU_id])//2):
        for suspiciousGuyEntry in range(len(entryRecord[entry])//2):
          covidGuyStartTime = datetime.datetime.strptime(entryRecord[HKU_id][covidGuyEntry * 2][1], "%Y-%m-%dT%H:%M:%SZ")
          covidGuyEndTime = datetime.datetime.strptime(entryRecord[HKU_id][covidGuyEntry * 2 + 1][1], "%Y-%m-%dT%H:%M:%SZ")
          suspiciousGuyStartTime = datetime.datetime.strptime(entryRecord[entry][suspiciousGuyEntry * 2][1], "%Y-%m-%dT%H:%M:%SZ")
          suspiciousGuyEndTime = datetime.datetime.strptime(entryRecord[entry][suspiciousGuyEntry * 2 + 1][1], "%Y-%m-%dT%H:%M:%SZ")

          bothStartMeetTime = covidGuyStartTime
          if (bothStartMeetTime < suspiciousGuyStartTime):
            bothStartMeetTime = suspiciousGuyStartTime
          
          bothEndMeetTime = covidGuyEndTime
          if (bothEndMeetTime > suspiciousGuyEndTime):
            bothEndMeetTime = suspiciousGuyEndTime
          
          if (entry not in contacts_list):
            # print(entry, covidGuyStartTime, covidGuyEndTime, suspiciousGuyStartTime , suspiciousGuyEndTime, bothEndMeetTime, bothStartMeetTime, (bothEndMeetTime - bothStartMeetTime).total_seconds())
            if ((bothEndMeetTime - bothStartMeetTime).total_seconds() >= 30 * 60):
              # print(entry, bothEndMeetTime, bothStartMeetTime)
              contacts_list.append(entry)

  contacts_list = sorted(contacts_list)
  # print(contacts_list)

  # final_contact_list = []
  # for i in range(len(contacts_list)):
  #   for j in member_list:
  #     if (j["hku_id"] == contacts_list[i]):
  #       final_contact_list.append(j["name"])
  return render(request, 'contacts.html', {'subject': HKU_id, 'date': date_of_diagnosis, 'contacts':contacts_list})

def venues(request):

  response = requests.get("https://damp-falls-81241.herokuapp.com/api/devices/?format=json").text
  response_devices = json.loads(response)
  
  venueList = [] #list to store visited venues
  
  for record in range (len(response_devices)):
    if (response_devices[record]["is_an_entry_record"] == True and response_devices[record]["hku_id"] == HKU_id) and response_devices[record]["venue_code"] not in venueList:
      venueList.append(response_devices[record]["venue_code"])
  
  venueList.sort()
      
  return render(request, 'venues.html', {"subject":HKU_id, "date":date_of_diagnosis, "venues":venueList})

def query(request, id, date):
  global HKU_id
  global date_of_diagnosis
  HKU_id = id
  date_of_diagnosis = date
  return render(request, 'base.html', {'subject': HKU_id, 'date': date_of_diagnosis})