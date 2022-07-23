import pyautogui
from boblox.account.bobux import bobux

def edit_bobux(bobux_amount):
    open('boblox\\account\\bobux.py', 'w').write('bobux=' + str(bobux_amount)); global bobux; bobux = bobux_amount

def add_to_bobux(amount):
    edit_bobux(bobux + int(amount))

def purchase(item_name, cost):
    if bobux - cost < 0: pyautogui.alert(title='Boblox', text='You do not have enough bobux to purchase this item', button='Alright')
    elif item_name in open('boblox\\account\\purchases', 'r').read(): pyautogui.alert(title='Boblox', text='You already own this item.', button='Alright')
    else:
        ask_buy = pyautogui.confirm(title='Boblox', text=f'Do you want to buy {item_name}?\n({cost} bobux)\nYour bobux will be {bobux - cost} after you purchase.', buttons=['Buy', 'Cancel'])
        if ask_buy == None: pass
        elif ask_buy == 'Cancel': pass
        elif ask_buy == 'Buy':
            open('boblox\\account\\purchases', 'w').write(open('boblox\\account\\purchases', 'r').read() + f'\n{item_name}')
            edit_bobux(str(bobux - cost))
            pyautogui.alert(title='Boblox', text=f'Purchased {item_name}', button='Alright')
