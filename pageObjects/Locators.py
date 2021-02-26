LOADING = {
    'load': 'dw-loading-active',
    'upload': '//*[@ng-disabled="vm.loadingOptions.active"]'
}

TAG = {
    'anchor': 'a'
}

MENU = {
    'menu': "//a[contains(text(),'{}')]"
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

CHECKBOX = {
    'check': 'grid_items'
}

BUTTONS = {
    'button': "//button[text()='{}']",
    'all_buttons': "//*[text()='{}']",
}

ACTIONS = {
    'actions_click': '//*[@class="fa fa-caret-down"]',
    'view_candidates': 'Event-Details-View-Candidates',
    'status_change': 'cardlist-view-Change-Applicant Status',
    'float_click_class': 'fa-angle-right',
    'float_action': ''
}

SEARCH = {
    'advance_search': 'cardlist-view-filter',
    'Name': 'Name',
    'name': 'name'
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

CHANGE_STATUS = {
    'stage': '//*[@ng-model="vm.selectedStage"]',
    'status': '//*[@ng-model="vm.selectedStatus"]',
    'comment': '//*[@ng-model="vm.comments"]'
}
