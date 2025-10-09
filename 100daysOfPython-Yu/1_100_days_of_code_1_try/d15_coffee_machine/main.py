import functions

is_turned_on = True

while is_turned_on:
    user_drink = functions.prompt_user_drink()

    is_coffe_brewable = functions.resources_sufficient(user_drink)

    user_payment = functions.count_money()

    is_transaction_successful = functions.check_transaction_success(user_payment, user_drink)

    functions.make_coffe(is_coffe_brewable, is_transaction_successful, user_drink)

    functions.refill()

    is_turned_on = functions.turn_machine_off()


