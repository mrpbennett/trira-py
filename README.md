[![Build Status](https://travis-ci.org/mrpbennett/unittests_tut.svg?branch=master)](https://travis-ci.org/mrpbennett/unittests_tut)

# trello_py

_A simple script to make my life easier..._

## The issue?

As a member of the CSM team, I rely on JIRA to keep track of my logged tickets, which sit with various internal teams. We have a slack channel dedicated to keeping on top of these tickets.

I use to maintain a list of my open tickets, so I could copy and paste them into the channel...this ended up fiddly and time-consuming as I had to open each ticket in a new browser tab, check it's status and then decide if it needs to be highlighted.

It was a pain! :cry:

I now use [Trello](https://trello.com) to manage the JIRA tickets. I use a certain naming convention.

`PROJECT-TICKET_NUMBER: DESCRIPTION`

I then attach a certain label to the card, so I know this is something I should bring up in our meeting. Having this process made things easier but it still became a little bit of a faff.

## The fix!

I now use the [Trello API](https://developers.trello.com/reference#introduction) and Python to make the whole process seamless. :boom:

I use the API via requests call the [Board endpoint](https://developers.trello.com/reference#boardsboardid-1) which allows me to request info of a single board.

### Step 1.

First, we have to modify the endpoint with our board ID turning this: `url = "https://api.trello.com/1/boards/` into this `url = "https://api.trello.com/1/boards/{board_id}` I struggled to get the `board_id` but after finding a post on StackOverflow. All you have to do is put `.json` on the end of your board URL to get the ID in the JSON response.

`https://trello.com/b/ru6s23QW/board_name.json` which outputs in the browser something like this

```json
{
  "id": "5d25d651252b4b37c8e8xxxx",
  "name": "JIRA Tickets",
  "desc": "",
  "descData": null,
  "closed": false,
  "idOrganization": null,
  "limits": {...
```

The queryString is simple, it's just your `API_Key` and `API_Token` which you get from [here](https://trello.com/app-key)

```python
qs = {
    'key': API_KEY,
    'token': API_TOKEN
}
```

### Step 2.

After using requests to get a response, I extracted the main part of the JSON into another variable so I was able to manage the data easier.

```python
# get a json response from Trello API
r = requests.get(url, params=qs)
data = r.json()

# extract the card list from data. So it's easier to manage.
cards = data.get(cards)
```

### Step 3.

I used some simple logic to output what I need to the terminal. After looking through the `card` list I knew I needed to look at the `name`, `closed` which was either `true` or `false` and then dig into the `labels` list which had the key `color`.

As I used a certain label to highlight the cards I needed to bring up, I knew that I had to check to see if cards had a red label and that the status was not closed.

I broke the logic out into mini functions to clean up the code as below.

```python
def open_tickets_func(color, status, list_ID):
    if color == 'red' and list_ID == open_ and status is False:
        name = open_tickets['name']
        ticket_num = name[0:7]
        print(f'{name} -> https://pixalate.atlassian.net/browse/{ticket_num}')
```

I then called the each function from `for` loop to clean up the loops.

```python
for open_tickets in cards:
    try:
        if open_tickets['labels']:

            # takes label color and status and stores it as a variable
            color = open_tickets['labels'][0]['color']
            status = open_tickets['closed']

            # call the function
            open_tickets_func(color, status, list_ID)
    except:
        print('error!')
```
Using the if statement `if color == 'red' and status is False:`  within the functions. I was able to check against the response for `color` with a value of `red` and `closed` was `False`. This would pull out all the cards I attached the red label too, these are the tickets I wish to bring up.

I then got the `name` and produced an URL from it. The `ticket_num` variable allowed me to append the JIRA URL with its ticket number.

I then sliced the first 6 characters from the name of the card to append to the URL using an f string. As my naming convention was `PROJECT-TICKET_NUMBER: DESCRIPTION` which is `CS-1234: something to fix` in reality. Which printed the name of the card and the tickets URL.

End results being:

```
Tickets:
CS-1234: some description -> https://domain.atlassian.net/browse/CS-1234
```

Building this allowed me to just run a simple script, instead of copying and pasting ticket URLs.

### Improvements / Ideas

I would like to try and run the script and it automatically put the output into the relevant slack channel. Removing one more copy and paste.
