import flet as ft
from time import sleep
def main(page):
    t = ft.Text()
    page.add(t)
    for i in range (10):
        t.value = f"{i}"
        page.update()
        sleep(1)
ft.app(target=main)