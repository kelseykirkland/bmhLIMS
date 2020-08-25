
def readfile(filename):
    print("START")
    print("Opening file: ")
    #click.echo(click.format_filename(filename))

#    f = Path(filename)

    counter = 1
    #with open(str(f)) as f:
    #    for line in f:
    #        if '[Data]' in line:
    #            break
    #        else:
    #            counter += 1
    #ss_df = pd.read_csv(f, sep=",", index_col=False, skiprows=counter)

    ss_df = pd.read_csv(str(f), skiprows=19)
    parse(ss_df)


def parse(ss_df):
    disCharList = ["#", "*", ".", "\\", "/", "[", "]", ":", ";", "|", "="]  # need to do """
    picklistValues = ["Salmonella", "VTEC", "Parasitology", "Botulism", "Listeria", "Vibrio",
                      "Virology" "Rapid-Diagnostics", "Other"]
    picklistValues2 = ["Cells in DNA/RNA Shield (~0.1ug cells in 400uL)", "Extracted DNA", "Amplicon", "Other"]

    #for col in ss_df.columns:
    #    print(col)
    col_list = list(ss_df.columns.values)
    print(col_list)

   # for i, row in ss_df.iterrows():
        # Sample_ID
        #checkforspaces(row['Sample_ID'])
        #disallowedchars(row['Sample_ID'], disCharList)
        #characterlimit(row['Sample_ID'])

        # Sample_Name
        #checkforspaces(row['Sample_Name'])
        #disallowedchars(row['Sample_Name'], disCharList)
        #characterlimit(row['Sample_Name'])

        # Sample_Plate  - free text, no rules

        # Sample_Well  - opt
        # Cap followed by 2 digits

        # Submitting_Lab
        # picklist(row['Submitting_Lab'], picklistValues)

        # Submission_Date
        # isdate(row['Submission_Date'])

        # Submission_Format
        # picklist(row['Submission_Format'], picklistValues2)

        # Sample_Volume
        # isdigit

        # Requested_Service
        # picklistValues3 = ["list"]
        # picklist(row['Requested_Service'], picklistValues3)

        # Submitter_Project_Name - free text

        # Genus - single capitalized word, only letters

        # Species - single capitalized word, only letter

        # Culture_Date
        # isdate(row["Culture_Date"])
