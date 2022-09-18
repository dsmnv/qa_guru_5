from selene.support.shared import browser
from selene import have, be, config
from variables import student


config.hold_browser_open = True



def test_text_box():
    browser.open_url('https://demoqa.com/text-box')
    browser.element('#userName').should(be.blank).type(student.first_name)
    browser.element('#userEmail').should(be.blank).type(student.email)
    browser.element('#currentAddress').should(be.blank).type(student.current_address)
    browser.element('#permanentAddress').should(be.blank).type(student.permanent_address)
    browser.element('#submit').should(be.visible).click()

    #verificatoin

    browser.element('#output').should(be.visible)
    browser.element('#name').should(have.text(student.first_name))
    browser.element('#email').should(have.text(student.email))





