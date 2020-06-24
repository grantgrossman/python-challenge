import os
import csv
os.chdir("/Users/Pharaoh/Desktop/python-challenge/PyPoll/Resources")
with open('Election_data.csv') as csv_file:
    votes=0
    candidates=[]
    khan_counter=0
    correy_counter=0
    li_counter=0
    otooley_counter=0
    election=csv.reader(csv_file,delimiter=",")
    next(election)
    for row in election:
        votes+=1
        if row[2] not in candidates:
            candidates.append(row[2])
        if row[2] == "Khan":
            khan_counter+=1
        elif row[2] == "Correy":
            correy_counter+=1
        elif row[2]== "Li":
            li_counter+=1
        elif row[2]=="O'Tooley":
            otooley_counter+=1
        if khan_counter>correy_counter and li_counter and otooley_counter:
            winner="Khan"
        elif correy_counter>khan_counter and li_counter and otooley_counter:
            winner="Correy"
        elif li_counter>khan_counter and correy_counter and otooley_counter:
            winner="Li"
        elif otooley_counter>khan_counter and correy_counter and li_counter:
            winner="O'Tooley"    
    khan_vp=khan_counter/votes
    correy_vp=correy_counter/votes
    li_vp=li_counter/votes
    otooley_vp=otooley_counter/votes
results=print(f'''Election Results
  -------------------------
  Total Votes: {votes}
  -------------------------
  Khan: {"{:.0%}".format(khan_vp)} ({khan_counter})
  Correy: {"{:.0%}".format(correy_vp)} ({correy_counter})
  Li: {"{:.0%}".format(li_vp)} ({li_counter})
  O'Tooley: {"{:.0%}".format(otooley_vp)} ({otooley_counter})
  -------------------------
  Winner: {winner}
  -------------------------''')
with open("election_results.txt", "w") as text_file:
    print(results,file=text_file)
