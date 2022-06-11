**Scrapy Automation**

**Billboard Top Artists**

**Soheil Raeisi**

**Date:** 2022/04/26

# Contents 

[**Web scraping** [2](#section)](#section)

[**Project Content** [2](#project-content)](#project-content)

[**Step by Step Instruction**
[3](#step-by-step-instruction)](#step-by-step-instruction)

[**Google Form & Data Summary**
[4](#google-form-data-summary)](#google-form-data-summary)

# 

# **Web scraping**

In today's competitive world everybody is looking for a way to innovate
and make use of new technologies. Web scraping (also called web data
extraction or [data scraping](https://www.zyte.com/data-extraction/))
provides a solution for those who want to get access to structured web
data in an automated fashion. Web scraping is useful if the public
website you want to get data from doesn't have an API, or it does but
provides only limited access to the data.

Billboard scraper is a program that firstly extracts the 5 previous
week's top artists from the Billboard website. Afterwards, the
repetitive names are removed from the artists list and then be uploaded
to the google drive as a google sheet file. On the google aps scripts
platform two functions are provided to firstly create a form for the
artists to be ranked by the respondents, and subsequently, produce an
average rate according to the responses for each artist. The Whole
program is attached within a folder named Billboard and you can find
instruction on the way it must be used and automated in the upcoming
paragraphs.

-   **This program can only be utilized for Billboard website**

# **Project Content**

The project file contains different files which are explained in
upcoming paragraphs.

-   Bilbord_scrapy.py

This is the main program that by the aid of Scrapy framework crawls
through the website and extracts the names and ranks of the artists of
past 4 weeks which is called the Spider. As can be seen the URL of the
web page is given to the program and by finding the date of the current
webpage and deduction of weeks from it the URL of the past 4 weeks are
produced, so the spider can go through 4 previous pages and according to
the CSS selectors extracts the artists names and ranks.

-   Data_Cleaner.py

Data cleaner file contains the function that removes the duplicated
names and all ranks. It also sorts all names alphabetically and save
them to a new file named Ultimate.csv. This function uses Pandas library
and it only works with CSV files.

-   UPLOAD.py

This program has the responsibility for connection between the local
server and the desired Google Drive. It gets the name and the type of
the file which wants to be sent the google drive and also the type of
the file which is intended to be saved in the drive. Undoubtedly, the
email of the destination drive must be added to the code.

-   GoogleAppScript.gs

Contains two functions for creation of form and data summary which can
be used in the google apps script editor.

-   Data.csv / Ultimate.csv

Data.csv is the raw extracted names and ranks of the top 5 artists of 4
previous weeks and Ultimate.csv is the file which contains cleaned data
and is going to be uploaded to the google drive. These two files have
been added to the project as examples, However it is highly recommended
that do not change the names of these files while running the program,
otherwise some modifications inside the codes must be done.

# **Step by Step Instruction**

Firstly copy the billboard folder on your system, then in order to use
the program follow the steps:

1.  Firstly, if you do not have a Google Cloud Project, it is needed to
    be created to be able to use the Google API:

- Open <https://cloud.google.com> then select ***Console*** select
    ***project*** ***New Project*** ***create***

- Enable the API at Console ***API &servicesLibrary***search
    "Drive API"***API enabled.***

2.  A very important step is that a Google service account must be
    created. Google API does not allow you to access the cloud with a
    normal account. Therefore a service account must be created. Please
    follow the steps:

-   click on
    <https://cloud.google.com/docs/authentication/getting-started>
    thenclick on (**Go to Create service account**)select your
    projectwrite a name and serve account for description then ***create
    and continue***select the ***owner*** as the ***role*** then press
    ***continueDone*** now the service account is created and you can
    see the email address

-   Now you have to create a service account keyclick on email
    addressclick on tab ***keys*** ***add keycreate new key***choose
    JSONby pressing ***create*** your credential JSON file which
    contains the service account key is downloaded. This is the file
    that is required to connect to Google API. Preferably put it beside
    the UPLOAD.py file.

-   At the end you must create an environment variable to link to the
    credential file. Its name is **GOOGLE_APPLICATION_CREDENTIALS.**
    just write in the command line or your IDE terminal :

> In Linux or macOS: **export**
> **GOOGLE_APPLICATION_CREDENTIALS={*KEY_PATH*}**
>
> In Windows : **\$env:GOOGLE_APPLICATION_CREDENTIALS={*KEY_PATH*}**

3.  Since we are going to use Google Python API to upload the file to
    Google drive firstly install google_api_python_client library: **pip
    install google_api_python_client**

4.  The only item that needs to be changed prior to run the program is
    the email address which you can find it in the line 41. Currently as
    an example my email address is written but it has to be the address
    of the location where the user intends to save the data as a google
    sheet.

5.  **Automation:** the processes of data extraction, data
    transformation and data loading must be scheduled to run once a
    month. As normally this program is run on the server which uses
    Linux, scheduling the program is explained for Crontab tool. However
    there is a subsystem for Crontab in windows called WSL which is free
    to download.

    -   **Crontab:** there are 3 files that must be scheduled,
        Billboard_scrapy.py ,Data_Cleaner.py and UPLOAD.py. firstly it
        is better to change the editor in Linux to a friendly one by the
        commandexport EDITOR=gedit

    -   Now run the Crontab tool crontab **--**e

    -   Write these three commands to schedule 3 files to be run once a
        month:

> 0 0 1 * * cd {path}/billbord && scrapy crawl Billboard -O Data.csv
>
> 2 0 1 * * cd {path}/billbord/Data_Cleaner.py
>
> 3 0 1 * * cd {path}/billbord/UPLOAD.py

-   **For running the scrapy do not forget to use capital "O" to
    override the previous file, as the previous data is no longer
    needed.**

# **Google Form & Data Summary**

At this point, the ultimate file has been uploaded to the Google Drive
and it can been accessed in the sheets tab. Open the uploaded sheet and
on the ribbon click on the **Extensions** then **apps script.** Now the
google scripts editor for the uploaded sheet is opened. From the GS file
in the project copy the whole two functions and paste them in the
editor. As can be seen there is a drop down tool which can be used to
select the name of the desired function. Firstly choose the createFrom
function, run it. The URL of the created form appears below the editor
page and with that the form can be used.

To use the data summary function firstly the ID of the form must be
written in the code like the example. The ID is accessible from the URL
of the form. After running the dataSummary code you can see that all the
average rankings are added in front of the names of the artists in the
sheet.
