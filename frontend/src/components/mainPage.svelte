<script>
    import {onMount} from 'svelte';
    import {userType, isNew, filename, condition} from './../stores/user.js';
    import Upload from "./upload.svelte";

    //async obtainFilename() {
    //}

    let file;
    let type;
    let cond;

    const unsubscribe = userType.subscribe(val => {
        type = val;
    });

    const unsubscribe2 = filename.subscribe(val => {
        file = val;
    })

    const unsubscribe3 = condition.subscribe(val => {
        cond = val;
    })
</script>

<div class="main">
    {#if type == "Doctor"}
        <h1>Upload lung image here:</h1>
        <Upload/>
        {#if file != ""}
            <p>{file} has been uploaded.</p>
            <p>Condition: {cond}</p>
        {/if}
    {:else if type == "Patient"}
        <h1>Status:</h1>
        <p>Condition: {cond}</p>
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