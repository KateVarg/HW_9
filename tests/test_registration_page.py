from selene import have
from modules.registration_page import RegistrationPage


def test_practice_form():
    registration_page = RegistrationPage()
    registration_page.open()

    registration_page.fill_first_name('Иван')
    registration_page.fill_last_name('Иванов')
    registration_page.fill_email('ivanivanov@test.com')
    registration_page.choose_gender('1')
    registration_page.fill_phone_number('8912345678')
    registration_page.choose_birth_date('015', '5', '1999')
    registration_page.fill_subject('English')
    registration_page.choose_hobbies('1')
    registration_page.choose_form_file('images.jpeg')
    registration_page.fill_address('Страна, город, улица, дом, этаж, квартира')
    registration_page.choose_state('0')
    registration_page.choose_city('1')
    registration_page.click_submit()

    registration_page.check_data(
            'Иван Иванов',
            'ivanivanov@test.com',
            'Male',
            '8912345678',
            '15 June,1999',
            'English',
            'Sports',
            'images.jpeg',
            'Страна, город, улица, дом, этаж, квартира',
            'NCR Gurgaon',
            )