# IDT-Coding-Challenge
## Part 1

Write a simple server, which provides a RESTful API. It should implement these two API calls:

GET /user/{id}
Returns user details based on the id. You can return static mock results.
PUT /user/{id}
Modifies a user property. It's ok to only store changes in memory. 

## Provided implementation
A simple SpringBoot application has been created with 2 rest endpoints (together with a generic home restpoint). I have decided
to create some sample data via a script here: ```/resources/demo_data.sql```. The script can be run through the h2 console at ```/h2-console```. 

## Part 2

Given the input string: ```"Hello world! How (sp?) are you today (;"``` split it into a list of words. You must strip all punctuation except for emoticons. Result for example: ```['Hello','world', 'how', 'sp', 'are', 'you', 'today', '(;']```

## Part 3
Architecture

Describe on a high level how you would design a messaging backend.

Provide an architecture schematic
Discuss scalability and performance issues
