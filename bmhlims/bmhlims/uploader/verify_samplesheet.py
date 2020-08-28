import click as click
import numpy as np
import pandas as pd
from pathlib import Path
import datetime


# Rules for Sample Submission Sheet
# All return True is the rule is violated and should be flagged, otherwise False

def checkforspaces(val: str):
    """
    this method checks for space characters
    :param val: string value of the row
    :return: False if there is no spaces, True if there is a space, and error message
    """
    if " " in val:
        mes = "Detected space character in {}".format(val)
        return True, mes
    return False, ""


def disallowedchars(val: str, discharlist):
    """
    this method check for any of the characters in the provided list
    :param val: string value of the row
    :param discharlist: list of characters to check for
    :return: False if none of the listed characters are there, True if there is character listed and error message
    """
    for x in discharlist:
        if x in val:
            mes = "Detected disallowed character {} in {}".format(x, val)
            return True, mes
    return False, ""


def characterlimit(val: str):
    """
    this method checks that val is under 20 characters
    :param val: string value of the row
    :return: False if val is 20 characters or under, True if it is over 20 characters and error message
    """
    if len(val) > 20:
        mes = "Exceeded character length of 20 for {}".format(val)
        return True, mes
    return False, ""


def picklist(val: str, picklistvalues):
    """
    this method checks is the val is in the provided list of strings
    :param val: string value of the row
    :param picklistvalues: list of strings
    :return: False if val is in picklistvalues, True is val is not in the picklistvalues and error message
    """
    if val not in picklistvalues:
        mes = "{} is not one of the accepted values".format(val)
        return True, mes
    return False, ""


def checknumbertype(val: str, numtype: str):
    """
    this method checks if a number is the right type, int or float
    :param val: string value of the row
    :param numtype: the expected type, int or float ir digit
    :return: True is the val is not the type given, False if it is the matching type and error message
    """
    if numtype == "float":
        if isinstance(val, float):
            return False, ""
        else:
            mes = "{} should be a Float (Decimal)".format(val)
            return True, mes
    if numtype == "int":
        if isinstance(val, int):
            return False, ""
        else:
            mes = "{} should be an int (No Decimal)".format(val)
            return True, mes
    if numtype == "digit":
        if val.isdigit():
            return False, ""
        else:
            mes = "{} should be a digit".format(val)
            return True, mes


def alluppercase(val: str):
    """
    this method checks if every value in val is uppercase
    :param val: string value of the row
    :return: True if there is a non uppercase character, False if val is all uppercase and error message
    """
    if val.isupper():
        return False, ""
    else:
        mes = "{} should be all uppercase letters".format(val)
        return True, mes


def isdate(val: str):
    """
    this method checks if val is a valid date in the proper format
    :param val: string value of the row
    :return: True if it is not in date format, False if val is a proper date and error message
    """
    try:
        datetime.datetime.strptime(val, '%Y-%m-%d')
    except ValueError:
        # raise ValueError("Incorrect data format, should be YYYY-MM-DD")
        mes = "Incorrect data format, should be YYYY-MM-DD"
        return True, mes
    return False, ""


def wellformat(val: str):
    """
    this method checks to see if it fits the Well format of Capital Letter then two digits
    :param val: string value in the row
    :return: True if it is not in the proper format, false if it is correct and error message
    """
    if len(val) > 3:
        mes = "Improper Well format for {}".format(val)
        return True, mes
    if (val[0].isalpha()) and val[0].isupper() and val[1].isdigit():
        return False, ""
    mes = "Improper Well format for {}".format(val)
    return True, mes


def singleword(val: str):
    """
    this method checks if val is a single capitalized word
    :param val: string value in the rule
    :return: True is it is not a single capitalized word, false if it is and error message
    """

    if val[0].islower():
        mes = "Not a single capitalized word for {}".format(val)
        return True, mes
    if not val.isalpha():
        mes = "Not a single capitalized word for {}".format(val)
        return True, mes
    return False, ""


def readfile():
    print("START")
    print("Opening file: ")
    # click.echo(click.format_filename(filename))

    filename = "/home/kelsey/Documents/SS_20200122_META_WGS_16S_M01308.csv"


    f = Path(filename)

    counter = 1
    with open(str(f)) as f:
        for line in f:
            if '[Data]' in line:
                break
            else:
                counter += 1
    ss_df = pd.read_csv(f, sep=",", index_col=False, skiprows=counter)

    # ss_df = pd.read_csv(str(f), skiprows=19)
    result = parse(ss_df)

    return result


def parse(ss_df):
    disCharList = ["#", "*", ".", "\\", "/", "[", "]", ":", ";", "|", "="]  # need to do """
    picklistValues = ["Salmonella", "VTEC", "Parasitology", "Botulism", "Listeria", "Vibrio",
                      "Virology" "Rapid-Diagnostics", "Other"]
    picklistValues2 = ["Cells in DNA/RNA Shield (~0.1ug cells in 400uL)", "Extracted DNA", "Amplicon", "Other"]

    messages = []
    flagList = []

    # for col in ss_df.columns:
    col_list = list(ss_df.columns.values)

    # Goes through each row, and each column checking the values
    # each method returns a tuple of the flag/result (True or False) and the error message.
    # if flag is False the message is empty string(""), if true it is a string
    # both get appended to a list, flagList or messages
    for i, row in ss_df.iterrows():

        # Sample_ID
        if 'Sample_ID' in ss_df.columns:
            holder = checkforspaces(row['Sample_ID'])
            flagList.append(holder[0])
            messages.append((holder[1]))

            holder = disallowedchars(row['Sample_ID'], disCharList)
            flagList.append(holder[0])
            messages.append((holder[1]))

            holder = characterlimit(row['Sample_ID'])
            flagList.append(holder[0])
            messages.append((holder[1]))

        # Sample_Name
        if 'Sample_Name' in ss_df.columns:
            holder = checkforspaces(row['Sample_Name'])
            flagList.append(holder[0])
            messages.append((holder[1]))

            holder = disallowedchars(row['Sample_Name'], disCharList)
            flagList.append(holder[0])
            messages.append((holder[1]))

            holder = characterlimit(row['Sample_Name'])
            flagList.append(holder[0])
            messages.append((holder[1]))

        # Sample_Well  - opt
        if 'Sample_Well' in ss_df.columns:
            holder = wellformat(row['Sample_Well'])
            flagList.append(holder[0])
            messages.append((holder[1]))

        # Submitting_Lab
        if 'Submitting_Lab' in ss_df.columns:
            holder = picklist(row['Submitting_Lab'], picklistValues)
            flagList.append(holder[0])
            messages.append((holder[1]))

        # Submission_Date
        if 'Submission_Date' in ss_df.columns:
            holder = isdate(row['Submission_Date'])
            flagList.append(holder[0])
            messages.append((holder[1]))

        # Submission_Format
        if 'Submission_Format' in ss_df.columns:
            holder = picklist(row['Submission_Format'], picklistValues2)
            flagList.append(holder[0])
            messages.append((holder[1]))

        # Sample_Volume
        if 'Sample_Volume' in ss_df.columns:
            holder = checknumbertype(row['Sample_Volume'], 'digit')
            flagList.append(holder[0])
            messages.append((holder[1]))

        # Genus - single capitalized word, only letters
        if 'Genus' in ss_df.columns:
            holder = checkforspaces(row['Genus'])
            flagList.append(holder[0])
            messages.append((holder[1]))

            holder = singleword(row['Genus'])
            flagList.append(holder[0])
            messages.append((holder[1]))

        # Species - single capitalized word, only letter
        if 'Species' in ss_df.columns:
            holder = checkforspaces(row['Species'])
            flagList.append(holder[0])
            messages.append((holder[1]))

            holder = singleword(row['Species'])
            flagList.append(holder[0])
            messages.append((holder[1]))

        # Culture_Date
        if 'Culture_Date' in ss_df.columns:
            holder = isdate(row['Culture_Date'])
            flagList.append(holder[0])
            messages.append((holder[1]))

    # checks the list of all the results for all the columns in the sheet
    # if a true exists in the list, the ss failed verification
    # if no true exists it is a success
    if True in flagList:
        result = ("FAIL")
    else:
        result = ("SUCCESS")

    # Goes through messages list and makes a list of the none empty("") ones
    errorsMessages = []
    for mes in messages:
        if mes is not "":
            errorsMessages.append(mes)

    # returns the result of verification (FAIL or SUCCESS) and a list of errorMessages or an empty list
    return result, errorsMessages


