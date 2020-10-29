#!/usr/bin/env python3
import os, datetime
from reports import generate_report
from run import process_data
from emails import generate_email, send_email


username = "student-00-78aa1a56aa59" ###### ADD THIS BEFORE RUNNING #######
attachment = '/tmp/processed.pdf'
title = "Processed Update on {}".format(datetime.datetime.now().strftime('%B %d, %Y'))


if __name__ == "__main__":

    data = process_data()

    pdf_body = ""

    for item in data:
        # name, weight & blank line
        name = "name: {}".format(item['name'])
        weight = "weight: {} lbs".format(item['weight'])
        #pdf_body.append("</br>")
        pdf_body += name + "<br/>" + weight + "<br/><br/>"


    generate_report(attachment, title, pdf_body)

    email = generate_email("automation@example.com",
     "{}@example.com".format(username),
      "Upload Completed - Online Fruit Store",
      "All fruits are uploaded to our website successfully. A detailed list is attached to this email.",
      attachment)

    print(email) # Check before sending
    #send_email(email)