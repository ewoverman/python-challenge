import csv
import collections as ct

f2 = open("demofile2.txt", "w")
#f2.write("Now the file has more content!") ## sample write out a file
#f2.close() ## sample close the file

filepath = "election_data.csv"
with open(filepath) as f:
    votes = ct.Counter()
    reader = csv.reader(f)
    next(reader)
    for line in reader:
        candidate = line[-1]
        votes[candidate] += 1
# print(votes)
# print(votes.most_common(1))
#print(sum(votes.values()))   ### prints out the total votes

#sum_list = list(votes)  ## prints out length of that list
#print(len(sum_list))

#print(votes.keys() ) ## the names
candidate_name = list(votes.keys())
# print(candidate_name[0]) #### the array candidate_name

#print(votes.values() )## the values
candidate_votes = list(votes.values())
# print(candidate_votes[0]) ### the array candidite_votes

print("\n\nElection Results\n"
      "-------------------------\n"
      "Total Votes:",sum(votes.values()),
      "\n-------------------------")

f2.write("Election Results\n")
f2.write("-------------------------\n")
f2.write("Total Votes:")
f2.write(str(sum(votes.values())))
f2.write("\n-------------------------")

for i in range(0, len(candidate_name)):
     print(candidate_name[i],": ","{:.3%}".format(candidate_votes[i] / sum(votes.values()))," (",int(candidate_votes[i]),")",sep=''
     )
     f2.write("\n")
     f2.write(candidate_name[i])
     f2.write(": ")
     f2.write(str("{:.3%}".format(candidate_votes[i] / sum(votes.values()))))
     f2.write(" (")
     f2.write(str(int(candidate_votes[i])))
     f2.write(")")

rows = votes.most_common(1) ## pulls back a tuple
res_list = [x[0] for x in rows] ## pulls back the first value of the tuple
res = res_list[0] ## pulls back the value

print("\n-------------------------\n"
      "Winner: ", res,
      "\n-------------------------"
) 

f2.write("\n-------------------------\n")
f2.write("Winner: ")
f2.write(res)
f2.write("\n-------------------------")
   

f2.close() ## sample close the file