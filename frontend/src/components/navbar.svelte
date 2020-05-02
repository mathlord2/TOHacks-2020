<script>
    import {onMount} from "svelte";
    export let userType = "Doctor";
</script>

<ul class="navbar">
    <h1>{userType}</h1>
    {#if userType == "Doctor"}
        <img src="static/doctor.jpg" alt="">
    {:else}
        <img src="static/patient.png" alt="">
    {/if}
    <li><a>Sign Out</a></li>
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