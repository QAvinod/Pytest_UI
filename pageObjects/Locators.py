LOADING = {
    'load': 'dw-loading-active',
    'upload': '//*[@ng-disabled="vm.loadingOptions.active"]'
}

TAG = {
    'anchor': 'a'
}

ATTACHMENT = {
    'file': '//input[@type="file"]'
}

NOTIFIER = {
    'message': 'growl-message',
    'dismiss': 'close'
}

PLACEHOLDER = {
    'text_ph': '//input[@type="text"][@placeholder="{}"]',
    'num_ph': '//input[@type="number"][@placeholder="{}"]'
}

TITLE = {
    'title': '//*[@title="{}"]'
}

BUTTONS = {
    'button': "//button[text()='{}']",
    'all_buttons': "//*[text()='{}']",
}

ACTIONS = {
    'actions_click': '//*[@class="fa fa-caret-down"]',
    'action': '',
    'float_click_class': 'fa-angle-right',
    'float_action': ''
}

LOGIN = {
    'alias': 'alias',
    'next': '.btn-default',
    'login_name': 'loginName',
    'password': '//input[@type="password"]',
    'login': 'login',
}

JOB = {
    'job_name': '//*[@placeholder="Name"]',
    'description': '//*[@id="mainBodyElement"]/div[3]/section/div/basic-job/div/div'
                   '[2]/div[8]/div/wysiwyg-edit/div/div[2]/iframe',
    'openings': 'openings'
}
