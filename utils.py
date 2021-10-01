import re
import argparse


# Here we are checking values, if they are consistent with our assignment
def name_type(arg_value):
    """
    String that checks if it contains only allowed characters and if it does not start or end with space " "
    :param arg_value:
    :return:
    """
    pat = re.compile(
        r"^[a-zA-Z0-9-áčďéěíňóřšťůúýžÁČĎÉĚÍŇÓŘŠŤŮÚÝŽ]+[a-zA-Z0-9- áčďéěíňóřšťůúýžÁČĎÉĚÍŇÓŘŠŤŮÚÝŽ]*[a-zA-Z0-9-áčďéěíňóřšťůúýžÁČĎÉĚÍŇÓŘŠŤŮÚÝŽ]+$")
    if not pat.match(arg_value):
        print("Not matching")
        raise argparse.ArgumentTypeError
    return arg_value


def phone_type(arg_value):
    """
    String that can, but does not have to, start with "+" and then contains only numbers
    :param arg_value:
    :return:
    """
    pat = re.compile(r"^\+?[0-9]+")
    if not pat.match(arg_value):
        raise argparse.ArgumentTypeError
    return arg_value


def year_type(arg_value):
    """
    Integer greater then 1901 and smaller then 2021
    :param arg_value:
    :return:
    """
    converted = int(arg_value)
    if converted <= 1901:
        raise ValueError
    if converted >= 2021:
        raise ValueError
    return arg_value


def email_type(arg_value):
    """
    String that must be unique regex found at
    https://stackoverflow.com/questions/201323/how-can-i-validate-an-email-address-using-a-regular-expression
    :param arg_value:
    :return:
    """
    pat = re.compile(
        r"(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"
    )
    if not pat.match(arg_value):
        raise argparse.ArgumentTypeError
    return arg_value


def password_type(arg_value):
    """
    String that must contain at least one upper letter and on number other than that it can contain any characters
    :param arg_value:
    :return:
    """
    pat = re.compile(r".*[0-9].*")
    if not pat.match(arg_value):
        raise argparse.ArgumentTypeError
    pat = re.compile(r".*[A-Z].*")
    if not pat.match(arg_value):
        raise argparse.ArgumentTypeError
    return arg_value


def id_type(arg_value):
    """
    Integer automatically generated for every new user can not be below 0
    :param arg_value:
    :return:
    """
    converted = int(arg_value)
    if converted <= 0:
        raise ValueError
    return arg_value


def dict_from_row(row):
    """
    We need dicts so the program interpret data stored properly
    https://stackoverflow.com/questions/3300464/how-can-i-get-dict-from-sqlite-query
    :param row:
    :return:
    """
    return dict(zip(row.keys(), row))
