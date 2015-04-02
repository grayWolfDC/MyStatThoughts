import survey
table = survey.Pregnancies()
table.ReadRecords()
print 'Number of Pregnancies',len(table.records)
print table.records[1]