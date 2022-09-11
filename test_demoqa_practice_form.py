import os.path
from selene.support.shared import browser
from selene import be, have, config



config.hold_browser_open = False

first_name = 'Dmitry'
last_name = 'Sem'
email = 'demotest@tete.com'
mobile_number = '9570000000'
current_address = 'Saint - P'


def test_demoqa():
    browser.open_url('https://demoqa.com/automation-practice-form')
    browser.element('#firstName').type(first_name)
    browser.element('#lastName').type(last_name)
    browser.element('#userEmail').type(email)
    browser.element('#gender-radio-1').double_click()
    browser.element('#userNumber').type(mobile_number)
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').type('November')
    browser.element('.react-datepicker__year-select').type('1995')
    browser.element('[aria-label="Choose Sunday, November 5th, 1995"]').click()
    browser.element('#subjectsInput').type('Eng').press_enter().type('comp').press_enter()
    browser.element('[for="hobbies-checkbox-2"]').click()
    browser.element('[for="hobbies-checkbox-3"]').click()
    browser.element('#uploadPicture').send_keys(os.path.abspath('images/donut.png'))
    browser.element('#currentAddress').type(current_address)
    browser.element('#react-select-3-input').type('ncr').press_enter()
    browser.element('#react-select-4-input').type('gurgaon').press_enter()
    browser.element('#submit').click()

    #verification

    browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))
    browser.element('.table-responsive').should(have.text(mobile_number))
    browser.element('.table-responsive').should(have.text('donut.png'))
    browser.element('#closeLargeModal').click()
    browser.element('#firstName').should(be.blank)
    browser.element('#lastName').should(be.blank)
    browser.element('#userEmail').should(be.blank)
    browser.element('#userNumber').should(be.blank)














