from Booking.booking import Booking


try:
    with Booking(teardown=False) as bot:

        bot.land_first_page()
        #bot.change_currency(currency='USD')
        bot.select_placeto_go(input("Where you want to go ?"))
        bot.select_dates(check_in_date=input("What is the check in date ?"),
                         check_out_date=input("What is the check out date ?"))
        bot.select_adults(int(input("How many people ?")))
        bot.select_rooms(int(input("How many rooms ?")))
        bot.search()
        bot.apply_filtrations()
        bot.refresh()
        bot.report_results()

except Exception as e:

    if 'in PATH' in str(e):
        print(
            'You are trying to run the bot from command line \n'
            'Please add to PATH your Selenium Drivers \n'
            'Windows: \n'
            '    set PATH=%PATH%;C:path-to-your-folder \n \n'
            'Linux: \n'
            '    PATH=$PATH:/path/toyour/folder/ \n'
        )
    else:
        raise

