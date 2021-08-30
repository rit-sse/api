from datetime import datetime
from time import mktime, strftime, strptime

from api import app, db
from api import models


@app.cli.command("create-membership")
def command_create_membership():
    dce = input("Please enter the member's RIT DCE (abc1234): ")
    name = input("Please enter the member's name (John Smith): ")
    start_str = input(
        "Please enter the start date of the membership ({}): ".format(
            datetime.now().strftime("%Y-%m-%d")
        )
    )
    end_str = input("Please enter the end date of the membership (2022-05-31): ")
    reason = input("Please give the reason for the membership: ")

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

    membership = models.Membership(
        rit_dce=dce,
        name=name,
        given=start_date,
        expires=end_date,
        given_by="cli",
        reason=reason,
        approved=True,
    )
    db.session.add(membership)
    db.session.commit()
    print("Created membership!")
