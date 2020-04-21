import requests
import openpyxl

""" Get Team Data from TBA """
# url
year = input("Year: ")
event = input("Event Key: ")
eventkey = year + event
teamslink = 'https://www.thebluealliance.com/api/v3/event/' + eventkey + '/teams/simple'

# header with token
headers = {
    'X-TBA-Auth-Key': ''
}

# team list at event
teams = requests.get(teamslink, headers=headers).json()

""" Creates Spreadsheet """
workbook = openpyxl.Workbook()
sheet = workbook.active

sheet["A1"] = "Teams at " + eventkey

# finds team in rankings and averages past rankings
for team in teams:
    teamnum = team['team_number']
    temparray = []
    temparray.append(str(teamnum))
    sheet.append(temparray)

filename = eventkey + 'teams' + ".xlsx"
workbook.save(filename=filename)
