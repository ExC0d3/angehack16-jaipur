#!/usr/bin/python

from pymongo import MongoClient

from pymongo.errors import DuplicateKeyError
from werkzeug.security import generate_password_hash


def main():
    # Connect to the DB
    collection = MongoClient()["supporti"]["users"]

    # Ask for data to store
    user = raw_input("Enter your username: ")
    password = raw_input("Enter your password: ")
    pass_hash = generate_password_hash(password, method='pbkdf2:sha256')

    # Insert the user in the DB
    try:
        collection.insert({"_id": user, "password": pass_hash})
        print "User created."
    except DuplicateKeyError:
        print "User already present in DB."


if __name__ == '__main__':
    main()
