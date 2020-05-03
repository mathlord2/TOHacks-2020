<script>
    import {onMount} from "svelte";
    import {loggedIn, currentUser, userType} from "./../stores/user.js";

    function signout() {
        firebase.auth().signOut().then(function() {
            loggedIn.set(false);
            currentUser.set(null);
            console.log("Signed out");
        });
    }

    let type;

    const unsubscribe = userType.subscribe(val => {
        type = val;
    });
</script>

<ul class="navbar">
    <h1>{type}</h1>
    {#if type == "Doctor"}
        <img src="static/doctor.jpg" alt="">
    {:else if type == "Patient"}
        <img src="static/patient.png" alt="">
    {/if}
    <li><a on:click={signout}>Sign Out</a></li>
</ul>

<style>
    .navbar {
        height: 100%;
        width: 15%;
        background-color: rgb(238, 221, 252);
        position: absolute;
        left: 0;
        top: 0;
        z-index: 1;
        text-align: center;
    }

    li {
        list-style-type: none;
        font-size: 20px;
        margin: 25px 0px;
    }

    li a {
        text-decoration: none;
        color: black;
    }
    
    li a:hover {
        color: grey;
    }

    h1 {
        margin-top: 20px;
        font-size: 30px;
    }
</style>