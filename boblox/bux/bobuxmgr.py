from ast import literal_eval
import pyautogui


bobux = literal_eval(open('boblox\\bux\\bobux', 'r').read())
bobux_dict = bobux
bobux = int(bobux['bobux'])
purchases = literal_eval(open('boblox\\purchases', 'r').read())
print(purchases)
print(bobux_dict)
print(bobux)

def add_to_bobux(amount):
    to_give = str(int(bobux+amount))
    bobux_dict.update({'bobux': to_give})
    open('boblox\\bux\\bobux', 'w').write(str(bobux_dict))
    return to_give

def remove_from_bobux(amount):
    if (bobux-amount) < 0:
        return 'fail'
    else:
        to_take = str(int(bobux-amount))
        bobux_dict.update({'bobux': to_take})
        open('boblox\\bux\\bobux', 'w').write(str(bobux_dict))
        return to_take

def purchase(item, cost):
    if remove_from_bobux(cost) == 'fail': pyautogui.alert(title='Boblox', text='You don\'t have enough bobux to purchase this item.', button='Okay')
    else:
        purchases.append(item)
        open('boblox\\purchases', 'w').write(str(purchases))
        pyautogui.alert(title='Boblox', text=f'You sucessfully bought {item}', button='Okay')
