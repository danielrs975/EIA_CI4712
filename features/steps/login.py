'''
Pasos para login.feature
'''
# pylint: disable=function-redefined
from selenium.webdriver.support.ui import Select
from behave import given, when, then # pylint: disable=no-name-in-module

@given('Usuario loggeado')
def step_impl(context):
    '''
    Pasos para acceder al sistema como superuser
    '''
    context.browser.get(context.base_url)
    context.browser.find_element_by_id('id_username').send_keys('admin')
    context.browser.find_element_by_id('id_password').send_keys('jaja1234')
    context.browser.find_element_by_id('id_submit').click()

@given('Usuario registrado')
def step_impl(context):
    '''
    Pasos para crear un usuario en el sistema
    '''
    # Creates a dummy user for our tests (user is not authenticated at this point)
    context.browser.get(context.base_url+'/users/create/')
    # pylint: disable=duplicate-code
    inputs_and_values = [
        ('id_first_name', 'Jean'),
        ('id_last_name', 'Guzman'),
        ('id_username', 'jguzman'),
        ('id_email', 'jguzman@usb.ve'),
        ('id_password1', 'jaja1234'),
        ('id_password2', 'jaja1234'),
        ('id_doc_identidad', 'V-90'),
    ]
    #find the form element
    for selector, value in inputs_and_values:
        context.browser.find_element_by_id(selector).send_keys(value)

    Select(context.browser.find_element_by_id('id_rol')).select_by_visible_text(
        'Administrador del Sistema')
    context.browser.find_element_by_id('registrar').click()

@when('Introduzco los datos correctamente')
def step_impl(context):
    '''
    Paso para loguearnos en el sistema
    '''
    context.browser.get(context.base_url)
    context.browser.find_element_by_id('id_username').send_keys('jguzman')
    context.browser.find_element_by_id('id_password').send_keys('jaja1234')
    context.browser.find_element_by_id('id_submit').click()

@then('Me redirigen a la vista de registro')
def step_impl(context):
    '''
    Revisar si estamos logueados
    '''
    # Checks success status
    assert context.browser.current_url.endswith('')
