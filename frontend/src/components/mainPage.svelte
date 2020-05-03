<script>
    import {onMount} from 'svelte';
    import {userType, isNew, filename, condition, trained} from './../stores/user.js';
    import Upload from "./upload.svelte";

    //async obtainFilename() {
    //}

    let file;
    let type;
    let cond;
    let train;

    const unsubscribe = userType.subscribe(val => {
        type = val;
    });

    const unsubscribe2 = filename.subscribe(val => {
        file = val;
    });

    const unsubscribe3 = condition.subscribe(val => {
        cond = val;
    });

    const unsubscribe4 = trained.subscribe(val => {
        train = val;
    });
</script>

<div class="main">
    {#if type == "Doctor"}
        <h1>Upload lung image here:</h1>
        <Upload/>
        {#if file != ""}
            {#if train}
                <p>{file} has been uploaded.</p>
                <p>Condition: {cond}</p>
            {/if}
        {/if}
    {:else if type == "Patient"}
        <h1>Status:</h1>
        <p>Condition: {cond}</p>
        <h1>Tips:</h1>
        <ul>
        {#if cond == "Infected"}
            <li>Drink lots of warm water.</li>
            <li>Maintain a safe distance (at least 2 m) from others.</li>
            <li>Self-quarantine yourself at home for at least 2 weeks.</li>
            <li>Cover any coughs or sneezes with your arm.</li>
            <li>If symptoms get extremely serious (e.g. coughing), call an ambulance.</li>
        {:else if cond == "Normal"}
            <li>Stay home as much as possible to prevent getting sick.</li>
            <li>Maintain a safe distance (at least 2 m) from others.</li>
            <li>Wash hands often.</li>
            <li>Try not to touch your face after touching a surface.</li>
            <li>Go outside for fresh air or exercise once in a while.</li>
            <li>Create applications like this one for the social good :)</li>
        {/if}
        </ul>
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
        margin-top: 40px;
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

    li {
        color: white;
        margin: 20px 0px;
    }
</style>