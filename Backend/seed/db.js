const {Pool}=require("pg");
const pool=new Pool({
    user:"postgres",
    password:"adi",
    host:"localhost",
    port:5432,
    database:"enginedb"
});
pool.connect().then(client=>{
    console.log("Postgres Connected")
    client.release();
})
.catch(err=>{
    console.log(err)
})

module.exports=pool;