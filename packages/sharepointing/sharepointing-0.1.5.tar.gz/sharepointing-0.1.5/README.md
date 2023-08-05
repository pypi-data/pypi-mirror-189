# Sharepointing
A library to establish connection to sharepoint. Then operate on this connection. Right now it's only possible to upload files.

This library depends on office 365 library, and it will use active directory authentication to connect to SharePoint.

## Installation
In order to install this library you need to obtain an `SSH code`

Use pip to install this library from Github:

    pip install sharepointing

## Requirements
First you need to initialize the the sharepoint connection, which is an object.
You have two options, either use embedded credentials in environment variables:

`USERNAME` for office365 email

`PASSWORD` for office365 password


Then you can use this call:

    sp = sharepointing.sp_site(site_url)

The second option is to provide the credentials in the class call:

    sp = sharepointing.sp_site(site_url,username,password)

Once the object is created successfully, you can call use `send_file` method to upload the files to sharepoiont

## Example
    site_url = "https://companysite.sharepoint.com/teams/teamsname"
    target = "/teams/teamsname/Shared Documents/General/"
    file = 'file.txt'
    sp = sharepointing.sp_site(site_url)
    sp.send_file(file,target)
