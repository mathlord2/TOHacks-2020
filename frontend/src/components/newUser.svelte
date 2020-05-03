<script>
    import {currentUser, userId, isNew, userType, condition} from "./../stores/user.js";

    let id;

    const unsubscribe = userId.subscribe(val => {
        id = val;
    });
    
    function setDoctor() {
        const userData = {
            idUser: id,
            type: "Doctor"
        }
        db.collection("users").add(userData).catch(function(error) {
            console.error("Error adding document: ", error);
        });

        userType.set("Doctor");
        isNew.set(null);
    }

    function setPatient() {
        const userData = {
            idUser: id,
            type: "Patient",
            condition: ""
        }
        db.collection("users").add(userData).catch(function(error) {
            console.error("Error adding document: ", error);
        });

        userType.set("Patient");
        isNew.set(null);
        condition.set("");
    }
</script>

<div class="new">
    <h1>Welcome! Please select your role:</h1>
    <button on:click={setDoctor}>Doctor</button>
    <button on:click={setPatient}>Patient</button>
</div>

<style>
    .new {
        width: 100%;
        text-align: center;
        color: white;
        padding: 50px 0px;
    }

    h1 {
        font-size: 40px;
        color: white;
    }

    button {
        border: none;
        border-radius: 10px;
        padding: 20px;
        font-size: 25px;
        background-color: aliceblue;
        margin: 20px 10px;
    }

    button:hover {
        background-color: rgb(175, 197, 209);
    }
</style>