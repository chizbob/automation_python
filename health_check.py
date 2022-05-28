#!/usr/bin/env python3

import shutil
import psutil
import os
import socket
import emails

# Report an error if CPU usage is over 80%
def cpu_check():
    cpu_usage = psutil.cpu_percent(1)
    return cpu_usage > 80

# Report an error if available disk space is lower than 20%
def disk_check():
    path = os.getcwd()
    disk_usage = shutil.disk_usage(path)
    free_percent = disk_usage[2]/disk_usage[0]
    return free_percent > 20

# Report an error if available memory is less than 500MB
def memory_check():
    free_memory = psutil.virtual_memory().total >> 20
    return free_memory > 500

# Report an error if the hostname "localhost" cannot be resolved to "127.0.0.1"
def ip_check():
    hostname_ip = socket.gethostbyname(socket.gethostname())
    return hostname_ip == "127.0.0.1"

# run checks to define error message
if cpu_check():
    error_message = "CPU usage is over 80%"
if disk_check():
    error_message = "Available disk space is lower than 20%"
if memory_check():
    error_message = "available memory is less than 500MB"
if ip_check():
    error_message = 'hostname "localhost" cannot be resolved to "127.0.0.1"'


if __name__ == "__main__":

    sender = "automation@example.com"
    recipient = "{}@example.com".format(os.environ.get('USER'))
    subject = "Error - {}".format(error_message)
    body = "Please check your system and resolve the issue as soon as possible."

    message = emails.generate_error_report(sender, recipient, subject, body)
    emails.send_email(message)
