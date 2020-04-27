import requests
import openpyxl
import re
import argparse

""" Choose Input Type """ 
ap = argparse.ArgumentParser()

""" Get Team Data from TBA """
# url
year = input("Year: ")
event = input("Event Key: ")
eventkey = year + event
teamslink = 'https://www.thebluealliance.com/api/v3/event/' + eventkey + '/teams/simple'

# header with token
headers = {
    'X-TBA-Auth-Key': 'Z8SwOAjHG0lDYA3CRv6Ha06tsUwHMibk3WhNh2jE22xWx8sULAYzeM5HqOptnCgn'
}

# team list at event
teams = requests.get(teamslink, headers=headers).json()
print(teams)
""" Creates Spreadsheet """
workbook = openpyxl.Workbook()
sheet = workbook.active

sheet["A1"] = "Teams at " + eventkey

# finds team in rankings and averages past rankings
for team in teams:
    teamnum = str(team['team_number'])
    teamname = team['nickname']
    fullteamname = teamnum + ' - ' + teamname
    temparray = []
    temparray.append(fullteamname)
    # Uncomment the line below and comment out the line above if you would like to only output team numbers
    # temparray.append(teamnum)
    sheet.append(temparray)

filename = eventkey + 'teams' + ".xlsx"
workbook.save(filename=filename)
