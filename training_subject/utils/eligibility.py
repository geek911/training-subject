from edc_constants.choices import YES_NO, YES
from edc_constants.constants import NO


def _check_literate(is_literate, is_witness_literate):
    if is_literate == YES:
        return True

    if is_literate == NO and is_witness_literate == YES:
        return True
    return False


def _check_citizenship(citizenship: str, spouse_citizenship: str, marriage_proof: str) -> bool:
    if citizenship == 'Botswana':
        return True

    if marriage_proof == YES and spouse_citizenship == 'Botswana':
        return True

    return False


def _check_age(age: int, guardian: str):
    if age < 18:
        if guardian == YES:
            return True
        else:
            False
    else:
        return True


def is_eligible(
        citizen: str,
        spouse_citizenship: str,
        marriage_proof: str,
        is_literate,
        is_witness_literate: str,
        guardian_available: str,
        age: int
):
    citizenship_status = _check_citizenship(citizen, spouse_citizenship, marriage_proof)
    literate_status = _check_literate(is_literate, is_witness_literate)
    age_status = _check_age(age, guardian_available)

    return citizenship_status and literate_status and age_status
