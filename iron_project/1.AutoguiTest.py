import pyautogui as auto

print(auto.position())
auto.click(200, 74)
auto.typewrite('How are you')
# use enter key not enter string
auto.typewrite(['enter'])
auto.hotkey('ctrl', 'c')
auto.hotkey('space')
