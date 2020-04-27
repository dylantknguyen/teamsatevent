# Teams at Event
This file finds a list of teams attending an inputted eventt using The Blue Alliance API. It outputs the data to a spreadsheet.

## Generating and Adding an Access Token
In order to make calls to the The Blue Alliance API, you must generate your own token. To do this, go to your TBA Account Dashboard. Next, scroll down to the `Read API Keys` section, enter a description into the description box, and click "Add New Key". 

After generating your key, go back to the code and find the line with `'X-TBA-Auth-Key': ''`. Add your key between the second pair of quotations so that it looks like `'X-TBA-Auth-Key': '[Your Token]'` with [Your Token] being the token you generated above. Now, you're set to start using The Blue Alliance API!

## Running Program
To install the program, just download the repo using the "Clone or Download" button. It is likely that you will need to install the python package `openpyxl` using the command `pip install openpyxl` in your command line interface.  Once you do that, just double click `teamsevent.py`. It should create an Excel spreadsheet in the same folder. Open it and check out the numbers.

Note: This requires Python to work. Install it [here](https://www.python.org/downloads/) if you do not have it.
## Finding an Event
To find the event key, go to [The Blue Alliance](https://www.thebluealliance.com/) and enter your desired event into the search bar. The event code will be in brackets.

### Example
Go to [The Blue Alliance](https://www.thebluealliance.com/) and search for `FIRST Chesapeake District Championship 2019`. The event key is `CHCMP` as that is the text between the brackets.

## Printing to Excel Spreadsheet
While you can add the data to an excel spreadsheet, you can also just have it print out the rankings. To do this, delete the following lines:
```
    temparray = []
    temparray.append(str(teamnum))
    sheet.append(temparray)

filename = eventkey + 'teams' + ".xlsx"
workbook.save(filename=filename)

```
Then, add `print(teamnum)` below the line that says `teamnum = team['team_number']`. Make sure the number of spaces from the left is consistent.
