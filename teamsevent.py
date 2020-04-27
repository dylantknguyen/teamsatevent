import requests
import openpyxl
import re

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

""" Creates Spreadsheet """
workbook = openpyxl.Workbook()
sheet = workbook.active

sheet["A1"] = "Teams at " + eventkey

# finds team in rankings and averages past rankings
for team in teams:
    teamnum = str(team['team_number'])
    teamname = team['nickname']
    temparray = []
    temparray.append(teamnum)
    temparray.append(teamname)
    sheet.append(temparray)

filename = eventkey + 'teams' + ".xlsx"
workbook.save(filename=filename)
