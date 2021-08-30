from datetime import datetime
from time import mktime, strptime

from api import app, db
from api import models


@app.cli.command("create-officer")
def command_create_officer():
    dce = input("Please enter the officer's RIT DCE (abc1234): ")
    name = input("Please enter the officer's name (John Smith): ")
    committee = input("Please name the officer's committe (technology): ")
    email = input("Please name the officer's email (technology): ")
    is_primary_str = input("Is the user a primary? [y/N]: ")
    is_primary = is_primary_str == "y" or is_primary_str == "Y"
    start_str = input(
        "Please enter the start date of the officer's term (2021-08-21): "
    )
    end_str = input("Please enter the end date of the officer's term (2022-05-31): ")

    # yikes: https://stackoverflow.com/a/1697907
    start_date = datetime.fromtimestamp(mktime(strptime(start_str, "%Y-%m-%d")))
    end_date = datetime.fromtimestamp(mktime(strptime(end_str, "%Y-%m-%d")))

    if end_date < start_date:
        print("Validation failure: start date cannot be after end date!")
        exit()
    if len(dce) > 7 or "@" in dce:
        print(
            "RIT DCE should only be the first part of the officer's email, ie abc1234"
        )
        exit()
    if "@" in email:
        print("email should ony be first part of the sse email, ie technology")
        exit()

    officer = models.Officer(
        rit_dce=dce,
        name=name,
        committee=committee,
        is_primary=is_primary,
        start_date=start_date,
        end_date=end_date,
        email=email,
    )
    db.session.add(officer)
    db.session.commit()
    print("Succesfully created officer!")
