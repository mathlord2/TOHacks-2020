<script>
    import {onMount} from "svelte";
    import {filename} from "./../stores/user.js";

    onMount(() => {
        window.$('input[type="file"]').change(function(e){
            filename.set(e.target.files[0].name);
        });
    });
    
</script>

<form id = "uploadForm" enctype = "multipart/form-data" action = "/api/photo" method = "post">
    <input type="file" name="userPhoto" id="file" class="inputFile" accept="image/png, image/jpeg">
    <label for="file">Upload <i class="fa fa-upload"></i></label>
    <!--<input type="submit" value="Upload Image" name="submit">-->
</form>

<style>
    form {
        margin-top: 30px;
    }

    .inputFile {
        width: 0.1px;
        height: 0.1px;
        opacity: 0;
        overflow: hidden;
        position: absolute;
        z-index: -1;
    }

    .inputFile + label {
        cursor: pointer;
        display: inline-block;
        background-color: aliceblue;
        color: black;
        padding: 20px;
        font-size: 25px;
        border-radius: 10px;
    }

    .inputFile:focus + label, .inputFile + label:hover {
        background-color: rgb(175, 197, 209);
    }
</style>