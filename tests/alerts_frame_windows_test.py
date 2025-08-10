import time
from pages.alert_frame_windows_page import BrowserWindowsPage, AlertsPage


class TestAlertsFrameWindow:
    class TestBrowserWindows:

        def test_new_tab(self, driver):
            browser_windows_page = BrowserWindowsPage(driver, 'https://demoqa.com/browser-windows')
            browser_windows_page.open()
            text_result = browser_windows_page.check_opened_new_tab()
            assert text_result == 'This is a sample page', 'the new tab has not opened or an incorrect tab has opened'

        def test_new_windows(self, driver):
            browser_windows_page = BrowserWindowsPage(driver, 'https://demoqa.com/browser-windows')
            browser_windows_page.open()
            text_result = browser_windows_page.check_opened_new_window()
            # time.sleep(5)
            assert text_result == 'This is a sample page', 'the new window has not opened or an incorrect window has opened'

    class TestAlerts:

        def test_see_alert(self, driver):
            alert_page = AlertsPage(driver, 'https://d emoqa.com/alerts')
            alert_page.open()
            alert_text = alert_page.check_see_alert()
            assert alert_text == 'You clicked a button', 'alert did not show up'

        def test_alert_appear_5_sec(self, driver):
            alert_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alert_page.open()
            alert_text = alert_page.check_alert_appear_5_sec()
            # print(alert_text)
            assert alert_text == 'This alert appeared after 5 seconds', 'alert did not show up'

        def test_confirm_alert(self, driver):
            alert_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alert_page.open()
            alert_text = alert_page.check_confirm_alert()
            # print(alert_text)
            assert alert_text == 'You selected Ok', 'alert did not show up'

        def test_promt_alert(self, driver):
            alert_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alert_page.open()
            text, alert_text = alert_page.check_promt_alert()
            # print(text)
            # print(alert_text)
            # assert alert_text == f"You entered {text}"
            assert text in alert_text, 'alert did not show up'
