from selene import browser, have
import os

class RegistrationPage:

    def open(self):
        browser.open('/automation-practice-form')

    def fill_first_name(self, first_name):
        browser.element('#firstName').type(first_name)

    def fill_last_name(self, last_name):
        browser.element('#lastName').type(last_name)

    def fill_email(self, email):
        browser.element('#userEmail').type(email)

    def choose_gender(self, gender):
        browser.element(f'[for="gender-radio-{gender}"]').click()

    def fill_phone_number(self, phone_number):
        browser.element('#userNumber').type(phone_number)

    def choose_birth_date(self, day, month, year):
        browser.element('#dateOfBirthInput').click()
        browser.element(f'.react-datepicker__month-select option[value="{month}"]').click()
        browser.element(f'.react-datepicker__year-select option[value="{year}"]').click()
        browser.element(f'.react-datepicker__day.react-datepicker__day--{day}').click()

    def fill_subject(self, subject):
        browser.element('#subjectsInput').type(subject)
        browser.element('.subjects-auto-complete__menu').click()

    def choose_hobbies(self, hobbies_1):
        browser.element(f'[for="hobbies-checkbox-{hobbies_1}"]').click()
      #  browser.element(f'[for="hobbies-checkbox-{hobbies_2}"]').click()
    #    browser.element(f'[for="hobbies-checkbox-{hobbies_3}"]').click()

    def choose_form_file(self, path):
        browser.element('.form-file').click().element('#uploadPicture').send_keys(os.path.abspath(f'images/{path}'))


    def fill_address(self, address):
        browser.element('#currentAddress').type(address)

    def choose_state(self, state):
        browser.element('#state').click()
        browser.element(f'#react-select-3-option-{state}').click()

    def choose_city(self, city):
        browser.element('#city').click()
        browser.element(f'#react-select-4-option-{city}').click()

    def click_submit(self):
        browser.element('#submit').click()

    def check_data(self, full_name, email, gender, phone_number, birth_date, subjects, hobbies, file, address, state):
        browser.element('.modal-content').element('table').all('tr').all('td').even.should(have.exact_texts(
            full_name,
            email,
            gender,
            phone_number,
            birth_date,
            subjects,
            hobbies,
            file,
            address,
            state,
            )
        )
