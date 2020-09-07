<template>
    <div id="app">
        <h1>根组件</h1>
        <router-link to="/home">留言</router-link>
        <router-link to="/users">用户页面</router-link>
<!--        <router-link to="/detail">详情</router-link>-->
        <hr>
        <router-view></router-view>

    </div>
</template>

<script>
    import Home from "./components/Home";
    import Users from "./components/Users";
    import Detail from "./components/Detail";

    export default {
        name: 'App',
        methods:{
        },
        components: {
            home: Home,
            users:Users,
            detail:Detail,
        }
    }
</script>

<style>

</style>
