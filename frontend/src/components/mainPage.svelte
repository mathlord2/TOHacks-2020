<script>
    import {onMount} from 'svelte';
    export let filename = "lung.jpg";
    export let userType = "Doctor"; //"Doctor" or "Patient"
    export let condition = "Normal";

    //async obtainFilename() {
    //}
</script>

<div class="main">
    {#if userType == "Doctor"}
        <h1>Upload lung image here:</h1>
        <button class="upload">Upload <i class="fa fa-upload"></i></button>
        {#if filename != ""}
            <p>{filename} has been uploaded.</p>
            <p>Condition: {condition}</p>
        {/if}
    {:else}
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
        padding: 10px;
    }

    button:hover {
        background: grey;
    }
    
    p {
        margin: 20px 0px;
    }
</style>