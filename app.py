import requests
import json
import os

API_KEY = os.environ.get('TRELLO_API_KEY')
API_TOKEN = os.environ.get('TRELLO_API_TOKEN')

trello_board_ID = '5d25d651252b4b37c8e8f011'

url = f'https://api.trello.com/1/boards/{trello_board_ID}/?cards=all'

qs = {
    'key': API_KEY,
    'token': API_TOKEN
}

# try to connect and if fails present an error msg
try:
    r = requests.get(url, params=qs)
    r.raise_for_status()
except requests.exceptions.HTTPError as err:
    print(err)

# put output into JSON
data = r.json()

# extracts the card list from data.
cards = data.get('cards')

# list ID variables
open_ = '5d25d6527ee01f05c33116a9'
in_progress_with_customer = '5d25d65291615c20f4694e0c'
needs_action = '5d5e43a04aa5aa30b02d2833'
resolved = '5d25d652618ce039711b335d'


def open_tickets_func(color, status, list_ID):
    if color == 'red' and list_ID == open_ and status is False:
        name = open_tickets['name']
        ticket_num = name[0:7]
        print(f'{name} -> https://pixalate.atlassian.net/browse/{ticket_num}')


def in_progress_with_customer_func(color, status, list_ID):
    if color == 'red' and list_ID == in_progress_with_customer and status is False:
        name = progess_customer['name']
        ticket_num = name[0:7]
        print(f'{name} -> https://pixalate.atlassian.net/browse/{ticket_num}')


def needs_action_func(color, status, list_ID):
    if color == 'red' and list_ID == needs_action and status is False:
        name = needs_action_['name']
        ticket_num = name[0:7]
        print(f'{name} -> https://pixalate.atlassian.net/browse/{ticket_num}')


def resolved_func(color, status, list_ID):
    if color == 'red' and list_ID == resolved and status is False:
        name = resolved_tickets['name']
        ticket_num = name[0:7]
        print(f'{name} -> https://pixalate.atlassian.net/browse/{ticket_num}')


print('Open Tickets:')
for open_tickets in cards:
    try:
        if open_tickets['labels']:

            # takes label color, status and stores it as a variable
            color = open_tickets['labels'][0]['color']
            status = open_tickets['closed']
            list_ID = open_tickets['idList']

            # loop through the json dict using 'red' and Fasle as logic to print out card names
            open_tickets_func(color, status, list_ID)
    except AssertionError as error:
        print(error)

print(" ")
print('In Progress / Waiting for customer tickets / On Hold:')
for progess_customer in cards:
    try:
        if progess_customer['labels']:

            # takes label color, status and stores it as a variable
            color = progess_customer['labels'][0]['color']
            status = progess_customer['closed']
            list_ID = progess_customer['idList']

            # loop through the json dict using 'red' and Fasle as logic to print out card names
            in_progress_with_customer_func(color, status, list_ID)
    except AssertionError as error:
        print(error)

print(" ")
print('Needs Attention:')
for needs_action_ in cards:
    try:
        if needs_action_['labels']:

            # takes label color, status and stores it as a variable
            color = needs_action_['labels'][0]['color']
            status = needs_action_['closed']
            list_ID = needs_action_['idList']

            # loop through the json dict using 'red' and Fasle as logic to print out card names
            needs_action_func(color, status, list_ID)
    except AssertionError as error:
        print(error)

print(" ")
print('Resolved:')
for resolved_tickets in cards:
    try:
        if resolved_tickets['labels']:

            # takes label color, status and stores it as a variable
            color = resolved_tickets['labels'][0]['color']
            status = resolved_tickets['closed']
            list_ID = resolved_tickets['idList']

            # loop through the json dict using 'red' and Fasle as logic to print out card names
            resolved_func(color, status, list_ID)
    except AssertionError as error:
        print(error)
