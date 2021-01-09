
Vue.component('open-modal', {
    template: `
    <div id="overlay" v-on:click.self="clickEvent">
        <div id="content" >
          <slot></slot>
          <span v-on:click="clickEvent" type="button"class="material-icons modal_clear">clear</span>
    </div></div>`,
    methods: {
        clickEvent: function () {
            this.$emit('from-child')
        }
    }
})

new Vue({
    el: '#todo-form-vue',
    data: {
        showContent: false,
        selectedDate: null,
    },
    methods: {
        openModal: function () {
            this.showContent = true
        },
        closeModal: function () {
            this.showContent = false
        },
    },

})


new Vue({
    el: '#room_vue',
    data: {
        showDetails: false,
        classRow: {
            'row': false

        },
        classCol10: {
            'col-10': false
        },
        footerCol: {
            'col-10': true,
            'col-8': false
        },
        open_todo_form_icon: {
            position: 'fixed',
            bottom: '90px',
            right: '35px'
        },
        showAddMenberModal: false,


    },
    methods: {
        openDetails: function () {
            this.showDetails = true
            this.classRow = { 'row': true }
            this.classCol10 = { 'col-10': true }
            this.footerCol = {
                'col-10': false,
                'col-8': true
            }
        },
        closeDetails: function () {
            this.showDetails = false
            this.classRow = { 'row': false }
            this.classCol10 = { 'col-10': false }
            this.footerCol = {
                'col-10': true,
                'col-8': false
            }

        },
        openModal: function () {
            this.showAddMenberModal = true
        },
        closeModal: function () {
            this.showAddMenberModal = false
        },
    },

})
new Vue({
    delimiters: ['[[', ']]'],
    el: '#sidebar_add_friend',
    data: function () {
        return {
            showAddFriend: false,
            userId: null,
            username: "",
            params: {
                query: ""
            },
            user_search_input: "",
            searchedUser: false,
            userDoseNotExist: false
        }
    },

    methods: {
        searchUser: function () {
            this.params.query = this.user_search_input
            axios
                .get('../../axios_test/', {
                    params: this.params
                })
                .then(response => {
                    if (response.data == "None") {
                        this.userDoseNotExist = true
                    } else {
                        // console.log(response.data)
                        this.userId = response.data[0].pk;
                        this.username = response.data[0].fields.username;
                        this.searchedUser = true
                    }

                })
        },
        openAddFriendModal: function () {
            this.showAddFriend = true
        },
        closeAddFriendModal: function () {
            this.showAddFriend = false
        }
    }
})

new Vue({
    el: '#sidebar_add_room',
    data: {
        showAddRoom: false,

    },
    methods: {
        openModal: function () {
            this.showAddRoom = true
        },
        closeModal: function () {
            this.showAddRoom = false
        },

    }
})


new Vue({
    delimiters: ['[[', ']]'],
    el: '#test_vue',
    data: function () {
        return {
            userId: null,
            username: "",
            params: {
                query: ""
            },
            user_search_input: "",
            searchedUser: false,
            userDoseNotExist: false
        }
    },

    methods: {
        searchUser: function () {
            this.params.query = this.user_search_input
            axios
                .get('../axios_test/', {
                    params: this.params
                })
                .then(response => {

                    if (response.data == "None") {
                        this.userDoseNotExist = true
                    } else {
                        console.log(response.data)
                        this.userId = response.data[0].pk;
                        this.username = response.data[0].fields.username;
                        this.searchedUser = true
                    }

                })
        },
    }
})