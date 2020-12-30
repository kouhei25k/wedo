
Vue.component('open-modal', {
    template: `
    <div id="overlay" v-on:click.self="clickEvent">
        <div id="content" >
          <slot></slot>
          <button v-on:click="clickEvent" name="create_new_room">close</button>
        </div>
    </div>
    `,
    methods: {
        clickEvent: function () {
            this.$emit('from-child')
        }
    }
})

new Vue({
    el: '#app',
    data: {
        showContent: false
    },
    methods: {
        openModal: function () {
            this.showContent = true
        },
        closeModal: function () {
            this.showContent = false
        },
    }
})
