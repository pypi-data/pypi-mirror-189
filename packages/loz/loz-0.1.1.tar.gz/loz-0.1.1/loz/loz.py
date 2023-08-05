"""
loz functions
"""
from loz import cry
from loz.exceptions import *
from os import path
import csv
import io
import json
import logging
import secrets

logger = logging.getLogger("loz")
storage_version = "1.0"

global pto


def load(loz_file):
    "Loads .loz file and returns storage object."
    global pto
    if not path.isfile(loz_file):
        raise LozFileDoesNotExist(f"No loz file found at {loz_file}.")
    storage = None
    logger.debug(f"opening {loz_file}")
    with open(loz_file, "r") as f:
        storage = json.loads(f.read())
        logger.debug(f"loaded storage from {loz_file}")
        if storage["version"] > storage_version:
            raise LozIncompatibleFileVersion(
                f"Found lozfile version {storage['version']} but supports up to {storage_version}."
            )
    pto = cry.Pto(storage["pub"])
    return storage


def save(storage, loz_file):
    "Saves storage object as json .loz file."
    logger.debug(f"opening {loz_file}")
    storage["version"] = storage_version
    with open(loz_file, "w") as f:
        f.write(json.dumps(storage, indent=4))
        logger.debug(f"storage written to {loz_file}")


def validate_key(storage, password=None):
    "Tries to unlock storage with a password. Store key as global for later use."
    global pto
    try:
        logger.debug("validating password")
        pto = cry.Pto(storage["pvt"], password)
        return True
    except Exception as e:
        print(e)
        return False


def init(password):
    "Initialize storage with master password."
    pvt, pub = cry.generate_key_pair(password)
    storage = {"pvt": pvt, "pub": pub, "data": {}}
    return storage


def export_csv(storage, csv_file=None):
    "Export plaintext storage and print to output or save to CSV file."
    return_contents = False
    if not csv_file:
        csv_file = io.StringIO()
        return_contents = True
    writer = csv.writer(
        csv_file,
        delimiter=" ",
        quotechar="|",
        quoting=csv.QUOTE_MINIMAL,
        lineterminator="\n",
    )
    for row in get_all(storage):
        writer.writerow(row)
    if return_contents:
        return csv_file.getvalue()


def import_csv(storage, csv_file):
    rows = csv.reader(
        csv_file,
        delimiter=" ",
        quotechar="|",
        quoting=csv.QUOTE_MINIMAL,
        lineterminator="\n",
    )
    total_change = ["", "", "", "total changes"]
    for row in rows:
        domain = row[0]
        user = row[1]
        secret = row[2]
        change = store(storage, domain, user, secret)
        yield change


def change_password(storage, new_pass):
    pvt, pub = cry.generate_key_pair(new_pass)
    new_storage = {"pvt": pvt, "pub": pub, "data": {}}
    new_pto = cry.Pto(new_storage["pvt"], new_pass)
    for domain, user, secret in get_all(storage):
        logger.debug(f"moving {domain}/{user} to new storage")
        encrypted = new_pto.encrypt(secret)
        if domain in new_storage["data"].keys():
            new_storage["data"][domain][user] = encrypted
        else:
            new_storage["data"][domain] = {user: encrypted}
    return new_storage


def store(storage, domain, user, secret):
    "Store secret for domain/user pair. Return [change_type, domain, user, message] list of changed item."
    global pto
    encrypted = pto.encrypt(secret)
    if exists(storage, domain, user):  # update existing
        logger.debug(f"updating secret for {domain}/{user}")
        storage["data"][domain][user] = encrypted
        return ["-+", domain, user, "Update existing secret."]
    if exists(storage, domain):  # add new user
        logger.debug(f"adding user {user} with secret for {domain}")
        storage["data"][domain][user] = encrypted
        return ["+", domain, user, "Add user and secret."]
    # add user and domain
    logger.debug(f"adding domain {domain} and user {user} with secret")
    storage["data"][domain] = {user: encrypted}
    return ["+", domain, user, "Add domain, user and secret."]


def make(storage, domain, user):
    "Generate and secret for domain/user pair. Return output of store(...)."
    global pto
    secret = cry.make_password()
    print(secret)
    return store(storage, domain, user, secret)


def exists(storage, domain, user=None):
    if domain not in storage["data"]:
        logger.debug(f"domain {domain} does not exist")
        return False
    if not user:
        logger.debug(f"domain {domain} exists")
        return True
    if user in storage["data"][domain]:
        logger.debug(f"user {user} exists in domain {domain}")
        return True
    logger.debug(f"user {user} does not exist in domain {domain}")
    return False


def get(storage, domain, user):
    "Return secret for 'domain user' pair."
    global pto
    if not exists(storage, domain, user):
        logger.warning(f"{domain}/{user} does not exist")
        return None
    secret = storage["data"][domain][user]
    return pto.decrypt(secret)


def get_all(storage):
    for domain in storage["data"].keys():
        for user in storage["data"][domain].keys():
            yield [
                domain,
                user,
                get(storage, domain, user),
            ]


def rm(storage, domain, user=None):
    "Delete user from domain or whole domain, return change."
    if not exists(storage, domain):
        return ["|", "", "", "No change."]
    if user and not exists(storage, domain, user):
        return ["|", "", "", "No change."]
    if user:
        del storage["data"][domain][user]
        if not storage["data"][domain]:
            del storage["data"][domain]
            return ["-", domain, "*", "Delete whole domain."]
        return ["-", domain, user, "Delete user."]
    else:
        del storage["data"][domain]
        return ["-", domain, "*", "Delete whole domain."]


def show(storage, domain):
    "List all secrets in one domain."
    if not exists(storage, domain):
        return None
    for user in ls(storage, domain):
        logger.debug("user found, decrypting secret")
        decrypted = get(storage, domain, user)
        yield [domain, user, decrypted]


def ls(storage, domain=None):
    "List all storage or users under one domain."
    if not domain:
        return list(storage["data"].keys())
    if not exists(storage, domain):
        return []
    return list(storage["data"][domain].keys())


def find(storage, word):
    "List storage and users that contain the search phrase."
    results = []
    for domain in storage["data"]:
        if word in domain:
            results.append(
                [
                    domain,
                ]
            )
        for user in storage["data"][domain]:
            if word in user:
                results.append([domain, user])
    return results
