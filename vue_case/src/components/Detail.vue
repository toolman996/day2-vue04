<template>
    <div>
        <span>id:{{$route.params.id}}</span><br>
        <span>name:{{$route.params.name}}</span><br>
        <span>age:{{$route.params.age}}</span><br>
        <button @click="add">返回首页</button>
        <button @click="back">返回用户页面</button>
    </div>

</template>

<script>
    export default {
        name: "Detail",
        methods:{
            add(){
                this.$router.push('/home')
            },
            back(){
                this.$router.push('/users')
            }
        }
    }
</script>

<style scoped>

</style>
