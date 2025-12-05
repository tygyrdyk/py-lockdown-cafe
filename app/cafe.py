import datetime

import app.errors as errors


class Cafe():
    def __init__(self, name):
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if not visitor["vaccine"]:
            raise errors.NotVaccinatedError
        if datetime.date.today() > visitor["vaccine"]["expiration_date"]:
            raise errors.OutdatedVaccineError
        if not visitor["wearing_a_mask"]:
            raise errors.NotWearingMaskError
        return f"Welcome to {self.name}"