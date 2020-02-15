# SkytrakStats

Upload data from range sessions on the iOS Skytrak app and download the results in Excel format. 

## Background
Skytrak is pretty pathetic in the amount of data that it gives you access to. For users of iOS app, the only available data is malformed csv or pdf table data that you can export after your sessions. This project aims to clean these data formats and provide a tidy Excel workbook of the data for further use. 

## How it works 
1. Since the only export method of the data is email, a mailgun route was setup to proxy the data exports
2. A Flask API endpoint ([upload](upload)) accepts the incoming mailgun requests and processes the data files before forwarding the records to the storage API
3. A Django Rest Framework API ([api](api)) accepts the incoming session data to store. It also provides an endpoint to format and return the requested data as an Excel workbook
4. An Angular dashboard ([frontend](frontend)) displays the available session data along with links to download the data
5. Authentication and authorization provided by Auth0. One caveat is the email address used to export the data must be the same as the email address configured for the authenticated profile