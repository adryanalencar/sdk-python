#coding: utf-8
from uuid import uuid4
from copy import deepcopy
from starkinfra import PixReversal
from random import randint, choice
from ..utils.end_to_end_id import get_end_to_end_id


example_pix_reversal = PixReversal(
    amount=1,
    external_id=str(uuid4()),
    reason="bankError",
    end_to_end_id=get_end_to_end_id()[0],
)


# TODO: Method, reconciliation_id and receiver_key_id are left out
def generateExamplePixReversalJson(n=1):
    pix_reversals = []
    for _ in range(n):
        pix_reversal = deepcopy(example_pix_reversal)
        amount = randint(1, 10)
        pix_reversal.amount = amount
        pix_reversal.external_id = str(uuid4())
        pix_reversal.end_to_end_id = choice(get_end_to_end_id())
        pix_reversal.reason = choice(["bankError", "fraud", "pixWithdrawError", "refund3ByEndCustomer"])
        pix_reversal.tags = [choice(["little", "girl", "no", "one"]), choice(["little", "girl", "no", "one"])]
        pix_reversals.append(pix_reversal)
    return pix_reversals
