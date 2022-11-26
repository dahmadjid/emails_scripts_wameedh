import os

all_list = []

with open("all/all.csv") as all_file:
    for line in all_file:
        line_content = line.split(",")
        all_list.append(line_content)

# print(all_list)
def getEmailFromName(line) -> str:
    for person in all_list:
        if line.strip() == person[1] + "," + person[2]:
            return person[0]
    return "None"


for file in os.listdir("groups_without_emails"):
    new_csv_text = ""
    with open("groups_without_emails/"+file) as f:
        with open("groups_with_emails/"+file, "w") as new_file:
            for line in f:
                line_content = line.split(",")
                email = getEmailFromName(line)
                if email == "None":
                    print("rip: " + line_content[0])
                    pass
                else:
                    new_csv_text+= email + "," + line_content[0] + "," + line_content[1]
            new_file.write(new_csv_text)






