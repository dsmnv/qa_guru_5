import pytest
from selene.support.shared import browser
from selene import be, have
from selene import config
from conftest import upload_file

config.hold_browser_open = True

first_name = 'Dmitry'
last_name = 'Sem'
email = 'demotest@tete.com'
mobile_number = '9570000000'
current_address = 'Saint - P'
file = 'images/donut.png'


def test_demoqa():
    browser.open_url('https://demoqa.com/automation-practice-form')

    # First_name, Last_name

    browser.element('#firstName').type(first_name)
    browser.element('#lastName').type(last_name)

    # email, gender, number

    browser.element('#userEmail').type(email)
    browser.element('#gender-radio-1').double_click()
    browser.element('#userNumber').type(mobile_number)

    #Birthday

    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').type('November')
    browser.element('.react-datepicker__year-select').type('1995')
    browser.element('[aria-label="Choose Sunday, November 5th, 1995"]').click()

    #Subjects

    browser.element('#subjectsInput').type('Eng').press_enter().type('comp').press_enter()

    # Hobbies

    browser.element('[for="hobbies-checkbox-2"]').click()
    browser.element('[for="hobbies-checkbox-3"]').click()

    # image
    #browser.element('#uploadPicture').send_keys(file)

    #Address

    browser.element('#currentAddress').type(current_address)

    #State and City

    browser.element('#react-select-3-input').type('ncr').press_enter()
    browser.element('#react-select-4-input').type('gurgaon').press_enter()



















