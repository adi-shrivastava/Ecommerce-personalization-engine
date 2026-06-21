const pool=require("./db");
users=[]
const cities=['Indore','Agra','Bangalore','Pune','Mumbai','Chennai','Delhi'];
const names=['Rahul','Arun','Ajay','Ankit']
function randomitem(cities){
    return cities[Math.floor(Math.random()*cities.length)];
}
function randomname(names){
    return names[Math.floor(Math.random()*names.length)];
}

async function seedusers(){
    const Users=await pool.query("Select * from users");
    for(let i=1; i<=1000; i++){
        const user='User${i}';
        const age=(Math.floor(Math.random()*40)+18);
        const name=randomname(names);
        const city=randomitem(cities);
        console.log({name,age,city});
        await pool.query('INSERT INTO USERS (name,age,city) Values($1,$2,$3)',[name,age,city])
    }
}
seedusers()

