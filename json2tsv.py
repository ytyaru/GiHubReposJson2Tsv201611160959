#!python3
#encoding:utf-8

import json
import csv

username = 'GitHubUserName'
filePath = "GitHub.{0}.Repositories.json".format(username)
file = open(filePath, 'r', encoding="UTF-8")
data = json.load(file)
file.close()

filePath = "GitHub.{0}.Repositories.tsv".format(username)
with open(filePath, 'w', encoding="UTF-8") as file:
	writer = csv.writer(file, delimiter='\t', lineterminator='\n')
	writer.writerow(['id', 'name', 'description', 'homepage', 'created_at'])
	for i in range(0, len(data)):
		writer.writerow([data[i]["id"], data[i]["name"], data[i]["description"], data[i]["homepage"], data[i]["created_at"]])
