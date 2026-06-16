const {pool}=require("pg");
const pool=new Pool({
    user:"postgres",
    password:"adi",
    host:"localhost",
    port:5432,
    database:"enginedb"
});
module.exports=pool;