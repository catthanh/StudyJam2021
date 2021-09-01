import urllib.request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup
import ssl
import csv

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

inputFile = "in.csv"
outputFile = "out.csv"

acceptedCourses = ["Serverless Firebase Development",
                   "Deploy to Kubernetes in Google Cloud",
                   "Implement DevOps in Google Cloud",
                   "Serverless Cloud Run Development",
                   "Monitor and Log with Google Cloud Operations Suite",
                   "Perform Foundational Infrastructure Tasks in Google Cloud",
                   "Create and Manage Cloud Resources",
                   "Secure Workloads in Google Kubernetes Engine",
                   "Set Up and Configure a Cloud Environment in Google Cloud"]
fields = []
rows = []
# import data
with open(inputFile) as inp:
    csvreader = csv.reader(inp)
    fields = next(csvreader)
    for row in csvreader:
        rows.append(row)
    print("Total no. of rows: %d" % (csvreader.line_num))

newRows = []
newFields = ['name', 'email']

for row in rows:
    url = row[2]
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    acceptedCoursesCount = 0
    # Retrieve all of the badges
    badgesList = soup.find_all("div", "profile-badge")

    for course in badgesList:
        a = course.find("span", "ql-subhead-1 l-mts")
        courseName = a.get_text().strip()
        if courseName in acceptedCourses:
            # print(courseName)
            acceptedCoursesCount += 1
    print('%s have completed %d course%s' % (
          row[1], acceptedCoursesCount, 's' if acceptedCoursesCount > 1 else ''))
    newRow = []
    if acceptedCoursesCount >= 6:
        newRow.append(row[1])
        newRow.append(row[0])
        newRows.append(newRow)
# export accepted data
with open(outputFile, 'w', newline='', encoding='utf-8') as out:
    csvwriter = csv.writer(out)
    csvwriter.writerow(newFields)
    csvwriter.writerows(newRows)
print()
