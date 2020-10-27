#!/usr/bin/env python3
import os, datetime
from reports import generate_report
from run import process_data
from emails import generate_email, send_email


username = "" ###### ADD THIS BEFORE RUNNING #######
attachment = '/tmp/processed.pdf'
title = "Processed Update on {}".format(datetime.date.today())


if __name__ == "__main__":

    data = process_data()

    pdf_body = []

    for item in data:
        # name, weight & blank line
        name = "name:{}".format(item['name'])
        pdf_body.append(name)
        weight = "weight:{} lbs".format(item['weight'])
        pdf_body.append(weight)
        pdf_body.append("</br>")

    pdf_body = "</br>".join(pdf_body)

    generate_report(attachment, title, pdf_body)

    email = generate_email("automation@example.com",
     "{}@example.com".format(username),
      "Upload Completed - Online Fruit Store",
      "All fruits are uploaded to our website successfully. A detailed list is attached to this email.",
      attachment)

    print(email) # Check before sending
    #send_email(email)