import PIL.Image, winshell, pystray, ctypes, sys, os

image = PIL.Image.open(f"{os.getcwd()}/icon.png")

def clear(icon, item):
	try:
		winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
		ctypes.windll.user32.MessageBoxW(0, "Bin was successfully emptied!", "Tray Bin", 0)
	except:
		ctypes.windll.user32.MessageBoxW(0, "Bin has been emptied", "Tray Bin", 0)

def app_exit():
	icon.stop()

icon = pystray.Icon("Tray Bin", image, menu=pystray.Menu(pystray.MenuItem("Clear bin", clear), pystray.MenuItem("Exit", app_exit)))

icon.run()