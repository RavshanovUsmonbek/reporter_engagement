window['reporters_reporter_issues'] = {
    $el: () => $('#selector_reporter_issues').closest('div.card').find('div.card-header input[type=checkbox]'),
    $select: () => $('#selector_reporter_issues .selectpicker'),
    get_data: () => {
        if (reporters_reporter_issues.$el().prop('checked')) {
            return reporters_reporter_issues.$select().val()
        }
    },
    set_data: data => {
        reporters_reporter_issues.$select().val(data || 'info').selectpicker('refresh')
        reporters_reporter_issues.$el().prop('checked', true)
        $('#selector_reporter_issues').collapse('show')
    },
    clear_data: () => {
        reporters_reporter_issues.$select().val('info').selectpicker('refresh')
        reporters_reporter_issues.$el().prop('checked', false)
        $('#selector_reporter_issues').collapse('hide')
    }
}
