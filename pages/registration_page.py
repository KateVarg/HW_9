from selene import browser, have
import os
from data.user import User
import tests


class RegistrationPage:

    def open(self):
        browser.open('/automation-practice-form')
        return self

    def fill_first_name(self, first_name):
        browser.element('#firstName').type(first_name)
        return self

    def fill_last_name(self, last_name):
        browser.element('#lastName').type(last_name)
        return self

    def fill_email(self, email):
        browser.element('#userEmail').type(email)
        return self

    def choose_gender(self, gender):
        browser.element(f'[name=gender][value={gender}]+label').click()
        return self

    def fill_phone_number(self, phone_number):
        browser.element('#userNumber').type(phone_number)
        return self

    def choose_birth_date(self, day, month, year):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').type(month)
        browser.element('.react-datepicker__year-select').type(year)
        browser.element(f'.react-datepicker__day.react-datepicker__day--0{day}').click()
        return self

    def fill_subject(self, subject):
        browser.element('#subjectsInput').type(subject)
        browser.element('.subjects-auto-complete__menu').click()
        return self

    def choose_hobbies(self, hobby):
        browser.all('.custom-control-label').element_by(have.exact_text(hobby)).click()
        return self

    def choose_form_file(self, path):
        browser.element('.form-file').click()
        browser.element('#uploadPicture').set_value(os.path.abspath(
            os.path.join(os.path.dirname(tests.__file__), f'images/{path}')))
        return self

    def fill_address(self, address):
        browser.element('#currentAddress').type(address)
        return self

    def choose_state(self, state):
        browser.element('#state').click()
        browser.all('[id^="react-select-3-option-"]').element_by(have.exact_text(state)).click()
        return self

    def choose_city(self, city):
        browser.element('#city').click()
        browser.all('[id^="react-select-4-option-"]').element_by(have.exact_text(city)).click()
        return self

    def click_submit(self):
        browser.element('#submit').click()
        return self

    def register(self, user: User):
        (
            self.fill_first_name(user.first_name)
            .fill_last_name(user.last_name)
            .fill_email(user.email)
            .choose_gender(user.gender)
            .fill_phone_number(user.phone_number)
            .choose_birth_date(user.date_day, user.date_month, user.date_year)
            .fill_subject(user.subject)
            .choose_hobbies(user.hobby)
            .choose_form_file(user.file)
            .fill_address(user.address)
            .choose_state(user.state)
            .choose_city(user.city)
            .click_submit()
        )
        return self

    def check_registrated_user(self, user: User):
        browser.element('.modal-content').element('table').all('tr').all('td').even.should(have.exact_texts(
            f'{user.first_name} {user.last_name}',
            user.email,
            user.gender,
            user.phone_number,
            f'{user.date_day} {user.date_month},{user.date_year}',
            user.subject,
            user.hobby,
            user.file,
            user.address,
            f'{user.state} {user.city}',
        )
        )
