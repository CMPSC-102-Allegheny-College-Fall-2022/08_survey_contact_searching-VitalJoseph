"""Search for an email address given a fragment of a job description."""

from typing import List

import csv

# note: see https://docs.python.org/3/library/csv.html


def search_for_email_given_job(job_description: str, contacts: str) -> List[List[str]]:
    """Search for and return job description(s) given an email address."""
    # create an empty list of the contacts
    # iterate through the file, parsing it line by line
    # refer to the file called input/contacts.txt to learn more about
    # the format of the comma separated value (CSV) file that we must parse
    # iterate through each line of the file and extract the current job
    # ---> extract the current job for the contact on this line of the CSV
    # ---> the job description matches and thus we should save it in the list
    # return the list of the contacts who have a job description that matches
    contacts_list = []
    with open(contacts, "r") as csv_file:
        contacts_data = csv.reader(csv_file)
        for contact_line in contacts_data:
            current_contact_job = contact_line[1]
            if job_description in current_contact_job.lower():
                contacts_list.append(contact_line)
        return contacts_list
