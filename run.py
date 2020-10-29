#!/usr/bin/env python3
import os, requests

ip_address = "34.122.125.197" ####### FILL IT IN #########
home_dir = os.path.expanduser("~")
dscr_dir = r"{0}/supplier-data/descriptions".format(home_dir)
url = r"http://{0}/fruits/".format(ip_address)


def process_data():
    '''Loops through description files and returns a list of dicts based on each txt file'''

    dscr_lst = []

    for dscr_file in os.listdir(dscr_dir):

        with open(os.path.join(dscr_dir, dscr_file)) as dscr_txt:
            dscr_lst.append(
                {
                    "name":dscr_txt.readline().rstrip("\n"),
                    "weight":int(dscr_txt.readline().rstrip("\n").split(" ")[0]),
                    "description":dscr_txt.read().rstrip("\n"),
                    "image_name":dscr_file.split(".")[0] + ".jpeg"
                }
            )
    return dscr_lst  


def post_data(dscr_lst):
    '''Receives list of dicts and posts each as a JSON dict to the Django server'''
    
    for dscr in dscr_lst:    
        r = requests.post(url, json=dscr)
        if r.status_code != 201:
            raise Exception('POST error status={}'.format(r.status_code))
        print('Created feedback ID: {}'.format(r.json()["id"]))



dscr_lst = process_data()
#print(dscr_lst)
post_data(dscr_lst)
