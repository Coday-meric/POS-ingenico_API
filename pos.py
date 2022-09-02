from telium import *


def pos_debit(amount):
    # Open device
    try:
        my_device = Telium('/dev/ttyACM0')
    except FileNotFoundError:
        return 'Device not connected'

    # Construct our payment infos
    my_payment = TeliumAsk.new_payment(
        amount,
        payment_mode='debit',  # other mode: credit or refund.
        target_currency='EUR',
        wait_for_transaction_to_end=True,  # If you need valid transaction status
        collect_payment_source_info=True,  # If you need to identify payment source
        force_bank_verification=False
    )

    # Send payment infos to device
    try:
        if not my_device.ask(my_payment):
            return 'Device refused transaction.'
    except TerminalInitializationFailedException as e:
        return format(e)

    # Wait for terminal to answer
    my_answer = my_device.verify(my_payment)

    if my_answer is not None:
        # Convert answered data to dict.
        dict = my_answer.__dict__

        # > {
        # '_pos_number': '01',
        # '_payment_mode': '1',
        # '_currency_numeric': '978',
        # '_amount': 12.5,
        # '_private': '0000000000',
        # 'has_succeeded': True,
        # 'transaction_id': '0000000000',
        # '_transaction_result': 0,
        # '_repport': '4711690463168807000000000000000000000000000000000000000',
        # '_card_type':
        #  {
        #      '_name': 'VISA',
        #      '_regex': '^4[0-9]{12}(?:[0-9]{3})?$',
        #      '_numbers': '4711690463168807',
        #      '_masked_numbers': 'XXXXXXXXXXXX8807'
        #  }
        # }

    if my_answer.has_succeeded:
        return "Payment processed {0} {1} {2}".format(my_answer.has_succeeded, my_answer.card_type.name,
                                                      my_answer.card_type.numbers)
    else:
        return "Payment rejected."
