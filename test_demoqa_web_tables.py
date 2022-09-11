from selene.support.shared import browser
from selene import be, have, config
import pytest

config.hold_browser_open = True

first_name = 'Dmitry'
last_name = 'Sem'
age = '26'
email = 'demotest@tete.com'
salary = '9999'
department = 'qa'


def test_demoqa_web_tables_edit():
    browser.open_url('https://demoqa.com/webtables')
    browser.element('#edit-record-2').click()
    browser.element('#registration-form-modal').should(have.text('Registration Form'))

    browser.element('#firstName').clear()
    browser.element('#firstName').type('la')

    browser.element('#lastName').clear()
    browser.element('#lastName').type("lo")

    browser.element('#userEmail').clear()
    browser.element('#userEmail').type(email)

    browser.element('#age').clear()
    browser.element('#age').type("33")

    browser.element('#salary').clear()
    browser.element('#salary').type("7777")

    browser.element('#department').clear()
    browser.element('#department').type("dep")

    browser.element('#submit').click()


def test_demoqa_web_tables_delete():
    browser.element('#delete-record-3').click()

def test_demoqa_web_tables_add():
    browser.element('#addNewRecordButton').click()
    browser.element('#firstName').type(first_name)
    browser.element('#lastName').type(last_name)
    browser.element('#userEmail').type(email)
    browser.element('#age').type(age)
    browser.element('#salary').type(salary)
    browser.element('#department').type(department)
    browser.element('#submit').click()

