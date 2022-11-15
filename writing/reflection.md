# Contact Searching

Make sure that you delete all of the markers and the written prompts
from this document. You should also ensure that the document does not have any
mistakes in spelling, grammar, or the syntax of Markdown. Ultimately, the final
version of your reflection should be a polished document that is suitable for
publication on your web site.

## Vital Joseph

## Program Output

### What is the output from running the following commands?

Use a fenced code block to provide the output for this command.

- `poetry run contactsearcher --job-description "engineer" --contacts-file input/contacts.txt`
```
The contacts file contains 100 people in it! Let's get searching!

  We are looking for contacts who have a job related to "engineer":

  joe70@yahoo.com is a Network engineer
  torresjames@white.info is a Electrical engineer
  grahamjoel@castillo-gilbert.net is a Engineer, technical sales
  gsutton@miller.com is a Engineer, maintenance
  gharris@villarreal-snow.com is a Water engineer
  williamsondavid@lopez.com is a Automotive engineer
  ronald83@yahoo.com is a Maintenance engineer
  zmarshall@yahoo.com is a Control and instrumentation engineer
  christopher35@yahoo.com is a Civil engineer, consulting
  jacquelinedavid@hotmail.com is a Engineer, electronics
  espinozadaryl@hill-maddox.com is a Engineering geologist
  edwardsjacob@gmail.com is a Chemical engineer

Wow, we found some contacts! Email them to learn about your job!
```

Use a fenced code block to provide the output for this command.

- `poetry run contactsearcher --job-description "neer" --contacts-file input/contacts.txt`
```
The contacts file contains 100 people in it! Let's get searching!

  We are looking for contacts who have a job related to "neer":

  joe70@yahoo.com is a Network engineer
  torresjames@white.info is a Electrical engineer
  grahamjoel@castillo-gilbert.net is a Engineer, technical sales
  gsutton@miller.com is a Engineer, maintenance
  gharris@villarreal-snow.com is a Water engineer
  williamsondavid@lopez.com is a Automotive engineer
  ronald83@yahoo.com is a Maintenance engineer
  zmarshall@yahoo.com is a Control and instrumentation engineer
  christopher35@yahoo.com is a Civil engineer, consulting
  jacquelinedavid@hotmail.com is a Engineer, electronics
  espinozadaryl@hill-maddox.com is a Engineering geologist
  edwardsjacob@gmail.com is a Chemical engineer

Wow, we found some contacts! Email them to learn about your job!
```

## Source Code and Configuration Files

### Describe in detail how your provided source code works

#### The source code statement that makes the `search` module available to `main`

Use a fenced code block to provide the requested source code
Write at least one paragraph to explain the request source code

```
from contactsearcher import search
```
This source code statement allows the code to implement components from the search python file. It does this by using a "from" and "import" statement. The "from" statement allows you to navigate from a specified folder or file in this case, its a folder called "contactsearcher". The "import" statement allows you to access a file functions and variables or you can use it to access a specific function from a file, in this case we have accessed a whole python file called "search" and now we are able to call functions in the main.py file that are originally located in  the search.py file.

#### The source code statement that extracts the current job description for a contact

Use a fenced code block to provide the requested source code
Write at least one paragraph to explain the request source code

```
if job_description in current_job.lower():
```

This source code statement is an if statement that tells the function, if the job_description matches the current job for the current contact then the statement will run. It does this by first extracting the current job of the current contract and stores it in "current_job". Then you use the if statement to see if the "job_description" that is inputted by the user matches the "current_job". The "lower" method is used just to clear up any user errors when telling the function what job description they want found. All it does is change the indicated string to all lowercase.

#### Invocation of the function called `search_for_email_given_job`

Use a fenced code block to provide the requested source code
Write at least one paragraph to explain the request source code

```
relevant_emails = search.search_for_email_given_job(job_description, contacts_file)
```
When you invoke a function, you basically call it indirectly. Like calling a function within a function. This source code is calling the "search_for_email_given_job" in the main module by mapping from the search.py file and then to the function.
#### Test case for the function called `search_for_email_given_job`

Use a fenced code block to provide the requested source code
Write at least one paragraph to explain the request source code

```
def test_find_zero_matching_result():
    """Check to ensure that search for contacts works for one match."""
    contacts_database = """kylebarnes@hotmail.com,Records manager
joe70@yahoo.com,Network engineer
torresjames@white.info,Electrical engineer
shawkins@watson.com,Science writer"""
    contacts_list = search.search_for_email_given_job("nurse", contacts_database)
    assert len(contacts_list) == 0
    contacts_list = search.search_for_email_given_job(
        "physical therapit", contacts_database
    )
    assert len(contacts_list) == 0
```
this test case tests for the correctness of the "search_for_email_given_job" function by using a literal called "contacts_database" and running it through our code."

#### Execute trace of the `contactsearcher` program

Explain each function call that takes place for the following run of the program
Write at least one paragraph to explain every function call when running `contactsearcher`

Your discussion should start with the invocation of the `contactsearcher`
function in the `main` module, explain all of the subsequent function calls in
the correct order, and then show how the program's control returns to the
`contactsearcher` function in the `main` module.

- `poetry run contactsearcher --job-description "engineer" --contacts-file input/contacts.txt`

So first the "search_for_email_given_job" is invoked in the main module by using the statement, "relevant_emails = search.search_for_email_given_job(job_description, contacts_file)," then it is called in the search.py file using the parameters called from the main module. Which are "job_description" and "contacts_file". Then the output of the function is used in the main module using this statement, "for emails in relevant_emails:".

## Professional Assessment

### So far this semester, what is one area in which you have struggled? How did you overcome this challenge?

Provide a one-paragraph response that answers this question in your own words.

I struggled with being able to write the reflections and articulate what the programs we have been working on are doing or what they are trying to do. I overcame this by being more specific when it comes to describing the course code of functions and that has helped me understand what each function is doing better then that helped me understand the overall functionality of the program.

### Based on your experiences with this project, what is one way in which you want to improve?

Provide a one-paragraph response that answers this question in your own words.

I want to improve in understanding test cases and what they are asking of the program a bit better. As well as get a better understanding of why we need test cases if the program works already.
