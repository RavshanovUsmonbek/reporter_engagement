const ReporterEngagement = {
    delimiters: ['[[', ']]'],
    props: ['instance_name', 'section', 'selected_integration', 'is_selected'],
    emits: ['set_data', 'clear_data'],
    data() {
        return this.initialState()
    },
    methods: {
        get_data() {
            if (this.is_selected) {
                const {selected_integration: id} = this
                return {id}
            }
        },
        set_data(data) {
            const {id} = data
            this.$emit('set_data', {id})
        },
        clear_data() {
            Object.assign(this.$data, this.initialState())
            this.$emit('clear_data')
        },
        initialState: () => ({})
    },
    template: `
        <div class="security_integration_item" data-name="reporter_engagement"></div>
    `
}

register_component('reporter-engagement', ReporterEngagement)