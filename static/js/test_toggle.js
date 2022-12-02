window['reporters_reporter_engagement'] = {
    $el: () => $('#selector_reporter_engagement').closest('div.card').find('div.card-header input[type=checkbox]'),
    $select: () => $('#selector_reporter_engagement .selectpicker'),
    get_data: () => {
        if (reporters_reporter_engagement.$el().prop('checked')) {
            return reporters_reporter_engagement.$select().val()
        }
    },
    set_data: data => {
        reporters_reporter_engagement.$select().val(data || 'info').selectpicker('refresh')
        reporters_reporter_engagement.$el().prop('checked', true)
        $('#selector_reporter_engagement').collapse('show')
    },
    clear_data: () => {
        reporters_reporter_engagement.$select().val('info').selectpicker('refresh')
        reporters_reporter_engagement.$el().prop('checked', false)
        $('#selector_reporter_engagement').collapse('hide')
    }
}
