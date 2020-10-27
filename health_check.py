#!/usr/bin/env python3
import psutil
import shutil
import socket
from emails import generate_email, send_email

username = ""  # ADD THIS BEFORE RUNNING #######
sender = "automation@example.com"
receiver = "{}@example.com".format(username)
email_body = "Please check your system and resolve the issue as soon as possible."


def check_cpu():
    '''# Check if CPU usage is greater than 80%'''
    cpu_util = psutil.cpu_percent(0.1)
    if cpu_util > 80:
        # send email
        cpu_email = generate_email(sender,
                                   receiver,
                                   "Error - CPU usage is over 80%",
                                   email_body)
        send_email(cpu_email)


def check_disk_space():
    '''Available disk space is lower than 20%'''
    total, used, free = shutil.disk_usage("/")
    percent_free = total/free * 100
    if percent_free < 20 :
        disk_email = generate_email(sender,
                                   receiver,
                                   "Error - Available disk space is less than 20%",
                                   email_body)
        send_email(disk_email)

def check_mem():
    '''available memory is less than 500MB'''
    mem = psutil.virtual_memory().free / (2**20)
    if mem < 500:
        mem_email = generate_email(sender,
                                    receiver,
                                    "Error - Available memory is less than 500MB",
                                    email_body)
        send_email(mem_email) 


def check_localhost():
    '''hostname "localhost" cannot be resolved to "127.0.0.1"'''
    if socket.gethostbyname("localhost") != "127.0.0.1":
        host_email = generate_email(sender,
                                    receiver,
                                    "Error - localhost cannot be resolved to 127.0.0.1",
                                    email_body)
        send_email(host_email) 






