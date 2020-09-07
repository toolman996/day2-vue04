<template>
    <div>
        <input type="text" v-model="data">
        <button @click="add">发表评论</button>
        <br>
        <span v-for="(value,index) in arry" :key="index">
        {{index+1}}.{{value}} <a href="javascript:" @click="del(index)">del</a><br>
    </span>
        <span>count:{{arry.length}}条</span><br>
<!--        <button @click="delall" v-show="JSON.parse(localStorage.date).length!=0">清空评论</button>-->
        <button @click="delall">清空评论</button>
    </div>
</template>

<script>
    export default {
        name: "Home",
      data(){
          return{
            data:'',
            arry:localStorage.date?JSON.parse(localStorage.date):[]
          }
        },
        //vue 所有的方法都在methods中
        // props:['args'],

        methods: {
            //this对象表示当前的vue实例对象
            add(){
                if (this.data)
                    this.arry.push(this.data)
                    //将数据持久化到浏览器
                    localStorage.date=JSON.stringify(this.arry)
                    this.data='';
            },
            del(index){
                this.arry.splice(index,1)
                localStorage.removeItem('date')
                localStorage.date=JSON.stringify(this.arry)
            },
            delall(){
              this.arry=''
              localStorage.removeItem('date')
            }
        },
    }
</script>

<style scoped>

</style>
