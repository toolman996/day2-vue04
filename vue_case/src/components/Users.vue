<template>
    <div>
        <table border="1" cellspacing="0">
            <tr>
                <td>id</td>
                <td>name</td>
                <td>age</td>
                <td>delect</td>
                <td>detail</td>

            </tr>
            <tr v-for="(value,index) in users":key="index">
                <td>{{value.id}}</td>
                <td>{{value.name}}</td>
                <td>{{value.age}}</td>
                <td><a href="javascript:" @click="del(index)">删除</a></td>
                <td> <router-link :to="`/detail/${value.id}/${value.name}/${value.age}`">详情</router-link></td>

            </tr>
        </table>
        id: <input type="text" v-model="msg"><br>
        name: <input type="text" v-model="msg1"><br>
        age: <input type="text" v-model="msg2"><br>
        <input type="button" value="添加" @click="click"><br>
    </div>
</template>

<script>
    export default {
        name: "Users",
        data(){
            return{
                users:[{id:1,name:'华为',age:18},
                    {id:2,name:'中兴',age:20},
                    {id:3,name:'小米',age:22},
                    {id:4,name:'oppo',age:24},
                    {id:5,name:'魅族',age:26},
                ],
                msg:'',
                msg1:"",
                msg2:"",
            }
        },
        methods:{
            del(arg){
                this.users.splice(arg,1)
            },
            click() {
        let msg=this.msg;
        let msg1 = this.msg1;
        let msg2 = this.msg2;
         if (msg&&msg1&&msg2) {
            this.users.push({id:msg,name:msg1,age:msg2});
            this.msg='';
            this.msg1 = "";
            this.msg2 = "";

        }
            }
        }
    }
</script>

<style scoped>

</style>
