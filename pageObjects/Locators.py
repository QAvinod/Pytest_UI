LOADING = {
    'load': 'dw-loading-active',
    'upload': '//*[@ng-disabled="vm.loadingOptions.active"]'
}

TAG = {
    'anchor': 'a',
    'h4': 'h4',
    'href': 'href'
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
    'place_holder': '//input[@placeholder="{}"]',
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
    'done': '//*[@ng-click="$hide();"]',
    'radio': 'label.btn-default',
    'actionClicked': '//button[@ng-click="vm.actionClicked({}{}{});"]'
}

ACTIONS = {
    'actions_click': "//span[contains(text(),'Actions')]",
    'view_candidates': 'Event-Details-View-Candidates',
    'slot_config': 'Event-Details-Configure-Interview-Slots',
    'status_change': 'cardlist-view-Change-Applicant Status',
    'lobby': 'Event-Details-View-Interview-Lobby',
    'float_click_class': 'fa-angle-right',
    'float_action': ''
}

SEARCH = {
    'advance_search': 'cardlist-view-filter',
    'Name': 'Name',
    'name': 'name'
}

MULTI_SELECTIONS = {
    'moveSelectedItemsRight': '//*[@data-ng-click="vm.moveSelectedItemsRight();"]',
    'moveAllItemsRight': '//*[@data-ng-click="vm.moveAllItemsRight();"]',
    'moveSelectedItemsLeft': '//*[@data-ng-click="vm.moveSelectedItemsLeft();"]',
    'moveAllItemsLeft': '//*[@data-ng-click="vm.moveAllItemsLeft();"]',
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

EVENT = {
    'configurations': '//*[@ui-sref="crpo.events.details.configurations"]',
    'owners': '//*[@crpo.events.details.owners]',
}

CHANGE_STATUS = {
    'stage': '//*[@ng-model="vm.selectedStage"]',
    'status': '//*[@ng-model="vm.selectedStatus"]',
    'comment': '//*[@ng-model="vm.comments"]'
}

CANDIDATE = {
    'id': '//*[@id="mainBodyElement"]/div[3]/div/div[1]/div[1]/div/div/div[2]/div[2]/p[2]/span[2]'
}

SLOT = {
    'assign': '//*[@bs-tooltip="{}{}{}"]'.format("'", 'Assign slots', "'")
}

CANDIDATE_LOBBY_LOGIN = {
    'candidate_name': "//label[contains(text(),'{}')]",
}

ROOM = {
    'active': '//*[@bs-tooltip="{}{}{}"]'.format("'", 'Activate Room', "'")
}
