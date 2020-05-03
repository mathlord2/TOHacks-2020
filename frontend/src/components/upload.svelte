<script>
    import {onMount} from "svelte";
    import {filename, trained, condition} from "./../stores/user.js";

    let dataURL;
    let modelURL;
    let model;
    let patients = [];

    onMount(() => {
        db.collection("users").get().then(function(querySnapshot) {
            querySnapshot.forEach(function(doc) {
                // doc.data() is never undefined for query doc snapshots
                if (doc.data().type == "Patient") {
                    patients[patients.length] = doc.data().idUser;
                }
            });
        });
    });

    onMount(() => {
        window.$('.inputFile').change(function(e){
            var reader = new FileReader();

            reader.onload = function() {
                dataURL = reader.result;
                filename.set(e.target.files[0].name);
            }

            let file = window.$('.inputFile').prop('files')[0];
            reader.readAsDataURL(file);
        });
    });

    let cond;

    const unsubscribe = condition.subscribe(val => {
        cond = val;
    });

    let id;
    
    function predict() {
        alert("Image is being trained on ...");
        setTimeout(() => {
            trained.set(true);
        }, 3000);

        var email = window.$("#patients").val();
        db.collection("users").get().then(function(querySnapshot) {
            querySnapshot.forEach(function(doc) {
                // doc.data() is never undefined for query doc snapshots
                if (email == doc.data().idUser) {
                    id = doc.id;
                }
            });
        }).then(() => {
            db.collection("users").doc(id).set({
                condition: cond
            }, {merge: true});
        });        
    }
</script>

<form id = "uploadForm" enctype = "multipart/form-data" action = "/api/photo" method = "post">
    <input type="file" name="userPhoto" id="file" class="inputFile" accept="image/png, image/jpeg">
    <label for="file">Upload Image <i class="fa fa-upload"></i></label>
</form>
<label for="patients">Select patient to deliver data:</label>
<select id="patients">
    {#each patients as patient}
        <option value={patient}>{patient}</option>
    {/each}
</select>
<br>
<button on:click={predict}>Run Model</button>
<br>
<img src={dataURL} alt="" id="selectedImage">

<style>
    form {
        margin: 15px 0px;
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
        margin: 10px 0px;
    }

    .inputFile:focus + label, .inputFile + label:hover {
        background-color: rgb(175, 197, 209);
    }

    img {
        margin-top: 20px;
    }

    button {
        border: none;
        border-radius: 10px;
        padding: 20px;
        font-size: 25px;
        background-color: aliceblue;
        margin: 20px 0px;
    }

    button:hover {
        background-color: rgb(175, 197, 209);
    }
</style>