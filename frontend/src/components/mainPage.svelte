<script>
    import {onMount} from 'svelte';
    import {userType, isNew} from './../stores/user.js';
    export let filename = "lung.jpg";
    export let condition = "Normal";

    //async obtainFilename() {
    //}

    let type;

    const unsubscribe = userType.subscribe(val => {
        type = val;
    });
</script>

<div class="main">
    {#if type == "Doctor"}
        <h1>Upload lung image here:</h1>
        <button class="upload">Upload <i class="fa fa-upload"></i></button>
        {#if filename != ""}
            <p>{filename} has been uploaded.</p>
            <p>Condition: {condition}</p>
        {/if}
    {:else if type == "Patient"}
        <h1>Status:</h1>
        <p>Condition: {condition}</p>
    {/if}
</div>

<style>
    .main {
        width: 100%;
        text-align: center;
        color: white;
        padding: 50px 0px;
    }

    .upload {
        margin-top: 20px;
    }

    h1 {
        font-size: 40px;
    }

    button {
        border: none;
        border-radius: 10px;
        padding: 20px;
        font-size: 25px;
        background-color: aliceblue;
    }

    button:hover {
        background-color: rgb(175, 197, 209);
    }
    
    p {
        margin: 20px 0px;
    }
</style>