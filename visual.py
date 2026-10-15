from playwright.sync_api import sync_playwright
import pyautogui as auto
from time import sleep
from tkinter import messagebox

pergunta = messagebox.askyesno("Confirmação", "Deseja realmente executar esta automação?")

if pergunta:

    with sync_playwright() as pw:
        browser = pw.chromium.launch(channel="msedge", headless=False)
        context = browser.new_context()
        page = context.new_page()
        
        page.goto("https://docs.google.com/spreadsheets/d/1KTBoj91zwghTOPKw_UixbmwUl4XKu7ueIlXx8SXe_pQ/edit?usp=sharing")
        auto.click(1225,30) # Tela cheia (Verificar local!)

        #  * Login *
        page.locator(".goog-inline-block.fixed4-inner-container").first.click()
        for i in range(5):
            if i < 3:
                auto.press('down')
            else:
                auto.press('right')
            sleep(0.5)
        page.locator("#waffle-rich-text-editor").press("F2")
        page.get_by_role("combobox", name="C4").fill("analista_01@e-mail.com")
        page.locator("#waffle-rich-text-editor").press("Enter")
        page.locator("#waffle-rich-text-editor").press("F2")
        page.get_by_role("combobox", name="C5").fill("1234")
        sleep(10)
        page.locator("#waffle-rich-text-editor").press("Tab")
        page.locator("#waffle-rich-text-editor").press("Tab")
        page.locator("#waffle-rich-text-editor").press("Enter")
        sleep(0.5)
        page.locator("#waffle-rich-text-editor").press("Tab")
        page.get_by_role("link", name="Cadastro").press("Enter")

        sleep(0.5)
        #  * Cadastro *
        page.locator(".goog-inline-block.fixed4-inner-container").first.click()
        for i in range(7):
            if i < 4:
                page.locator("#waffle-rich-text-editor").press("ArrowDown")
            else:
                page.locator("#waffle-rich-text-editor").press("ArrowRight")
            sleep(0.5)
        page.locator("#waffle-rich-text-editor").press("F2")
        page.get_by_role("combobox", name="D5").fill("Neoenergia Distribuição Brasília S.A.")
        page.locator("#waffle-rich-text-editor").press("Enter")
        page.locator("#waffle-rich-text-editor").press("ArrowDown")
        page.locator("#waffle-rich-text-editor").press("F2")
        page.get_by_role("combobox", name="D7").fill("123456")
        page.locator("#waffle-rich-text-editor").press("Enter")
        page.locator("#waffle-rich-text-editor").press("ArrowDown")
        page.locator("#waffle-rich-text-editor").press("F2")
        page.get_by_role("combobox", name="D9").fill("31/01/2026")
        page.locator("#waffle-rich-text-editor").press("Enter")
        page.locator("#waffle-rich-text-editor").press("ArrowDown")
        page.locator("#waffle-rich-text-editor").press("F2")
        page.get_by_role("combobox", name="D11").fill("50,00 / 25,00 / 25,00")
        page.locator("#waffle-rich-text-editor").press("Enter")
        page.locator("#waffle-rich-text-editor").press("ArrowDown")
        page.locator("#waffle-rich-text-editor").press("F2")
        page.get_by_role("combobox", name="D13").fill("500,00")
        page.locator("#waffle-rich-text-editor").press("Enter")
        page.locator("#waffle-rich-text-editor").press("ArrowDown")
        page.locator("#waffle-rich-text-editor").press("F2")
        page.get_by_role("combobox", name="D15").fill("400,00")
        page.locator("#waffle-rich-text-editor").press("Enter")
        page.locator("#waffle-rich-text-editor").press("ArrowDown")
        page.locator("#waffle-rich-text-editor").press("F2")
        page.get_by_role("combobox", name="D17").fill("Conta de luz - Janeiro 26")
        sleep(10)
        page.locator("#waffle-rich-text-editor").press("Tab")
        page.locator("#waffle-rich-text-editor").press("Tab")
        page.locator("#waffle-rich-text-editor").press("Enter")
        sleep(0.5)
        page.locator("#waffle-rich-text-editor").press("Tab")
        page.get_by_role("link", name="Informativo").press("Enter")
        
        #  * Informativo *

        sleep(10) # 3600 = 1h
        browser.close()

else:
    pass
