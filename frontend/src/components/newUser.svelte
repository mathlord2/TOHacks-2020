<script>
    import {currentUser, isNew, userType} from "./../stores/user.js";
    
    function setDoctor() {
        userType.set("Doctor");
        isNew.set(null);
    }

    function setPatient() {
        userType.set("Patient");
        isNew.set(null);
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