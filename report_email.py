#!/usr/bin/env python3

import os
from datetime import date
import reports


today = date.today().strftime("%B %d, %Y")
title = "Processed Update on {}".format(today)

source_path = "supplier-data/descriptions"
message_by_item = []

def create_message(source_path):
    for file in os.listdir(source_path):
        with open(os.path.join(source_path, file), "r") as f:
            file_list = f.read().splitlines()
            message_by_item.append("name: {}<br/>weight: {}\n".format(file_list[0], file_list[1]))
    return "<br/>".join(message_by_item)

if __name__ == "__main__":
    reports.generate_report("/tmp/processed.pdf", title, create_message(source_path))

    sender = "automation@example.com"
    recipient = "{}@example.com".format(os.environ.get('USER'))
    subject = "Upload Completed - Online Fruit Store"
    body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
    attachment_path = "/tmp/processed.pdf"

    message = emails.generate_email()
    emails.send_email(message)
