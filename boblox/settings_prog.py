import pyautogui


def open_settings():
    settings_option = pyautogui.confirm(title='Boblox', text='Settings\n\n', buttons=['Change Username', 'Reset Account'])
    if settings_option == None: pass
    elif settings_option == 'Change Username':
        new_username = pyautogui.prompt(title='Boblox', text='Enter new username')
        if new_username == None: del new_username
        else:
            open('boblox\\account\\username', 'w').write(new_username)
            del new_username
            pyautogui.alert(title='Boblox', text='Username has been changed. Boblox will now close.', button='Okay')
            del settings_option
            quit()

    elif settings_option == 'Reset Account':
        open('boblox\\account\\username', 'w').write('')
        open('boblox\\account\\bobux', 'w').write('bobux=0')
        open('boblox\\account\\purchases', 'w').write('')
        pyautogui.alert(title='Boblox', text='Account Reset. Boblox will now close.', button='Okay')
        del settings_option
        quit()






    del settings_option